"""Fetch real API responses and cache them as JSON files.

Usage:
    python scripts/fetch_responses.py --token TOKEN
    python scripts/fetch_responses.py --token TOKEN --refresh
    python scripts/fetch_responses.py --token TOKEN --refresh /v1/user/by/username
    python scripts/fetch_responses.py --token TOKEN --missing
"""

import argparse
import json
import sys
from pathlib import Path

import httpx

# Allow importing from scripts/
SCRIPTS_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPTS_DIR))

from test_data import API_BASE, ENDPOINT_PARAMS  # noqa: E402

EXAMPLES_DIR = Path(__file__).parent.parent / "docs" / "examples"


def path_to_filename(endpoint_path: str) -> str:
    """Convert /v1/user/by/id to v1-user-by-id.json."""
    return endpoint_path.lstrip("/").replace("/", "-") + ".json"


def truncate_arrays(obj, max_items: int = 3):
    """Recursively truncate all lists to max_items elements."""
    if isinstance(obj, list):
        truncated = obj[:max_items]
        return [truncate_arrays(item, max_items) for item in truncated]
    if isinstance(obj, dict):
        return {k: truncate_arrays(v, max_items) for k, v in obj.items()}
    return obj


# Fields to strip entirely — large blobs useless for developers
STRIP_FIELDS = {
    "video_dash_manifest",
    "dash_manifest",
    "clips_metadata",
    "friendship_status",
    "progressive_download_url",
}

# Array fields to keep only first element
KEEP_FIRST_FIELDS = {
    "video_versions",
    "image_versions",
}


def _shorten_url(url):
    """Shorten CDN URLs: keep scheme + host + /..."""
    if not isinstance(url, str) or not url.startswith("http"):
        return url
    try:
        from urllib.parse import urlparse

        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}/..."
    except Exception:
        return url


def clean_response(obj, keep=frozenset()):
    """Remove noisy fields and shorten URLs for docs.

    ``keep`` — STRIP_FIELDS entries to preserve for this endpoint (e.g. the
    clips_metadata endpoint exists to return ``clips_metadata``).
    """
    if isinstance(obj, list):
        return [clean_response(item, keep) for item in obj]
    if not isinstance(obj, dict):
        return obj

    cleaned = {}
    for key, value in obj.items():
        # Strip heavy/useless fields
        if key in STRIP_FIELDS and key not in keep:
            continue

        # Keep only first element in video/image versions
        if key in KEEP_FIRST_FIELDS and isinstance(value, list):
            value = value[:1]

        # Shorten CDN URLs (profile pics, thumbnails, video)
        if isinstance(value, str) and "cdninstagram.com" in value:
            value = _shorten_url(value)

        cleaned[key] = clean_response(value, keep)
    return cleaned


def fetch_endpoint(
    client: httpx.Client, endpoint_path: str, params: dict
) -> dict | None:
    """Fetch a single endpoint. Returns parsed JSON or None on failure."""
    url = API_BASE + endpoint_path
    try:
        response = client.get(url, params=params)
    except Exception as exc:
        print(f"  ERROR {endpoint_path}: {exc}")
        return None

    if response.status_code != 200:
        print(f"  SKIP  {endpoint_path} (HTTP {response.status_code})")
        return None

    try:
        data = response.json()
    except Exception as exc:
        print(f"  ERROR {endpoint_path}: invalid JSON — {exc}")
        return None

    return data


def main():
    parser = argparse.ArgumentParser(description="Fetch and cache HikerAPI responses.")
    parser.add_argument("--token", required=True, help="API access key (x-access-key)")
    parser.add_argument(
        "--refresh",
        nargs="?",
        const=True,
        default=False,
        metavar="ENDPOINT",
        help="Re-fetch all endpoints, or just ENDPOINT if specified",
    )
    parser.add_argument(
        "--missing",
        action="store_true",
        help="Only fetch endpoints without a cached file",
    )
    args = parser.parse_args()

    EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)

    headers = {
        "x-access-key": args.token,
        "accept": "application/json",
    }

    # Build the list of endpoints to process
    if args.refresh and args.refresh is not True:
        # Single endpoint refresh
        endpoint = args.refresh
        if endpoint not in ENDPOINT_PARAMS:
            print(f"Unknown endpoint: {endpoint}")
            sys.exit(1)
        endpoints_to_fetch = {endpoint: ENDPOINT_PARAMS[endpoint]}
    elif args.refresh is True:
        # Refresh all
        endpoints_to_fetch = dict(ENDPOINT_PARAMS)
    elif args.missing:
        # Only missing
        endpoints_to_fetch = {
            path: params
            for path, params in ENDPOINT_PARAMS.items()
            if not (EXAMPLES_DIR / path_to_filename(path)).exists()
        }
    else:
        # Default: skip already cached
        endpoints_to_fetch = {
            path: params
            for path, params in ENDPOINT_PARAMS.items()
            if not (EXAMPLES_DIR / path_to_filename(path)).exists()
        }

    if not endpoints_to_fetch:
        print("Nothing to fetch — all endpoints are already cached.")
        return

    fetched = 0
    skipped = 0

    with httpx.Client(headers=headers, timeout=30.0) as client:
        for endpoint_path, params in endpoints_to_fetch.items():
            data = fetch_endpoint(client, endpoint_path, params)
            if data is None:
                skipped += 1
                continue

            data = truncate_arrays(data, max_items=3)
            keep = (
                {"clips_metadata"}
                if endpoint_path == "/gql/media/clips_metadata"
                else frozenset()
            )
            data = clean_response(data, keep)
            cache_file = EXAMPLES_DIR / path_to_filename(endpoint_path)
            cache_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
            print(f"  OK    {endpoint_path} -> {cache_file.name}")
            fetched += 1

    print(f"\nDone: {fetched} fetched, {skipped} skipped")


if __name__ == "__main__":
    main()
