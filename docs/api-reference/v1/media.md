# Media Endpoints

Get posts, reels, likes, comments, and media details.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v1/media/by/code`](#get-v1mediabycode) | [`/v1/media/by/id`](#get-v1mediabyid) | [`/v1/media/by/url`](#get-v1mediabyurl) | [`/v1/media/code/from/pk`](#get-v1mediacodefrompk) | [`/v1/media/comments/chunk`](#get-v1mediacommentschunk) | [`/v1/media/insight`](#get-v1mediainsight) | [`/v1/media/likers`](#get-v1medialikers) | [`/v1/media/oembed`](#get-v1mediaoembed) | [`/v1/media/pk/from/code`](#get-v1mediapkfromcode) | [`/v1/media/pk/from/url`](#get-v1mediapkfromurl) | [`/v1/media/user`](#get-v1mediauser)

---

### GET /v1/media/by/code

Get media object. Returns a Media object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `code` | string | Yes | Code |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/by/code?code=DRqAYKuAIUx"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_by_code_v1(code="DRqAYKuAIUx")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/by/code",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"code": "DRqAYKuAIUx"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/by/code?code=DRqAYKuAIUx",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "3776832898280228145",
  "id": "3776832898280228145_787132",
  "code": "DRqAYKuAIUx",
  "taken_at": "2025-11-29T22:00:31Z",
  "taken_at_ts": 1764453631,
  "media_type": 2,
  "product_type": "clips",
  "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/...",
  "user": {
    "pk": "787132",
    "id": "787132",
    "username": "natgeo",
    "full_name": "National Geographic",
    "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/...",
    "is_private": false,
    "is_verified": true
  },
  "comment_count": 485,
  "comments_disabled": false,
  "like_count": 135428,
  "play_count": 2866123,
  "has_liked": false,
  "caption_text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
  "usertags": [],
  "sponsor_tags": [],
  "video_url": "https://scontent-lax3-1.cdninstagram.com/...",
  "view_count": 0,
  "video_duration": 22.31399917602539,
  "title": "",
  "resources": [],
  "image_versions": [
    {
      "estimated_scans_sizes": [
        27870,
        55740,
        83610
      ],
      "height": 1333,
      "scans_profile": "e35",
      "url": "https://scontent-lax3-1.cdninstagram.com/...",
      "width": 750,
      "is_spatial_image": false
    }
  ],
  "video_versions": [
    {
      "bandwidth": 2315752,
      "height": 1280,
      "id": "1525428988604088v",
      "type": 101,
      "url": "https://scontent-lax3-1.cdninstagram.com/...",
      "url_expiration_timestamp_us": null,
      "width": 720,
      "fallback": null
    }
  ],
  "like_and_view_counts_disabled": false,
  "coauthor_producers": [],
  "is_paid_partnership": false
}
```

</details>

---

### GET /v1/media/by/id

