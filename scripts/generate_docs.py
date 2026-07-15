#!/usr/bin/env python3
"""Generate API reference markdown for all resource pages.

Reads the per-resource OpenAPI specs, SDK method signatures, and cached
response examples to produce complete markdown with code tabs for each
endpoint.

Usage:
    python scripts/generate_docs.py
"""

import inspect
import json
import sys
from pathlib import Path

# Allow importing from scripts/
SCRIPTS_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPTS_DIR))

from test_data import ENDPOINT_PARAMS, SDK_METHODS  # noqa: E402

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
OPENAPI_DIR = DOCS_DIR / "openapi"
EXAMPLES_DIR = DOCS_DIR / "examples"
API_REF_DIR = DOCS_DIR / "api-reference"

API_BASE = "https://api.hikerapi.com"

# ── Resource grouping ────────────────────────────────────────────

RESOURCES = {
    "v1/user": {
        "prefixes": ["/v1/user/"],
        "excludes": ["/v1/user/stories", "/v1/user/highlights"],
    },
    "v1/media": {"prefixes": ["/v1/media/"], "excludes": []},
    "v1/stories": {
        "prefixes": ["/v1/story/", "/v1/user/stories"],
        "excludes": [],
    },
    "v1/highlights": {
        "prefixes": ["/v1/highlight/", "/v1/user/highlights"],
        "excludes": [],
    },
    "v1/hashtags": {"prefixes": ["/v1/hashtag/"], "excludes": []},
    "v1/locations": {"prefixes": ["/v1/location/"], "excludes": []},
    "v1/search": {
        "prefixes": ["/v1/search/", "/v1/fbsearch/", "/v1/share/"],
        "excludes": [],
    },
    "v2/user": {
        "prefixes": ["/v2/user/", "/a2/user", "/v2/userstream/"],
        "excludes": [],
    },
    "v2/media": {"prefixes": ["/v2/media/"], "excludes": []},
    "v2/stories": {"prefixes": ["/v2/story/"], "excludes": []},
    "v2/highlights": {"prefixes": ["/v2/highlight/"], "excludes": []},
    "v2/hashtags": {"prefixes": ["/v2/hashtag/"], "excludes": []},
    "v2/search": {
        "prefixes": ["/v2/search/", "/v2/fbsearch/"],
        "excludes": [],
    },
    "v2/track": {"prefixes": ["/v2/track/", "/v3/"], "excludes": []},
    "gql": {"prefixes": ["/gql/", "/g1/", "/g2/"], "excludes": []},
    "system": {"prefixes": ["/sys/"], "excludes": []},
}

# ── Output file mapping ─────────────────────────────────────────

OUTPUT_FILES = {
    "v1/user": API_REF_DIR / "v1" / "user.md",
    "v1/media": API_REF_DIR / "v1" / "media.md",
    "v1/stories": API_REF_DIR / "v1" / "stories.md",
    "v1/highlights": API_REF_DIR / "v1" / "highlights.md",
    "v1/hashtags": API_REF_DIR / "v1" / "hashtags.md",
    "v1/locations": API_REF_DIR / "v1" / "locations.md",
    "v1/search": API_REF_DIR / "v1" / "search.md",
    "v2/user": API_REF_DIR / "v2" / "user.md",
    "v2/media": API_REF_DIR / "v2" / "media.md",
    "v2/stories": API_REF_DIR / "v2" / "stories.md",
    "v2/highlights": API_REF_DIR / "v2" / "highlights.md",
    "v2/hashtags": API_REF_DIR / "v2" / "hashtags.md",
    "v2/search": API_REF_DIR / "v2" / "search.md",
    "v2/track": API_REF_DIR / "v2" / "track.md",
    "gql": API_REF_DIR / "gql" / "index.md",
    "system": API_REF_DIR / "system.md",
}

# ── OpenAPI spec file mapping ────────────────────────────────────

SPEC_FILES = {
    "v1/user": "v1-user.json",
    "v1/media": "v1-media.json",
    "v1/stories": "v1-stories.json",
    "v1/highlights": "v1-highlights.json",
    "v1/hashtags": "v1-hashtags.json",
    "v1/locations": "v1-locations.json",
    "v1/search": "v1-search.json",
    "v2/user": "v2-user.json",
    "v2/media": "v2-media.json",
    "v2/stories": "v2-stories.json",
    "v2/highlights": "v2-highlights.json",
    "v2/hashtags": "v2-hashtags.json",
    "v2/search": "v2-search.json",
    "v2/track": "v2-track.json",
    "gql": "gql.json",
    "system": "sys.json",
}

