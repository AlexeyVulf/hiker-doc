# User Endpoints

Get user profiles, followers, following lists, and search.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v1/user/about`](#get-v1userabout) | [`/v1/user/by/id`](#get-v1userbyid) | [`/v1/user/by/url`](#get-v1userbyurl) | [`/v1/user/by/username`](#get-v1userbyusername) | [`/v1/user/clips/chunk`](#get-v1userclipschunk) | [`/v1/user/followers/chunk`](#get-v1userfollowerschunk) | [`/v1/user/following/chunk`](#get-v1userfollowingchunk) | [`/v1/user/medias/chunk`](#get-v1usermediaschunk) | [`/v1/user/medias/pinned`](#get-v1usermediaspinned) | [`/v1/user/search/followers`](#get-v1usersearchfollowers) | [`/v1/user/search/following`](#get-v1usersearchfollowing) | [`/v1/user/tag/medias/chunk`](#get-v1usertagmediaschunk)

---

### GET /v1/user/about

Get the "About this account" panel for a user: verified status,
country of registration, date the account was created, and the list
of former usernames. Returns user about info.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/about?id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_about_v1(id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/about",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/about?id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "username": "natgeo",
  "is_verified": true,
  "country": "United States",
  "date": "November 2010",
  "former_usernames": ""
}
```

</details>

---

### GET /v1/user/by/id

Get user object by id. Returns a User object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/by/id?id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_by_id_v1(id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/by/id",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/by/id?id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": 787132,
  "username": "natgeo",
  "full_name": "National Geographic",
  "is_private": false,
  "profile_pic_url": "https://scontent-fra3-1.cdninstagram.com/...",
  "profile_pic_url_hd": null,
  "is_verified": true,
  "media_count": 31529,
  "follower_count": 274988955,
  "following_count": 193,
  "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
  "external_url": "http://visitstore.bio/natgeo",
  "account_type": 2,
  "is_business": true,
  "public_email": "",
  "contact_phone_number": "",
  "public_phone_country_code": "",
  "public_phone_number": "",
  "business_contact_method": "UNKNOWN",
  "business_category_name": null,
  "category_name": null,
  "category": "",
  "address_street": "",
  "city_id": "0",
  "city_name": "",
  "latitude": null,
  "longitude": null,
  "zip": "",
  "instagram_location_id": "",
  "interop_messaging_user_fbid": 113671860027320
}
```

</details>

---

### GET /v1/user/by/url

Get user object by URL. Returns a User object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/by/url?url=https://www.instagram.com/natgeo/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_by_url_v1(url="https://www.instagram.com/natgeo/")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/by/url",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/natgeo/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/by/url?url=https://www.instagram.com/natgeo/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": 787132,
  "username": "natgeo",
  "full_name": "National Geographic",
  "is_private": false,
  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
  "profile_pic_url_hd": null,
  "is_verified": true,
  "media_count": 31529,
  "follower_count": 274988955,
  "following_count": 193,
  "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
  "external_url": "http://visitstore.bio/natgeo",
  "account_type": 2,
  "is_business": true,
  "public_email": "",
  "contact_phone_number": "",
  "public_phone_country_code": "",
  "public_phone_number": "",
  "business_contact_method": "UNKNOWN",
  "business_category_name": null,
  "category_name": null,
  "category": "",
  "address_street": "",
  "city_id": "0",
  "city_name": "",
  "latitude": null,
  "longitude": null,
  "zip": "",
  "instagram_location_id": "",
  "interop_messaging_user_fbid": 113671860027320
}
```

</details>

---

### GET /v1/user/by/username

Get user object by username. Returns a User object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/by/username?username=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_by_username_v1(username="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/by/username",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/by/username?username=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": 787132,
  "username": "natgeo",
  "full_name": "National Geographic",
  "is_private": false,
  "profile_pic_url": "https://scontent-lis1-1.cdninstagram.com/...",
  "profile_pic_url_hd": null,
  "is_verified": true,
  "media_count": 31529,
  "follower_count": 274988955,
  "following_count": 193,
  "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
  "external_url": "http://visitstore.bio/natgeo",
  "account_type": 2,
  "is_business": true,
  "public_email": "",
  "contact_phone_number": "",
  "public_phone_country_code": "",
  "public_phone_number": "",
  "business_contact_method": "UNKNOWN",
  "business_category_name": null,
  "category_name": null,
  "category": "",
  "address_street": "",
  "city_id": "0",
  "city_name": "",
  "latitude": null,
  "longitude": null,
  "zip": "",
  "instagram_location_id": "",
  "interop_messaging_user_fbid": 113671860027320
}
```

</details>

---

### GET /v1/user/clips/chunk

Get part of user clips with cursor

The response includes trial publications
https://help.instagram.com/1013292530224018

Trial publications have no "reshare_count" field if you need to filter them. Returns a list of Media objects (Reels).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `end_cursor` | string | No | End Cursor |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/clips/chunk?user_id=787132"
    # Next page: add &end_cursor=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_clips_chunk_v1(user_id="787132")
    # Next page: cl.user_clips_chunk_v1(user_id="787132", end_cursor="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/clips/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "end_cursor": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/clips/chunk?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    // Next page: add &end_cursor=... to URL
    ```