Get media object. Returns a Media object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/by/id?id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_by_id_v1(id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/by/id",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/by/id?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "3776832898280228145",
  "id": "3776832898280228145_787132",
  "code": "DRqAYKuAIUx",
  "taken_at": "2025-11-29T22:00:31Z",
  "taken_at_ts": 1764453631,
  "media_type": 2,
  "product_type": "clips",
  "thumbnail_url": "https://scontent-sjc3-1.cdninstagram.com/...",
  "user": {
    "pk": "787132",
    "id": "787132",
    "username": "natgeo",
    "full_name": "National Geographic",
    "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/...",
    "is_private": false,
    "is_verified": true
  },
  "comment_count": 485,
  "comments_disabled": false,
  "like_count": 135428,
  "play_count": 2866123,
  "has_liked": false,
  "caption_text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
  "usertags": [],
  "sponsor_tags": [],
  "video_url": "https://scontent-sjc3-1.cdninstagram.com/...",
  "view_count": 0,
  "video_duration": 22.31399917602539,
  "title": "",
  "resources": [],
  "image_versions": [
    {
      "estimated_scans_sizes": [
        27870,
        55740,
        83610
      ],
      "height": 1333,
      "scans_profile": "e35",
      "url": "https://scontent-sjc3-1.cdninstagram.com/...",
      "width": 750,
      "is_spatial_image": false
    }
  ],
  "video_versions": [
    {
      "bandwidth": 2315752,
      "height": 1280,
      "id": "1525428988604088v",
      "type": 101,
      "url": "https://scontent-sjc3-1.cdninstagram.com/...",
      "url_expiration_timestamp_us": null,
      "width": 720,
      "fallback": null
    }
  ],
  "like_and_view_counts_disabled": false,
  "coauthor_producers": [],
  "is_paid_partnership": false
}
```

</details>

---

### GET /v1/media/by/url

Get media object. Returns a Media object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_by_url_v1(url="https://www.instagram.com/p/DRqAYKuAIUx/")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/by/url",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/p/DRqAYKuAIUx/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "3776832898280228145",
  "id": "3776832898280228145_787132",
  "code": "DRqAYKuAIUx",
  "taken_at": "2025-11-29T22:00:31Z",
  "taken_at_ts": 1764453631,
  "media_type": 2,
  "product_type": "clips",
  "thumbnail_url": "https://scontent-sea1-1.cdninstagram.com/...",
  "user": {
    "pk": "787132",
    "id": "787132",
    "username": "natgeo",
    "full_name": "National Geographic",
    "profile_pic_url": "https://scontent-sea1-1.cdninstagram.com/...",
    "is_private": false,
    "is_verified": true
  },
  "comment_count": 485,
  "comments_disabled": false,
  "like_count": 135428,
  "play_count": 2866123,
  "has_liked": false,
  "caption_text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
  "usertags": [],
  "sponsor_tags": [],
  "video_url": "https://scontent-sea5-1.cdninstagram.com/...",
  "view_count": 0,
  "video_duration": 22.31399917602539,
  "title": "",
  "resources": [],
  "image_versions": [
    {
      "estimated_scans_sizes": [
        27870,
        55740,
        83610
      ],
      "height": 1333,
      "scans_profile": "e35",
      "url": "https://scontent-sea1-1.cdninstagram.com/...",
      "width": 750,
      "is_spatial_image": false
    }
  ],
  "video_versions": [
    {
      "bandwidth": 2315752,
      "height": 1280,
      "id": "1525428988604088v",
      "type": 101,
      "url": "https://scontent-sea5-1.cdninstagram.com/...",
      "url_expiration_timestamp_us": null,
      "width": 720,
      "fallback": null
    }
  ],
  "like_and_view_counts_disabled": false,
  "coauthor_producers": [],
  "is_paid_partnership": false
}
```

</details>

---

### GET /v1/media/code/from/pk

Get media code from pk

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pk` | string | Yes | Pk |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/code/from/pk?pk=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_code_from_pk_v1(pk="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/code/from/pk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"pk": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/code/from/pk?pk=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
"DRqAYKuAIUx"
```

</details>

---

### GET /v1/media/comments/chunk