# ── Page metadata ────────────────────────────────────────────────

PAGE_META = {
    "v1/user": (
        "User Endpoints",
        "Get user profiles, followers, following lists, and search.",
    ),
    "v1/media": (
        "Media Endpoints",
        "Get posts, reels, likes, comments, and media details.",
    ),
    "v1/stories": (
        "Stories Endpoints",
        "Get user stories and story items.",
    ),
    "v1/highlights": (
        "Highlights Endpoints",
        "Get story highlights by ID or URL.",
    ),
    "v1/hashtags": (
        "Hashtag Endpoints",
        "Get hashtag info, top and recent media.",
    ),
    "v1/locations": (
        "Location Endpoints",
        "Get location info and media by location ID.",
    ),
    "v1/search": (
        "Search Endpoints",
        "Search users, hashtags, locations, and music.",
    ),
    "v2/user": (
        "User Endpoints",
        "Enhanced user data with pagination via page_id.",
    ),
    "v2/media": (
        "Media Endpoints",
        "Get posts, comments, and media details.",
    ),
    "v2/stories": (
        "Stories Endpoints",
        "Get stories and story viewers.",
    ),
    "v2/highlights": (
        "Highlights Endpoints",
        "Get story highlights by ID.",
    ),
    "v2/hashtags": (
        "Hashtag Endpoints",
        "Get hashtag info and media.",
    ),
    "v2/search": (
        "Search Endpoints",
        "Search across users, hashtags, places, reels.",
    ),
    "v2/track": (
        "Track Endpoints",
        "Get audio tracks, likers, and associated media.",
    ),
    "gql": (
        "GraphQL API",
        "Instagram GraphQL endpoints with cursor-based pagination.",
    ),
    "system": (
        "System Endpoints",
        "Account balance and rate limit info.",
    ),
}

UTM = {
    "v1/user": "api-v1-user",
    "v1/media": "api-v1-media",
    "v1/stories": "api-v1-stories",
    "v1/highlights": "api-v1-highlights",
    "v1/hashtags": "api-v1-hashtags",
    "v1/locations": "api-v1-locations",
    "v1/search": "api-v1-search",
    "v2/user": "api-v2-user",
    "v2/media": "api-v2-media",
    "v2/stories": "api-v2-stories",
    "v2/highlights": "api-v2-highlights",
    "v2/hashtags": "api-v2-hashtags",
    "v2/search": "api-v2-search",
    "v2/track": "api-v2-track",
    "gql": "api-gql",
    "system": "api-system",
}

MAX_RESPONSE_LINES = 80


# ── Helpers ──────────────────────────────────────────────────────


def _load_sdk_signatures():
    """Load SDK method signatures from the installed hikerapi package."""
    from hikerapi import Client

    sigs = {}
    for endpoint_path, method_name in SDK_METHODS.items():
        method = getattr(Client, method_name, None)
        if method is None:
            continue
        sig = inspect.signature(method)
        # Collect param names, skipping 'self'
        params = []
        for name, param in sig.parameters.items():
            if name == "self":
                continue
            params.append((name, param.default is inspect.Parameter.empty))
        sigs[endpoint_path] = {
            "method_name": method_name,
            "params": params,
        }
    return sigs


def _path_to_anchor(path):
    """Convert /v1/user/by/username -> get-v1userbyusername."""
    slug = path.lstrip("/").replace("/", "")
    return f"get-{slug}"


def _path_to_example_file(path):
    """Convert /v1/user/by/id -> v1-user-by-id.json."""
    return path.lstrip("/").replace("/", "-") + ".json"


def _get_param_type(param_schema):
    """Extract a human-readable type from an OpenAPI parameter schema."""
    if not param_schema:
        return "string"
    if "type" in param_schema:
        return param_schema["type"]
    if "anyOf" in param_schema:
        types = [
            s.get("type", "") for s in param_schema["anyOf"] if s.get("type") != "null"
        ]
        return types[0] if types else "string"
    return "string"


def _get_auth_links(resource_key):
    """Return (auth_link, response_codes_link) relative paths."""
    if resource_key == "system":
        return (
            "../getting-started/authentication.md",
            "response-codes.md",
        )
    # v1/*, v2/*, gql (gql/index.md is in a subdir)
    return (
        "../../getting-started/authentication.md",
        "../response-codes.md",
    )