<details>
<summary>Example response</summary>

```json
[
  [
    {
      "pk": "3870025531093850440",
      "id": "3870025531093850440_1029649300",
      "code": "DW1F7dciplI",
      "taken_at": "2026-04-07T13:00:04Z",
      "taken_at_ts": 1775566804,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-sea5-1.cdninstagram.com/...",
      "location": null,
      "user": {
        "pk": "1029649300",
        "id": "1029649300",
        "username": "natgeoanimals",
        "full_name": "National Geographic Animals",
        "profile_pic_url": "https://scontent-sea1-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      },
      "comment_count": 499,
      "comments_disabled": false,
      "like_count": 51252,
      "play_count": 2625727,
      "has_liked": false,
      "caption_text": "Intruder alert! 🚨 Murder Hornets eat bees and their larvae, but these Asian honey bees aren't going to let their hive be destroyed without a fight. \n\n#SecretsOfTheBees is now streaming on @DisneyPlus and @hulu",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-sea5-1.cdninstagram.com/...",
      "view_count": 0,
      "video_duration": 60.736000061035156,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            18248,
            36496,
            54745
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-sea5-1.cdninstagram.com/...",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 1579353,
          "height": 1280,
          "id": "4284559321859069v",
          "type": 101,
          "url": "https://scontent-sea5-1.cdninstagram.com/...",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [
        {
          "strong_id__": "787132",
          "pk": 787132,
          "pk_id": "787132",
          "id": "787132",
          "username": "natgeo",
          "full_name": "National Geographic",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-sea1-1.cdninstagram.com/..."
        }
      ],
      "is_paid_partnership": false
    },
    {
      "pk": "3869494020385423326",
      "id": "3869494020385423326_787132",
      "code": "DWzNE9hkj_e",
      "taken_at": "2026-04-06T19:00:16Z",
      "taken_at_ts": 1775502016,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-sea1-1.cdninstagram.com/...",
      "location": null,
      "user": {
        "pk": "787132",
        "id": "787132",
        "username": "natgeo",
        "full_name": "National Geographic",
        "profile_pic_url": "https://scontent-sea1-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      },
      "comment_count": 65,
      "comments_disabled": false,
      "like_count": 11175,
      "play_count": 1496248,
      "has_liked": false,
      "caption_text": "In Hoppers, Piper Curda’s character Mabel explored her sense of wonder for the natural world with the help of hopping technology. For now, we still have to do it the old-fashioned way.\n\nSee Disney and Pixar’s new movie Hoppers, now playing, only in theaters, and step into wonder with National Geographic’s #EarthMonth collection on @DisneyPlus.",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-sea5-1.cdninstagram.com/...",
      "view_count": 0,
      "video_duration": 55.44499969482422,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            13479,
            26958,
            40438
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
          "bandwidth": 1113315,
          "height": 1280,
          "id": "2358585431274531v",
          "type": 101,
          "url": "https://scontent-sea5-1.cdninstagram.com/...",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [
        {
          "strong_id__": "284634753",
          "pk": 284634753,
          "pk_id": "284634753",
          "id": "284634753",
          "username": "pixar",
          "full_name": "Pixar",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3715495057937025462_284634753",
          "profile_pic_url": "https://scontent-sea1-1.cdninstagram.com/..."
        },
        {
          "strong_id__": "18091046",
          "pk": 18091046,
          "pk_id": "18091046",
          "id": "18091046",
          "username": "natgeotv",
          "full_name": "National Geographic TV",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865691934048399589_18091046",
          "profile_pic_url": "https://scontent-sea1-1.cdninstagram.com/..."
        }
      ],
      "is_paid_partnership": false
    },
    {
      "pk": "3868170261056492782",
      "id": "3868170261056492782_787132",
      "code": "DWugFulAJTu",
      "taken_at": "2026-04-05T16:00:10Z",
      "taken_at_ts": 1775404810,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-sea5-1.cdninstagram.com/...",
      "location": null,
      "user": {
        "pk": "787132",
        "id": "787132",
        "username": "natgeo",
        "full_name": "National Geographic",
        "profile_pic_url": "https://scontent-sea1-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      },
      "comment_count": 78,
      "comments_disabled": false,
      "like_count": 7490,
      "play_count": 1307765,
      "has_liked": false,
      "caption_text": "Spotted hyenas are a powerful example of the resilience and strength found in nature. For wildlife ecologist, conservation scientist, and National Geographic Explorer Dr. Christine Wilkinson (@christine_eleanor), these reminders are what wonder is all about. \n\n#StepIntoWonder with National Geographic’s #EarthMonth collection on @DisneyPlus.",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-sea5-1.cdninstagram.com/...",
      "view_count": 0,
      "video_duration": 47.893001556396484,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            18831,
            37662,
            56494
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-sea5-1.cdninstagram.com/...",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 1064730,
          "height": 1280,
          "id": "799234956583164v",
          "type": 101,
          "url": "https://scontent-sea5-1.cdninstagram.com/...",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [
        {
          "strong_id__": "271370325",
          "pk": 271370325,
          "pk_id": "271370325",
          "id": "271370325",
          "username": "christine_eleanor",
          "full_name": "christine wilkinson, phd",
          "is_private": false,
          "is_verified": false,
          "profile_pic_id": "3245086179333885169_271370325",
          "profile_pic_url": "https://scontent-sea1-1.cdninstagram.com/..."
        }
      ],
      "is_paid_partnership": false
    }
  ],
  "QVFBS1NTZjNnYzQ0X2k3cDNuTUZWb2QxTTRHZ3V2a2dPWUx6Ti1yMjdSOWVWSkpvanZFbFcxSjc0YjVNdmh4MFJranozbTNReFg5bGJYaEJwUENUNmxicw=="
]
```