Get comments on a media. Returns a list of Comment objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |
| `min_id` | string | No | Min Id |
| `max_id` | string | No | Max Id |
| `can_support_threading` | boolean | No | Can Support Threading |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/comments/chunk?id=3776832898280228145"
    # Next page: add &max_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_comments_chunk_v1(id="3776832898280228145")
    # Next page: cl.media_comments_chunk_v1(id="3776832898280228145", max_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/comments/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "3776832898280228145"},
    )
    # Next page: add "max_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/comments/chunk?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    // Next page: add &max_id=... to URL
    ```

<details>
<summary>Example response</summary>

```json
[
  [
    {
      "pk": "18333964546215235",
      "text": "Wooow🔥👏",
      "user": {
        "pk": "40128242138",
        "id": "40128242138",
        "username": "_pauline_perla_",
        "full_name": "Paulina",
        "profile_pic_url": "https://scontent-lis1-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "created_at_utc": "2025-11-30T07:52:06Z",
      "content_type": "comment",
      "status": "Active",
      "has_liked": false,
      "like_count": 3
    },
    {
      "pk": "17992046705899459",
      "text": "😍😍😍amazing",
      "user": {
        "pk": "1791264033",
        "id": "1791264033",
        "username": "victoria.mvr",
        "full_name": "Victoria💫",
        "profile_pic_url": "https://scontent-lis1-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": true,
        "is_verified": false
      },
      "created_at_utc": "2025-11-29T22:20:18Z",
      "content_type": "comment",
      "status": "Active",
      "has_liked": false,
      "like_count": 4
    },
    {
      "pk": "18178774921320754",
      "text": "God bless our planet 💚🙏",
      "user": {
        "pk": "5646775780",
        "id": "5646775780",
        "username": "adriana.prn.71",
        "full_name": "Adriana Peñaloza",
        "profile_pic_url": "https://scontent-lis1-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": true,
        "is_verified": false
      },
      "created_at_utc": "2025-11-30T00:38:59Z",
      "content_type": "comment",
      "status": "Active",
      "has_liked": false,
      "like_count": 35
    }
  ],
  "IntcImNhY2hlZF9jb21tZW50c19jdXJzb3JcIjpcIjE4MDUzOTA1MDI1NjYyNTA3XCIsXCJiaWZpbHRlcl90b2tlblwiOlwiR2dZWWdRRUFkVzNGVnRDTlB3QkREUnJFcENKQkFNUDNyOUNyNno4QU1obWozWC1WUUFEZXZ1NnZac2NfQU1KTWQyWEZwVDhBMWdrRzZEUVFRQUJhTGg2bV9VQkJBQ0VLWVdLYmZVQUFVOFpNblY1UVFBQXVmY2xwekhvX0FMc0lvT0JzRzBBQUpSX2YxWVVfUUFBMVVNSHlZTVVfQUR4RmRHYUJLRUFBdl8xY01WNk5Qd0FBXCJ9Ig==",
  null
]
```

</details>

---

### GET /v1/media/insight

Get media insight

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_id` | string | Yes | Media Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/insight?media_id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_insight_v1(media_id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/insight",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"media_id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/insight?media_id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "id": "18065011277571522",
  "creation_time": 1764453631,
  "has_product_tags": false,
  "instagram_media_id": "3776832898280228145",
  "instagram_media_owner_id": "787132",
  "instagram_actor": {
    "instagram_actor_id": "503011999733264",
    "id": "17841400573960012"
  },
  "inline_insights_node": null,
  "display_url": "https://scontent-dfw5-2.cdninstagram.com/...",
  "instagram_media_type": "VIDEO",
  "image": {
    "height": 640,
    "width": 360
  },
  "comment_count": 485,
  "like_count": 135428,
  "save_count": null,
  "ad_media": null,
  "organic_instagram_media_id": "3776832898280228145",
  "shopping_outbound_click_count": null,
  "shopping_product_click_count": null,
  "shopping_product_insights": {
    "shopping_product_by_tag_click_count": [],
    "shopping_product_by_tag_outbound_click_count": []
  }
}
```

</details>

---

### GET /v1/media/likers

Get user's likers. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/likers?id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_likers_v1(id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/likers",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/likers?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "1469722832",
    "id": "1469722832",
    "username": "jorge10.ds",
    "full_name": "🅙orge Delgado 🦖",
    "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/...",
    "is_private": true,
    "is_verified": false
  },
  {
    "pk": "48158574428",
    "id": "48158574428",
    "username": "only_looking_at_fashionpeople",
    "full_name": "",
    "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/...",
    "is_private": true,
    "is_verified": false
  },
  {
    "pk": "77145556919",
    "id": "77145556919",
    "username": "xin.wei.chang261891",
    "full_name": "張心瑋",
    "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
    "is_private": false,
    "is_verified": true
  }
]
```

</details>

---

### GET /v1/media/oembed

Return info about media and user from post URL

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/oembed?url=https://www.instagram.com/p/DRqAYKuAIUx/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_oembed_v1(url="https://www.instagram.com/p/DRqAYKuAIUx/")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/oembed",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/p/DRqAYKuAIUx/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/oembed?url=https://www.instagram.com/p/DRqAYKuAIUx/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "title": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
  "author_name": "natgeo",
  "author_url": "https://www.instagram.com/natgeo",
  "author_id": "787132",
  "media_id": "3776832898280228145_787132",
  "provider_name": "Instagram",
  "provider_url": "https://www.instagram.com",
  "type": "rich",
  "width": 658,
  "height": null,
  "html": "<blockquote class=\"instagram-media\" data-instgrm-captioned data-instgrm-permalink=\"https://www.instagram.com/reel/DRqAYKuAIUx/?utm_source=ig_embed&amp;utm_campaign=loading\" data-instgrm-version=\"14\" style=\" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:658px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);\"><div style=\"padding:16px;\"> <a href=\"https://www.instagram.com/reel/DRqAYKuAIUx/?utm_source=ig_embed&amp;utm_campaign=loading\" style=\" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;\" target=\"_blank\"> <div style=\" display: flex; flex-direction: row; align-items: center;\"> <div style=\"background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;\"></div> <div style=\"display: flex; flex-direction: column; flex-grow: 1; justify-content: center;\"> <div style=\" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;\"></div> <div style=\" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;\"></div></div></div><div style=\"padding: 19% 0;\"></div> <div style=\"display:block; height:50px; margin:0 auto 12px; width:50px;\"><svg width=\"50px\" height=\"50px\" viewBox=\"0 0 60 60\" version=\"1.1\" xmlns=\"https://www.w3.org/2000/svg\" xmlns:xlink=\"https://www.w3.org/1999/xlink\"><g stroke=\"none\" stroke-width=\"1\" fill=\"none\" fill-rule=\"evenodd\"><g transform=\"translate(-511.000000, -20.000000)\" fill=\"#000000\"><g><path d=\"M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631\"></path></g></g></g></svg></div><div style=\"padding-top: 8px;\"> <div style=\" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;\">View this post on Instagram</div></div><div style=\"padding: 12.5% 0;\"></div> <div style=\"display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;\"><div> <div style=\"background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);\"></div> <div style=\"background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;\"></div> <div style=\"background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);\"></div></div><div style=\"margin-left: 8px;\"> <div style=\" background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;\"></div> <div style=\" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)\"></div></div><div style=\"margin-left: auto;\"> <div style=\" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);\"></div> <div style=\" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);\"></div> <div style=\" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);\"></div></div></div> <div style=\"display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;\"> <div style=\" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;\"></div> <div style=\" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;\"></div></div></a><p style=\" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;\"><a href=\"https://www.instagram.com/reel/DRqAYKuAIUx/?utm_source=ig_embed&amp;utm_campaign=loading\" style=\" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;\" target=\"_blank\">A post shared by National Geographic (@natgeo)</a></p></div></blockquote>\n<script async src=\"//www.instagram.com/embed.js\"></script>",
  "thumbnail_url": "https://scontent-jnb2-1.cdninstagram.com/...",
  "thumbnail_width": 640,
  "thumbnail_height": 1137,
  "can_view": null
}
```

</details>

---

### GET /v1/media/pk/from/code

Get media pk from code

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `code` | string | Yes | Code |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/pk/from/code?code=DRqAYKuAIUx"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_pk_from_code_v1(code="DRqAYKuAIUx")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/pk/from/code",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"code": "DRqAYKuAIUx"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/pk/from/code?code=DRqAYKuAIUx",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
"3776832898280228145"
```