def _get_endpoints_for_resource(spec, resource_key):
    """Return sorted list of endpoint paths for a resource."""
    res = RESOURCES[resource_key]
    prefixes = res["prefixes"]
    excludes = res["excludes"]

    paths = []
    for path in spec.get("paths", {}):
        if any(path.startswith(p) for p in prefixes) and not any(
            path.startswith(e) for e in excludes
        ):
            paths.append(path)

    return sorted(paths)


def _get_example_params(path):
    """Get example parameter values from ENDPOINT_PARAMS."""
    return ENDPOINT_PARAMS.get(path, {})


def _indent(text, prefix="    "):
    """Indent text, but keep empty lines empty (no trailing spaces)."""
    result = []
    for line in text.split("\n"):
        if line.strip():
            result.append(prefix + line)
        else:
            result.append("")
    return result


def _truncate_json(json_str, max_lines=MAX_RESPONSE_LINES):
    """Truncate JSON string to max_lines, adding ellipsis if needed."""
    lines = json_str.split("\n")
    if len(lines) <= max_lines:
        return json_str
    truncated = lines[:max_lines]
    # Try to end cleanly: find last line that isn't just whitespace
    result = "\n".join(truncated)
    result += "\n  // ... truncated"
    return result


def _build_curl_example(path, params, cursor_param=None):
    """Build a curl code example."""
    url = f"{API_BASE}{path}"
    if params:
        query = "&".join(f"{k}={v}" for k, v in params.items())
        full_url = f"{url}?{query}"
    else:
        full_url = url

    line = f'curl -H "x-access-key: YOUR_TOKEN" \\\n  "{full_url}"'
    if cursor_param:
        line += f"\n# Next page: add &{cursor_param}=... from previous response"
    return line


def _build_python_sdk_example(sdk_info, params, cursor_param=None):
    """Build a Python SDK code example."""
    method_name = sdk_info["method_name"]
    sdk_params = sdk_info["params"]

    # Build kwargs using only required params (matching test_data)
    kwargs_parts = []
    for param_name, is_required in sdk_params:
        if param_name in params:
            val = params[param_name]
            if isinstance(val, str):
                kwargs_parts.append(f'{param_name}="{val}"')
            else:
                kwargs_parts.append(f"{param_name}={val}")

    kwargs_str = ", ".join(kwargs_parts)

    lines = [
        "from hikerapi import Client",
        "",
        'cl = Client(token="YOUR_TOKEN")',
        f"result = cl.{method_name}({kwargs_str})",
    ]
    if cursor_param:
        lines.append(
            f"# Next page: cl.{method_name}(" f'{kwargs_str}, {cursor_param}="...")'
        )
    return "\n".join(lines)


def _build_requests_example(path, params, cursor_param=None):
    """Build a Python requests code example."""
    url = f"{API_BASE}{path}"

    lines = [
        "import requests",
        "",
        "response = requests.get(",
        f'    "{url}",',
        '    headers={"x-access-key": "YOUR_TOKEN"},',
    ]

    if params:
        params_str = "{"
        items = list(params.items())
        if len(items) == 1:
            k, v = items[0]
            if isinstance(v, str):
                params_str += f'"{k}": "{v}"'
            else:
                params_str += f'"{k}": {v}'
            params_str += "}"
        else:
            parts = []
            for k, v in items:
                if isinstance(v, str):
                    parts.append(f'"{k}": "{v}"')
                else:
                    parts.append(f'"{k}": {v}')
            params_str += ", ".join(parts) + "}"
        lines.append(f"    params={params_str},")

    lines.append(")")
    if cursor_param:
        lines.append(f'# Next page: add "{cursor_param}": "..." to params')
    lines.append("print(response.json())")
    return "\n".join(lines)


def _build_js_example(path, params, cursor_param=None):
    """Build a JavaScript fetch code example."""
    url = f"{API_BASE}{path}"
    if params:
        query = "&".join(f"{k}={v}" for k, v in params.items())
        full_url = f"{url}?{query}"
    else:
        full_url = url

    lines = [
        "const response = await fetch(",
        f'  "{full_url}",',
        '  { headers: { "x-access-key": "YOUR_TOKEN" } }',
        ");",
        "const data = await response.json();",
    ]
    if cursor_param:
        lines.append(f"// Next page: add &{cursor_param}=... to URL")
    return "\n".join(lines)


