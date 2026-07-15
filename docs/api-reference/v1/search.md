# Search Endpoints

Search users, hashtags, locations, and music.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v1/fbsearch/places`](#get-v1fbsearchplaces) | [`/v1/fbsearch/topsearch/hashtags`](#get-v1fbsearchtopsearchhashtags) | [`/v1/search/hashtags`](#get-v1searchhashtags) | [`/v1/search/music`](#get-v1searchmusic) | [`/v1/search/users`](#get-v1searchusers) | [`/v1/share/by/code`](#get-v1sharebycode) | [`/v1/share/by/url`](#get-v1sharebyurl) | [`/v1/share/reel/by/url`](#get-v1sharereelbyurl)

---

### GET /v1/fbsearch/places

Search locations. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |
| `lat` | number | No | Lat |
| `lng` | number | No | Lng |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/fbsearch/places?query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.fbsearch_places_v1(query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/fbsearch/places",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/fbsearch/places?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": 252923412072688,
    "name": "NatGeo Roof Deck",
    "phone": "",
    "website": "",
    "category": "",
    "hours": {},
    "address": "161 6th Ave",
    "city": "",
    "zip": null,
    "lng": -74.004295349121,
    "lat": 40.725898742676,
    "external_id": "252923412072688",
    "external_id_source": "facebook_places"
  },
  {
    "pk": 617882014,
    "name": "أسرار Nat Geo",
    "phone": "",
    "website": "",
    "category": "",
    "hours": {},
    "address": "625 Union St",
    "city": "",
    "zip": null,
    "lng": -73.98444,
    "lat": 40.67817,
    "external_id": "219266724863910",
    "external_id_source": "facebook_places"
  },
  {
    "pk": 103142692753506,
    "name": "NatGeo Fish",
    "phone": "",
    "website": "",
    "category": "",
    "hours": {},
    "address": "8593 Fawn St. Brooklyn",
    "city": "",
    "zip": null,
    "lng": -73.89254,
    "lat": 40.66595,
    "external_id": "103142692753506",
    "external_id_source": "facebook_places"
  }
]
```

</details>

---

### GET /v1/fbsearch/topsearch/hashtags