</details>

---

### GET /v1/media/pk/from/url

Get Media pk from URL

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/pk/from/url?url=https://www.instagram.com/p/DRqAYKuAIUx/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_pk_from_url_v1(url="https://www.instagram.com/p/DRqAYKuAIUx/")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/pk/from/url",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/p/DRqAYKuAIUx/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/pk/from/url?url=https://www.instagram.com/p/DRqAYKuAIUx/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
"3776832898280228145"
```

</details>

---

### GET /v1/media/user

Get author of the media

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_id` | string | Yes | Media Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/user?media_id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_user_v1(media_id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/user",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"media_id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/user?media_id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "787132",
  "id": "787132",
  "username": "natgeo",
  "full_name": "National Geographic",
  "profile_pic_url": "https://scontent-mia3-2.cdninstagram.com/...",
  "is_private": false,
  "is_verified": true
}
```

</details>

---

## Deprecated endpoints

These endpoints are deprecated — use the recommended alternatives. Retired ones respond with **410 Gone** and are never charged (see [Response Codes](../response-codes.md)); the rest still work but will be removed in a future version.

### ~~GET /v1/media/comments~~

!!! warning
    Get media comments (one request is required for every 20 comments)

### ~~GET /v1/media/download/photo~~

!!! warning
    Photo Download

### ~~GET /v1/media/download/photo/by/url~~

!!! warning
    Photo Download By Url

### ~~GET /v1/media/download/video~~

!!! warning
    Video Download

### ~~GET /v1/media/download/video/by/url~~

!!! warning
    Video Download By Url

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-media){ target=_blank }