def _generate_endpoint_section(path, operation, sdk_sigs, resource_key):
    """Generate markdown for a single endpoint."""
    lines = []

    # Heading
    lines.append(f"### GET {path}")
    lines.append("")

    # Description
    desc = operation.get("description", "")
    summary = operation.get("summary", "")
    # Prefer description, fall back to summary
    display_desc = desc or summary
    if display_desc:
        # Strip trailing whitespace from each line in description
        cleaned = "\n".join(line.rstrip() for line in display_desc.split("\n"))
        lines.append(cleaned)
        lines.append("")

    # Parameters table
    params = operation.get("parameters", [])
    # Filter out APIKeyHeader
    params = [
        p
        for p in params
        if not (p.get("name") == "APIKeyHeader" and p.get("in") == "header")
    ]

    if params:
        lines.append("| Parameter | Type | Required | Description |")
        lines.append("|-----------|------|----------|-------------|")
        for p in params:
            name = p.get("name", "")
            schema = p.get("schema", {})
            ptype = _get_param_type(schema)
            required = "Yes" if p.get("required") else "No"
            pdesc = (
                p.get("description", "")
                or schema.get("description", "")
                or schema.get("title", "")
            )
            # Collapse multi-line descriptions for table cells
            # and strip trailing whitespace
            pdesc = " ".join(pdesc.split()).strip()
            lines.append(f"| `{name}` | {ptype} | {required} | {pdesc} |")
        lines.append("")

    # Example params from test_data
    example_params = _get_example_params(path)

    # Detect pagination cursor param (optional, not in example_params)
    cursor_names = {
        "end_cursor",
        "max_id",
        "page_id",
        "page_token",
        "next_max_id",
        "reels_max_id",
        "repost_next_max_id",
        "profile_grid_items_cursor",
    }
    cursor_param = None
    for p in params:
        if p.get("name") in cursor_names and not p.get("required"):
            cursor_param = p.get("name")
            break

    # Code tabs
    has_sdk = path in sdk_sigs
    sdk_info = sdk_sigs.get(path)

    if has_sdk:
        # 4 tabs: curl, Python SDK, Python requests, JavaScript
        lines.append('=== "curl"')
        lines.append("")
        lines.append("    ```bash")
        lines.extend(_indent(_build_curl_example(path, example_params, cursor_param)))
        lines.append("    ```")
        lines.append("")

        lines.append('=== "Python"')
        lines.append("")
        lines.append("    ```python")
        lines.extend(
            _indent(_build_python_sdk_example(sdk_info, example_params, cursor_param))
        )
        lines.append("    ```")
        lines.append("")

        lines.append('=== "Python (requests)"')
        lines.append("")
        lines.append("    ```python")
        lines.extend(
            _indent(_build_requests_example(path, example_params, cursor_param))
        )
        lines.append("    ```")
        lines.append("")

        lines.append('=== "JavaScript"')
        lines.append("")
        lines.append("    ```javascript")
        lines.extend(_indent(_build_js_example(path, example_params, cursor_param)))
        lines.append("    ```")
        lines.append("")
    else:
        # 3 tabs: curl, Python requests, JavaScript
        lines.append('=== "curl"')
        lines.append("")
        lines.append("    ```bash")
        lines.extend(_indent(_build_curl_example(path, example_params, cursor_param)))
        lines.append("    ```")
        lines.append("")

        lines.append('=== "Python (requests)"')
        lines.append("")
        lines.append("    ```python")
        lines.extend(
            _indent(_build_requests_example(path, example_params, cursor_param))
        )
        lines.append("    ```")
        lines.append("")

        lines.append('=== "JavaScript"')
        lines.append("")
        lines.append("    ```javascript")
        lines.extend(_indent(_build_js_example(path, example_params, cursor_param)))
        lines.append("    ```")
        lines.append("")

    # Response example
    example_file = EXAMPLES_DIR / _path_to_example_file(path)
    if example_file.exists():
        try:
            json_text = example_file.read_text()
            # Re-format to consistent indentation
            data = json.loads(json_text)
            formatted = json.dumps(data, indent=2, ensure_ascii=False)
            lines.append("<details>")
            lines.append("<summary>Example response</summary>")
            lines.append("")
            lines.append("```json")
            lines.append(formatted)
            lines.append("```")
            lines.append("")
            lines.append("</details>")
            lines.append("")
        except (json.JSONDecodeError, OSError):
            pass

    return "\n".join(lines)