Search hashtags via topsearch. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/fbsearch/topsearch/hashtags?query=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.fbsearch_topsearch_hashtags_v1(query="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/fbsearch/topsearch/hashtags",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"query": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/fbsearch/topsearch/hashtags?query=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[]
```

</details>

---

### GET /v1/search/hashtags

Search hashtags. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/search/hashtags?query=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.search_hashtags_v1(query="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/search/hashtags",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"query": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/search/hashtags?query=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "id": "17843826142012701",
    "name": "love",
    "media_count": 2147483647,
    "allow_following": false,
    "profile_pic_url": null
  },
  {
    "id": "17843851987047311",
    "name": "lovehim",
    "media_count": 41384631,
    "allow_following": false,
    "profile_pic_url": null
  },
  {
    "id": "17843776981016110",
    "name": "lovestory",
    "media_count": 38695836,
    "allow_following": false,
    "profile_pic_url": null
  }
]
```

</details>

---

### GET /v1/search/music

Search music. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/search/music?query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.search_music_v1(query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/search/music",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/search/music?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "id": "1283502475113803",
    "title": "National Geographic",
    "subtitle": "",
    "display_artist": "Winterlight",
    "audio_cluster_id": "2045685665695806",
    "artist_id": null,
    "cover_artwork_uri": "https://scontent-atl3-1.cdninstagram.com/...",
    "cover_artwork_thumbnail_uri": "https://scontent-atl3-1.cdninstagram.com/...",
    "fast_start_progressive_download_url": "https://scontent-atl3-3.cdninstagram.com/...",
    "reactive_audio_download_url": null,
    "highlight_start_times_in_ms": [
      113000,
      128500,
      1500
    ],
    "is_explicit": false,
    "has_lyrics": false,
    "audio_asset_id": "1283502475113803",
    "duration_in_ms": 345560,
    "dark_message": null,
    "allows_saving": false,
    "territory_validity_periods": null
  },
  {
    "id": "3071277199804105",
    "title": "Until I Found You",
    "subtitle": "",
    "display_artist": "Stephen Sanchez, Em Beihold",
    "audio_cluster_id": "354492766725899",
    "artist_id": null,
    "cover_artwork_uri": "https://scontent-atl3-1.cdninstagram.com/...",
    "cover_artwork_thumbnail_uri": "https://scontent-atl3-1.cdninstagram.com/...",
    "fast_start_progressive_download_url": "https://scontent-atl3-1.cdninstagram.com/...",
    "reactive_audio_download_url": null,
    "highlight_start_times_in_ms": [
      27000,
      93000,
      66500
    ],
    "is_explicit": false,
    "has_lyrics": false,
    "audio_asset_id": "3071277199804105",
    "duration_in_ms": 176440,
    "dark_message": null,
    "allows_saving": false,
    "territory_validity_periods": null
  },
  {
    "id": "796720467705509",
    "title": "Nanila",
    "subtitle": "",
    "display_artist": "Sukhishvili Georgian National Ballet",
    "audio_cluster_id": "521947385822142",
    "artist_id": null,
    "cover_artwork_uri": "https://scontent-atl3-2.cdninstagram.com/...",
    "cover_artwork_thumbnail_uri": "https://scontent-atl3-2.cdninstagram.com/...",
    "fast_start_progressive_download_url": "https://scontent-atl3-2.cdninstagram.com/...",
    "reactive_audio_download_url": null,
    "highlight_start_times_in_ms": [
      45000,
      91000,
      60000
    ],
    "is_explicit": false,
    "has_lyrics": false,
    "audio_asset_id": "796720467705509",
    "duration_in_ms": 247680,
    "dark_message": null,
    "allows_saving": false,
    "territory_validity_periods": null
  }
]
```

</details>

---

### GET /v1/search/users

Search users. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/search/users?query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.search_users_v1(query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/search/users",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/search/users?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": 787132,
    "id": "787132",
    "username": "natgeo",
    "full_name": "National Geographic",
    "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/...",
    "profile_pic_url_hd": null,
    "is_private": null,
    "is_verified": null
  },
  {
    "pk": 1934468093,
    "id": "1934468093",
    "username": "natgeo_africa",
    "full_name": "Nat Geo Channel Africa",
    "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/...",
    "profile_pic_url_hd": null,
    "is_private": null,
    "is_verified": null
  },
  {
    "pk": 23947096,
    "id": "23947096",
    "username": "natgeotravel",
    "full_name": "National Geographic Travel",
    "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/...",
    "profile_pic_url_hd": null,
    "is_private": null,
    "is_verified": null
  }
]
```

</details>

---

### GET /v1/share/by/code

Get share object by code (aGlnaGxpZ2h0OjE4MTQ2MjE2Njk4MDIyMTc0 ->
{"pk": 18146216698022176, "type": "highlight"}). Returns shared content data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `code` | string | Yes | Code |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/share/by/code?code=aGlnaGxpZ2h0OjE3ODkzMjA5ODI1MjgxMjIx"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.share_by_code_v1(code="aGlnaGxpZ2h0OjE3ODkzMjA5ODI1MjgxMjIx")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/share/by/code",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"code": "aGlnaGxpZ2h0OjE3ODkzMjA5ODI1MjgxMjIx"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/share/by/code?code=aGlnaGxpZ2h0OjE3ODkzMjA5ODI1MjgxMjIx",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "17893209825281221",
  "type": "highlight"
}
```

</details>

---

### GET /v1/share/by/url

Get share object by url (
https://www.ins...ram.com/s/aGlnaGxpZ2h0OjE4MTQ2MjE2Njk4MDIyMTc0 ->
{"pk": 18146216698022176, "type": "highlight"}). Returns shared content data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/share/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.share_by_url_v1(url="https://www.instagram.com/p/DRqAYKuAIUx/")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/share/by/url",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/p/DRqAYKuAIUx/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/share/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/share/reel/by/url

Returns shared content data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/share/reel/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.share_reel_by_url_v1(url="https://www.instagram.com/p/DRqAYKuAIUx/")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/share/reel/by/url",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/p/DRqAYKuAIUx/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/share/reel/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

## Deprecated endpoints

These endpoints are deprecated — use the recommended alternatives. Retired ones respond with **410 Gone** and are never charged (see [Response Codes](../response-codes.md)); the rest still work but will be removed in a future version.

### ~~GET /v1/fbsearch/topsearch~~

!!! warning
    Use /gql/topsearch instead (broken upstream — IG returns 5xx)

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-search){ target=_blank }