</details>

---

### GET /v1/user/followers/chunk

Get part (one page) of followers users with cursor. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/followers/chunk?user_id=787132"
    # Next page: add &max_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_followers_chunk_v1(user_id="787132")
    # Next page: cl.user_followers_chunk_v1(user_id="787132", max_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/followers/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "max_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/followers/chunk?user_id=787132",
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
      "pk": "43714748721",
      "id": "43714748721",
      "username": "shruti_pvttttttt",
      "full_name": "",
      "profile_pic_url": "https://instagram.ffbe3-1.fna.fbcdn.net/v/t51.2885-19/573323465_1219825463302212_7278921664109726296_n.png?stp=dst-webp&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=instagram.ffbe3-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gGSXSvPUsAQIGGg74eSceuqb6Q4kir2zKYfnTk1gxLxfH7bzhLlBxhhXLvXlJ_2kyxV_p3-JbZ9BVUR9z1M8kd1&_nc_ohc=xpiLrADWZlUQ7kNvwHWqZ-C&_nc_gid=-eqti3INcuPT52NbMzaoVA&edm=AJ9x6zYBAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.3-ccb7-5&oh=00_Af1Z7e41pQbQqlg7yEWiW75KQFsD46Fv2EagEvdtrl-WTQ&oe=69DC6EAA&_nc_sid=65462d",
      "is_private": true,
      "is_verified": false
    },
    {
      "pk": "60997697028",
      "id": "60997697028",
      "username": "sisforspiderman",
      "full_name": "자살",
      "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/...",
      "is_private": true,
      "is_verified": false
    },
    {
      "pk": "68506469492",
      "id": "68506469492",
      "username": "its_raviranjan_ydv_18",
      "full_name": "🤘💝only RCB fan💝🤘",
      "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/...",
      "is_private": false,
      "is_verified": false
    }
  ],
  null
]
```

</details>

---

### GET /v1/user/following/chunk

Get part (one page) of following users with cursor. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/following/chunk?user_id=787132"
    # Next page: add &max_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_following_chunk_v1(user_id="787132")
    # Next page: cl.user_following_chunk_v1(user_id="787132", max_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/following/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "max_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/following/chunk?user_id=787132",
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
      "pk": "14331657700",
      "id": "14331657700",
      "username": "natgeomagjp",
      "full_name": "ナショナルジオグラフィック日本版",
      "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/...",
      "is_private": false,
      "is_verified": false
    },
    {
      "pk": "8958735",
      "id": "8958735",
      "username": "christiehemmklok",
      "full_name": "Christie Hemm Klok",
      "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/...",
      "is_private": false,
      "is_verified": true
    },
    {
      "pk": "2558720332",
      "id": "2558720332",
      "username": "natgeouk",
      "full_name": "National Geographic UK",
      "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/...",
      "is_private": false,
      "is_verified": true
    }
  ],
  "25"
]
```

</details>

---

### GET /v1/user/medias/chunk