def _generate_page(resource_key, spec, sdk_sigs):
    """Generate complete markdown for a resource page."""
    title, description = PAGE_META[resource_key]
    auth_link, codes_link = _get_auth_links(resource_key)
    utm_content = UTM[resource_key]

    all_endpoints = _get_endpoints_for_resource(spec, resource_key)

    # Split into active and deprecated
    active = []
    deprecated = []
    for ep in all_endpoints:
        op = spec["paths"].get(ep, {}).get("get", {})
        if op.get("deprecated"):
            deprecated.append(ep)
        else:
            active.append(ep)

    lines = []

    # Title and description
    lines.append(f"# {title}")
    lines.append("")
    lines.append(description)
    lines.append("")

    # Auth info box
    lines.append('!!! info "Authentication & errors"')
    lines.append(
        f"    All endpoints require `x-access-key` header. "
        f"See [Authentication]({auth_link}). "
        f"Error responses: [Response Codes]({codes_link})."
    )
    lines.append("")

    # Endpoint index (active only)
    if active:
        anchors = []
        for ep in active:
            anchor = _path_to_anchor(ep)
            anchors.append(f"[`{ep}`](#{anchor})")
        lines.append("**Endpoints:** " + " | ".join(anchors))
        lines.append("")

    # Separator before first endpoint
    lines.append("---")
    lines.append("")

    # Active endpoints (full rendering)
    for i, ep in enumerate(active):
        path_methods = spec["paths"].get(ep, {})
        operation = path_methods.get("get", {})
        section = _generate_endpoint_section(ep, operation, sdk_sigs, resource_key)
        lines.append(section)

        if i < len(active) - 1:
            lines.append("---")
            lines.append("")

    # Deprecated endpoints (minimal rendering)
    if deprecated:
        lines.append("---")
        lines.append("")
        lines.append("## Deprecated endpoints")
        lines.append("")
        lines.append(
            "These endpoints are deprecated — use the recommended "
            "alternatives. Retired ones respond with **410 Gone** and are "
            f"never charged (see [Response Codes]({codes_link})); the rest "
            "still work but will be removed in a future version."
        )
        lines.append("")
        for ep in deprecated:
            op = spec["paths"].get(ep, {}).get("get", {})
            # summary has the WARNING text, description is generic
            warn = op.get("summary", "") or op.get("description", "")
            lines.append(f"### ~~GET {ep}~~")
            lines.append("")
            if warn:
                lines.append("!!! warning")
                lines.append(f"    {warn}")
                lines.append("")

    # CTA footer
    lines.append("---")
    lines.append("")
    lines.append(
        "**Ready to integrate?** First 100 requests free "
        "— [Get your API key "
        f"→](https://hikerapi.com/p/7it8oc2i?"
        f"utm_source=docs&utm_medium=cta"
        f"&utm_content={utm_content})"
        "{ target=_blank }"
    )
    lines.append("")

    return "\n".join(lines)


def _load_full_spec():
    """Load the full openapi.json spec."""
    source = DOCS_DIR / "openapi.json"
    with open(source) as f:
        return json.load(f)


def _load_resource_spec(resource_key):
    """Load the per-resource OpenAPI spec file."""
    filename = SPEC_FILES[resource_key]
    spec_path = OPENAPI_DIR / filename
    with open(spec_path) as f:
        return json.load(f)


def main():
    print("Loading SDK signatures...")
    sdk_sigs = _load_sdk_signatures()
    print(f"  Found {len(sdk_sigs)} SDK methods")

    total_endpoints = 0

    for resource_key in RESOURCES:
        print(f"\nGenerating {resource_key}...")

        spec = _load_resource_spec(resource_key)
        endpoints = _get_endpoints_for_resource(spec, resource_key)
        print(f"  {len(endpoints)} endpoints")
        total_endpoints += len(endpoints)

        markdown = _generate_page(resource_key, spec, sdk_sigs)

        output_file = OUTPUT_FILES[resource_key]
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(markdown)
        print(f"  -> {output_file.relative_to(DOCS_DIR.parent)}")

    print(f"\nDone: {total_endpoints} endpoints across " f"{len(RESOURCES)} pages")


if __name__ == "__main__":
    main()
