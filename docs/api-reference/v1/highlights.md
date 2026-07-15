# Highlights Endpoints

Get story highlights by ID or URL.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v1/highlight/by/url`](#get-v1highlightbyurl) | [`/v1/user/highlights`](#get-v1userhighlights) | [`/v1/user/highlights/by/username`](#get-v1userhighlightsbyusername)

---

### GET /v1/highlight/by/url

Get highlight object by id. Returns a Highlight object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/highlight/by/url?url=https://www.instagram.com/stories/highlights/18085475671830440/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.highlight_by_url_v1(url="https://www.instagram.com/stories/highlights/18085475671830440/")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/highlight/by/url",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/stories/highlights/18085475671830440/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/highlight/by/url?url=https://www.instagram.com/stories/highlights/18085475671830440/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "18085475671830440",
  "id": "highlight:18085475671830440",
  "latest_reel_media": 1773304526,
  "cover_media": {
    "cropped_image_version": {
      "width": 150,
      "height": 150,
      "url": "https://scontent-sjc6-1.cdninstagram.com/...",
      "scans_profile": ""
    },
    "crop_rect": [
      0.0,
      0.30167106,
      1.0
    ],
    "media_id": "3849652044117864571_75885841119",
    "full_image_version": null,
    "upload_id": null
  },
  "user": {
    "pk": "75885841119",
    "id": "75885841119",
    "username": "salwaaa_ki",
    "full_name": "𓆩سلوى 𓆪",
    "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/...",
    "profile_pic_url_hd": null,
    "is_private": false,
    "is_verified": false
  },
  "title": "me 🦋",
  "created_at": "2025-11-26T06:32:13+00:00",
  "is_pinned_highlight": false,
  "media_count": 98,
  "media_ids": [
    3772053608293416704,
    3773586006193708855,
    3777839902093167269
  ],
  "items": [
    {
      "pk": "3772053608293416704",
      "id": "3772053608293416704_75885841119",
      "code": "DRZBsWEDz8A",
      "taken_at": "2025-11-23T07:44:11+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://scontent-sjc3-1.cdninstagram.com/...",
      "user": {
        "pk": "75885841119",
        "id": "75885841119",
        "username": null,
        "full_name": "",
        "profile_pic_url": null,
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": null
      },
      "video_url": "https://scontent-sjc3-1.cdninstagram.com/...",
      "video_duration": 20.014999389648438,
      "sponsor_tags": [],
      "mentions": [],
      "links": [],
      "hashtags": [],
      "locations": [],
      "stickers": [],
      "medias": []
    },
    {
      "pk": "3773586006193708855",
      "id": "3773586006193708855_75885841119",
      "code": "DReeHq0j583",
      "taken_at": "2025-11-25T10:28:38+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://scontent-sjc6-1.cdninstagram.com/...",
      "user": {
        "pk": "75885841119",
        "id": "75885841119",
        "username": null,
        "full_name": "",
        "profile_pic_url": null,
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": null
      },
      "video_url": "https://scontent-sjc6-1.cdninstagram.com/...",
      "video_duration": 20.038000106811523,
      "sponsor_tags": [],
      "mentions": [],
      "links": [],
      "hashtags": [],
      "locations": [],
      "stickers": [],
      "medias": []
    },
    {
      "pk": "3777839902093167269",
      "id": "3777839902093167269_75885841119",
      "code": "DRtlWAGj0ql",
      "taken_at": "2025-12-01T07:20:23+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://scontent-sjc6-1.cdninstagram.com/...",
      "user": {
        "pk": "75885841119",
        "id": "75885841119",
        "username": null,
        "full_name": "",
        "profile_pic_url": null,
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": null
      },
      "video_url": "https://scontent-sjc3-1.cdninstagram.com/...",
      "video_duration": 20.038000106811523,
      "sponsor_tags": [],
      "mentions": [],
      "links": [],
      "hashtags": [],
      "locations": [],
      "stickers": [],
      "medias": []
    }
  ]
}
```

</details>

---

### GET /v1/user/highlights

⚠️ Billing: 2 requests per call. Returns a list of Highlight objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `amount` | integer | No | Amount |
| `force` | boolean | No | Skip account privacy check |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/highlights?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_highlights_v1(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/highlights",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/highlights?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "17983616051768088",
    "id": "highlight:17983616051768088",
    "latest_reel_media": 1766242839,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-lax3-1.cdninstagram.com/...",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "Gift Guide",
    "created_at": "2025-12-04T11:06:31Z",
    "is_pinned_highlight": false,
    "media_count": 12,
    "media_ids": [],
    "items": []
  },
  {
    "pk": "18018069326790931",
    "id": "highlight:18018069326790931",
    "latest_reel_media": 1762870363,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-lax3-1.cdninstagram.com/...",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "BOTW 2026",
    "created_at": "2025-10-21T13:07:47Z",
    "is_pinned_highlight": false,
    "media_count": 11,
    "media_ids": [],
    "items": []
  },
  {
    "pk": "17893209825281221",
    "id": "highlight:17893209825281221",
    "latest_reel_media": 1752840788,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-lax3-2.cdninstagram.com/...",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "Limitless",
    "created_at": "2025-08-08T17:33:52Z",
    "is_pinned_highlight": false,
    "media_count": 11,
    "media_ids": [],
    "items": []
  }
]
```

</details>

---

### GET /v1/user/highlights/by/username

⚠️ Billing: 3 requests per call. Returns a list of Highlight objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |
| `amount` | integer | No | Amount |
| `force` | boolean | No | Skip account privacy check |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/highlights/by/username?username=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_highlights_by_username_v1(username="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/highlights/by/username",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/highlights/by/username?username=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "17983616051768088",
    "id": "highlight:17983616051768088",
    "latest_reel_media": 1766242839,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-dfw5-1.cdninstagram.com/...",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "Gift Guide",
    "created_at": "2025-12-04T11:06:31Z",
    "is_pinned_highlight": false,
    "media_count": 12,
    "media_ids": [],
    "items": []
  },
  {
    "pk": "18018069326790931",
    "id": "highlight:18018069326790931",
    "latest_reel_media": 1762870363,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-dfw6-1.cdninstagram.com/...",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "BOTW 2026",
    "created_at": "2025-10-21T13:07:47Z",
    "is_pinned_highlight": false,
    "media_count": 11,
    "media_ids": [],
    "items": []
  },
  {
    "pk": "17893209825281221",
    "id": "highlight:17893209825281221",
    "latest_reel_media": 1752840788,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-dfw5-2.cdninstagram.com/...",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "Limitless",
    "created_at": "2025-08-08T17:33:52Z",
    "is_pinned_highlight": false,
    "media_count": 11,
    "media_ids": [],
    "items": []
  }
]
```

</details>

---

## Deprecated endpoints

These endpoints are deprecated — use the recommended alternatives. Retired ones respond with **410 Gone** and are never charged (see [Response Codes](../response-codes.md)); the rest still work but will be removed in a future version.

### ~~GET /v1/highlight/by/id~~

!!! warning
    Highlight By Id

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-highlights){ target=_blank }