Get part of user medias with cursor. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `end_cursor` | string | No | End Cursor |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/medias/chunk?user_id=787132"
    # Next page: add &end_cursor=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_medias_chunk_v1(user_id="787132")
    # Next page: cl.user_medias_chunk_v1(user_id="787132", end_cursor="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/medias/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "end_cursor": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/medias/chunk?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    // Next page: add &end_cursor=... to URL
    ```

<details>
<summary>Example response</summary>

```json
[
  [
    {
      "pk": "3865659729796199935",
      "id": "3865659729796199935_787132",
      "code": "DWllQsJCPX_",
      "taken_at": "2026-04-01T13:00:03Z",
      "taken_at_ts": 1775048403,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/...",
      "location": null,
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
      "comment_count": 236,
      "comments_disabled": false,
      "like_count": 35895,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "This Earth Month, step into wonder with National Geographic as we celebrate everything that makes our planet so extraordinary 🌍\n\nStream the National Geographic #EarthMonth collection all April long on @DisneyPlus. #StepIntoWonder",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-dfw5-1.cdninstagram.com/...",
      "view_count": 0,
      "video_duration": 60.10100173950195,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            24827,
            49654,
            74482
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-2.cdninstagram.com/...",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 1568436,
          "height": 1280,
          "id": "1258679306414510v",
          "type": 101,
          "url": "https://scontent-dfw5-1.cdninstagram.com/...",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [
        {
          "strong_id__": "18091046",
          "pk": 18091046,
          "pk_id": "18091046",
          "id": "18091046",
          "username": "natgeotv",
          "full_name": "National Geographic TV",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865691934048399589_18091046",
          "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/..."
        },
        {
          "strong_id__": "284634734",
          "pk": 284634734,
          "pk_id": "284634734",
          "id": "284634734",
          "username": "disney",
          "full_name": "Disney",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3859143390382675003_284634734",
          "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/..."
        }
      ],
      "is_paid_partnership": false
    },
    {
      "pk": "3844732796656436386",
      "id": "3844732796656436386_787132",
      "code": "DVbPBu5AESi",
      "taken_at": "2026-03-03T15:00:04Z",
      "taken_at_ts": 1772550004,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/...",
      "location": null,
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
      "comment_count": 614,
      "comments_disabled": false,
      "like_count": 66086,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Small in size, but their impact on our planet is huge 🐝 Join @bertiegregory as he explores the weird and wonderful world of bees.\n\n#SecretsOfTheBees premieres Tuesday, March 31 at 8/7c on @natgeotv. Stream on @DisneyPlus and @hulu.",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-dfw5-1.cdninstagram.com/...",
      "view_count": 0,
      "video_duration": 60.07400131225586,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            48270,
            96540,
            144811
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-dfw6-1.cdninstagram.com/...",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 1607971,
          "height": 1280,
          "id": "1791310395606912v",
          "type": 101,
          "url": "https://scontent-dfw5-1.cdninstagram.com/...",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [
        {
          "strong_id__": "10506924608",
          "pk": 10506924608,
          "pk_id": "10506924608",
          "id": "10506924608",
          "username": "jamescameronofficial",
          "full_name": "James Cameron",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "1964371814524155358_10506924608",
          "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/..."
        },
        {
          "strong_id__": "1029649300",
          "pk": 1029649300,
          "pk_id": "1029649300",
          "id": "1029649300",
          "username": "natgeoanimals",
          "full_name": "National Geographic Animals",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865698702530758137_1029649300",
          "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/..."
        }
      ],
      "is_paid_partnership": false
    },
    {
      "pk": "3870670793969876810",
      "id": "3870670793969876810_787132",
      "code": "DW3YpRVDb9K",
      "taken_at": "2026-04-08T10:00:01Z",
      "taken_at_ts": 1775642401,
      "media_type": 8,
      "product_type": "carousel_container",
      "thumbnail_url": null,
      "location": null,
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
      "comment_count": 118,
      "comments_disabled": false,
      "like_count": 43706,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Whorls, hexagons, and half-moon patterns can be found throughout nature, formed by natural processes such as wind and crashing waves. After spending time along the seashore, photographer and conservationist Jon McCormack discovered that our planet's familiar shapes and designs have guided his work for years. To celebrate this, he set out on a journey to capture nature's intriguing forms at every scale.\n\nSee more of his work and learn about nature's patterns at the link in bio.\n\nPhotographs by @jonmccormackphoto, courtesy of Damiani’s upcoming book Jon McCormack: Patterns - Art of the Natural World",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [
        {
          "pk": "3870670683399590370",
          "id": "3870670683399590370_787132",
          "video_url": null,
          "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/...",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                56778,
                113556,
                170335
              ],
              "height": 959,
              "scans_profile": "e35",
              "url": "https://scontent-dfw6-1.cdninstagram.com/...",
              "width": 1439,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870670793969876810_787132",
          "commerciality_status": "not_commercial",
          "taken_at": 1775642401
        },
        {
          "pk": "3870670679968669302",
          "id": "3870670679968669302_787132",
          "video_url": null,
          "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/...",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                40239,
                80479,
                120719
              ],
              "height": 959,
              "scans_profile": "e35",
              "url": "https://scontent-dfw6-1.cdninstagram.com/...",
              "width": 1439,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870670793969876810_787132",
          "commerciality_status": "not_commercial",
          "taken_at": 1775642401
        },
        {
          "pk": "3870670694816531730",
          "id": "3870670694816531730_787132",
          "video_url": null,
          "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/...",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                51971,
                103943,
                155915
              ],
              "height": 1080,
              "scans_profile": "e35",
              "url": "https://scontent-dfw6-1.cdninstagram.com/...",
              "width": 1440,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870670793969876810_787132",
          "commerciality_status": "not_commercial",
          "taken_at": 1775642401
        }
      ],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            56778,
            113556,
            170335
          ],
          "height": 959,
          "scans_profile": "e35",
          "url": "https://scontent-dfw6-1.cdninstagram.com/...",
          "width": 1439,
          "is_spatial_image": false
        }
      ],
      "video_versions": [],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    }
  ],
  "3868170261056492782_787132"
]
```

</details>

---

### GET /v1/user/medias/pinned

Get user medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/medias/pinned?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_medias_pinned_v1(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/medias/pinned",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/medias/pinned?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "3865659729796199935",
    "id": "3865659729796199935_787132",
    "code": "DWllQsJCPX_",
    "taken_at": "2026-04-01T13:00:03Z",
    "taken_at_ts": 1775048403,
    "media_type": 2,
    "product_type": "clips",
    "thumbnail_url": "https://scontent-lga3-3.cdninstagram.com/...",
    "location": null,
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "comment_count": 236,
    "comments_disabled": false,
    "like_count": 35895,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "This Earth Month, step into wonder with National Geographic as we celebrate everything that makes our planet so extraordinary 🌍\n\nStream the National Geographic #EarthMonth collection all April long on @DisneyPlus. #StepIntoWonder",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-lga3-2.cdninstagram.com/...",
    "view_count": 0,
    "video_duration": 60.10100173950195,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          24827,
          49654,
          74482
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-lga3-3.cdninstagram.com/...",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [
      {
        "bandwidth": 1568436,
        "height": 1280,
        "id": "1258679306414510v",
        "type": 101,
        "url": "https://scontent-lga3-2.cdninstagram.com/...",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      }
    ],
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [
      {
        "strong_id__": "18091046",
        "pk": 18091046,
        "pk_id": "18091046",
        "id": "18091046",
        "username": "natgeotv",
        "full_name": "National Geographic TV",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865691934048399589_18091046",
        "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/..."
      },
      {
        "strong_id__": "284634734",
        "pk": 284634734,
        "pk_id": "284634734",
        "id": "284634734",
        "username": "disney",
        "full_name": "Disney",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3859143390382675003_284634734",
        "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/..."
      }
    ],
    "is_paid_partnership": false
  },
  {
    "pk": "3844732796656436386",
    "id": "3844732796656436386_787132",
    "code": "DVbPBu5AESi",
    "taken_at": "2026-03-03T15:00:04Z",
    "taken_at_ts": 1772550004,
    "media_type": 2,
    "product_type": "clips",
    "thumbnail_url": "https://scontent-lga3-3.cdninstagram.com/...",
    "location": null,
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "comment_count": 614,
    "comments_disabled": false,
    "like_count": 66086,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Small in size, but their impact on our planet is huge 🐝 Join @bertiegregory as he explores the weird and wonderful world of bees.\n\n#SecretsOfTheBees premieres Tuesday, March 31 at 8/7c on @natgeotv. Stream on @DisneyPlus and @hulu.",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-lga3-1.cdninstagram.com/...",
    "view_count": 0,
    "video_duration": 60.07400131225586,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          48270,
          96540,
          144811
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-lga3-3.cdninstagram.com/...",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [
      {
        "bandwidth": 1607971,
        "height": 1280,
        "id": "1791310395606912v",
        "type": 101,
        "url": "https://scontent-lga3-1.cdninstagram.com/...",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      }
    ],
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [
      {
        "strong_id__": "10506924608",
        "pk": 10506924608,
        "pk_id": "10506924608",
        "id": "10506924608",
        "username": "jamescameronofficial",
        "full_name": "James Cameron",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "1964371814524155358_10506924608",
        "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/..."
      },
      {
        "strong_id__": "1029649300",
        "pk": 1029649300,
        "pk_id": "1029649300",
        "id": "1029649300",
        "username": "natgeoanimals",
        "full_name": "National Geographic Animals",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865698702530758137_1029649300",
        "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/..."
      }
    ],
    "is_paid_partnership": false
  },
  {
    "pk": "3870670793969876810",
    "id": "3870670793969876810_787132",
    "code": "DW3YpRVDb9K",
    "taken_at": "2026-04-08T10:00:01Z",
    "taken_at_ts": 1775642401,
    "media_type": 8,
    "product_type": "carousel_container",
    "thumbnail_url": null,
    "location": null,
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "comment_count": 118,
    "comments_disabled": false,
    "like_count": 43706,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Whorls, hexagons, and half-moon patterns can be found throughout nature, formed by natural processes such as wind and crashing waves. After spending time along the seashore, photographer and conservationist Jon McCormack discovered that our planet's familiar shapes and designs have guided his work for years. To celebrate this, he set out on a journey to capture nature's intriguing forms at every scale.\n\nSee more of his work and learn about nature's patterns at the link in bio.\n\nPhotographs by @jonmccormackphoto, courtesy of Damiani’s upcoming book Jon McCormack: Patterns - Art of the Natural World",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [
      {
        "pk": "3870670683399590370",
        "id": "3870670683399590370_787132",
        "video_url": null,
        "thumbnail_url": "https://scontent-lga3-1.cdninstagram.com/...",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              56778,
              113556,
              170335
            ],
            "height": 959,
            "scans_profile": "e35",
            "url": "https://scontent-lga3-1.cdninstagram.com/...",
            "width": 1439,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870670793969876810_787132",
        "commerciality_status": "not_commercial",
        "taken_at": 1775642401
      },
      {
        "pk": "3870670679968669302",
        "id": "3870670679968669302_787132",
        "video_url": null,
        "thumbnail_url": "https://scontent-lga3-1.cdninstagram.com/...",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              40239,
              80479,
              120719
            ],
            "height": 959,
            "scans_profile": "e35",
            "url": "https://scontent-lga3-1.cdninstagram.com/...",
            "width": 1439,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870670793969876810_787132",
        "commerciality_status": "not_commercial",
        "taken_at": 1775642401
      },
      {
        "pk": "3870670694816531730",
        "id": "3870670694816531730_787132",
        "video_url": null,
        "thumbnail_url": "https://scontent-lga3-1.cdninstagram.com/...",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              51971,
              103943,
              155915
            ],
            "height": 1080,
            "scans_profile": "e35",
            "url": "https://scontent-lga3-1.cdninstagram.com/...",
            "width": 1440,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870670793969876810_787132",
        "commerciality_status": "not_commercial",
        "taken_at": 1775642401
      }
    ],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          56778,
          113556,
          170335
        ],
        "height": 959,
        "scans_profile": "e35",
        "url": "https://scontent-lga3-1.cdninstagram.com/...",
        "width": 1439,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  }
]
```

