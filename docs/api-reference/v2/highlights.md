# Highlights Endpoints

Get story highlights by ID.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v2/highlight/by/id`](#get-v2highlightbyid)

---

### GET /v2/highlight/by/id

Get highlight object by id. Returns a Highlight object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/highlight/by/id?id=18085475671830440"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.highlight_by_id_v2(id="18085475671830440")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/highlight/by/id",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "18085475671830440"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/highlight/by/id?id=18085475671830440",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "reels": {
      "highlight:18085475671830440": {
        "id": "highlight:18085475671830440",
        "strong_id__": "highlight:18085475671830440",
        "latest_reel_media": 1773304526,
        "seen": null,
        "can_reply": true,
        "can_gif_quick_reply": true,
        "can_reshare": true,
        "reel_type": "highlight_reel",
        "ad_expiry_timestamp_in_millis": null,
        "is_cta_sticker_available": null,
        "should_treat_link_sticker_as_cta": null,
        "pool_refresh_ttl_in_sec": null,
        "can_react_with_avatar": false,
        "prefetch_count": 0,
        "cover_media": {
          "cropped_image_version": {
            "width": 150,
            "height": 150,
            "url": "https://scontent-lax3-1.cdninstagram.com/...",
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
          "strong_id__": "75885841119",
          "pk": "75885841119",
          "pk_id": "75885841119",
          "id": "75885841119",
          "username": "salwaaa_ki",
          "full_name": "𓆩سلوى 𓆪",
          "is_private": false,
          "is_ring_creator": false,
          "show_ring_award": false,
          "is_verified": false,
          "profile_pic_id": "3868671456830255699_75885841119",
          "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/...",
          "interop_messaging_user_fbid": 17843112720529120,
          "is_creator_agent_enabled": false,
          "transparency_product_enabled": false,
          "is_screenshot_blocking_enabled": false
        },
        "items": [
          {
            "pk": "3772053608293416704",
            "id": "3772053608293416704_75885841119",
            "code": "DRZBsWEDz8A",
            "taken_at": "2025-11-23T07:44:11Z",
            "media_type": 2,
            "product_type": "story",
            "thumbnail_url": "https://scontent-lax7-1.cdninstagram.com/...",
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
            "video_url": "https://scontent-lax7-1.cdninstagram.com/...",
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
            "taken_at": "2025-11-25T10:28:38Z",
            "media_type": 2,
            "product_type": "story",
            "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/...",
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
            "video_url": "https://scontent-lax3-1.cdninstagram.com/...",
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
            "taken_at": "2025-12-01T07:20:23Z",
            "media_type": 2,
            "product_type": "story",
            "thumbnail_url": "https://scontent-lax7-1.cdninstagram.com/...",
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
            "video_url": "https://scontent-lax7-1.cdninstagram.com/...",
            "video_duration": 20.038000106811523,
            "sponsor_tags": [],
            "mentions": [],
            "links": [],
            "hashtags": [],
            "locations": [],
            "stickers": [],
            "medias": []
          }
        ],
        "is_nux": false,
        "title": "me 🦋",
        "created_at": 1764138733,
        "is_pinned_highlight": false,
        "media_count": 98,
        "media_ids": [
          3772053608293416704,
          3773586006193708855,
          3777839902093167269
        ],
        "is_cacheable": true,
        "is_converted_to_clips": false,
        "disabled_reply_types": [
          "story_remix_reply",
          "story_selfie_reply",
          "story_voice_reply"
        ],
        "highlight_reel_type": "DEFAULT",
        "is_added_to_main_grid": false,
        "is_archived": false,
        "show_expiration_tray_signal": false,
        "pk": "18085475671830440"
      }
    },
    "status": "ok"
  }
}
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v2-highlights){ target=_blank }