</details>

---

### GET /v1/user/search/followers

Search users by followers. Returns matching User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `query` | string | Yes | Query |
| `force` | boolean | No | Skip account privacy check |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/search/followers?user_id=787132&query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_search_followers_v1(user_id="787132", query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/search/followers",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132", "query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/search/followers?user_id=787132&query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "43714748721",
    "id": "43714748721",
    "username": "shruti_pvttttttt",
    "full_name": "",
    "profile_pic_url": "https://instagram.foss2-1.fna.fbcdn.net/v/t51.2885-19/573323465_1219825463302212_7278921664109726296_n.png?stp=dst-jpg_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=instagram.foss2-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gFLnin5QObKUUZfEFNjiCudxoqo7M_g2CU5Oe_G4-BtLihn4muDmdVfshUy01-tSm8&_nc_ohc=xpiLrADWZlUQ7kNvwGQ9TZw&_nc_gid=ZQGbpmf_utgSr9R9VGk5ow&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.3-ccb7-5&oh=00_Af1S2GvpaxsUT8rW0d6T9Ou_p8MTkTF1Yxm4jhtJhTGNIw&oe=69DC6EAA&_nc_sid=10d13b",
    "is_private": true,
    "is_verified": false
  },
  {
    "pk": "60997697028",
    "id": "60997697028",
    "username": "sisforspiderman",
    "full_name": "자살",
    "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/...",
    "is_private": true,
    "is_verified": false
  },
  {
    "pk": "46749442090",
    "id": "46749442090",
    "username": "salah_salah_1989",
    "full_name": "صالح Salah",
    "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/...",
    "is_private": false,
    "is_verified": false
  }
]
```

</details>

---

### GET /v1/user/search/following

Search users by following users. Returns matching User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `query` | string | Yes | Query |
| `force` | boolean | No | Skip account privacy check |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/search/following?user_id=787132&query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_search_following_v1(user_id="787132", query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/search/following",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132", "query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/search/following?user_id=787132&query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "23947096",
    "id": "23947096",
    "username": "natgeotravel",
    "full_name": "National Geographic Travel",
    "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
    "is_private": false,
    "is_verified": true
  },
  {
    "pk": "1029649300",
    "id": "1029649300",
    "username": "natgeoanimals",
    "full_name": "National Geographic Animals",
    "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
    "is_private": false,
    "is_verified": true
  },
  {
    "pk": "414805671",
    "id": "414805671",
    "username": "natgeoscience",
    "full_name": "National Geographic Science",
    "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
    "is_private": false,
    "is_verified": true
  }
]
```

</details>

---

### GET /v1/user/tag/medias/chunk

Get usertag medias

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/tag/medias/chunk?user_id=787132"
    # Next page: add &max_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_tag_medias_chunk_v1(user_id="787132")
    # Next page: cl.user_tag_medias_chunk_v1(user_id="787132", max_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/tag/medias/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "max_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/tag/medias/chunk?user_id=787132",
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
      "pk": "1929261108986102451",
      "id": "1929261108986102451_429173",
      "code": "BrGHMHIF8Kz",
      "taken_at": "2018-12-07T18:04:27Z",
      "taken_at_ts": 1544205867,
      "media_type": 1,
      "product_type": "feed",
      "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/...",
      "location": {
        "pk": 250376789,
        "name": "Vardzia, Aspindzis Raioni, Georgia",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "",
        "city": "",
        "zip": null,
        "lng": 43.2575,
        "lat": 41.3753,
        "external_id": "109068119127535",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "429173",
        "id": "429173",
        "username": "hynecheck",
        "full_name": "Hynek Hampl",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 579,
      "comments_disabled": false,
      "like_count": 14016,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Vardzia is a cave monastery site located in southern Georgia. It is excavated from the slopes of the Erusheti Mountain on the left side of the Kura River. Oh Georgia, I miss you when I look at these images 😭 #georgia #exploregeorgia #MavicPro\n.\n.\n.\n.\n.\n#mymavic #awesome_earthpix #collectivelycreate #exploretocreate #livefolk #beautifuldestinations #iglifecz #folkcreative #exklusive_shot #AGameOfTones #igerscz #discoverglobe #QueekyGrams #ourplanetdaily #adventureculture #welivetoexplore #stayandwander #dnescestujem #droneofficial #droneoftheday #dronesdaily #dji #fromwhereidrone #earthofficial #natgeo #MavicPro @beautifuldestinations @roamtheplanet @earthofficial @earthpix @folkmagazine @liveoutdoor.s @awesomeglobe @awesome.earth @djiglobal @fromwhereidrone @dronestagr.am @droneoftheday @droneofficial @earthstoke @livefolk @global_hotshotz @vzcomood @artofvisuals @majestic_earth_ @folkvibe @welivetoexplore @lastingvisuals @mountainsphoto @theglobewanderer @tentree @awesome.earth @awesomeglobe @ourplanetdaily",
      "accessibility_caption": null,
      "usertags": [
        {
          "user": {
            "pk": "1709655155",
            "id": "1709655155",
            "username": "fromwhereidrone",
            "full_name": "From Where I Drone®",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": false
          },
          "x": 0.9639999866000001,
          "y": 0.0160000008
        },
        {
          "user": {
            "pk": "195270438",
            "id": "195270438",
            "username": "wonderful_places",
            "full_name": "Wonderful Places",
            "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/...",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "x": 0.8700000048000001,
          "y": 0.0496000014
        },
        {
          "user": {
            "pk": "2280748136",
            "id": "2280748136",
            "username": "droneofficial",
            "full_name": "droneofficial™",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": false
          },
          "x": 0.9319999814000001,
          "y": 0.0912000015
        }
      ],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            50179,
            100358,
            150537
          ],
          "height": 1334,
          "scans_profile": "e35",
          "url": "https://scontent-dfw6-1.cdninstagram.com/...",
          "width": 1080,
          "is_spatial_image": false
        }
      ],
      "video_versions": [],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    },
    {
      "pk": "1929229904589027835",
      "id": "1929229904589027835_276524869",
      "code": "BrGAGBxFvn7",
      "taken_at": "2018-12-07T17:02:28Z",
      "taken_at_ts": 1544202148,
      "media_type": 1,
      "product_type": "feed",
      "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/...",
      "location": {
        "pk": 1141278516000361,
        "name": "Tàu Cát Bà Xanh",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "Số 235 , đường Cái Bèo ",
        "city": "",
        "zip": null,
        "lng": 107.05010223359,
        "lat": 20.724692987102,
        "external_id": "1141278516000361",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "276524869",
        "id": "276524869",
        "username": "samuellemieux",
        "full_name": "Samuel Lemieux",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 182,
      "comments_disabled": false,
      "like_count": 6172,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "No helmet needed once your on Cát Bà Island.\n.\nCát Bà Island || Vietnam\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\nShot on EOS T3i and SIGMA 85mm F1.4 EX DG HSM\nISO 100 | f/1.4 | 1/2000\n——\n#vietnam #vietnamese #vietnamesefood #vietnamflashback #vietnamesegirl #vietnamtravel #vietnamtrip #vietnamesehair #vietnamwar #vietnamesecuisine #vietnamflashbacks #vietnamesecoffee #vietnamfood #Canon #canonphotography #canonphoto #canon6d #canoneos #canonusa #canon70d #canon5dmarkiii #canon5d #canonaustralia #canonphotos #canon7d #canon60d #canon700d #canon5dmarkiv #canonphotographer #canoncanada",
      "accessibility_caption": null,
      "usertags": [
        {
          "user": {
            "pk": "1029649300",
            "id": "1029649300",
            "username": "natgeoanimals",
            "full_name": "National Geographic Animals",
            "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/...",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "x": 0.5,
          "y": 0.5
        },
        {
          "user": {
            "pk": "1315608830",
            "id": "1315608830",
            "username": "canonusa",
            "full_name": "Canon USA",
            "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/...",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "x": 0.5,
          "y": 0.5
        },
        {
          "user": {
            "pk": "1364955209",
            "id": "1364955209",
            "username": "travelawesome",
            "full_name": "TRAVEL AWESOME",
            "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/...",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": false
          },
          "x": 0.5,
          "y": 0.5
        }
      ],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            16232,
            32464,
            48696
          ],
          "height": 720,
          "scans_profile": "e35",
          "url": "https://scontent-dfw6-1.cdninstagram.com/...",
          "width": 1080,
          "is_spatial_image": false
        }
      ],
      "video_versions": [],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    },
    {
      "pk": "1929198769279088926",
      "id": "1929198769279088926_1423130965",
      "code": "BrF5A8wADke",
      "taken_at": "2018-12-07T16:00:36Z",
      "taken_at_ts": 1544198436,
      "media_type": 1,
      "product_type": "feed",
      "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/...",
      "location": {
        "pk": 109714185714936,
        "name": "Florida",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "",
        "city": "",
        "zip": null,
        "lng": -81.631666666667,
        "lat": 28.133333333333,
        "external_id": "109714185714936",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "1423130965",
        "id": "1423130965",
        "username": "canusatouristik",
        "full_name": "CANUSA TOURISTIK 🇺🇸 & 🇨🇦",
        "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 204,
      "comments_disabled": false,
      "like_count": 5581,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "☀️Warme Sonnenstrahlen, herrliche Seeluft und weicher Sandstrand - erlebt den ewigen Sommer in Florida😍 Die rund 700 Kilometer lange Landzunge zwischen dem Atlantik und dem Golf von Mexiko wird auch Sunshine State genannt und wird seinem Namen auf jeden Fall gerecht - rund 300 Sonnentage im Jahr kann man in dem US-Bundeststaat genießen.🏝#mycanusa #sunshinestate #visitflorida #florida #exploremore #visittheusa",
      "accessibility_caption": null,
      "usertags": [
        {
          "user": {
            "pk": "20388776",
            "id": "20388776",
            "username": "visittheusa",
            "full_name": "Visit The USA",
            "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/...",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "x": 0.4499999881,
          "y": 0.5911949873
        },
        {
          "user": {
            "pk": "28867825",
            "id": "28867825",
            "username": "visitflorida",
            "full_name": "VISITFLORIDA",
            "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/...",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "x": 0.7916666865,
          "y": 0.6509433985
        },
        {
          "user": {
            "pk": "57636",
            "id": "57636",
            "username": "lonelyplanet",
            "full_name": "Lonely Planet",
            "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/...",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "x": 0.5124999881,
          "y": 0.267295599
        }
      ],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            25149,
            50299,
            75448
          ],
          "height": 716,
          "scans_profile": "e35",
          "url": "https://scontent-dfw6-1.cdninstagram.com/...",
          "width": 1080,
          "is_spatial_image": false
        }
      ],
      "video_versions": [],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    }
  ],
  "1926933891264902156"
]
```

</details>

---

## Deprecated endpoints

These endpoints are deprecated — use the recommended alternatives. Retired ones respond with **410 Gone** and are never charged (see [Response Codes](../response-codes.md)); the rest still work but will be removed in a future version.

### ~~GET /v1/user/clips~~

!!! warning
    WARNING: Use v1/user/clips/chunk. Get user clips - first page

### ~~GET /v1/user/followers~~

!!! warning
    WARNING: Use /v2/user/followers of /v1/user/followers/chunk. Get first page user followers

### ~~GET /v1/user/following~~

!!! warning
    WARNING: Use /v2/user/following or /v1/user/following/chunk. Get first page user following

### ~~GET /v1/user/guides~~

!!! warning
    User Guides V1

### ~~GET /v1/user/medias~~

!!! warning
    WARNING: Use /v2/user/medias (better) or /v1/user/medias/chunk. Get user medias - first page

### ~~GET /v1/user/tag/medias~~

!!! warning
    Usertag Medias

### ~~GET /v1/user/videos~~

!!! warning
    Prefer using /v2/user/clips or /v2/user/medias instead

### ~~GET /v1/user/videos/chunk~~

!!! warning
    Prefer using /v2/user/clips or /v2/user/medias instead

### ~~GET /v1/user/web_profile_info~~

!!! warning
    WARNING: Deprecated. Instagram returns ~90% false UserNotFound since Feb 2, 2026. Use /gql/user/web_profile_info instead (accepts numeric user ID, much more reliable).

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-user){ target=_blank }
