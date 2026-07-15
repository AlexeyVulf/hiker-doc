# GraphQL API

Instagram GraphQL endpoints with cursor-based pagination.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/g1/user/followers`](#get-g1userfollowers) | [`/g1/user/following`](#get-g1userfollowing) | [`/g2/user/followers`](#get-g2userfollowers) | [`/g2/user/following`](#get-g2userfollowing) | [`/g2/user/medias`](#get-g2usermedias) | [`/gql/comment/likers/chunk`](#get-gqlcommentlikerschunk) | [`/gql/media/likers`](#get-gqlmedialikers) | [`/gql/media/usertags`](#get-gqlmediausertags) | [`/gql/topsearch`](#get-gqltopsearch) | [`/gql/user/about`](#get-gqluserabout) | [`/gql/user/clips`](#get-gqluserclips) | [`/gql/user/followers/chunk`](#get-gqluserfollowerschunk) | [`/gql/user/following/chunk`](#get-gqluserfollowingchunk) | [`/gql/user/medias`](#get-gqlusermedias) | [`/gql/user/reposts`](#get-gqluserreposts) | [`/gql/user/web_profile_info`](#get-gqluserweb_profile_info)

---

### GET /g1/user/followers

⚠️ Billing: 1 requests per call. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `end_cursor` | string | No | End Cursor |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/g1/user/followers?user_id=787132"
    # Next page: add &end_cursor=... from previous response
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/g1/user/followers",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "end_cursor": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/g1/user/followers?user_id=787132",
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
      "pk": "16456403414",
      "id": "16456403414",
      "username": "akaporto78j",
      "full_name": "",
      "profile_pic_url": "https://instagram.fsac1-2.fna.fbcdn.net/v/t51.2885-19/573323465_1219825463302212_7278921664109726296_n.png?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=instagram.fsac1-2.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gHFE3eBz3TDgeyKG-N4mRCcbEN7ETNgZrkI0Bc5cUEPCSlWPKkAkN6e5wehS-cjqbhcA2wDD0GlTm_dsYSVXKRi&_nc_ohc=bhH7TUwRnv4Q7kNvwFm-w3d&_nc_gid=fKdlCKrXGSXAhU90kYk5eQ&edm=AL4D0a4BAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.3-ccb7-5&oh=00_Af8Oo0p1T392rmVIMTTY1-B4CGfEWRC-v78igJCm81oySA&oe=6A430B6A&_nc_sid=9e8221",
      "is_private": false,
      "is_verified": false,
      "reel": {
        "id": 16456403414,
        "expiring_at": 1782478387,
        "has_pride_media": false,
        "latest_reel_media": 0,
        "owner": {
          "id": 16456403414,
          "profile_pic_url": "https://instagram.fsac1-2.fna.fbcdn.net/v/t51.2885-19/573323465_1219825463302212_7278921664109726296_n.png?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=instagram.fsac1-2.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gHFE3eBz3TDgeyKG-N4mRCcbEN7ETNgZrkI0Bc5cUEPCSlWPKkAkN6e5wehS-cjqbhcA2wDD0GlTm_dsYSVXKRi&_nc_ohc=bhH7TUwRnv4Q7kNvwFm-w3d&_nc_gid=fKdlCKrXGSXAhU90kYk5eQ&edm=AL4D0a4BAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.3-ccb7-5&oh=00_Af8Oo0p1T392rmVIMTTY1-B4CGfEWRC-v78igJCm81oySA&oe=6A430B6A&_nc_sid=9e8221",
          "username": "akaporto78j"
        }
      }
    },
    {
      "pk": "23983965254",
      "id": "23983965254",
      "username": "ridfebres",
      "full_name": "Richard Febres",
      "profile_pic_url": "https://scontent-fml1-1.cdninstagram.com/...",
      "is_private": false,
      "is_verified": false,
      "reel": {
        "id": 23983965254,
        "expiring_at": 1782478387,
        "has_pride_media": false,
        "latest_reel_media": 0,
        "owner": {
          "id": 23983965254,
          "profile_pic_url": "https://scontent-fml1-1.cdninstagram.com/...",
          "username": "ridfebres"
        }
      }
    },
    {
      "pk": "75427741203",
      "id": "75427741203",
      "username": "crips.susu",
      "full_name": "liiiiii",
      "profile_pic_url": "https://scontent-fml1-1.cdninstagram.com/...",
      "is_private": false,
      "is_verified": false,
      "reel": {
        "id": 75427741203,
        "expiring_at": 1782478387,
        "has_pride_media": false,
        "latest_reel_media": 1782385358,
        "owner": {
          "id": 75427741203,
          "profile_pic_url": "https://scontent-fml1-1.cdninstagram.com/...",
          "username": "crips.susu"
        }
      }
    }
  ],
  "QVFBOENSMDNreHg0dm43UVZJS01mMGtCaXItRkV5NG5aX2tFX0ZWWmJyclNiYjFqOHFjQS1nRm43R0V2RTk4MnpSWDNFbC12dS1TcGdvQjlvaUQwVkc5UA=="
]
```

</details>

---

### GET /g1/user/following

⚠️ Billing: 1 requests per call. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `end_cursor` | string | No | End Cursor |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/g1/user/following?user_id=787132"
    # Next page: add &end_cursor=... from previous response
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/g1/user/following",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "end_cursor": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/g1/user/following?user_id=787132",
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
      "pk": "364094780",
      "id": "364094780",
      "username": "marcuswestbergphotography",
      "full_name": "Photographer & Storyteller",
      "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
      "is_private": false,
      "is_verified": false
    },
    {
      "pk": "68012770661",
      "id": "68012770661",
      "username": "natgeofamily",
      "full_name": "National Geographic Family",
      "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
      "is_private": false,
      "is_verified": true
    },
    {
      "pk": "20650647",
      "id": "20650647",
      "username": "russwest44",
      "full_name": "Russell Westbrook",
      "profile_pic_url": "https://scontent-dfw5-3.cdninstagram.com/...",
      "is_private": false,
      "is_verified": true
    }
  ],
  "QVFBcHhxWl95eXYxUlNPRGRzd3lsQ08tYlhTMXM3Q2pSMHpyem1yc0h4bkN2VjBSWTg1Y0w0ZmxURGpobFdtUVdfM1BYbkhkMVJYaEZLNWdYRHgyTC14dw=="
]
```

</details>

---

### GET /g2/user/followers

Get part (one page) of followers users with cursor. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `page_id` | string | No | Page Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/g2/user/followers?user_id=787132"
    # Next page: add &page_id=... from previous response
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/g2/user/followers",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "page_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/g2/user/followers?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    // Next page: add &page_id=... to URL
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "users": [
      {
        "__typename": "XDTUserDict",
        "strong_id__": "43714748721",
        "id": "43714748721",
        "is_fulfilled__(name:\"XDTUserDict\")": true,
        "allowed_commenter_type": null,
        "fbid_v2": "17841443821634343",
        "full_name": "",
        "has_anonymous_profile_picture": true,
        "interop_messaging_user_fbid": null,
        "is_private": true,
        "is_verified": false,
        "1llatest_reel_media": 0,
        "liked_clips_count": null,
        "account_badges": [],
        "social_context": null,
        "pk": "43714748721",
        "profile_pic_id": null,
        "profile_pic_url": "https://scontent-phx1-1.cdninstagram.com/...",
        "reel_auto_archive": null,
        "username": "shruti_pvttttttt",
        "all_media_count": null
      },
      {
        "__typename": "XDTUserDict",
        "strong_id__": "60997697028",
        "id": "60997697028",
        "is_fulfilled__(name:\"XDTUserDict\")": true,
        "allowed_commenter_type": null,
        "fbid_v2": "17841460990844712",
        "full_name": "자살",
        "has_anonymous_profile_picture": false,
        "interop_messaging_user_fbid": null,
        "is_private": true,
        "is_verified": false,
        "1llatest_reel_media": 0,
        "liked_clips_count": null,
        "account_badges": [],
        "social_context": null,
        "pk": "60997697028",
        "profile_pic_id": "3860713229006140436_60997697028",
        "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
        "reel_auto_archive": null,
        "username": "sisforspiderman",
        "all_media_count": null
      },
      {
        "__typename": "XDTUserDict",
        "strong_id__": "39562800177",
        "id": "39562800177",
        "is_fulfilled__(name:\"XDTUserDict\")": true,
        "allowed_commenter_type": null,
        "fbid_v2": "17841439365335350",
        "full_name": "Zoran Pirel",
        "has_anonymous_profile_picture": false,
        "interop_messaging_user_fbid": null,
        "is_private": false,
        "is_verified": false,
        "1llatest_reel_media": 0,
        "liked_clips_count": null,
        "account_badges": [],
        "social_context": null,
        "pk": "39562800177",
        "profile_pic_id": "3868362992077388192_39562800177",
        "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/...",
        "reel_auto_archive": null,
        "username": "zpirel2026",
        "all_media_count": null
      }
    ],
    "next_max_id": null,
    "should_limit_list_of_followers": true
  },
  "next_page_id": null
}
```

</details>

---

### GET /g2/user/following

Get part (one page) of following users with cursor. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `page_id` | string | No | Page Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/g2/user/following?user_id=787132"
    # Next page: add &page_id=... from previous response
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/g2/user/following",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "page_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/g2/user/following?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    // Next page: add &page_id=... to URL
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "users": [
      {
        "__typename": "XDTUserDict",
        "strong_id__": "14331657700",
        "id": "14331657700",
        "is_fulfilled__(name:\"XDTUserDict\")": true,
        "allowed_commenter_type": null,
        "fbid_v2": "17841414211021457",
        "full_name": "ナショナルジオグラフィック日本版",
        "has_anonymous_profile_picture": false,
        "interop_messaging_user_fbid": null,
        "is_private": false,
        "is_verified": false,
        "1llatest_reel_media": 0,
        "liked_clips_count": null,
        "account_badges": [],
        "social_context": null,
        "pk": "14331657700",
        "profile_pic_id": "2073867961613189688_14331657700",
        "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/...",
        "reel_auto_archive": null,
        "username": "natgeomagjp",
        "all_media_count": null
      },
      {
        "__typename": "XDTUserDict",
        "strong_id__": "8958735",
        "id": "8958735",
        "is_fulfilled__(name:\"XDTUserDict\")": true,
        "allowed_commenter_type": null,
        "fbid_v2": "17841401882050139",
        "full_name": "Christie Hemm Klok",
        "has_anonymous_profile_picture": false,
        "interop_messaging_user_fbid": null,
        "is_private": false,
        "is_verified": true,
        "1llatest_reel_media": 0,
        "liked_clips_count": null,
        "account_badges": [],
        "social_context": null,
        "pk": "8958735",
        "profile_pic_id": "3354861487016662033_8958735",
        "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/...",
        "reel_auto_archive": null,
        "username": "christiehemmklok",
        "all_media_count": null
      },
      {
        "__typename": "XDTUserDict",
        "strong_id__": "12802178",
        "id": "12802178",
        "is_fulfilled__(name:\"XDTUserDict\")": true,
        "allowed_commenter_type": null,
        "fbid_v2": "17841400065340200",
        "full_name": "Stephanie Mei-Ling",
        "has_anonymous_profile_picture": false,
        "interop_messaging_user_fbid": null,
        "is_private": false,
        "is_verified": true,
        "1llatest_reel_media": 0,
        "liked_clips_count": null,
        "account_badges": [],
        "social_context": null,
        "pk": "12802178",
        "profile_pic_id": "3274170007750843044_12802178",
        "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/...",
        "reel_auto_archive": null,
        "username": "stephaniemeiling",
        "all_media_count": null
      }
    ],
    "next_max_id": "25",
    "has_more": true
  },
  "next_page_id": "25"
}
```

</details>

---

### GET /g2/user/medias

Get part (one page) of user medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `next_page_id` | string | No | Next Page Id |
| `flat` | boolean | No | Flat |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/g2/user/medias?user_id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/g2/user/medias",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/g2/user/medias?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "is_fulfilled__(name:\"XDTProfileFeedDict\")": true,
    "pinned_profile_grid_items_ids": "",
    "profile_grid_items_cursor": "QVFCbGVKc0Nkc2NkVE5rUHZhbXZVWHluMnUxTGdmTkRaWS1Jb3N0bDZTbDdxbGRma0FIVkxtQWdYUDhJNTZMZ0EzXzE3LXhnR1VMTV9oU2MzQWNoekdTZw==",
    "more_available": true,
    "next_max_id": "3930350924921293024",
    "num_results": 9,
    "auto_load_more_enabled": true,
    "items": [
      {
        "__typename": "XDTMediaDict",
        "strong_id__": "3920738671208852726_787132",
        "id": "3920738671208852726_787132",
        "is_fulfilled__(name:\"XDTMediaDict\")": true,
        "is_unseen_by_viewer": false,
        "carousel_media_count": null,
        "carousel_media": null,
        "content_views_count": null,
        "image_versions2": {
          "additional_candidates": {
            "first_frame": {
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-dfw6-2.cdninstagram.com/...",
              "width": 640
            },
            "igtv_first_frame": {
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-dfw6-2.cdninstagram.com/...",
              "width": 640
            }
          },
          "candidates": [
            {
              "estimated_scans_sizes": [
                19047,
                38095,
                57143
              ],
              "height": 1333,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-2.cdninstagram.com/...",
              "width": 750
            }
          ],
          "scrubber_spritesheet_info_candidates": {
            "default": {
              "file_size_kb": 197,
              "max_thumbnails_per_sprite": 105,
              "rendered_width": 96,
              "sprite_height": 1232,
              "sprite_width": 1500,
              "1fthumbnail_duration": 1.0384761905,
              "thumbnail_height": 176,
              "thumbnail_width": 100,
              "thumbnails_per_row": 15,
              "total_thumbnail_num_per_sprite": 105,
              "1fvideo_length": 109.04
            }
          }
        },
        "media_cropping_info": null,
        "media_type": 2,
        "original_height": 1920,
        "original_width": 1080,
        "profile_grid_thumbnail_fitting_style": "UNSET",
        "product_type": "clips",
        "timeline_pinned_user_ids": [
          "18091046",
          "379895100",
          "787132"
        ],
        "user": {
          "__typename": "XDTUserDict",
          "strong_id__": "787132",
          "id": "787132",
          "account_type": 2,
          "all_media_count": null,
          "allowed_commenter_type": null,
          "can_boost_post": null,
          "can_see_organic_insights": null,
          "fan_club_info": {
            "autosave_to_exclusive_highlight": null,
            "connected_member_count": null,
            "fan_club_id": null,
            "fan_club_name": null,
            "fan_consideration_page_revamp_eligiblity": null,
            "has_enough_subscribers_for_ssc": null,
            "is_fan_club_referral_eligible": null,
            "is_fan_club_gifting_eligible": null,
            "subscriber_count": null
          },
          "fbid_v2": "17841400573960012",
          "feed_post_reshare_disabled": false,
          "full_name": "National Geographic",
          "has_anonymous_profile_picture": false,
          "has_onboarded_to_text_post_app": null,
          "interop_messaging_user_fbid": "113671860027320",
          "is_active_on_text_post_app": true,
          "is_favorite": false,
          "is_private": false,
          "is_unpublished": false,
          "is_verified": true,
          "liked_clips_count": null,
          "profile_pic_id": "3887353266858160741_787132",
          "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
          "reel_auto_archive": null,
          "show_account_transparency_details": true,
          "show_insights_terms": null,
          "third_party_downloads_enabled": 2,
          "transparency_product_enabled": false,
          "username": "natgeo"
        },
        "1ltaken_at": 1781625607,
        "media_ui_attributions_data": [],
        "linked_media_data": null,
        "linked_media_playlist_data": null,
        "is_eligible_for_shoppable_everything": null,
        "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
        "injected": null,
        "1lbrs_severity": 80,
        "ai_interactive_embodiment_attachment_style_info": null,
        "channel_tag_data": null,
        "story_prompts": null,
        "carousel_media_pending_post_count": null,
        "main_feed_carousel_starting_media_id": null,
        "1ftallest_media_aspect_ratio": null,
        "open_to_public_submission_description_text": null,
        "is_dismiss_pending_media_banner": null,
        "is_early_access_reel": false,
        "save_count": 17473,
        "enable_waist": true,
        "open_carousel_submission_state": null,
        "all_previous_submitters": null,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "ai_label_info": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMjc3NmZhZTgwNWExNDE5MThiZjQ4NTA0NWM3MzMyMDgzOTIwNzM4NjcxMjA4ODUyNzI2Iiwic2VydmVyX3Rva2VuIjoiMTc4MzAxMjE2OTIyN3wzOTIwNzM4NjcxMjA4ODUyNzI2fDE3NDcwMjk4MTc5fGQ1MzU4YjU3ODdhMWIyNDMxNDdhMDkwOGNlN2E2ZWRiYjRmYjZjMDE5OTRmOTNhYTFlNmJlMzNjZTFlNjhiZDUifSwic2lnbmF0dXJlIjoiIn0=",
        "wearable_attribution_info": null,
        "accessibility_caption": null,
        "are_remixes_crosspostable": true,
        "crosspost": null,
        "crosspost_metadata": {
          "fb_crosspost_deeplink_profile_id": null,
          "fb_crosspost_fbid": null,
          "is_feedback_aggregated": null,
          "is_feed_feedback_aggregated": null,
          "th_unified_feedback_row_tap_target_url": null,
          "unified_feedback_enabled": null,
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "cta_rendering_config": {
          "multiple_cta_style": null,
          "primary_cta_type": "NONE",
          "primary_cta": {
            "cta_type": null,
            "enable_swap_for_cdd": true,
            "enable_swap_for_rap": false
          },
          "secondary_cta_type": null,
          "secondary_cta": null
        },
        "attribution_content_url": null,
        "audience": null,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boosted_post_id": null,
        "boosted_status": null,
        "original_media_has_visual_reply_media": false,
        "like_and_view_counts_disabled": false,
        "share_count_disabled": false,
        "code": "DZpQwxqimz2",
        "coauthor_producer_can_see_organic_insights": false,
        "coauthor_producers": [
          {
            "__typename": "XDTUserDict",
            "strong_id__": "191074609",
            "id": "191074609",
            "full_name": "Hulu",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3756416250542097738_191074609",
            "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
            "username": "hulu",
            "user_activation_info": {
              "activation_type": null
            }
          },
          {
            "__typename": "XDTUserDict",
            "strong_id__": "18091046",
            "id": "18091046",
            "full_name": "National Geographic TV",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3887340006734059597_18091046",
            "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
            "username": "natgeotv",
            "user_activation_info": {
              "activation_type": null
            }
          },
          {
            "__typename": "XDTUserDict",
            "strong_id__": "379895100",
            "id": "379895100",
            "full_name": "National Geographic History",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3887344599689968079_379895100",
            "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
            "username": "natgeohistory",
            "user_activation_info": {
              "activation_type": null
            }
          }
        ],
        "invited_coauthor_producers": [],
        "caption": {
          "__typename": "XDTCommentDict",
          "strong_id__": "18048063437557840",
          "pk": "18048063437557840",
          "bit_flags": 0,
          "content_type": "comment",
          "1lcreated_at": 1781625610,
          "1lcreated_at_utc": 1781625610,
          "did_report_as_spam": false,
          "fb_mentioned_users": null,
          "has_translation": null,
          "is_covered": false,
          "is_ranked_comment": false,
          "media_id": "3920738671208852726",
          "private_reply_status": 0,
          "share_enabled": false,
          "status": "Active",
          "text": "There's more to the story of Pompeii than just destruction. Join Tom Hiddleston as he traces the stories of those who experienced the eruption and those who survived.\n\n#PompeiiOutOfTime with @twhiddleston premieres July 22 on @NatGeoTV. Streaming on @DisneyPlus and @hulu.",
          "text_translation": "There's more to the story of Pompeii than just destruction. Join Tom Hiddleston as he traces the stories of those who experienced the eruption and those who survived. \n\n #PompeiiOutOfTime with @twhiddleston premieres July 22 on @NatGeoTV. Streaming on @DisneyPlus and @hulu.",
          "type": 1,
          "user": {
            "__typename": "XDTUserDict",
            "strong_id__": "787132",
            "id": "787132",
            "username": "natgeo",
            "full_name": "National Geographic",
            "is_private": false,
            "1fcoeff_weight": null,
            "social_context": null,
            "is_active": null,
            "is_verified": true,
            "profile_pic_id": "3887353266858160741_787132",
            "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
            "has_onboarded_to_text_post_app": null,
            "follower_count": 269145394,
            "fbid_v2": "17841400573960012"
          }
        },
        "caption_add_on": null,
        "caption_is_edited": false,
        "carousel_last_edited_at": null,
        "community_notes_info": {
          "has_viewer_submitted_note": false,
          "note_submission_disabled": false,
          "enable_submission_friction": false,
          "is_eligible_for_request_a_note": true
        },
        "can_modify_carousel": null,
        "can_viewer_save": true,
        "can_viewer_reshare": true,
        "eligible_insights_entrypoints": "NONE",
        "is_eligible_for_redesigned_insights": null,
        "has_liked": false,
        "top_likers": [],
        "facepile_top_likers": null,
        "floating_context_items": [],
        "social_context": [],
        "is_comments_gif_composer_enabled": false,
        "is_photo_comments_composer_enabled_for_author": false,
        "is_currently_promoting_by_sponsor": null,
        "is_cutout_sticker_allowed": false,
        "is_reuse_allowed": false,
        "is_post_live_clips_media": false,
        "is_quiet_post": false,
        "is_shared_from_basel": null,
        "media_attributions_data": [],
        "igbio_product": null,
        "location": null,
        "play_count": 4438023,
        "like_count": 127476,
        "client_cache_key": "MzkyMDczODY3MTIwODg1MjcyNg==.3",
        "filter_type": 0,
        "can_viewer_add_media_to_grid": null,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "subscribe_cta_visible": false,
        "video_subtitles_locale": null,
        "translated_video_subtitles": null,
        "byoa_langs": null,
        "video_sticker_locales": [],
        "sticker_translations_enabled": null,
        "original_lang_for_translations": "en",
        "is_eligible_for_autodub": false,
        "is_eligible_for_autodub_upsell": false,
        "clips_captions": null,
        "snippets_overlays": null,
        "clips_captions_translations_urls": null,
        "clips_text": null,
        "should_request_ads": false,
        "is_paid_partnership": false,
        "sponsor_tags": null,
        "clips_tab_pinned_user_ids": [],
        "is_in_profile_grid": false,
        "profile_grid_control_enabled": false,
        "fundraiser_tag": {
          "beneficiary_username": null,
          "beneficiary_name": null,
          "can_viewer_donate": null,
          "contextual_title_str": null,
          "formatted_amount_raised": null,
          "formatted_fundraiser_progress_info_text": null,
          "formatted_goal_amount": null,
          "fundraiser_id": null,
          "fundraiser_title": null,
          "fundraiser_type": null,
          "has_standalone_fundraiser": false,
          "progress_str": null,
          "thumbnail_display_url": null,
          "is_media_owner_fundraiser_owner": null,
          "fundraiser_owner_username": null,
          "show_fundraiser_owner_attribution": null,
          "can_viewer_remove_fundraiser_tag": null
        },
        "comment_likes_enabled": true,
        "comments_disabled": null,
        "creative_config": null,
        "max_num_visible_preview_comments": 2,
        "has_more_comments": true,
        "has_tagged_users": true,
        "fb_user_tags": {
          "in": []
        },
        "has_reshares": null,
        "preview": null,
        "product_collection_tag": null,
        "product_suggestions": null,
        "product_tags": null,
        "photo_of_you": false,
        "is_organic_product_tagging_eligible": true,
        "media_notice": null,
        "media_overlay_info": null,
        "is_fb_only": null,
        "is_artist_pick": false,
        "can_see_insights_as_brand": false,
        "comment_count": 1038,
        "comment_inform_treatment": {
          "action_type": null,
          "should_have_inform_treatment": false,
          "text": "",
          "url": null
        },
        "can_view_more_preview_comments": false,
        "hide_view_all_comment_entrypoint": true,
        "is_third_party_downloads_eligible": false,
        "ig_media_sharing_disabled": false,
        "has_viewer_saved": null,
        "number_of_qualities": 8,
        "is_dash_eligible": 1,
        "upcoming_event": null,
        "usertags": null,
        "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
        "video_versions": [
          {
            "url": "https://scontent-dfw6-2.cdninstagram.com/...",
            "type": 101,
            "width": 720,
            "height": 1280
          }
        ],
        "1fvideo_duration": 109.0559997559,
        "1fvideo_subtitles_confidence": null,
        "video_subtitles_enabled": false,
        "video_subtitles_generated": null,
        "video_subtitles_status": null,
        "video_subtitles_uri": null,
        "visibility": null,
        "view_count": null,
        "visual_comment_reply_sticker_info": null,
        "visual_replies_info": null,
        "xpost_deny_reason": null,
        "xpost_deny_reason_enum": null,
        "threads_xpost_deny_reason": null,
        "has_audio": true,
        "has_delayed_metadata": false,
        "has_hidden_comments": null,
        "reshare_count": 35812,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_post_live": null,
        "deleted_reason": 0,
        "has_shared_to_fb": 0,
        "dominant_color": null,
        "music_metadata": null,
        "fb_comment_count": null,
        "fb_like_count": null,
        "fb_play_count": null,
        "ig_play_count": 4438023,
        "autodub_status": null,
        "snippets_attribution_info": null,
        "mashup_info": null,
        "enable_media_notes_production": true,
        "media_repost_count": 3514,
        "media_reposter_bottomsheet_enabled": false,
        "media_ui_attributions_data_v2": [],
        "media_notes": {
          "items": []
        },
        "voice_translations_consumption_data": null,
        "clips_attribution_info": null,
        "mv_link": null,
        "mv_link_info": null,
        "shimmed_mv_link": null,
        "pk": "3920738671208852726",
        "owner": {
          "__typename": "XDTUserDict",
          "strong_id__": "787132",
          "id": "787132",
          "account_type": 2,
          "all_media_count": null,
          "allowed_commenter_type": null,
          "can_boost_post": null,
          "can_see_organic_insights": null,
          "fan_club_info": {
            "autosave_to_exclusive_highlight": null,
            "connected_member_count": null,
            "fan_club_id": null,
            "fan_club_name": null,
            "fan_consideration_page_revamp_eligiblity": null,
            "has_enough_subscribers_for_ssc": null,
            "is_fan_club_referral_eligible": null,
            "is_fan_club_gifting_eligible": null,
            "subscriber_count": null
          },
          "fbid_v2": "17841400573960012",
          "feed_post_reshare_disabled": false,
          "full_name": "National Geographic",
          "has_anonymous_profile_picture": false,
          "has_onboarded_to_text_post_app": null,
          "interop_messaging_user_fbid": "113671860027320",
          "is_active_on_text_post_app": true,
          "is_favorite": false,
          "is_private": false,
          "is_unpublished": false,
          "is_verified": true,
          "liked_clips_count": null,
          "profile_pic_id": "3887353266858160741_787132",
          "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
          "reel_auto_archive": null,
          "show_account_transparency_details": true,
          "show_insights_terms": null,
          "third_party_downloads_enabled": 2,
          "transparency_product_enabled": false,
          "username": "natgeo"
        }
      },
      {
        "__typename": "XDTMediaDict",
        "strong_id__": "3900557621921709539_787132",
        "id": "3900557621921709539_787132",
        "is_fulfilled__(name:\"XDTMediaDict\")": true,
        "is_unseen_by_viewer": false,
        "carousel_media_count": null,
        "carousel_media": null,
        "content_views_count": null,
        "image_versions2": {
          "additional_candidates": {
            "first_frame": {
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-dfw6-1.cdninstagram.com/...",
              "width": 640
            },
            "igtv_first_frame": {
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-dfw6-1.cdninstagram.com/...",
              "width": 640
            }
          },
          "candidates": [
            {
              "estimated_scans_sizes": [
                20673,
                41346,
                62019
              ],
              "height": 1333,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-1.cdninstagram.com/...",
              "width": 750
            }
          ],
          "scrubber_spritesheet_info_candidates": {
            "default": {
              "file_size_kb": 313,
              "max_thumbnails_per_sprite": 105,
              "rendered_width": 96,
              "sprite_height": 1232,
              "sprite_width": 1500,
              "1fthumbnail_duration": 0.8512857143,
              "thumbnail_height": 176,
              "thumbnail_width": 100,
              "thumbnails_per_row": 15,
              "total_thumbnail_num_per_sprite": 105,
              "1fvideo_length": 89.385
            }
          }
        },
        "media_cropping_info": null,
        "media_type": 2,
        "original_height": 1920,
        "original_width": 1080,
        "profile_grid_thumbnail_fitting_style": "UNSET",
        "product_type": "clips",
        "timeline_pinned_user_ids": [
          "257220481",
          "23947096",
          "787132"
        ],
        "user": {
          "__typename": "XDTUserDict",
          "strong_id__": "787132",
          "id": "787132",
          "account_type": 2,
          "all_media_count": null,
          "allowed_commenter_type": null,
          "can_boost_post": null,
          "can_see_organic_insights": null,
          "fan_club_info": {
            "autosave_to_exclusive_highlight": null,
            "connected_member_count": null,
            "fan_club_id": null,
            "fan_club_name": null,
            "fan_consideration_page_revamp_eligiblity": null,
            "has_enough_subscribers_for_ssc": null,
            "is_fan_club_referral_eligible": null,
            "is_fan_club_gifting_eligible": null,
            "subscriber_count": null
          },
          "fbid_v2": "17841400573960012",
          "feed_post_reshare_disabled": false,
          "full_name": "National Geographic",
          "has_anonymous_profile_picture": false,
          "has_onboarded_to_text_post_app": null,
          "interop_messaging_user_fbid": "113671860027320",
          "is_active_on_text_post_app": true,
          "is_favorite": false,
          "is_private": false,
          "is_unpublished": false,
          "is_verified": true,
          "liked_clips_count": null,
          "profile_pic_id": "3887353266858160741_787132",
          "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
          "reel_auto_archive": null,
          "show_account_transparency_details": true,
          "show_insights_terms": null,
          "third_party_downloads_enabled": 2,
          "transparency_product_enabled": false,
          "username": "natgeo"
        },
        "1ltaken_at": 1779206409,
        "media_ui_attributions_data": [],
        "linked_media_data": null,
        "linked_media_playlist_data": null,
        "is_eligible_for_shoppable_everything": null,
        "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
        "injected": null,
        "1lbrs_severity": 70,
        "ai_interactive_embodiment_attachment_style_info": null,
        "channel_tag_data": null,
        "story_prompts": null,
        "carousel_media_pending_post_count": null,
        "main_feed_carousel_starting_media_id": null,
        "1ftallest_media_aspect_ratio": null,
        "open_to_public_submission_description_text": null,
        "is_dismiss_pending_media_banner": null,
        "is_early_access_reel": false,
        "save_count": 5466,
        "enable_waist": true,
        "open_carousel_submission_state": null,
        "all_previous_submitters": null,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "ai_label_info": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMjc3NmZhZTgwNWExNDE5MThiZjQ4NTA0NWM3MzMyMDgzOTAwNTU3NjIxOTIxNzA5NTM5Iiwic2VydmVyX3Rva2VuIjoiMTc4MzAxMjE2OTI1MXwzOTAwNTU3NjIxOTIxNzA5NTM5fDE3NDcwMjk4MTc5fGU4YjRiZjdhZWYwYTBhNDRhNjlkNjNlMTE4ZjUzMzBkZDcyYTU1Njc2NWJiNTM1OTIxMzNjNzJlY2U3NGZlMmMifSwic2lnbmF0dXJlIjoiIn0=",
        "wearable_attribution_info": null,
        "accessibility_caption": null,
        "are_remixes_crosspostable": true,
        "crosspost": null,
        "crosspost_metadata": {
          "fb_crosspost_deeplink_profile_id": null,
          "fb_crosspost_fbid": null,
          "is_feedback_aggregated": null,
          "is_feed_feedback_aggregated": null,
          "th_unified_feedback_row_tap_target_url": null,
          "unified_feedback_enabled": null,
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "cta_rendering_config": {
          "multiple_cta_style": null,
          "primary_cta_type": "NONE",
          "primary_cta": {
            "cta_type": null,
            "enable_swap_for_cdd": true,
            "enable_swap_for_rap": false
          },
          "secondary_cta_type": null,
          "secondary_cta": null
        },
        "attribution_content_url": null,
        "audience": null,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boosted_post_id": null,
        "boosted_status": null,
        "original_media_has_visual_reply_media": false,
        "like_and_view_counts_disabled": false,
        "share_count_disabled": false,
        "code": "DYhkH24lf3j",
        "coauthor_producer_can_see_organic_insights": false,
        "coauthor_producers": [
          {
            "__typename": "XDTUserDict",
            "strong_id__": "191074609",
            "id": "191074609",
            "full_name": "Hulu",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3756416250542097738_191074609",
            "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
            "username": "hulu",
            "user_activation_info": {
              "activation_type": null
            }
          },
          {
            "__typename": "XDTUserDict",
            "strong_id__": "23947096",
            "id": "23947096",
            "full_name": "National Geographic Travel",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3887340767454691449_23947096",
            "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
            "username": "natgeotravel",
            "user_activation_info": {
              "activation_type": null
            }
          },
          {
            "__typename": "XDTUserDict",
            "strong_id__": "18091046",
            "id": "18091046",
            "full_name": "National Geographic TV",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3887340006734059597_18091046",
            "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
            "username": "natgeotv",
            "user_activation_info": {
              "activation_type": null
            }
          }
        ],
        "invited_coauthor_producers": [],
        "caption": {
          "__typename": "XDTCommentDict",
          "strong_id__": "18115030429771953",
          "pk": "18115030429771953",
          "bit_flags": 0,
          "content_type": "comment",
          "1lcreated_at": 1779206412,
          "1lcreated_at_utc": 1779206412,
          "did_report_as_spam": false,
          "fb_mentioned_users": null,
          "has_translation": null,
          "is_covered": false,
          "is_ranked_comment": false,
          "media_id": "3900557621921709539",
          "private_reply_status": 0,
          "share_enabled": false,
          "status": "Active",
          "text": "@antoni is on a quest to find the best sights, tastes, and experiences the world has to offer, and you're invited. \n\n#BestOfTheWorld with Antoni Porowski premieres Sunday, June 7 at 9/8c on National Geographic. Stream on @DisneyPlus and @hulu",
          "text_translation": null,
          "type": 1,
          "user": {
            "__typename": "XDTUserDict",
            "strong_id__": "787132",
            "id": "787132",
            "username": "natgeo",
            "full_name": "National Geographic",
            "is_private": false,
            "1fcoeff_weight": null,
            "social_context": null,
            "is_active": null,
            "is_verified": true,
            "profile_pic_id": "3887353266858160741_787132",
            "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
            "has_onboarded_to_text_post_app": null,
            "follower_count": 269145394,
            "fbid_v2": "17841400573960012"
          }
        },
        "caption_add_on": null,
        "caption_is_edited": false,
        "carousel_last_edited_at": null,
        "community_notes_info": {
          "has_viewer_submitted_note": false,
          "note_submission_disabled": false,
          "enable_submission_friction": false,
          "is_eligible_for_request_a_note": true
        },
        "can_modify_carousel": null,
        "can_viewer_save": true,
        "can_viewer_reshare": true,
        "eligible_insights_entrypoints": "NONE",
        "is_eligible_for_redesigned_insights": null,
        "has_liked": false,
        "top_likers": [],
        "facepile_top_likers": null,
        "floating_context_items": [],
        "social_context": [],
        "is_comments_gif_composer_enabled": false,
        "is_photo_comments_composer_enabled_for_author": false,
        "is_currently_promoting_by_sponsor": null,
        "is_cutout_sticker_allowed": false,
        "is_reuse_allowed": false,
        "is_post_live_clips_media": false,
        "is_quiet_post": false,
        "is_shared_from_basel": null,
        "media_attributions_data": [],
        "igbio_product": null,
        "location": null,
        "play_count": 3045697,
        "like_count": 56406,
        "client_cache_key": "MzkwMDU1NzYyMTkyMTcwOTUzOQ==.3",
        "filter_type": 0,
        "can_viewer_add_media_to_grid": null,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "subscribe_cta_visible": false,
        "video_subtitles_locale": null,
        "translated_video_subtitles": null,
        "byoa_langs": null,
        "video_sticker_locales": [],
        "sticker_translations_enabled": null,
        "original_lang_for_translations": "en",
        "is_eligible_for_autodub": false,
        "is_eligible_for_autodub_upsell": false,
        "clips_captions": null,
        "snippets_overlays": null,
        "clips_captions_translations_urls": null,
        "clips_text": null,
        "should_request_ads": false,
        "is_paid_partnership": false,
        "sponsor_tags": null,
        "clips_tab_pinned_user_ids": [],
        "is_in_profile_grid": false,
        "profile_grid_control_enabled": false,
        "fundraiser_tag": {
          "beneficiary_username": null,
          "beneficiary_name": null,
          "can_viewer_donate": null,
          "contextual_title_str": null,
          "formatted_amount_raised": null,
          "formatted_fundraiser_progress_info_text": null,
          "formatted_goal_amount": null,
          "fundraiser_id": null,
          "fundraiser_title": null,
          "fundraiser_type": null,
          "has_standalone_fundraiser": false,
          "progress_str": null,
          "thumbnail_display_url": null,
          "is_media_owner_fundraiser_owner": null,
          "fundraiser_owner_username": null,
          "show_fundraiser_owner_attribution": null,
          "can_viewer_remove_fundraiser_tag": null
        },
        "comment_likes_enabled": true,
        "comments_disabled": null,
        "creative_config": null,
        "max_num_visible_preview_comments": 2,
        "has_more_comments": true,
        "has_tagged_users": true,
        "fb_user_tags": {
          "in": []
        },
        "has_reshares": null,
        "preview": null,
        "product_collection_tag": null,
        "product_suggestions": null,
        "product_tags": null,
        "photo_of_you": false,
        "is_organic_product_tagging_eligible": true,
        "media_notice": null,
        "media_overlay_info": null,
        "is_fb_only": null,
        "is_artist_pick": false,
        "can_see_insights_as_brand": false,
        "comment_count": 825,
        "comment_inform_treatment": {
          "action_type": null,
          "should_have_inform_treatment": false,
          "text": "",
          "url": null
        },
        "can_view_more_preview_comments": false,
        "hide_view_all_comment_entrypoint": true,
        "is_third_party_downloads_eligible": false,
        "ig_media_sharing_disabled": false,
        "has_viewer_saved": null,
        "number_of_qualities": 8,
        "is_dash_eligible": 1,
        "upcoming_event": null,
        "usertags": null,
        "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
        "video_versions": [
          {
            "url": "https://scontent-dfw6-2.cdninstagram.com/...",
            "type": 101,
            "width": 720,
            "height": 1280
          }
        ],
        "1fvideo_duration": 89.3860015869,
        "1fvideo_subtitles_confidence": null,
        "video_subtitles_enabled": false,
        "video_subtitles_generated": null,
        "video_subtitles_status": null,
        "video_subtitles_uri": null,
        "visibility": null,
        "view_count": null,
        "visual_comment_reply_sticker_info": null,
        "visual_replies_info": null,
        "xpost_deny_reason": null,
        "xpost_deny_reason_enum": null,
        "threads_xpost_deny_reason": null,
        "has_audio": true,
        "has_delayed_metadata": false,
        "has_hidden_comments": null,
        "reshare_count": 15616,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_post_live": null,
        "deleted_reason": 0,
        "has_shared_to_fb": 0,
        "dominant_color": null,
        "music_metadata": null,
        "fb_comment_count": null,
        "fb_like_count": null,
        "fb_play_count": null,
        "ig_play_count": 3045697,
        "autodub_status": null,
        "snippets_attribution_info": null,
        "mashup_info": null,
        "enable_media_notes_production": true,
        "media_repost_count": 446,
        "media_reposter_bottomsheet_enabled": false,
        "media_ui_attributions_data_v2": [],
        "media_notes": {
          "items": []
        },
        "voice_translations_consumption_data": null,
        "clips_attribution_info": null,
        "mv_link": null,
        "mv_link_info": null,
        "shimmed_mv_link": null,
        "pk": "3900557621921709539",
        "owner": {
          "__typename": "XDTUserDict",
          "strong_id__": "787132",
          "id": "787132",
          "account_type": 2,
          "all_media_count": null,
          "allowed_commenter_type": null,
          "can_boost_post": null,
          "can_see_organic_insights": null,
          "fan_club_info": {
            "autosave_to_exclusive_highlight": null,
            "connected_member_count": null,
            "fan_club_id": null,
            "fan_club_name": null,
            "fan_consideration_page_revamp_eligiblity": null,
            "has_enough_subscribers_for_ssc": null,
            "is_fan_club_referral_eligible": null,
            "is_fan_club_gifting_eligible": null,
            "subscriber_count": null
          },
          "fbid_v2": "17841400573960012",
          "feed_post_reshare_disabled": false,
          "full_name": "National Geographic",
          "has_anonymous_profile_picture": false,
          "has_onboarded_to_text_post_app": null,
          "interop_messaging_user_fbid": "113671860027320",
          "is_active_on_text_post_app": true,
          "is_favorite": false,
          "is_private": false,
          "is_unpublished": false,
          "is_verified": true,
          "liked_clips_count": null,
          "profile_pic_id": "3887353266858160741_787132",
          "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
          "reel_auto_archive": null,
          "show_account_transparency_details": true,
          "show_insights_terms": null,
          "third_party_downloads_enabled": 2,
          "transparency_product_enabled": false,
          "username": "natgeo"
        }
      },
      {
        "__typename": "XDTMediaDict",
        "strong_id__": "3932357843969243147_787132",
        "id": "3932357843969243147_787132",
        "is_fulfilled__(name:\"XDTMediaDict\")": true,
        "is_unseen_by_viewer": false,
        "carousel_media_count": null,
        "carousel_media": null,
        "content_views_count": null,
        "image_versions2": {
          "additional_candidates": {
            "first_frame": {
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-dfw6-2.cdninstagram.com/...",
              "width": 640
            },
            "igtv_first_frame": {
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-dfw6-2.cdninstagram.com/...",
              "width": 640
            }
          },
          "candidates": [
            {
              "estimated_scans_sizes": [
                19409,
                38819,
                58229
              ],
              "height": 1333,
              "scans_profile": "e35",
              "url": "https://scontent-dfw6-2.cdninstagram.com/...",
              "width": 750
            }
          ],
          "scrubber_spritesheet_info_candidates": {
            "default": {
              "file_size_kb": 315,
              "max_thumbnails_per_sprite": 105,
              "rendered_width": 96,
              "sprite_height": 1232,
              "sprite_width": 1500,
              "1fthumbnail_duration": 0.1120571429,
              "thumbnail_height": 176,
              "thumbnail_width": 100,
              "thumbnails_per_row": 15,
              "total_thumbnail_num_per_sprite": 105,
              "1fvideo_length": 11.766
            }
          }
        },
        "media_cropping_info": null,
        "media_type": 2,
        "original_height": 1920,
        "original_width": 1080,
        "profile_grid_thumbnail_fitting_style": "UNSET",
        "product_type": "clips",
        "timeline_pinned_user_ids": [],
        "user": {
          "__typename": "XDTUserDict",
          "strong_id__": "787132",
          "id": "787132",
          "account_type": 2,
          "all_media_count": null,
          "allowed_commenter_type": null,
          "can_boost_post": null,
          "can_see_organic_insights": null,
          "fan_club_info": {
            "autosave_to_exclusive_highlight": null,
            "connected_member_count": null,
            "fan_club_id": null,
            "fan_club_name": null,
            "fan_consideration_page_revamp_eligiblity": null,
            "has_enough_subscribers_for_ssc": null,
            "is_fan_club_referral_eligible": null,
            "is_fan_club_gifting_eligible": null,
            "subscriber_count": null
          },
          "fbid_v2": "17841400573960012",
          "feed_post_reshare_disabled": false,
          "full_name": "National Geographic",
          "has_anonymous_profile_picture": false,
          "has_onboarded_to_text_post_app": null,
          "interop_messaging_user_fbid": "113671860027320",
          "is_active_on_text_post_app": true,
          "is_favorite": false,
          "is_private": false,
          "is_unpublished": false,
          "is_verified": true,
          "liked_clips_count": null,
          "profile_pic_id": "3887353266858160741_787132",
          "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
          "reel_auto_archive": null,
          "show_account_transparency_details": true,
          "show_insights_terms": null,
          "third_party_downloads_enabled": 2,
          "transparency_product_enabled": false,
          "username": "natgeo"
        },
        "1ltaken_at": 1782993636,
        "media_ui_attributions_data": [],
        "linked_media_data": null,
        "linked_media_playlist_data": null,
        "is_eligible_for_shoppable_everything": null,
        "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
        "injected": null,
        "1lbrs_severity": 70,
        "ai_interactive_embodiment_attachment_style_info": null,
        "channel_tag_data": null,
        "story_prompts": null,
        "carousel_media_pending_post_count": null,
        "main_feed_carousel_starting_media_id": null,
        "1ftallest_media_aspect_ratio": null,
        "open_to_public_submission_description_text": null,
        "is_dismiss_pending_media_banner": null,
        "is_early_access_reel": false,
        "save_count": 1271,
        "enable_waist": true,
        "open_carousel_submission_state": null,
        "all_previous_submitters": null,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "ai_label_info": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMjc3NmZhZTgwNWExNDE5MThiZjQ4NTA0NWM3MzMyMDgzOTMyMzU3ODQzOTY5MjQzMTQ3Iiwic2VydmVyX3Rva2VuIjoiMTc4MzAxMjE2OTI2MHwzOTMyMzU3ODQzOTY5MjQzMTQ3fDE3NDcwMjk4MTc5fGE0OWE3ZTViYzE3MzIyZGUyODBkNTUxYTMyNWQ3ZmMzZTRmOGNkYzg3ZWNmMTI2MWQzYWJlNjE0NDIyOWExNzgifSwic2lnbmF0dXJlIjoiIn0=",
        "wearable_attribution_info": null,
        "accessibility_caption": null,
        "are_remixes_crosspostable": true,
        "crosspost": null,
        "crosspost_metadata": {
          "fb_crosspost_deeplink_profile_id": null,
          "fb_crosspost_fbid": null,
          "is_feedback_aggregated": null,
          "is_feed_feedback_aggregated": null,
          "th_unified_feedback_row_tap_target_url": null,
          "unified_feedback_enabled": null,
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "cta_rendering_config": {
          "multiple_cta_style": null,
          "primary_cta_type": "NONE",
          "primary_cta": {
            "cta_type": null,
            "enable_swap_for_cdd": true,
            "enable_swap_for_rap": false
          },
          "secondary_cta_type": null,
          "secondary_cta": null
        },
        "attribution_content_url": null,
        "audience": null,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boosted_post_id": null,
        "boosted_status": null,
        "original_media_has_visual_reply_media": false,
        "like_and_view_counts_disabled": false,
        "share_count_disabled": false,
        "code": "DaSip_jgfgL",
        "coauthor_producer_can_see_organic_insights": false,
        "coauthor_producers": [
          {
            "__typename": "XDTUserDict",
            "strong_id__": "23947096",
            "id": "23947096",
            "full_name": "National Geographic Travel",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3887340767454691449_23947096",
            "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
            "username": "natgeotravel",
            "user_activation_info": {
              "activation_type": null
            }
          }
        ],
        "invited_coauthor_producers": [],
        "caption": {
          "__typename": "XDTCommentDict",
          "strong_id__": "18134275528592277",
          "pk": "18134275528592277",
          "bit_flags": 0,
          "content_type": "comment",
          "1lcreated_at": 1783010885,
          "1lcreated_at_utc": 1783010885,
          "did_report_as_spam": false,
          "fb_mentioned_users": null,
          "has_translation": null,
          "is_covered": false,
          "is_ranked_comment": false,
          "media_id": "3932357843969243147",
          "private_reply_status": 0,
          "share_enabled": false,
          "status": "Active",
          "text": "A moment of awe. While searching for the Seven Natural Wonders of America, @debrobertsabc and National Geographic Explorer James Edward Mills (@thejoytripproject) captured this beautiful view. Can you guess where they are? \n\nDiscover more beauty and nature in the final Wonders of America list, revealed during the 24-hour “Disney Celebrates America” live event special on July 4th on ABC, Disney+ and Nat Geo.",
          "text_translation": "A moment of awe. While searching for the Seven Natural Wonders of America, @debrobertsabc and National Geographic Explorer James Edward Mills (@thejoytripproject) captured this beautiful view. Can you guess where they are? \n\n Discover more beauty and nature in the final Wonders of America list, revealed during the 24-hour “Disney Celebrates America” live event special on July 4th on ABC, Disney+ and Nat Geo.",
          "type": 1,
          "user": {
            "__typename": "XDTUserDict",
            "strong_id__": "787132",
            "id": "787132",
            "username": "natgeo",
            "full_name": "National Geographic",
            "is_private": false,
            "1fcoeff_weight": null,
            "social_context": null,
            "is_active": null,
            "is_verified": true,
            "profile_pic_id": "3887353266858160741_787132",
            "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
            "has_onboarded_to_text_post_app": null,
            "follower_count": 269145394,
            "fbid_v2": "17841400573960012"
          }
        },
        "caption_add_on": null,
        "caption_is_edited": true,
        "carousel_last_edited_at": null,
        "community_notes_info": {
          "has_viewer_submitted_note": false,
          "note_submission_disabled": false,
          "enable_submission_friction": false,
          "is_eligible_for_request_a_note": true
        },
        "can_modify_carousel": null,
        "can_viewer_save": true,
        "can_viewer_reshare": true,
        "eligible_insights_entrypoints": "NONE",
        "is_eligible_for_redesigned_insights": null,
        "has_liked": false,
        "top_likers": [],
        "facepile_top_likers": null,
        "floating_context_items": [],
        "social_context": [],
        "is_comments_gif_composer_enabled": false,
        "is_photo_comments_composer_enabled_for_author": false,
        "is_currently_promoting_by_sponsor": null,
        "is_cutout_sticker_allowed": false,
        "is_reuse_allowed": false,
        "is_post_live_clips_media": false,
        "is_quiet_post": false,
        "is_shared_from_basel": null,
        "media_attributions_data": [],
        "igbio_product": null,
        "location": null,
        "play_count": 1236645,
        "like_count": 46596,
        "client_cache_key": "MzkzMjM1Nzg0Mzk2OTI0MzE0Nw==.3",
        "filter_type": 0,
        "can_viewer_add_media_to_grid": null,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "subscribe_cta_visible": false,
        "video_subtitles_locale": null,
        "translated_video_subtitles": null,
        "byoa_langs": null,
        "video_sticker_locales": [],
        "sticker_translations_enabled": null,
        "original_lang_for_translations": null,
        "is_eligible_for_autodub": false,
        "is_eligible_for_autodub_upsell": false,
        "clips_captions": null,
        "snippets_overlays": null,
        "clips_captions_translations_urls": null,
        "clips_text": null,
        "should_request_ads": false,
        "is_paid_partnership": false,
        "sponsor_tags": null,
        "clips_tab_pinned_user_ids": [],
        "is_in_profile_grid": false,
        "profile_grid_control_enabled": false,
        "fundraiser_tag": {
          "beneficiary_username": null,
          "beneficiary_name": null,
          "can_viewer_donate": null,
          "contextual_title_str": null,
          "formatted_amount_raised": null,
          "formatted_fundraiser_progress_info_text": null,
          "formatted_goal_amount": null,
          "fundraiser_id": null,
          "fundraiser_title": null,
          "fundraiser_type": null,
          "has_standalone_fundraiser": false,
          "progress_str": null,
          "thumbnail_display_url": null,
          "is_media_owner_fundraiser_owner": null,
          "fundraiser_owner_username": null,
          "show_fundraiser_owner_attribution": null,
          "can_viewer_remove_fundraiser_tag": null
        },
        "comment_likes_enabled": true,
        "comments_disabled": null,
        "creative_config": null,
        "max_num_visible_preview_comments": 2,
        "has_more_comments": true,
        "has_tagged_users": true,
        "fb_user_tags": {
          "in": []
        },
        "has_reshares": null,
        "preview": null,
        "product_collection_tag": null,
        "product_suggestions": null,
        "product_tags": null,
        "photo_of_you": false,
        "is_organic_product_tagging_eligible": true,
        "media_notice": null,
        "media_overlay_info": null,
        "is_fb_only": null,
        "is_artist_pick": false,
        "can_see_insights_as_brand": false,
        "comment_count": 406,
        "comment_inform_treatment": {
          "action_type": null,
          "should_have_inform_treatment": false,
          "text": "",
          "url": null
        },
        "can_view_more_preview_comments": false,
        "hide_view_all_comment_entrypoint": true,
        "is_third_party_downloads_eligible": false,
        "ig_media_sharing_disabled": false,
        "has_viewer_saved": null,
        "number_of_qualities": 8,
        "is_dash_eligible": 1,
        "upcoming_event": null,
        "usertags": null,
        "video_codec": "av01.0.05M.08",
        "video_versions": [
          {
            "url": "https://scontent-dfw5-2.cdninstagram.com/...",
            "type": 101,
            "width": 720,
            "height": 1280
          }
        ],
        "1fvideo_duration": 11.765999794,
        "1fvideo_subtitles_confidence": null,
        "video_subtitles_enabled": false,
        "video_subtitles_generated": null,
        "video_subtitles_status": null,
        "video_subtitles_uri": null,
        "visibility": null,
        "view_count": null,
        "visual_comment_reply_sticker_info": null,
        "visual_replies_info": null,
        "xpost_deny_reason": null,
        "xpost_deny_reason_enum": null,
        "threads_xpost_deny_reason": null,
        "has_audio": true,
        "has_delayed_metadata": false,
        "has_hidden_comments": null,
        "reshare_count": 1378,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_post_live": null,
        "deleted_reason": 0,
        "has_shared_to_fb": 0,
        "dominant_color": null,
        "music_metadata": null,
        "fb_comment_count": null,
        "fb_like_count": null,
        "fb_play_count": null,
        "ig_play_count": 1236645,
        "autodub_status": null,
        "snippets_attribution_info": null,
        "mashup_info": null,
        "enable_media_notes_production": true,
        "media_repost_count": 510,
        "media_reposter_bottomsheet_enabled": false,
        "media_ui_attributions_data_v2": [],
        "media_notes": {
          "items": []
        },
        "voice_translations_consumption_data": null,
        "clips_attribution_info": null,
        "mv_link": null,
        "mv_link_info": null,
        "shimmed_mv_link": null,
        "pk": "3932357843969243147",
        "owner": {
          "__typename": "XDTUserDict",
          "strong_id__": "787132",
          "id": "787132",
          "account_type": 2,
          "all_media_count": null,
          "allowed_commenter_type": null,
          "can_boost_post": null,
          "can_see_organic_insights": null,
          "fan_club_info": {
            "autosave_to_exclusive_highlight": null,
            "connected_member_count": null,
            "fan_club_id": null,
            "fan_club_name": null,
            "fan_consideration_page_revamp_eligiblity": null,
            "has_enough_subscribers_for_ssc": null,
            "is_fan_club_referral_eligible": null,
            "is_fan_club_gifting_eligible": null,
            "subscriber_count": null
          },
          "fbid_v2": "17841400573960012",
          "feed_post_reshare_disabled": false,
          "full_name": "National Geographic",
          "has_anonymous_profile_picture": false,
          "has_onboarded_to_text_post_app": null,
          "interop_messaging_user_fbid": "113671860027320",
          "is_active_on_text_post_app": true,
          "is_favorite": false,
          "is_private": false,
          "is_unpublished": false,
          "is_verified": true,
          "liked_clips_count": null,
          "profile_pic_id": "3887353266858160741_787132",
          "profile_pic_url": "https://scontent-dfw6-2.cdninstagram.com/...",
          "reel_auto_archive": null,
          "show_account_transparency_details": true,
          "show_insights_terms": null,
          "third_party_downloads_enabled": 2,
          "transparency_product_enabled": false,
          "username": "natgeo"
        }
      }
    ]
  },
  "next_page_id": "QVFCbGVKc0Nkc2NkVE5rUHZhbXZVWHluMnUxTGdmTkRaWS1Jb3N0bDZTbDdxbGRma0FIVkxtQWdYUDhJNTZMZ0EzXzE3LXhnR1VMTV9oU2MzQWNoekdTZw=="
}
```

</details>

---

### GET /gql/comment/likers/chunk

Get likers on a comment

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `comment_id` | string | No | Comment Id |
| `media_id` | string | No | Media Id |
| `end_cursor` | string | No | End Cursor |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/comment/likers/chunk?comment_id=17901801633335930&media_id=3776832898280228145"
    # Next page: add &end_cursor=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.comment_likers_chunk_gql(comment_id="17901801633335930", media_id="3776832898280228145")
    # Next page: cl.comment_likers_chunk_gql(comment_id="17901801633335930", media_id="3776832898280228145", end_cursor="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/gql/comment/likers/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"comment_id": "17901801633335930", "media_id": "3776832898280228145"},
    )
    # Next page: add "end_cursor": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/comment/likers/chunk?comment_id=17901801633335930&media_id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    // Next page: add &end_cursor=... to URL
    ```

---

### GET /gql/media/likers

Get likers on a media (paging is unavailable on this endpoint). Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_id` | string | Yes | Media Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/media/likers?media_id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_likers_gql(media_id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/gql/media/likers",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"media_id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/media/likers?media_id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "2228799241",
    "__typename": "XDTUserDict",
    "username": "miftasya._",
    "full_name": "Mifta D. Syafira",
    "profile_pic_url": "https://scontent-lhr6-1.cdninstagram.com/...",
    "is_verified": false,
    "social_context": null,
    "supervision_info": null,
    "id": "2228799241"
  },
  {
    "pk": "277099018",
    "__typename": "XDTUserDict",
    "username": "nikki_says_meow",
    "full_name": "Nikki Gosal",
    "profile_pic_url": "https://scontent-lhr8-2.cdninstagram.com/...",
    "is_verified": false,
    "social_context": null,
    "supervision_info": null,
    "id": "277099018"
  },
  {
    "pk": "3992818700",
    "__typename": "XDTUserDict",
    "username": "linethquirurgica",
    "full_name": "Lineth García González",
    "profile_pic_url": "https://scontent-lhr8-1.cdninstagram.com/...",
    "is_verified": false,
    "social_context": null,
    "supervision_info": null,
    "id": "3992818700"
  }
]
```

</details>

---

### GET /gql/media/usertags

Returns users tagged in the video. You can pass up to 10 media ids

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_ids` | array | No | Media Ids |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/media/usertags?media_ids=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_usertags_gql(media_ids="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/gql/media/usertags",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"media_ids": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/media/usertags?media_ids=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "data": {
    "__typename": "Query",
    "strong_id__": null,
    "1$multifetch__XDTMediaDict(ids:$media_ids)": [
      {
        "node": {
          "__typename": "XDTMediaDict",
          "strong_id__": "3776832898280228145_787132",
          "id": "3776832898280228145_787132",
          "usertags": null
        }
      }
    ]
  },
  "extensions": {
    "server_metadata": {
      "request_start_time_ms": 1775669085934,
      "time_at_flush_ms": 1775669085965
    },
    "is_final": true
  }
}
```

</details>

---

### GET /gql/topsearch

Search top content by keyword.

Returns top accounts AND top media interleaved in one stream —
discriminate by `__typename` (`XDTUserDict` / `XDTMediaDict`).

`flat=true` returns flat `items[]` instead of `stream_rows`.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |
| `end_cursor` | string | No | End Cursor |
| `flat` | boolean | No | Flatten stream_rows into a single items[] list |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/topsearch?query=natgeo"
    # Next page: add &end_cursor=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.topsearch_gql(query="natgeo")
    # Next page: cl.topsearch_gql(query="natgeo", end_cursor="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/gql/topsearch",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"query": "natgeo"},
    )
    # Next page: add "end_cursor": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/topsearch?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    // Next page: add &end_cursor=... to URL
    ```

<details>
<summary>Example response</summary>

```json
{
  "stream_rows": [
    {
      "data": {
        "__typename": "Query",
        "strong_id__": null,
        "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})": {
          "edges": [
            {
              "__typename": "XDTTopSerpGraphQLConnectionEdge",
              "strong_id__": null,
              "node": {
                "__typename": "XDTTopSerpMetaAIHCMUnit",
                "strong_id__": null,
                "is_fulfilled__(name:\"XDTTopSerpUnitInterface\")": true,
                "unit_type": "META_AI_HCM",
                "is_fulfilled__(name:\"XDTTopSerpMetaAIHCMUnit\")": true
              },
              "cursor": null
            }
          ]
        }
      },
      "extensions": {
        "is_final": false,
        "server_metadata": {
          "request_start_time_ms": 1775669295929,
          "time_at_flush_ms": 1775669296099
        }
      },
      "status": "ok"
    },
    {
      "path": [
        "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})",
        "edges",
        0
      ],
      "label": "TopSerpMetaAIHCMFragment__force_flush",
      "data": {
        "is_fulfilled__(name:\"XDTTopSerpMetaAIHCMUnit\")": true,
        "1$meta_ai_hcm(hcm_request_data:{\"entrypoint\":$hcm_entrypoint})": [
          {
            "is_fulfilled__(name:\"XDTMetaAIHCMCompletion\")": true,
            "status": "FETCHING",
            "text_response_id": null,
            "text": null,
            "text_request_id": null,
            "replacement_text": null,
            "is_final_text_chunk": false,
            "module_type": "RESPONSE",
            "prompts_display_behavior": "HIDE_BEHIND_SEE_MORE",
            "search_plugin_response": null,
            "prompts": null,
            "entities": null,
            "debug_information": null
          }
        ]
      },
      "extensions": {
        "is_final": false
      }
    },
    [
      {
        "path": [
          "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})",
          "edges",
          1
        ],
        "label": "units",
        "data": {
          "__typename": "XDTTopSerpGraphQLConnectionEdge",
          "strong_id__": null,
          "node": {
            "__typename": "XDTTopSerpHeaderUnit",
            "strong_id__": null,
            "is_fulfilled__(name:\"XDTTopSerpUnitInterface\")": true,
            "unit_type": "HEADER",
            "is_fulfilled__(name:\"XDTTopSerpHeaderUnit\")": true,
            "header": "Accounts"
          },
          "cursor": null
        },
        "extensions": {
          "is_final": false,
          "fulfilled_payloads": [
            {
              "label": "TopSerpHeaderFragment__force_flush",
              "path": [
                "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})",
                "edges",
                1
              ]
            }
          ]
        }
      },
      {
        "path": [
          "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})",
          "edges",
          2
        ],
        "label": "units",
        "data": {
          "__typename": "XDTTopSerpGraphQLConnectionEdge",
          "strong_id__": null,
          "node": {
            "__typename": "XDTTopSerpAccountsHCMUnit",
            "strong_id__": null,
            "is_fulfilled__(name:\"XDTTopSerpUnitInterface\")": true,
            "unit_type": "ACCOUNTS_HCM",
            "is_fulfilled__(name:\"XDTTopSerpAccountsHCMUnit\")": true,
            "rank_token": "1775669296269|6263b0f0a51af5839ec7294a2adef3a28c5b76d0a45cc94687aa702f404f8b78",
            "items": [
              {
                "__typename": "XDTUserDict",
                "strong_id__": "787132",
                "id": "787132",
                "is_fulfilled__(name:\"XDTUserDict\")": true,
                "fbid_v2": "17841400573960012",
                "username": "natgeo",
                "full_name": "National Geographic",
                "profile_pic_id": "3865702555259028436_787132",
                "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/..."
              },
              {
                "__typename": "XDTUserDict",
                "strong_id__": "18091046",
                "id": "18091046",
                "is_fulfilled__(name:\"XDTUserDict\")": true,
                "fbid_v2": "17841401291380282",
                "username": "natgeotv",
                "full_name": "National Geographic TV",
                "profile_pic_id": "3865691934048399589_18091046",
                "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/..."
              }
            ]
          },
          "cursor": null
        },
        "extensions": {
          "is_final": false,
          "fulfilled_payloads": [
            {
              "label": "TopSerpAccountsHCMFragment__force_flush",
              "path": [
                "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})",
                "edges",
                2
              ]
            }
          ]
        }
      }
    ]
  ]
}
```

</details>

---

### GET /gql/user/about

Get the "About this account" panel for a user: verified status,
country of registration, date the account was created, and the list
of former usernames. Returns user about info.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/about?id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/gql/user/about",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/about?id=787132",
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

### GET /gql/user/clips

Get user clips. Returns a list of Media objects (Reels).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `max_id` | string | No | Max Id |
| `sort_by_views` | boolean | No | Sort By Views |
| `flat` | boolean | No | Flatten nested media objects into a single list |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/clips?user_id=787132"
    # Next page: add &max_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_clips_gql(user_id="787132")
    # Next page: cl.user_clips_gql(user_id="787132", max_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/gql/user/clips",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "max_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/clips?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    // Next page: add &max_id=... to URL
    ```

<details>
<summary>Example response</summary>

```json
{
  "stream_rows": [
    {
      "data": {
        "__typename": "Query",
        "strong_id__": null,
        "1$xdt_user_clips_graphql(data:$data)": {
          "is_fulfilled__(name:\"XDTGraphqlUserClipsResponse\")": true,
          "first_seen_media_id": null,
          "just_watched_context": null,
          "items": [
            {
              "media": {
                "__typename": "XDTMediaDict",
                "strong_id__": "3870025531093850440_1029649300",
                "id": "3870025531093850440_1029649300",
                "is_fulfilled__(name:\"XDTMediaDict\")": true,
                "clips_tab_pinned_user_ids": [],
                "clips_trial": null,
                "enable_media_notes_production": true,
                "inventory_source": null,
                "media_notes": {
                  "items": []
                },
                "floating_context_items": [],
                "media_overlay_info": null,
                "wearable_attribution_info": null,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-jnb2-1.cdninstagram.com/...",
                      "width": 640
                    },
                    "igtv_first_frame": {
                      "width": 640,
                      "height": 1136,
                      "url": "https://scontent-jnb2-1.cdninstagram.com/...",
                      "scans_profile": "e15"
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "height": 1333,
                      "scans_profile": "e35",
                      "url": "https://scontent-jnb2-1.cdninstagram.com/...",
                      "width": 750
                    }
                  ],
                  "smart_thumbnail_enabled": null,
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "1fvideo_length": 60.727,
                      "thumbnail_width": 100,
                      "thumbnail_height": 176,
                      "1fthumbnail_duration": 0.578352380952381,
                      "sprite_urls": [
                        "https://scontent-jnb2-1.cdninstagram.com/v/t51.71878-15/661377490_4446710915609804_6368747692439450584_n.jpg?_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gEdNZ8Rt4BXgIk_OIdIWnE_8QWMqY6776chA5BT6KCzAP_x9z1wa_dIiu9XcoxDYME&_nc_ohc=8YQN_m5Qfl0Q7kNvwESe46L&_nc_gid=hGipKzY9A3hyuapavqrJaQ&edm=AL8dhF4BAAAA&ccb=7-5&oh=00_Af02Inz7qsyu48TTmAoaAy5Wg52Hsp3gkJ4OTH5G7NOhqg&oe=69DC46C6&_nc_sid=dc74e4"
                      ],
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "max_thumbnails_per_sprite": 105,
                      "sprite_width": 1500,
                      "sprite_height": 1232,
                      "rendered_width": 96,
                      "file_size_kb": 271
                    }
                  }
                },
                "media_type": 2,
                "original_height": 1920,
                "original_width": 1080,
                "pk": "3870025531093850440",
                "play_count": 2626281,
                "product_type": "clips",
                "video_versions": [
                  {
                    "height": 1280,
                    "id": "4284559321859069v",
                    "type": 101,
                    "url": "https://scontent-jnb2-1.cdninstagram.com/...",
                    "width": 720
                  }
                ],
                "1fvideo_duration": 60.736000061035156,
                "meta_ai_content_deep_dive_prompt_v2": null,
                "meta_ai_contextual_voice_data": null,
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "mv_link": null,
                "shimmed_mv_link": null
              }
            },
            {
              "media": {
                "__typename": "XDTMediaDict",
                "strong_id__": "3869494020385423326_787132",
                "id": "3869494020385423326_787132",
                "is_fulfilled__(name:\"XDTMediaDict\")": true,
                "clips_tab_pinned_user_ids": [],
                "clips_trial": null,
                "enable_media_notes_production": true,
                "inventory_source": null,
                "media_notes": {
                  "items": []
                },
                "floating_context_items": [],
                "media_overlay_info": null,
                "wearable_attribution_info": null,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-jnb2-1.cdninstagram.com/...",
                      "width": 640
                    },
                    "igtv_first_frame": {
                      "width": 640,
                      "height": 1136,
                      "url": "https://scontent-jnb2-1.cdninstagram.com/...",
                      "scans_profile": "e15"
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "height": 1333,
                      "scans_profile": "e35",
                      "url": "https://scontent-jnb2-1.cdninstagram.com/...",
                      "width": 750
                    }
                  ],
                  "smart_thumbnail_enabled": null,
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "1fvideo_length": 55.43,
                      "thumbnail_width": 100,
                      "thumbnail_height": 176,
                      "1fthumbnail_duration": 0.5279047619047619,
                      "sprite_urls": [
                        "https://scontent-jnb2-1.cdninstagram.com/v/t51.71878-15/660026027_948875084508987_6617144121092333726_n.jpg?_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gEdNZ8Rt4BXgIk_OIdIWnE_8QWMqY6776chA5BT6KCzAP_x9z1wa_dIiu9XcoxDYME&_nc_ohc=a82HNH3lYl8Q7kNvwGZuHLq&_nc_gid=hGipKzY9A3hyuapavqrJaQ&edm=AL8dhF4BAAAA&ccb=7-5&oh=00_Af0-HXlvB5U5H4RFOOnh6BnUnXsIrbfEdQf34VBzF8jSOg&oe=69DC6F24&_nc_sid=dc74e4"
                      ],
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "max_thumbnails_per_sprite": 105,
                      "sprite_width": 1500,
                      "sprite_height": 1232,
                      "rendered_width": 96,
                      "file_size_kb": 276
                    }
                  }
                },
                "media_type": 2,
                "original_height": 1920,
                "original_width": 1080,
                "pk": "3869494020385423326",
                "play_count": 1496384,
                "product_type": "clips",
                "video_versions": [
                  {
                    "height": 1280,
                    "id": "2358585431274531v",
                    "type": 101,
                    "url": "https://scontent-jnb2-1.cdninstagram.com/...",
                    "width": 720
                  }
                ],
                "1fvideo_duration": 55.44499969482422,
                "meta_ai_content_deep_dive_prompt_v2": null,
                "meta_ai_contextual_voice_data": null,
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "mv_link": null,
                "shimmed_mv_link": null
              }
            },
            {
              "media": {
                "__typename": "XDTMediaDict",
                "strong_id__": "3868170261056492782_787132",
                "id": "3868170261056492782_787132",
                "is_fulfilled__(name:\"XDTMediaDict\")": true,
                "clips_tab_pinned_user_ids": [],
                "clips_trial": null,
                "enable_media_notes_production": true,
                "inventory_source": null,
                "media_notes": {
                  "items": []
                },
                "floating_context_items": [],
                "media_overlay_info": null,
                "wearable_attribution_info": null,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-jnb2-1.cdninstagram.com/...",
                      "width": 640
                    },
                    "igtv_first_frame": {
                      "width": 640,
                      "height": 1136,
                      "url": "https://scontent-jnb2-1.cdninstagram.com/...",
                      "scans_profile": "e15"
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "height": 1333,
                      "scans_profile": "e35",
                      "url": "https://scontent-jnb2-1.cdninstagram.com/...",
                      "width": 750
                    }
                  ],
                  "smart_thumbnail_enabled": null,
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "1fvideo_length": 47.881,
                      "thumbnail_width": 100,
                      "thumbnail_height": 176,
                      "1fthumbnail_duration": 0.4560095238095238,
                      "sprite_urls": [
                        "https://scontent-jnb2-1.cdninstagram.com/v/t51.71878-15/661407041_2382063302308753_1177647765954686603_n.jpg?_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gEdNZ8Rt4BXgIk_OIdIWnE_8QWMqY6776chA5BT6KCzAP_x9z1wa_dIiu9XcoxDYME&_nc_ohc=n5iQezOC2T8Q7kNvwHHli1Q&_nc_gid=hGipKzY9A3hyuapavqrJaQ&edm=AL8dhF4BAAAA&ccb=7-5&oh=00_Af04_bnNERIpWzKHbTZzudkajFjzIPsSSVvzI6EyDHHRqg&oe=69DC5D1E&_nc_sid=dc74e4"
                      ],
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "max_thumbnails_per_sprite": 105,
                      "sprite_width": 1500,
                      "sprite_height": 1232,
                      "rendered_width": 96,
                      "file_size_kb": 274
                    }
                  }
                },
                "media_type": 2,
                "original_height": 1920,
                "original_width": 1080,
                "pk": "3868170261056492782",
                "play_count": 1307812,
                "product_type": "clips",
                "video_versions": [
                  {
                    "height": 1280,
                    "id": "799234956583164v",
                    "type": 101,
                    "url": "https://scontent-jnb2-1.cdninstagram.com/...",
                    "width": 720
                  }
                ],
                "1fvideo_duration": 47.893001556396484,
                "meta_ai_content_deep_dive_prompt_v2": null,
                "meta_ai_contextual_voice_data": null,
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "mv_link": null,
                "shimmed_mv_link": null
              }
            }
          ]
        }
      },
      "extensions": {
        "is_final": false,
        "server_metadata": {
          "request_start_time_ms": 1775669050005,
          "time_at_flush_ms": 1775669050307
        }
      },
      "status": "ok"
    },
    {
      "path": [
        "1$xdt_user_clips_graphql(data:$data)"
      ],
      "label": "ClipsProfilePagingInfo__force_flush",
      "data": {
        "is_fulfilled__(name:\"XDTGraphqlUserClipsResponse\")": true,
        "paging_info": {
          "max_id": "QVFEX2VqYVdpeWlJd3RRd1FHR2tjUjFnOTRjeWtxN3I3YkRXa21FRGtweTE0WHZmQnp5R21tdV9kVExYOXlIMVR3bFlqbzRuejdkeDZKYWRhOFdobFc5aw==",
          "more_available": true
        }
      },
      "extensions": {
        "is_final": false
      }
    },
    {
      "path": [
        "1$xdt_user_clips_graphql(data:$data)",
        "items",
        0
      ],
      "label": "ClipsViewerGraphQLFragment",
      "data": {
        "__typename": "XDTMediaDict",
        "strong_id__": "3870025531093850440_1029649300",
        "id": "3870025531093850440_1029649300",
        "is_fulfilled__(name:\"XDTMediaDict\")": true,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "wearable_attribution_info": null,
        "are_remixes_crosspostable": true,
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "creator_viewer_insights": null,
        "attribution": null,
        "audience": null,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boosted_by_sponsor": null,
        "boosted_post_id": null,
        "boosted_status": null,
        "branded_content_ads_boost_post_tokens": null,
        "can_see_insights_as_brand": false,
        "can_view_more_preview_comments": false,
        "can_viewer_reshare": true,
        "can_viewer_save": true,
        "caption": {
          "__typename": "XDTCommentDict",
          "strong_id__": "18064245098343903",
          "pk": "18064245098343903",
          "bit_flags": 0,
          "content_type": "comment",
          "1lcreated_at": 1775566807,
          "1lcreated_at_utc": 1775566807,
          "did_report_as_spam": false,
          "fb_mentioned_users": null,
          "is_covered": false,
          "is_ranked_comment": false,
          "media_id": "3870025531093850440",
          "private_reply_status": 0,
          "share_enabled": false,
          "status": "Active",
          "text": "Intruder alert! 🚨 Murder Hornets eat bees and their larvae, but these Asian honey bees aren't going to let their hive be destroyed without a fight. \n\n#SecretsOfTheBees is now streaming on @DisneyPlus and @hulu",
          "text_translation": null,
          "type": 1,
          "user": {
            "__typename": "XDTUserDict",
            "strong_id__": "1029649300",
            "id": "1029649300",
            "is_fulfilled__(name:\"XDTUserDict\")": true,
            "pk": "1029649300",
            "username": "natgeoanimals",
            "full_name": "National Geographic Animals",
            "is_private": false,
            "1fcoeff_weight": null,
            "social_context": null,
            "is_active": null,
            "is_verified": true,
            "profile_pic_id": "3865698702530758137_1029649300",
            "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/...",
            "has_onboarded_to_text_post_app": null,
            "follower_count": 15107879,
            "fbid_v2": "17841400519016088"
          },
          "user_id": "1029649300"
        },
        "caption_is_edited": false,
        "client_cache_key": "Mzg3MDAyNTUzMTA5Mzg1MDQ0MA==.3",
        "clips_attribution_info": null,
        "clips_tab_pinned_user_ids": [],
        "clips_trial": null,
        "coauthor_producer_can_see_organic_insights": false,
        "coauthor_producers": [
          {
            "__typename": "XDTUserDict",
            "strong_id__": "787132",
            "id": "787132",
            "full_name": "National Geographic",
            "has_onboarded_to_text_post_app": null,
            "is_private": false,
            "is_verified": true,
            "pk": "787132",
            "profile_pic_id": "3865702555259028436_787132",
            "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/...",
            "username": "natgeo"
          }
        ],
        "code": "DW1F7dciplI",
        "comment_count": 499,
        "comment_inform_treatment": {
          "should_have_inform_treatment": false,
          "text": ""
        },
        "comment_likes_enabled": true,
        "comment_threading_enabled": true,
        "commenting_disabled_for_viewer": null,
        "comments_disabled": null,
        "commerciality_status": "not_commercial",
        "creative_config": null,
        "deleted_reason": 0,
        "1ldevice_timestamp": 177556301582,
        "dominant_color": null,
        "enable_media_notes_production": true,
        "inventory_source": null,
        "media_notes": {
          "items": []
        },
        "enable_waist": true,
        "explore_hide_comments": null,
        "facepile_top_likers": null,
        "fb_like_count": null,
        "fb_play_count": null,
        "filter_type": 0,
        "fundraiser_tag": {
          "beneficiary_name": null,
          "beneficiary_username": null,
          "can_viewer_donate": null,
          "can_viewer_remove_fundraiser_tag": null,
          "contextual_title_str": null,
          "formatted_amount_raised": null,
          "formatted_fundraiser_progress_info_text": null,
          "formatted_goal_amount": null,
          "fundraiser_id": null,
          "fundraiser_owner_username": null,
          "fundraiser_title": null,
          "fundraiser_type": null,
          "is_media_owner_fundraiser_owner": null,
          "progress_str": null,
          "show_fundraiser_owner_attribution": null,
          "thumbnail_display_url": null
        },
        "has_audio": true,
        "has_delayed_metadata": false,
        "has_hidden_comments": null,
        "has_liked": false,
        "has_more_comments": true,
        "has_reshares": null,
        "has_shared_to_fb": 0,
        "has_viewer_saved": null,
        "has_views_fetching": true,
        "hide_view_all_comment_entrypoint": true,
        "ig_media_sharing_disabled": false,
        "igtv_exists_in_viewer_series": null,
        "igtv_series_info": null,
        "igtv_shopping_info": null,
        "image_versions2": {
          "additional_candidates": {
            "first_frame": {
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-jnb2-1.cdninstagram.com/...",
              "width": 640
            },
            "igtv_first_frame": {
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-jnb2-1.cdninstagram.com/...",
              "width": 640
            }
          },
          "candidates": [
            {
              "height": 1333,
              "scans_profile": "e35",
              "url": "https://scontent-jnb2-1.cdninstagram.com/...",
              "width": 750
            }
          ],
          "scrubber_spritesheet_info_candidates": {
            "default": {
              "file_size_kb": 271,
              "max_thumbnails_per_sprite": 105,
              "rendered_width": 96,
              "sprite_height": 1232,
              "sprite_width": 1500,
              "1fthumbnail_duration": 0.578352381,
              "thumbnail_height": 176,
              "thumbnail_width": 100,
              "thumbnails_per_row": 15,
              "total_thumbnail_num_per_sprite": 105,
              "1fvideo_length": 60.727
            }
          },
          "smart_thumbnail_enabled": null
        },
        "integrity_review_decision": "pending",
        "invited_coauthor_producers": [],
        "is_artist_pick": false,
        "is_comments_gif_composer_enabled": false,
        "is_currently_promoting_by_sponsor": null,
        "is_dash_eligible": 1,
        "is_fb_only": null,
        "is_in_profile_grid": false,
        "is_internal_only": null,
        "is_organic_product_tagging_eligible": true,
        "is_paid_partnership": false,
        "is_post_live": null,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_shared_from_basel": null,
        "is_third_party_downloads_eligible": false,
        "is_unified_video": false,
        "is_visual_reply_commenter_notice_enabled": true,
        "1flat": null,
        "like_and_view_counts_disabled": false,
        "share_count_disabled": false,
        "like_count": 51262,
        "1flng": null,
        "location": null,
        "logging_info_token": null,
        "mashup_info": null,
        "max_num_visible_preview_comments": 2,
        "media_appreciation_settings": null,
        "media_cropping_info": null,
        "media_notice": null,
        "media_overlay_info": null,
        "media_type": 2,
        "media_attributions_data": [],
        "music_metadata": null,
        "nearly_complete_copyright_match": null,
        "next_max_id": null,
        "number_of_qualities": 8,
        "organic_cta_info": null,
        "organic_cta_type": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiYTAzNjc4YTY4MzY1NGI4Nzg2MzgwY2Y2NjA3OTJkZWMzODcwMDI1NTMxMDkzODUwNDQwIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTA1MDMyM3wzODcwMDI1NTMxMDkzODUwNDQwfDMxOTYwMDgzOTU5fGVhNTI3NGY2NjRlN2Y3OGQ0YWJlNzFiMTJjMzNhYWI0NzhmZjNjZjMyOTY4MTFjNGQ5OTBjODY4Njg2MzA4YzgifSwic2lnbmF0dXJlIjoiIn0=",
        "original_height": 1920,
        "original_media_has_visual_reply_media": false,
        "original_width": 1080,
        "photo_of_you": false,
        "play_count": 2626281,
        "preview": null,
        "product_tags": null,
        "profile_grid_control_enabled": false,
        "reshare_count": 11654,
        "senders": [],
        "sharing_friction_info": {
          "should_have_sharing_friction": false
        },
        "shop_routing_user_id": null,
        "should_request_ads": false,
        "floating_context_items": [],
        "social_context": [],
        "sponsor_tags": null,
        "story_notify_me_stickers": null,
        "story_polls": null,
        "story_prompts": null,
        "story_sliders": null,
        "subscribe_cta_visible": false,
        "subscription_media_visibility": null,
        "1ltaken_at": 1775566804,
        "thumbnails": null,
        "title": null,
        "upcoming_event": null,
        "user": {
          "__typename": "XDTUserDict",
          "strong_id__": "1029649300",
          "id": "1029649300",
          "is_fulfilled__(name:\"XDTUserDict\")": true,
          "pk": "1029649300",
          "username": "natgeoanimals",
          "full_name": "National Geographic Animals",
          "is_private": false,
          "1fcoeff_weight": null,
          "social_context": null,
          "is_active": null,
          "is_verified": true,
          "profile_pic_id": "3865698702530758137_1029649300",
          "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/...",
          "has_onboarded_to_text_post_app": null,
          "follower_count": 15107879,
          "fbid_v2": "17841400519016088"
        },
        "usertags": null,
        "video_codec": "av01.0.04M.08.0.111.01.01.01.0",
        "1fvideo_subtitles_confidence": null,
        "video_subtitles_enabled": null,
        "video_subtitles_status": null,
        "video_subtitles_uri": null,
        "video_subtitles_locale": null,
        "byoa_langs": null,
        "translated_video_subtitles": null,
        "video_sticker_locales": [],
        "sticker_translations_enabled": null,
        "clips_karaoke_caption": null,
        "clips_captions": null,
        "clips_captions_translations_urls": null,
        "clips_text": null,
        "view_count": null,
        "view_state_item_type": 128,
        "visual_comment_reply_sticker_info": null,
        "visual_replies_info": null,
        "xpost_deny_reason": null,
        "top_likers": []
      },
      "extensions": {
        "is_final": false
      }
    }
  ]
}
```

</details>

---

### GET /gql/user/followers/chunk

⚠️ Billing: 2 requests per call. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `end_cursor` | string | No | End Cursor |
| `force` | boolean | No | Skip account privacy check |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/followers/chunk?user_id=787132"
    # Next page: add &end_cursor=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_followers_chunk_gql(user_id="787132")
    # Next page: cl.user_followers_chunk_gql(user_id="787132", end_cursor="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/gql/user/followers/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "end_cursor": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/followers/chunk?user_id=787132",
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
      "pk": "39306753607",
      "id": "39306753607",
      "username": "mollahnathan",
      "full_name": "Nathan Mollah",
      "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/...",
      "is_private": false,
      "is_verified": false,
      "reel": {
        "id": 39306753607,
        "expiring_at": 1775755446,
        "has_pride_media": false,
        "latest_reel_media": 0,
        "owner": {
          "id": 39306753607,
          "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/...",
          "username": "mollahnathan"
        }
      }
    },
    {
      "pk": "79702408816",
      "id": "79702408816",
      "username": "ilsrtr",
      "full_name": "李 聖 靈 統 領",
      "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/...",
      "is_private": false,
      "is_verified": false,
      "reel": {
        "id": 79702408816,
        "expiring_at": 1775755446,
        "has_pride_media": false,
        "latest_reel_media": 1775643912,
        "owner": {
          "id": 79702408816,
          "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/...",
          "username": "ilsrtr"
        }
      }
    },
    {
      "pk": "32456705511",
      "id": "32456705511",
      "username": "was_wildanimalssurvival",
      "full_name": "Wild Animals Survival",
      "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/...",
      "is_private": false,
      "is_verified": false,
      "reel": {
        "id": 32456705511,
        "expiring_at": 1775755446,
        "has_pride_media": false,
        "latest_reel_media": 0,
        "owner": {
          "id": 32456705511,
          "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/...",
          "username": "was_wildanimalssurvival"
        }
      }
    }
  ],
  "QVFDVHduT05fM3B5SnIyNko4X3VHRVBSMXdURU9vaWEtVm5OVFB4OGszMEpZcVpOaTB5N1RRSU9haVozOTFpNURoeEhXN1hOVHkyRlFsZldnYmcybVEtQg=="
]
```

</details>

---

### GET /gql/user/following/chunk

⚠️ Billing: 2 requests per call. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `end_cursor` | string | No | End Cursor |
| `force` | boolean | No | Skip account privacy check |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/following/chunk?user_id=787132"
    # Next page: add &end_cursor=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_following_chunk_gql(user_id="787132")
    # Next page: cl.user_following_chunk_gql(user_id="787132", end_cursor="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/gql/user/following/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "end_cursor": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/following/chunk?user_id=787132",
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
      "pk": "68012770661",
      "id": "68012770661",
      "username": "natgeofamily",
      "full_name": "National Geographic Family",
      "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/...",
      "is_private": false,
      "is_verified": false
    },
    {
      "pk": "20650647",
      "id": "20650647",
      "username": "russwest44",
      "full_name": "Russell Westbrook",
      "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/...",
      "is_private": false,
      "is_verified": true
    },
    {
      "pk": "3956077735",
      "id": "3956077735",
      "username": "borgeousland",
      "full_name": "Børge Ousland",
      "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/...",
      "is_private": false,
      "is_verified": true
    }
  ],
  "QVFCWGNtMTAzWDZLY3lvRk8wSFdDX3VTcDRrbDhmV3lCcXBaZGVaekU1azZ6SG9WWmZyaUJRZzNKb2MzcmJObm5TdzNJRjhoN2FOS3R3WEFRVjluZ2Zzcg=="
]
```

</details>

---

### GET /gql/user/medias

Get user medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `profile_grid_items_cursor` | string | No | Profile Grid Items Cursor |
| `flat` | boolean | No | Flatten nested media objects into a single list |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/medias?user_id=787132"
    # Next page: add &profile_grid_items_cursor=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_medias_gql(user_id="787132")
    # Next page: cl.user_medias_gql(user_id="787132", profile_grid_items_cursor="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/gql/user/medias",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "profile_grid_items_cursor": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/medias?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    // Next page: add &profile_grid_items_cursor=... to URL
    ```

<details>
<summary>Example response</summary>

```json
{
  "stream_rows": [
    {
      "data": {
        "__typename": "Query",
        "strong_id__": null,
        "1$xdt_api__v1__profile_timeline(_request_data:{\"count\":$count,\"exclude_comment\":$exclude_comment,\"fetch_all_highlights\":$fetch_all_highlights,\"fetch_media_for_highlights\":$include_associated_highlights,\"fetch_profile_grid_items\":$fetch_profile_grid_items,\"is_pull_to_refresh\":$is_pull_to_refresh,\"max_id\":$max_id,\"pinned_profile_grid_items_ids\":$pinned_profile_grid_items_ids,\"profile_grid_items_cursor\":$profile_grid_items_cursor},user_id:$user_id)": {
          "is_fulfilled__(name:\"XDTProfileFeedDict\")": true,
          "__typename": "XDTProfileFeedDict",
          "strong_id__": null,
          "is_fulfilled__(name:\"XDTHintableResponse\")": true,
          "client_hints": {
            "is_fulfilled__(name:\"XDTClientHints\")": true,
            "version": 4,
            "media": [
              {
                "is_fulfilled__(name:\"XDTMediaHint\")": true,
                "resources": [
                  {
                    "is_fulfilled__(name:\"XDTMediaResourceHint\")": true,
                    "image": {
                      "is_fulfilled__(name:\"XDTImageCandidate\")": true,
                      "width": 750,
                      "height": 1333,
                      "url": "https://scontent-lga3-3.cdninstagram.com/...",
                      "scans_profile": "e35"
                    }
                  }
                ]
              },
              {
                "is_fulfilled__(name:\"XDTMediaHint\")": true,
                "resources": [
                  {
                    "is_fulfilled__(name:\"XDTMediaResourceHint\")": true,
                    "image": {
                      "is_fulfilled__(name:\"XDTImageCandidate\")": true,
                      "width": 750,
                      "height": 1333,
                      "url": "https://scontent-lga3-3.cdninstagram.com/...",
                      "scans_profile": "e35"
                    }
                  }
                ]
              },
              {
                "is_fulfilled__(name:\"XDTMediaHint\")": true,
                "resources": [
                  {
                    "is_fulfilled__(name:\"XDTMediaResourceHint\")": true,
                    "image": {
                      "is_fulfilled__(name:\"XDTImageCandidate\")": true,
                      "width": 750,
                      "height": 500,
                      "url": "https://scontent-lga3-2.cdninstagram.com/...",
                      "scans_profile": "e35"
                    }
                  }
                ]
              }
            ]
          }
        }
      },
      "extensions": {
        "is_final": false,
        "fulfilled_payloads": [
          {
            "label": "ClientHintsResponse__force_flush",
            "path": [
              "1$xdt_api__v1__profile_timeline(_request_data:{\"count\":$count,\"exclude_comment\":$exclude_comment,\"fetch_all_highlights\":$fetch_all_highlights,\"fetch_media_for_highlights\":$include_associated_highlights,\"fetch_profile_grid_items\":$fetch_profile_grid_items,\"is_pull_to_refresh\":$is_pull_to_refresh,\"max_id\":$max_id,\"pinned_profile_grid_items_ids\":$pinned_profile_grid_items_ids,\"profile_grid_items_cursor\":$profile_grid_items_cursor},user_id:$user_id)"
            ]
          }
        ],
        "server_metadata": {
          "request_start_time_ms": 1775669043059,
          "time_at_flush_ms": 1775669043410
        }
      },
      "status": "ok"
    },
    {
      "path": [
        "1$xdt_api__v1__profile_timeline(_request_data:{\"count\":$count,\"exclude_comment\":$exclude_comment,\"fetch_all_highlights\":$fetch_all_highlights,\"fetch_media_for_highlights\":$include_associated_highlights,\"fetch_profile_grid_items\":$fetch_profile_grid_items,\"is_pull_to_refresh\":$is_pull_to_refresh,\"max_id\":$max_id,\"pinned_profile_grid_items_ids\":$pinned_profile_grid_items_ids,\"profile_grid_items_cursor\":$profile_grid_items_cursor},user_id:$user_id)"
      ],
      "label": "ProfileTimelineFragment__force_flush",
      "data": {
        "is_fulfilled__(name:\"XDTProfileFeedDict\")": true,
        "pinned_profile_grid_items_ids": "",
        "profile_grid_items_cursor": "QVFCckZvU1EzbFRPY19MRE1rSklVM0ptelB1eERGa3lvOWJuaFN3ZkUxdVBSS3RWenpjbXFGM0V6bnRNWEl5cnpoOF9iWEI1dTFzOW03bGRYUE5lQTdGQQ==",
        "profile_grid_items": [
          {
            "__typename": "XDTProfileGridItemDict",
            "strong_id__": null,
            "is_fulfilled__(name:\"XDTProfileGridItemDict\")": true,
            "highlight": null,
            "item_type": "media",
            "media": {
              "__typename": "XDTMediaDict",
              "strong_id__": "3865659729796199935_787132",
              "id": "3865659729796199935_787132",
              "is_fulfilled__(name:\"XDTMediaDict\")": true,
              "carousel_media_count": null,
              "carousel_media": null,
              "content_views_count": null,
              "enable_waist": true,
              "image_versions2": {
                "additional_candidates": {
                  "first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lga3-3.cdninstagram.com/...",
                    "width": 640
                  },
                  "igtv_first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lga3-3.cdninstagram.com/...",
                    "width": 640
                  },
                  "smart_frame": null
                },
                "candidates": [
                  {
                    "estimated_scans_sizes": [
                      24827,
                      49654,
                      74482
                    ],
                    "height": 1333,
                    "scans_profile": "e35",
                    "url": "https://scontent-lga3-3.cdninstagram.com/...",
                    "width": 750
                  }
                ],
                "scrubber_spritesheet_info_candidates": {
                  "default": {
                    "file_size_kb": 264,
                    "max_thumbnails_per_sprite": 105,
                    "rendered_width": 96,
                    "sprite_height": 1232,
                    "sprite_width": 1500,
                    "1fthumbnail_duration": 0.5723904762,
                    "thumbnail_height": 176,
                    "thumbnail_width": 100,
                    "thumbnails_per_row": 15,
                    "total_thumbnail_num_per_sprite": 105,
                    "1fvideo_length": 60.101
                  }
                },
                "smart_thumbnail_enabled": null
              },
              "media_cropping_info": null,
              "media_type": 2,
              "original_height": 1280,
              "original_width": 720,
              "pk": "3865659729796199935",
              "profile_grid_thumbnail_fitting_style": "UNSET",
              "product_type": "clips",
              "timeline_pinned_user_ids": [
                "787132"
              ],
              "open_carousel_submission_state": null,
              "all_previous_submitters": null,
              "user": {
                "__typename": "XDTUserDict",
                "strong_id__": "787132",
                "id": "787132",
                "account_type": 2,
                "all_media_count": null,
                "allowed_commenter_type": null,
                "can_boost_post": null,
                "can_see_organic_insights": null,
                "fan_club_info": {
                  "autosave_to_exclusive_highlight": null,
                  "connected_member_count": null,
                  "fan_club_id": null,
                  "fan_club_name": null,
                  "fan_consideration_page_revamp_eligiblity": null,
                  "has_enough_subscribers_for_ssc": null,
                  "is_fan_club_referral_eligible": null,
                  "is_fan_club_gifting_eligible": null,
                  "subscriber_count": null
                },
                "fbid_v2": "17841400573960012",
                "feed_post_reshare_disabled": false,
                "full_name": "National Geographic",
                "has_anonymous_profile_picture": false,
                "has_onboarded_to_text_post_app": null,
                "interop_messaging_user_fbid": "113671860027320",
                "is_active_on_text_post_app": true,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "liked_clips_count": null,
                "pk": "787132",
                "profile_pic_id": "3865702555259028436_787132",
                "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/...",
                "reel_auto_archive": null,
                "show_account_transparency_details": true,
                "show_insights_terms": null,
                "third_party_downloads_enabled": 2,
                "transparency_product_enabled": false,
                "username": "natgeo"
              },
              "1ltaken_at": 1775048403
            }
          },
          {
            "__typename": "XDTProfileGridItemDict",
            "strong_id__": null,
            "is_fulfilled__(name:\"XDTProfileGridItemDict\")": true,
            "highlight": null,
            "item_type": "media",
            "media": {
              "__typename": "XDTMediaDict",
              "strong_id__": "3844732796656436386_787132",
              "id": "3844732796656436386_787132",
              "is_fulfilled__(name:\"XDTMediaDict\")": true,
              "carousel_media_count": null,
              "carousel_media": null,
              "content_views_count": null,
              "enable_waist": true,
              "image_versions2": {
                "additional_candidates": {
                  "first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lga3-3.cdninstagram.com/...",
                    "width": 640
                  },
                  "igtv_first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lga3-3.cdninstagram.com/...",
                    "width": 640
                  },
                  "smart_frame": null
                },
                "candidates": [
                  {
                    "estimated_scans_sizes": [
                      48270,
                      96540,
                      144811
                    ],
                    "height": 1333,
                    "scans_profile": "e35",
                    "url": "https://scontent-lga3-3.cdninstagram.com/...",
                    "width": 750
                  }
                ],
                "scrubber_spritesheet_info_candidates": {
                  "default": {
                    "file_size_kb": 313,
                    "max_thumbnails_per_sprite": 105,
                    "rendered_width": 96,
                    "sprite_height": 1232,
                    "sprite_width": 1500,
                    "1fthumbnail_duration": 0.5721333333,
                    "thumbnail_height": 176,
                    "thumbnail_width": 100,
                    "thumbnails_per_row": 15,
                    "total_thumbnail_num_per_sprite": 105,
                    "1fvideo_length": 60.074
                  }
                },
                "smart_thumbnail_enabled": null
              },
              "media_cropping_info": null,
              "media_type": 2,
              "original_height": 1280,
              "original_width": 720,
              "pk": "3844732796656436386",
              "profile_grid_thumbnail_fitting_style": "UNSET",
              "product_type": "clips",
              "timeline_pinned_user_ids": [
                "787132"
              ],
              "open_carousel_submission_state": null,
              "all_previous_submitters": null,
              "user": {
                "__typename": "XDTUserDict",
                "strong_id__": "787132",
                "id": "787132",
                "account_type": 2,
                "all_media_count": null,
                "allowed_commenter_type": null,
                "can_boost_post": null,
                "can_see_organic_insights": null,
                "fan_club_info": {
                  "autosave_to_exclusive_highlight": null,
                  "connected_member_count": null,
                  "fan_club_id": null,
                  "fan_club_name": null,
                  "fan_consideration_page_revamp_eligiblity": null,
                  "has_enough_subscribers_for_ssc": null,
                  "is_fan_club_referral_eligible": null,
                  "is_fan_club_gifting_eligible": null,
                  "subscriber_count": null
                },
                "fbid_v2": "17841400573960012",
                "feed_post_reshare_disabled": false,
                "full_name": "National Geographic",
                "has_anonymous_profile_picture": false,
                "has_onboarded_to_text_post_app": null,
                "interop_messaging_user_fbid": "113671860027320",
                "is_active_on_text_post_app": true,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "liked_clips_count": null,
                "pk": "787132",
                "profile_pic_id": "3865702555259028436_787132",
                "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/...",
                "reel_auto_archive": null,
                "show_account_transparency_details": true,
                "show_insights_terms": null,
                "third_party_downloads_enabled": 2,
                "transparency_product_enabled": false,
                "username": "natgeo"
              },
              "1ltaken_at": 1772550004
            }
          },
          {
            "__typename": "XDTProfileGridItemDict",
            "strong_id__": null,
            "is_fulfilled__(name:\"XDTProfileGridItemDict\")": true,
            "highlight": null,
            "item_type": "media",
            "media": {
              "__typename": "XDTMediaDict",
              "strong_id__": "3870670793969876810_787132",
              "id": "3870670793969876810_787132",
              "is_fulfilled__(name:\"XDTMediaDict\")": true,
              "carousel_media_count": 10,
              "carousel_media": [
                {
                  "__typename": "XDTMediaDict",
                  "strong_id__": "3870670683399590370_787132",
                  "id": "3870670683399590370_787132",
                  "carousel_parent_id": "3870670793969876810_787132",
                  "image_versions2": {
                    "candidates": [
                      {
                        "width": 1439,
                        "height": 959,
                        "url": "https://scontent-lga3-2.cdninstagram.com/...",
                        "scans_profile": "e35",
                        "estimated_scans_sizes": [
                          56778,
                          113556,
                          170335
                        ]
                      },
                      {
                        "width": 750,
                        "height": 500,
                        "url": "https://scontent-lga3-2.cdninstagram.com/...",
                        "scans_profile": "e35",
                        "estimated_scans_sizes": [
                          27979,
                          55958,
                          83938
                        ]
                      }
                    ],
                    "smart_thumbnail_enabled": null
                  },
                  "is_dash_eligible": null,
                  "media_type": 1,
                  "original_width": 1439,
                  "original_height": 959,
                  "pk": "3870670683399590370"
                },
                {
                  "__typename": "XDTMediaDict",
                  "strong_id__": "3870670679968669302_787132",
                  "id": "3870670679968669302_787132",
                  "carousel_parent_id": "3870670793969876810_787132",
                  "image_versions2": {
                    "candidates": [
                      {
                        "width": 1439,
                        "height": 959,
                        "url": "https://scontent-lga3-2.cdninstagram.com/...",
                        "scans_profile": "e35",
                        "estimated_scans_sizes": [
                          40239,
                          80479,
                          120719
                        ]
                      },
                      {
                        "width": 750,
                        "height": 500,
                        "url": "https://scontent-lga3-2.cdninstagram.com/...",
                        "scans_profile": "e35",
                        "estimated_scans_sizes": [
                          19829,
                          39659,
                          59488
                        ]
                      }
                    ],
                    "smart_thumbnail_enabled": null
                  },
                  "is_dash_eligible": null,
                  "media_type": 1,
                  "original_width": 1439,
                  "original_height": 959,
                  "pk": "3870670679968669302"
                },
                {
                  "__typename": "XDTMediaDict",
                  "strong_id__": "3870670694816531730_787132",
                  "id": "3870670694816531730_787132",
                  "carousel_parent_id": "3870670793969876810_787132",
                  "image_versions2": {
                    "candidates": [
                      {
                        "width": 1440,
                        "height": 1080,
                        "url": "https://scontent-lga3-2.cdninstagram.com/...",
                        "scans_profile": "e35",
                        "estimated_scans_sizes": [
                          51971,
                          103943,
                          155915
                        ]
                      },
                      {
                        "width": 750,
                        "height": 563,
                        "url": "https://scontent-lga3-2.cdninstagram.com/...",
                        "scans_profile": "e35",
                        "estimated_scans_sizes": [
                          25599,
                          51198,
                          76797
                        ]
                      }
                    ],
                    "smart_thumbnail_enabled": null
                  },
                  "is_dash_eligible": null,
                  "media_type": 1,
                  "original_width": 1440,
                  "original_height": 1080,
                  "pk": "3870670694816531730"
                }
              ],
              "content_views_count": null,
              "enable_waist": true,
              "image_versions2": {
                "additional_candidates": null,
                "candidates": [
                  {
                    "estimated_scans_sizes": [
                      56778,
                      113556,
                      170335
                    ],
                    "height": 959,
                    "scans_profile": "e35",
                    "url": "https://scontent-lga3-2.cdninstagram.com/...",
                    "width": 1439
                  },
                  {
                    "estimated_scans_sizes": [
                      27979,
                      55958,
                      83938
                    ],
                    "height": 500,
                    "scans_profile": "e35",
                    "url": "https://scontent-lga3-2.cdninstagram.com/...",
                    "width": 750
                  }
                ],
                "scrubber_spritesheet_info_candidates": null,
                "smart_thumbnail_enabled": null
              },
              "media_cropping_info": null,
              "media_type": 8,
              "original_height": 959,
              "original_width": 1439,
              "pk": "3870670793969876810",
              "profile_grid_thumbnail_fitting_style": "UNSET",
              "product_type": "carousel_container",
              "timeline_pinned_user_ids": [],
              "open_carousel_submission_state": "closed",
              "all_previous_submitters": [],
              "user": {
                "__typename": "XDTUserDict",
                "strong_id__": "787132",
                "id": "787132",
                "account_type": 2,
                "all_media_count": null,
                "allowed_commenter_type": null,
                "can_boost_post": null,
                "can_see_organic_insights": null,
                "fan_club_info": {
                  "autosave_to_exclusive_highlight": null,
                  "connected_member_count": null,
                  "fan_club_id": null,
                  "fan_club_name": null,
                  "fan_consideration_page_revamp_eligiblity": null,
                  "has_enough_subscribers_for_ssc": null,
                  "is_fan_club_referral_eligible": null,
                  "is_fan_club_gifting_eligible": null,
                  "subscriber_count": null
                },
                "fbid_v2": "17841400573960012",
                "feed_post_reshare_disabled": false,
                "full_name": "National Geographic",
                "has_anonymous_profile_picture": false,
                "has_onboarded_to_text_post_app": null,
                "interop_messaging_user_fbid": "113671860027320",
                "is_active_on_text_post_app": true,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "liked_clips_count": null,
                "pk": "787132",
                "profile_pic_id": "3865702555259028436_787132",
                "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/...",
                "reel_auto_archive": null,
                "show_account_transparency_details": true,
                "show_insights_terms": null,
                "third_party_downloads_enabled": 2,
                "transparency_product_enabled": false,
                "username": "natgeo"
              },
              "1ltaken_at": 1775642401
            }
          }
        ],
        "more_available": true,
        "next_max_id": "3868170261056492782",
        "num_results": 12,
        "user": {
          "__typename": "XDTUserDict",
          "strong_id__": "787132",
          "id": "787132",
          "full_name": "National Geographic",
          "has_onboarded_to_text_post_app": null,
          "is_cannes": false,
          "is_private": false,
          "is_verified": true,
          "pk": "787132",
          "profile_grid_display_type": "default",
          "profile_overlay_info": {
            "bloks_payload": null,
            "overlay_format": "NONE"
          },
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/...",
          "username": "natgeo",
          "user_activation_info": {
            "activation_type": null
          }
        },
        "auto_load_more_enabled": true
      },
      "extensions": {
        "is_final": false
      }
    },
    {
      "path": [
        "1$xdt_api__v1__profile_timeline(_request_data:{\"count\":$count,\"exclude_comment\":$exclude_comment,\"fetch_all_highlights\":$fetch_all_highlights,\"fetch_media_for_highlights\":$include_associated_highlights,\"fetch_profile_grid_items\":$fetch_profile_grid_items,\"is_pull_to_refresh\":$is_pull_to_refresh,\"max_id\":$max_id,\"pinned_profile_grid_items_ids\":$pinned_profile_grid_items_ids,\"profile_grid_items_cursor\":$profile_grid_items_cursor},user_id:$user_id)",
        "profile_grid_items",
        11
      ],
      "label": "ProfileTimelineMediaItemDeferredFields",
      "data": {
        "__typename": "XDTMediaDict",
        "strong_id__": "3868170261056492782_787132",
        "id": "3868170261056492782_787132",
        "is_fulfilled__(name:\"XDTMediaDict\")": true,
        "linked_media_data": null,
        "channel_tag_data": null,
        "organic_cta_type": null,
        "organic_cta_info": null,
        "story_prompts": null,
        "carousel_media_pending_post_count": null,
        "main_feed_carousel_starting_media_id": null,
        "1ftallest_media_aspect_ratio": null,
        "open_to_public_submission_description_text": null,
        "is_dismiss_pending_media_banner": null,
        "save_count": null,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiNTdjODYyYTBkNzEzNDhhNjk0YzVkYzhhN2QxZWEzMzIzODY4MTcwMjYxMDU2NDkyNzgyIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTA0MzgyM3wzODY4MTcwMjYxMDU2NDkyNzgyfDM0MTY1NDk1NTU5fDE3NmMwMzc0ZDNhZWFkZGQwOWJlYWQxZjNiZDU5NzQ2NThhNTVlOGI1Mjg5NDRiNzhkNDhmMzYyZjBlMWQzMWUifSwic2lnbmF0dXJlIjoiIn0=",
        "wearable_attribution_info": null,
        "accessibility_caption": null,
        "are_remixes_crosspostable": true,
        "crosspost": null,
        "crosspost_metadata": {
          "fb_crosspost_deeplink_profile_id": null,
          "fb_crosspost_fbid": null,
          "is_feedback_aggregated": null,
          "th_unified_feedback_row_tap_target_url": null,
          "unified_feedback_enabled": null,
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "attribution_content_url": null,
        "audience": null,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boosted_post_id": null,
        "boosted_status": null,
        "original_media_has_visual_reply_media": false,
        "like_and_view_counts_disabled": false,
        "share_count_disabled": false,
        "code": "DWugFulAJTu",
        "coauthor_producer_can_see_organic_insights": false,
        "coauthor_producers": [
          {
            "__typename": "XDTUserDict",
            "strong_id__": "271370325",
            "id": "271370325",
            "full_name": "christine wilkinson, phd",
            "is_private": false,
            "is_verified": false,
            "profile_pic_id": "3245086179333885169_271370325",
            "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/...",
            "username": "christine_eleanor",
            "user_activation_info": {
              "activation_type": null
            }
          }
        ],
        "invited_coauthor_producers": [],
        "caption": {
          "__typename": "XDTCommentDict",
          "strong_id__": "18083194658064008",
          "pk": "18083194658064008",
          "bit_flags": 0,
          "content_type": "comment",
          "1lcreated_at": 1775404813,
          "1lcreated_at_utc": 1775404813,
          "did_report_as_spam": false,
          "fb_mentioned_users": null,
          "has_translation": null,
          "is_covered": false,
          "is_ranked_comment": false,
          "media_id": "3868170261056492782",
          "private_reply_status": 0,
          "share_enabled": false,
          "status": "Active",
          "text": "Spotted hyenas are a powerful example of the resilience and strength found in nature. For wildlife ecologist, conservation scientist, and National Geographic Explorer Dr. Christine Wilkinson (@christine_eleanor), these reminders are what wonder is all about. \n\n#StepIntoWonder with National Geographic’s #EarthMonth collection on @DisneyPlus.",
          "text_translation": null,
          "type": 1,
          "user": {
            "__typename": "XDTUserDict",
            "strong_id__": "787132",
            "id": "787132",
            "username": "natgeo",
            "full_name": "National Geographic",
            "is_private": false,
            "1fcoeff_weight": null,
            "social_context": null,
            "is_active": null,
            "is_verified": true,
            "profile_pic_id": "3865702555259028436_787132",
            "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/...",
            "has_onboarded_to_text_post_app": null,
            "follower_count": 274988953,
            "fbid_v2": "17841400573960012"
          }
        },
        "caption_add_on": null,
        "caption_is_edited": false,
        "carousel_last_edited_at": null,
        "creator_viewer_insights": null,
        "community_notes_info": {
          "has_viewer_submitted_note": false,
          "note_submission_disabled": false,
          "enable_submission_friction": false,
          "is_eligible_for_request_a_note": true
        },
        "can_modify_carousel": null,
        "can_viewer_save": true,
        "can_viewer_reshare": true,
        "has_liked": false,
        "top_likers": [],
        "facepile_top_likers": null,
        "floating_context_items": [],
        "social_context": [],
        "is_comments_gif_composer_enabled": false,
        "is_currently_promoting_by_sponsor": null,
        "is_auto_created": null,
        "is_cutout_sticker_allowed": false,
        "is_eligible_for_media_note_recs_nux": null,
        "is_reuse_allowed": false,
        "is_post_live_clips_media": false,
        "is_quiet_post": false,
        "is_shared_from_basel": null,
        "media_attributions_data": [],
        "igbio_product": null,
        "location": null,
        "play_count": 1307812,
        "like_count": 7490,
        "client_cache_key": "Mzg2ODE3MDI2MTA1NjQ5Mjc4Mg==.3",
        "filter_type": 0,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "subscribe_cta_visible": false,
        "video_subtitles_locale": null,
        "translated_video_subtitles": null,
        "byoa_langs": null,
        "video_sticker_locales": [],
        "sticker_translations_enabled": null,
        "clips_karaoke_caption": null,
        "clips_captions": null,
        "clips_captions_translations_urls": null,
        "clips_text": null,
        "should_request_ads": false,
        "is_paid_partnership": false,
        "sponsor_tags": null,
        "is_visual_reply_commenter_notice_enabled": true,
        "clips_tab_pinned_user_ids": [],
        "is_in_profile_grid": false,
        "profile_grid_control_enabled": false,
        "owner": {
          "__typename": "XDTUserDict",
          "strong_id__": "787132",
          "id": "787132",
          "can_see_quiet_post_attribution": true,
          "fbid_v2": "17841400573960012",
          "feed_post_reshare_disabled": false,
          "full_name": "National Geographic",
          "has_anonymous_profile_picture": false,
          "is_favorite": false,
          "is_private": false,
          "is_unpublished": false,
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/...",
          "show_account_transparency_details": true,
          "transparency_product_enabled": false,
          "username": "natgeo"
        },
        "fundraiser_tag": {
          "beneficiary_username": null,
          "beneficiary_name": null,
          "can_viewer_donate": null,
          "contextual_title_str": null,
          "formatted_amount_raised": null,
          "formatted_fundraiser_progress_info_text": null,
          "formatted_goal_amount": null,
          "fundraiser_id": null,
          "fundraiser_title": null,
          "fundraiser_type": null,
          "has_standalone_fundraiser": false,
          "progress_str": null,
          "thumbnail_display_url": null,
          "is_media_owner_fundraiser_owner": null,
          "fundraiser_owner_username": null,
          "show_fundraiser_owner_attribution": null,
          "can_viewer_remove_fundraiser_tag": null
        },
        "comment_likes_enabled": true,
        "comments_disabled": null,
        "comment_threading_enabled": true,
        "creative_config": null,
        "max_num_visible_preview_comments": 2,
        "has_more_comments": true,
        "has_tagged_users": true,
        "fb_user_tags": {
          "in": []
        },
        "has_reshares": null,
        "preview": null,
        "product_collection_tag": null,
        "product_suggestions": null,
        "product_tags": null,
        "photo_of_you": false,
        "is_organic_product_tagging_eligible": true,
        "media_notice": null,
        "media_overlay_info": null,
        "boost_upsell_banner_payload": null,
        "is_fb_only": null,
        "is_artist_pick": false,
        "can_see_insights_as_brand": false,
        "comment_count": 78,
        "comment_inform_treatment": {
          "action_type": null,
          "should_have_inform_treatment": false,
          "text": "",
          "url": null
        },
        "can_view_more_preview_comments": false,
        "hide_view_all_comment_entrypoint": true,
        "inline_composer_display_condition": null,
        "1finline_composer_imp_trigger_time": null,
        "is_third_party_downloads_eligible": false,
        "ig_media_sharing_disabled": false,
        "has_viewer_saved": null,
        "carousel_media": null,
        "number_of_qualities": 7,
        "is_dash_eligible": 1,
        "upcoming_event": null,
        "usertags": null,
        "video_codec": "vp09.00.31.08.00.01.01.01.00",
        "video_versions": [
          {
            "url": "https://scontent-lga3-1.cdninstagram.com/...",
            "type": 101,
            "width": 720,
            "height": 1280
          }
        ],
        "1fvideo_duration": 47.8930015564,
        "1fvideo_subtitles_confidence": null,
        "video_subtitles_enabled": null,
        "video_subtitles_status": null,
        "video_subtitles_uri": null,
        "visibility": null,
        "view_count": null,
        "visual_comment_reply_sticker_info": null,
        "visual_replies_info": null,
        "xpost_deny_reason": null,
        "xpost_deny_reason_enum": null,
        "threads_xpost_deny_reason": null,
        "has_audio": true,
        "has_delayed_metadata": false,
        "has_hidden_comments": null,
        "reshare_count": 154,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_post_live": null,
        "deleted_reason": 0,
        "has_shared_to_fb": 0,
        "dominant_color": null,
        "music_metadata": null,
        "fb_comment_count": null,
        "fb_like_count": null,
        "fb_play_count": null,
        "ig_play_count": 1307812,
        "autodub_status": null,
        "mashup_info": null,
        "enable_media_notes_production": true,
        "media_repost_count": 91,
        "media_reposter_bottomsheet_enabled": false,
        "media_notes": {
          "items": []
        },
        "clips_attribution_info": null,
        "mv_link": null,
        "shimmed_mv_link": null
      },
      "extensions": {
        "is_final": false
      }
    }
  ]
}
```

</details>

---

### GET /gql/user/reposts

Get user media reposts

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `repost_next_max_id` | string | No | Repost Next Max Id |
| `flat` | boolean | No | Flatten nested response into simple items list |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/reposts?user_id=787132"
    # Next page: add &repost_next_max_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_reposts_gql(user_id="787132")
    # Next page: cl.user_reposts_gql(user_id="787132", repost_next_max_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/gql/user/reposts",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "repost_next_max_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/reposts?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    // Next page: add &repost_next_max_id=... to URL
    ```

<details>
<summary>Example response</summary>

```json
{
  "data": {
    "__typename": "Query",
    "strong_id__": null,
    "1$fetch__XDTUserDict(id:$id)": {
      "__typename": "XDTUserDict",
      "strong_id__": "787132",
      "id": "787132",
      "username": "natgeo",
      "1$user_reposts_timeline(max_id:$max_id)": {
        "is_fulfilled__(name:\"XDTProfileFeedDict\")": true,
        "repost_grid_items": [
          {
            "item_type": "media",
            "media": {
              "__typename": "XDTMediaDict",
              "strong_id__": "3870843069143258083_30018101",
              "id": "3870843069143258083_30018101",
              "is_fulfilled__(name:\"XDTMediaDict\")": true,
              "all_previous_submitters": null,
              "carousel_media": null,
              "carousel_media_count": null,
              "carousel_media_pending_post_count": null,
              "channel_tag_data": null,
              "content_views_count": null,
              "enable_media_notes_production": true,
              "enable_waist": true,
              "facepile_top_likers": null,
              "gen_ai_detection_method": {
                "detection_method": "NONE"
              },
              "has_delayed_metadata": false,
              "image_versions2": {
                "additional_candidates": {
                  "first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lax7-1.cdninstagram.com/...",
                    "width": 640
                  },
                  "igtv_first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lax7-1.cdninstagram.com/...",
                    "width": 640
                  },
                  "smart_frame": null
                },
                "candidates": [
                  {
                    "estimated_scans_sizes": [
                      7834,
                      15669,
                      23504
                    ],
                    "height": 1280,
                    "scans_profile": "e15",
                    "url": "https://scontent-lax3-2.cdninstagram.com/...",
                    "width": 720
                  }
                ],
                "scrubber_spritesheet_info_candidates": {
                  "default": {
                    "file_size_kb": 504,
                    "max_thumbnails_per_sprite": 105,
                    "rendered_width": 96,
                    "sprite_height": 1232,
                    "sprite_width": 1500,
                    "1fthumbnail_duration": 1.4113333333333333,
                    "thumbnail_height": 176,
                    "thumbnail_width": 100,
                    "thumbnails_per_row": 15,
                    "total_thumbnail_num_per_sprite": 105,
                    "1fvideo_length": 148.19
                  }
                },
                "smart_thumbnail_enabled": null
              },
              "is_dismiss_pending_media_banner": null,
              "main_feed_carousel_starting_media_id": null,
              "media_cropping_info": {
                "four_by_three_crop": {
                  "1fcrop_bottom": 0.842105263157894,
                  "1fcrop_left": 0.0,
                  "1fcrop_right": 1.0,
                  "1fcrop_top": 0.092426187419768
                },
                "square_crop": null
              },
              "media_notes": {
                "is_fulfilled__(name:\"XDTMediaNotesResponse\")": true,
                "items": [
                  {
                    "audience": 7,
                    "1lcreated_at": 1775668091,
                    "has_translation": false,
                    "id": "18067580990658315",
                    "note_response_info": null,
                    "note_style": 13,
                    "reactions": [],
                    "text": "",
                    "user": {
                      "__typename": "XDTUserDict",
                      "strong_id__": "787132",
                      "id": "787132",
                      "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                      "username": "natgeo"
                    },
                    "user_id": "787132"
                  }
                ]
              },
              "media_repost_count": 1,
              "media_reposter_bottomsheet_enabled": false,
              "media_type": 2,
              "open_carousel_submission_state": null,
              "open_to_public_submission_description_text": null,
              "organic_cta_info": null,
              "organic_cta_type": null,
              "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiZGE4MGE2NDlhNGU1NGMzNGEzYmY0YWMyMzUwMjBhNDMzODcwODQzMDY5MTQzMjU4MDgzIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTA0NzgyM3wzODcwODQzMDY5MTQzMjU4MDgzfDMyNjk0NjI2NjQ2fDI0YTUxMjAwN2U0NDk5M2M5ZTA1NDk2MTQyNDU1YjQ5ODg4ZWU2Yzc4MzVjYjg0NzIzMGViZDU2MWUzN2MyMzgifSwic2lnbmF0dXJlIjoiIn0=",
              "original_height": 1920,
              "original_width": 1080,
              "pk": "3870843069143258083",
              "product_type": "clips",
              "profile_grid_thumbnail_fitting_style": "UNSET",
              "save_count": null,
              "story_prompts": null,
              "1ltaken_at": 1775660746,
              "1ftallest_media_aspect_ratio": null,
              "timeline_pinned_user_ids": [],
              "user": {
                "__typename": "XDTUserDict",
                "strong_id__": "30018101",
                "id": "30018101",
                "account_type": 2,
                "all_media_count": null,
                "allowed_commenter_type": null,
                "can_boost_post": null,
                "can_see_organic_insights": null,
                "fan_club_info": {
                  "autosave_to_exclusive_highlight": null,
                  "connected_member_count": null,
                  "fan_club_id": null,
                  "fan_club_name": null,
                  "fan_consideration_page_revamp_eligiblity": null,
                  "has_enough_subscribers_for_ssc": null,
                  "is_fan_club_gifting_eligible": null,
                  "is_fan_club_referral_eligible": null,
                  "subscriber_count": null
                },
                "fbid_v2": "17841400063030469",
                "feed_post_reshare_disabled": false,
                "full_name": "Hollywood Records",
                "has_anonymous_profile_picture": false,
                "has_onboarded_to_text_post_app": null,
                "interop_messaging_user_fbid": "102264417840763",
                "is_active_on_text_post_app": true,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "liked_clips_count": null,
                "pk": "30018101",
                "profile_pic_id": "3801355028326713704_30018101",
                "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                "reel_auto_archive": null,
                "show_account_transparency_details": true,
                "show_insights_terms": null,
                "third_party_downloads_enabled": 1,
                "transparency_product_enabled": false,
                "username": "hollywoodrecords"
              },
              "wearable_attribution_info": null,
              "accessibility_caption": null,
              "are_remixes_crosspostable": true,
              "attribution_content_url": null,
              "audience": null,
              "autodub_status": null,
              "boost_unavailable_identifier": null,
              "boost_unavailable_reason": null,
              "boost_upsell_banner_payload": null,
              "boosted_post_id": null,
              "boosted_status": null,
              "byoa_langs": null,
              "can_modify_carousel": null,
              "can_see_insights_as_brand": false,
              "can_view_more_preview_comments": false,
              "can_viewer_reshare": true,
              "can_viewer_save": true,
              "caption": {
                "__typename": "XDTCommentDict",
                "strong_id__": "18067566809658315",
                "pk": "18067566809658315",
                "bit_flags": 0,
                "content_type": "comment",
                "1lcreated_at": 1775660697,
                "1lcreated_at_utc": 1775660697,
                "did_report_as_spam": false,
                "has_translation": null,
                "is_covered": false,
                "is_ranked_comment": false,
                "media_id": "3870843069143258083",
                "private_reply_status": 0,
                "share_enabled": false,
                "status": "Active",
                "text": "We are all one, vibrating together. 🙏🍃 @maejor dives into the inspiration behind @natgeo’s Earth Moods: Frequencies, Vol. 1 from Maejor, featuring five instrumental songs built around therapeutic frequencies and global soundscapes. This #EarthMonth, find calm, support your focus and well-being...listen now wherever you stream music.\n\n#StepIntoWonder with Earth Moods and the full #EarthMonth collection from National Geographic, now streaming on @disneyplus.",
                "type": 1,
                "user": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "30018101",
                  "id": "30018101",
                  "1fcoeff_weight": null,
                  "fbid_v2": "17841400063030469",
                  "follower_count": 306651,
                  "full_name": "Hollywood Records",
                  "has_onboarded_to_text_post_app": null,
                  "is_active": null,
                  "is_private": false,
                  "is_verified": true,
                  "pk": "30018101",
                  "profile_pic_id": "3801355028326713704_30018101",
                  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                  "social_context": null,
                  "username": "hollywoodrecords"
                }
              },
              "caption_add_on": null,
              "caption_is_edited": false,
              "carousel_last_edited_at": null,
              "client_cache_key": "Mzg3MDg0MzA2OTE0MzI1ODA4Mw==.3",
              "clips_attribution_info": null,
              "clips_karaoke_caption": null,
              "clips_captions": null,
              "clips_captions_translations_urls": null,
              "clips_tab_pinned_user_ids": [],
              "clips_text": null,
              "coauthor_producer_can_see_organic_insights": false,
              "coauthor_producers": [
                {
                  "__typename": "XDTUserDict",
                  "strong_id__": "18091046",
                  "id": "18091046",
                  "full_name": "National Geographic TV",
                  "is_private": false,
                  "is_verified": true,
                  "pk": "18091046",
                  "profile_pic_id": "3865691934048399589_18091046",
                  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                  "username": "natgeotv"
                }
              ],
              "code": "DW3_0NFkRPj",
              "comment_count": 0,
              "comment_inform_treatment": {
                "action_type": null,
                "should_have_inform_treatment": false,
                "text": "",
                "url": null
              },
              "comment_likes_enabled": true,
              "comment_threading_enabled": true,
              "comments_disabled": null,
              "community_notes_info": {
                "enable_submission_friction": false,
                "has_viewer_submitted_note": false,
                "note_submission_disabled": false
              },
              "creative_config": null,
              "creator_viewer_insights": null,
              "crosspost": null,
              "crosspost_metadata": {
                "fb_crosspost_deeplink_profile_id": null,
                "fb_crosspost_fbid": null,
                "fb_downstream_use_xpost_metadata": {
                  "downstream_use_xpost_deny_reason": "NONE"
                },
                "is_feedback_aggregated": null,
                "th_unified_feedback_row_tap_target_url": null,
                "unified_feedback_enabled": null
              },
              "deleted_reason": 0,
              "dominant_color": null,
              "fb_comment_count": null,
              "fb_like_count": null,
              "fb_play_count": null,
              "filter_type": 0,
              "fundraiser_tag": {
                "beneficiary_name": null,
                "beneficiary_username": null,
                "can_viewer_donate": null,
                "can_viewer_remove_fundraiser_tag": null,
                "contextual_title_str": null,
                "formatted_amount_raised": null,
                "formatted_fundraiser_progress_info_text": null,
                "formatted_goal_amount": null,
                "fundraiser_id": null,
                "fundraiser_owner_username": null,
                "fundraiser_title": null,
                "fundraiser_type": null,
                "has_standalone_fundraiser": false,
                "is_media_owner_fundraiser_owner": null,
                "progress_str": null,
                "show_fundraiser_owner_attribution": null,
                "thumbnail_display_url": null
              },
              "has_audio": true,
              "has_hidden_comments": null,
              "has_liked": false,
              "has_more_comments": false,
              "has_reshares": null,
              "has_shared_to_fb": 0,
              "has_tagged_users": true,
              "has_viewer_saved": null,
              "hide_view_all_comment_entrypoint": true,
              "ig_media_sharing_disabled": false,
              "ig_play_count": 3228,
              "igbio_product": null,
              "inline_composer_display_condition": null,
              "1finline_composer_imp_trigger_time": null,
              "invited_coauthor_producers": [],
              "is_artist_pick": false,
              "is_auto_created": null,
              "is_comments_gif_composer_enabled": true,
              "is_currently_promoting_by_sponsor": null,
              "is_cutout_sticker_allowed": false,
              "is_dash_eligible": 1,
              "is_eligible_for_media_note_recs_nux": null,
              "is_fb_only": null,
              "is_in_profile_grid": false,
              "is_organic_product_tagging_eligible": true,
              "is_paid_partnership": false,
              "is_post_live": null,
              "is_post_live_clips_media": false,
              "is_quiet_post": false,
              "is_reshare_of_text_post_app_media_in_ig": false,
              "is_reuse_allowed": false,
              "is_shared_from_basel": null,
              "is_third_party_downloads_eligible": true,
              "is_visual_reply_commenter_notice_enabled": true,
              "like_and_view_counts_disabled": false,
              "like_count": 51,
              "media_attributions_data": [],
              "location": null,
              "mashup_info": null,
              "max_num_visible_preview_comments": 2,
              "media_notice": null,
              "media_overlay_info": null,
              "music_metadata": null,
              "mv_link": null,
              "number_of_qualities": 4,
              "original_media_has_visual_reply_media": false,
              "owner": {
                "__typename": "XDTUserDict",
                "strong_id__": "30018101",
                "id": "30018101",
                "can_see_quiet_post_attribution": true,
                "fbid_v2": "17841400063030469",
                "feed_post_reshare_disabled": false,
                "full_name": "Hollywood Records",
                "has_anonymous_profile_picture": false,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "pk": "30018101",
                "profile_pic_id": "3801355028326713704_30018101",
                "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                "show_account_transparency_details": true,
                "transparency_product_enabled": false,
                "username": "hollywoodrecords"
              },
              "photo_of_you": false,
              "play_count": 3228,
              "preview": null,
              "product_collection_tag": null,
              "product_suggestions": null,
              "product_tags": null,
              "profile_grid_control_enabled": false,
              "reshare_count": 0,
              "share_count_disabled": false,
              "shimmed_mv_link": null,
              "should_request_ads": false,
              "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
              "social_context": [],
              "sticker_translations_enabled": null,
              "subscribe_cta_visible": false,
              "threads_xpost_deny_reason": null,
              "top_likers": [],
              "translated_video_subtitles": null,
              "upcoming_event": null,
              "usertags": null,
              "video_codec": "vp09.00.21.08.00.01.01.01.00",
              "1fvideo_duration": 148.20799255371094,
              "video_sticker_locales": [],
              "1fvideo_subtitles_confidence": null,
              "video_subtitles_enabled": null,
              "video_subtitles_locale": null,
              "video_subtitles_status": null,
              "video_subtitles_uri": null,
              "video_versions": [
                {
                  "height": 1280,
                  "id": "1430983184998566v",
                  "type": 101,
                  "url": "https://scontent-lax3-1.cdninstagram.com/...",
                  "width": 720
                }
              ],
              "view_count": null,
              "visibility": null,
              "visual_comment_reply_sticker_info": null,
              "visual_replies_info": null,
              "xpost_deny_reason": null,
              "xpost_deny_reason_enum": null,
              "floating_context_items": []
            }
          },
          {
            "item_type": "media",
            "media": {
              "__typename": "XDTMediaDict",
              "strong_id__": "3870130142916282392_18091046",
              "id": "3870130142916282392_18091046",
              "is_fulfilled__(name:\"XDTMediaDict\")": true,
              "all_previous_submitters": null,
              "carousel_media": null,
              "carousel_media_count": null,
              "carousel_media_pending_post_count": null,
              "channel_tag_data": null,
              "content_views_count": null,
              "enable_media_notes_production": true,
              "enable_waist": true,
              "facepile_top_likers": null,
              "gen_ai_detection_method": {
                "detection_method": "NONE"
              },
              "has_delayed_metadata": false,
              "image_versions2": {
                "additional_candidates": {
                  "first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lax7-1.cdninstagram.com/...",
                    "width": 640
                  },
                  "igtv_first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lax7-1.cdninstagram.com/...",
                    "width": 640
                  },
                  "smart_frame": null
                },
                "candidates": [
                  {
                    "estimated_scans_sizes": [
                      22800,
                      45600,
                      68400
                    ],
                    "height": 1333,
                    "scans_profile": "e35",
                    "url": "https://scontent-lax3-1.cdninstagram.com/...",
                    "width": 750
                  }
                ],
                "scrubber_spritesheet_info_candidates": {
                  "default": {
                    "file_size_kb": 368,
                    "max_thumbnails_per_sprite": 105,
                    "rendered_width": 96,
                    "sprite_height": 1232,
                    "sprite_width": 1500,
                    "1fthumbnail_duration": 0.4081809523809524,
                    "thumbnail_height": 176,
                    "thumbnail_width": 100,
                    "thumbnails_per_row": 15,
                    "total_thumbnail_num_per_sprite": 105,
                    "1fvideo_length": 42.859
                  }
                },
                "smart_thumbnail_enabled": null
              },
              "is_dismiss_pending_media_banner": null,
              "main_feed_carousel_starting_media_id": null,
              "media_cropping_info": null,
              "media_notes": {
                "is_fulfilled__(name:\"XDTMediaNotesResponse\")": true,
                "items": [
                  {
                    "audience": 7,
                    "1lcreated_at": 1775577889,
                    "has_translation": false,
                    "id": "17948733029984622",
                    "note_response_info": null,
                    "note_style": 13,
                    "reactions": [],
                    "text": "",
                    "user": {
                      "__typename": "XDTUserDict",
                      "strong_id__": "787132",
                      "id": "787132",
                      "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                      "username": "natgeo"
                    },
                    "user_id": "787132"
                  }
                ]
              },
              "media_repost_count": 33,
              "media_reposter_bottomsheet_enabled": false,
              "media_type": 2,
              "open_carousel_submission_state": null,
              "open_to_public_submission_description_text": null,
              "organic_cta_info": null,
              "organic_cta_type": null,
              "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiZGE4MGE2NDlhNGU1NGMzNGEzYmY0YWMyMzUwMjBhNDMzODcwMTMwMTQyOTE2MjgyMzkyIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTA0NzgzOXwzODcwMTMwMTQyOTE2MjgyMzkyfDMyNjk0NjI2NjQ2fGMyYzMyNDM5OWExOGMxZmE1MGE3YTU1OWEzOTIzZjEzZTU3NTFmY2Q4YzNmMTIzZDk1NzZmMDhlMTdmOWI0N2YifSwic2lnbmF0dXJlIjoiIn0=",
              "original_height": 1920,
              "original_width": 1080,
              "pk": "3870130142916282392",
              "product_type": "clips",
              "profile_grid_thumbnail_fitting_style": "UNSET",
              "save_count": null,
              "story_prompts": null,
              "1ltaken_at": 1775577621,
              "1ftallest_media_aspect_ratio": null,
              "timeline_pinned_user_ids": [],
              "user": {
                "__typename": "XDTUserDict",
                "strong_id__": "18091046",
                "id": "18091046",
                "account_type": 2,
                "all_media_count": null,
                "allowed_commenter_type": null,
                "can_boost_post": null,
                "can_see_organic_insights": null,
                "fan_club_info": {
                  "autosave_to_exclusive_highlight": null,
                  "connected_member_count": null,
                  "fan_club_id": null,
                  "fan_club_name": null,
                  "fan_consideration_page_revamp_eligiblity": null,
                  "has_enough_subscribers_for_ssc": null,
                  "is_fan_club_gifting_eligible": null,
                  "is_fan_club_referral_eligible": null,
                  "subscriber_count": null
                },
                "fbid_v2": "17841401291380282",
                "feed_post_reshare_disabled": false,
                "full_name": "National Geographic TV",
                "has_anonymous_profile_picture": false,
                "has_onboarded_to_text_post_app": null,
                "interop_messaging_user_fbid": "105432187515418",
                "is_active_on_text_post_app": true,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "liked_clips_count": null,
                "pk": "18091046",
                "profile_pic_id": "3865691934048399589_18091046",
                "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                "reel_auto_archive": null,
                "show_account_transparency_details": true,
                "show_insights_terms": null,
                "third_party_downloads_enabled": 2,
                "transparency_product_enabled": false,
                "username": "natgeotv"
              },
              "wearable_attribution_info": null,
              "accessibility_caption": null,
              "are_remixes_crosspostable": true,
              "attribution_content_url": null,
              "audience": null,
              "autodub_status": null,
              "boost_unavailable_identifier": null,
              "boost_unavailable_reason": null,
              "boost_upsell_banner_payload": null,
              "boosted_post_id": null,
              "boosted_status": null,
              "byoa_langs": null,
              "can_modify_carousel": null,
              "can_see_insights_as_brand": false,
              "can_view_more_preview_comments": false,
              "can_viewer_reshare": true,
              "can_viewer_save": true,
              "caption": {
                "__typename": "XDTCommentDict",
                "strong_id__": "17948732129984622",
                "pk": "17948732129984622",
                "bit_flags": 0,
                "content_type": "comment",
                "1lcreated_at": 1775577607,
                "1lcreated_at_utc": 1775577607,
                "did_report_as_spam": false,
                "has_translation": null,
                "is_covered": false,
                "is_ranked_comment": false,
                "media_id": "3870130142916282392",
                "private_reply_status": 0,
                "share_enabled": false,
                "status": "Active",
                "text": "Moments of wonder don't just come from nature—but from those who understand it masterfully too. That was conservationist and National Geographic Explorer @drsteveboyes' experience when searching for Angola's mythical \"ghost elephants\" with Xui, a San master tracker. \n\n#StepIntoWonder with National Geographic’s #EarthMonth collection and stream #GhostElephants on @DisneyPlus.",
                "type": 1,
                "user": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "18091046",
                  "id": "18091046",
                  "1fcoeff_weight": null,
                  "fbid_v2": "17841401291380282",
                  "follower_count": 7301283,
                  "full_name": "National Geographic TV",
                  "has_onboarded_to_text_post_app": null,
                  "is_active": null,
                  "is_private": false,
                  "is_verified": true,
                  "pk": "18091046",
                  "profile_pic_id": "3865691934048399589_18091046",
                  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                  "social_context": null,
                  "username": "natgeotv"
                }
              },
              "caption_add_on": null,
              "caption_is_edited": false,
              "carousel_last_edited_at": null,
              "client_cache_key": "Mzg3MDEzMDE0MjkxNjI4MjM5Mg==.3",
              "clips_attribution_info": null,
              "clips_karaoke_caption": null,
              "clips_captions": null,
              "clips_captions_translations_urls": null,
              "clips_tab_pinned_user_ids": [],
              "clips_text": null,
              "coauthor_producer_can_see_organic_insights": false,
              "coauthor_producers": [
                {
                  "__typename": "XDTUserDict",
                  "strong_id__": "1260571151",
                  "id": "1260571151",
                  "full_name": "Steve Boyes",
                  "is_private": false,
                  "is_verified": true,
                  "pk": "1260571151",
                  "profile_pic_id": "3019168329369961544_1260571151",
                  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                  "username": "drsteveboyes"
                },
                {
                  "__typename": "XDTUserDict",
                  "strong_id__": "15473083628",
                  "id": "15473083628",
                  "full_name": "Nat Geo Documentary Films",
                  "is_private": false,
                  "is_verified": true,
                  "pk": "15473083628",
                  "profile_pic_id": "3865721697802787660_15473083628",
                  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                  "username": "natgeodocs"
                }
              ],
              "code": "DW1dtwzDogY",
              "comment_count": 26,
              "comment_inform_treatment": {
                "action_type": null,
                "should_have_inform_treatment": false,
                "text": "",
                "url": null
              },
              "comment_likes_enabled": true,
              "comment_threading_enabled": true,
              "comments_disabled": null,
              "community_notes_info": {
                "enable_submission_friction": false,
                "has_viewer_submitted_note": false,
                "note_submission_disabled": false
              },
              "creative_config": null,
              "creator_viewer_insights": null,
              "crosspost": null,
              "crosspost_metadata": {
                "fb_crosspost_deeplink_profile_id": null,
                "fb_crosspost_fbid": null,
                "fb_downstream_use_xpost_metadata": {
                  "downstream_use_xpost_deny_reason": "NONE"
                },
                "is_feedback_aggregated": null,
                "th_unified_feedback_row_tap_target_url": null,
                "unified_feedback_enabled": null
              },
              "deleted_reason": 0,
              "dominant_color": null,
              "fb_comment_count": null,
              "fb_like_count": null,
              "fb_play_count": null,
              "filter_type": 0,
              "fundraiser_tag": {
                "beneficiary_name": null,
                "beneficiary_username": null,
                "can_viewer_donate": null,
                "can_viewer_remove_fundraiser_tag": null,
                "contextual_title_str": null,
                "formatted_amount_raised": null,
                "formatted_fundraiser_progress_info_text": null,
                "formatted_goal_amount": null,
                "fundraiser_id": null,
                "fundraiser_owner_username": null,
                "fundraiser_title": null,
                "fundraiser_type": null,
                "has_standalone_fundraiser": false,
                "is_media_owner_fundraiser_owner": null,
                "progress_str": null,
                "show_fundraiser_owner_attribution": null,
                "thumbnail_display_url": null
              },
              "has_audio": true,
              "has_hidden_comments": null,
              "has_liked": false,
              "has_more_comments": true,
              "has_reshares": null,
              "has_shared_to_fb": 0,
              "has_tagged_users": true,
              "has_viewer_saved": null,
              "hide_view_all_comment_entrypoint": true,
              "ig_media_sharing_disabled": false,
              "ig_play_count": 93699,
              "igbio_product": null,
              "inline_composer_display_condition": null,
              "1finline_composer_imp_trigger_time": null,
              "invited_coauthor_producers": [],
              "is_artist_pick": false,
              "is_auto_created": null,
              "is_comments_gif_composer_enabled": false,
              "is_currently_promoting_by_sponsor": null,
              "is_cutout_sticker_allowed": false,
              "is_dash_eligible": 1,
              "is_eligible_for_media_note_recs_nux": null,
              "is_fb_only": null,
              "is_in_profile_grid": false,
              "is_organic_product_tagging_eligible": true,
              "is_paid_partnership": false,
              "is_post_live": null,
              "is_post_live_clips_media": false,
              "is_quiet_post": false,
              "is_reshare_of_text_post_app_media_in_ig": false,
              "is_reuse_allowed": false,
              "is_shared_from_basel": null,
              "is_third_party_downloads_eligible": false,
              "is_visual_reply_commenter_notice_enabled": true,
              "like_and_view_counts_disabled": false,
              "like_count": 2510,
              "media_attributions_data": [],
              "location": null,
              "mashup_info": null,
              "max_num_visible_preview_comments": 2,
              "media_notice": null,
              "media_overlay_info": null,
              "music_metadata": null,
              "mv_link": null,
              "number_of_qualities": 8,
              "original_media_has_visual_reply_media": false,
              "owner": {
                "__typename": "XDTUserDict",
                "strong_id__": "18091046",
                "id": "18091046",
                "can_see_quiet_post_attribution": true,
                "fbid_v2": "17841401291380282",
                "feed_post_reshare_disabled": false,
                "full_name": "National Geographic TV",
                "has_anonymous_profile_picture": false,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "pk": "18091046",
                "profile_pic_id": "3865691934048399589_18091046",
                "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                "show_account_transparency_details": true,
                "transparency_product_enabled": false,
                "username": "natgeotv"
              },
              "photo_of_you": false,
              "play_count": 93699,
              "preview": null,
              "product_collection_tag": null,
              "product_suggestions": null,
              "product_tags": null,
              "profile_grid_control_enabled": false,
              "reshare_count": 35,
              "share_count_disabled": false,
              "shimmed_mv_link": null,
              "should_request_ads": false,
              "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
              "social_context": [],
              "sticker_translations_enabled": null,
              "subscribe_cta_visible": false,
              "threads_xpost_deny_reason": null,
              "top_likers": [],
              "translated_video_subtitles": null,
              "upcoming_event": null,
              "usertags": null,
              "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
              "1fvideo_duration": 42.858001708984375,
              "video_sticker_locales": [],
              "1fvideo_subtitles_confidence": null,
              "video_subtitles_enabled": null,
              "video_subtitles_locale": null,
              "video_subtitles_status": null,
              "video_subtitles_uri": null,
              "video_versions": [
                {
                  "height": 1280,
                  "id": "1291971733040522v",
                  "type": 101,
                  "url": "https://scontent-lax3-2.cdninstagram.com/...",
                  "width": 720
                }
              ],
              "view_count": null,
              "visibility": null,
              "visual_comment_reply_sticker_info": null,
              "visual_replies_info": null,
              "xpost_deny_reason": null,
              "xpost_deny_reason_enum": null,
              "floating_context_items": []
            }
          },
          {
            "item_type": "media",
            "media": {
              "__typename": "XDTMediaDict",
              "strong_id__": "3869523223822719896_18091046",
              "id": "3869523223822719896_18091046",
              "is_fulfilled__(name:\"XDTMediaDict\")": true,
              "all_previous_submitters": null,
              "carousel_media": null,
              "carousel_media_count": null,
              "carousel_media_pending_post_count": null,
              "channel_tag_data": null,
              "content_views_count": null,
              "enable_media_notes_production": true,
              "enable_waist": true,
              "facepile_top_likers": null,
              "gen_ai_detection_method": {
                "detection_method": "NONE"
              },
              "has_delayed_metadata": false,
              "image_versions2": {
                "additional_candidates": {
                  "first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lax3-1.cdninstagram.com/...",
                    "width": 640
                  },
                  "igtv_first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lax3-1.cdninstagram.com/...",
                    "width": 640
                  },
                  "smart_frame": null
                },
                "candidates": [
                  {
                    "estimated_scans_sizes": [
                      18719,
                      37438,
                      56158
                    ],
                    "height": 1333,
                    "scans_profile": "e35",
                    "url": "https://scontent-lax7-1.cdninstagram.com/...",
                    "width": 750
                  }
                ],
                "scrubber_spritesheet_info_candidates": {
                  "default": {
                    "file_size_kb": 315,
                    "max_thumbnails_per_sprite": 105,
                    "rendered_width": 96,
                    "sprite_height": 1232,
                    "sprite_width": 1500,
                    "1fthumbnail_duration": 0.7265142857142858,
                    "thumbnail_height": 176,
                    "thumbnail_width": 100,
                    "thumbnails_per_row": 15,
                    "total_thumbnail_num_per_sprite": 105,
                    "1fvideo_length": 76.284
                  }
                },
                "smart_thumbnail_enabled": null
              },
              "is_dismiss_pending_media_banner": null,
              "main_feed_carousel_starting_media_id": null,
              "media_cropping_info": null,
              "media_notes": {
                "is_fulfilled__(name:\"XDTMediaNotesResponse\")": true,
                "items": [
                  {
                    "audience": 7,
                    "1lcreated_at": 1775510140,
                    "has_translation": false,
                    "id": "17924460174101740",
                    "note_response_info": null,
                    "note_style": 13,
                    "reactions": [],
                    "text": "",
                    "user": {
                      "__typename": "XDTUserDict",
                      "strong_id__": "787132",
                      "id": "787132",
                      "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                      "username": "natgeo"
                    },
                    "user_id": "787132"
                  }
                ]
              },
              "media_repost_count": 203,
              "media_reposter_bottomsheet_enabled": false,
              "media_type": 2,
              "open_carousel_submission_state": null,
              "open_to_public_submission_description_text": null,
              "organic_cta_info": null,
              "organic_cta_type": null,
              "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiZGE4MGE2NDlhNGU1NGMzNGEzYmY0YWMyMzUwMjBhNDMzODY5NTIzMjIzODIyNzE5ODk2Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTA0NzgzOXwzODY5NTIzMjIzODIyNzE5ODk2fDMyNjk0NjI2NjQ2fDIyNzIxZjZkMDA1NmI1ZWQ4ZWRhZGEzOWU4ZTZlOTYzNjQ0ZGRkMDRiNjIyY2Q1ZmM4Njk2ZjZiN2I5MDI3NTMifSwic2lnbmF0dXJlIjoiIn0=",
              "original_height": 1920,
              "original_width": 1080,
              "pk": "3869523223822719896",
              "product_type": "clips",
              "profile_grid_thumbnail_fitting_style": "UNSET",
              "save_count": null,
              "story_prompts": null,
              "1ltaken_at": 1775509220,
              "1ftallest_media_aspect_ratio": null,
              "timeline_pinned_user_ids": [],
              "user": {
                "__typename": "XDTUserDict",
                "strong_id__": "18091046",
                "id": "18091046",
                "account_type": 2,
                "all_media_count": null,
                "allowed_commenter_type": null,
                "can_boost_post": null,
                "can_see_organic_insights": null,
                "fan_club_info": {
                  "autosave_to_exclusive_highlight": null,
                  "connected_member_count": null,
                  "fan_club_id": null,
                  "fan_club_name": null,
                  "fan_consideration_page_revamp_eligiblity": null,
                  "has_enough_subscribers_for_ssc": null,
                  "is_fan_club_gifting_eligible": null,
                  "is_fan_club_referral_eligible": null,
                  "subscriber_count": null
                },
                "fbid_v2": "17841401291380282",
                "feed_post_reshare_disabled": false,
                "full_name": "National Geographic TV",
                "has_anonymous_profile_picture": false,
                "has_onboarded_to_text_post_app": null,
                "interop_messaging_user_fbid": "105432187515418",
                "is_active_on_text_post_app": true,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "liked_clips_count": null,
                "pk": "18091046",
                "profile_pic_id": "3865691934048399589_18091046",
                "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                "reel_auto_archive": null,
                "show_account_transparency_details": true,
                "show_insights_terms": null,
                "third_party_downloads_enabled": 2,
                "transparency_product_enabled": false,
                "username": "natgeotv"
              },
              "wearable_attribution_info": null,
              "accessibility_caption": null,
              "are_remixes_crosspostable": true,
              "attribution_content_url": null,
              "audience": null,
              "autodub_status": null,
              "boost_unavailable_identifier": null,
              "boost_unavailable_reason": null,
              "boost_upsell_banner_payload": null,
              "boosted_post_id": null,
              "boosted_status": null,
              "byoa_langs": null,
              "can_modify_carousel": null,
              "can_see_insights_as_brand": false,
              "can_view_more_preview_comments": false,
              "can_viewer_reshare": true,
              "can_viewer_save": true,
              "caption": {
                "__typename": "XDTCommentDict",
                "strong_id__": "17924459310101740",
                "pk": "17924459310101740",
                "bit_flags": 0,
                "content_type": "comment",
                "1lcreated_at": 1775509207,
                "1lcreated_at_utc": 1775509207,
                "did_report_as_spam": false,
                "has_translation": null,
                "is_covered": false,
                "is_ranked_comment": false,
                "media_id": "3869523223822719896",
                "private_reply_status": 0,
                "share_enabled": false,
                "status": "Active",
                "text": "Nat Geo Explorer-at-Large @jamescameronofficial and entomologist @drsammygrams may use different tools when it comes to telling stories, but they're both devoted to sharing the wonders of the natural world. Even down to the lives of the tiniest bees.\n\nNarrated by @bertiegregory, #SecretsOfTheBees is now streaming on @DisneyPlus and @hulu.",
                "type": 1,
                "user": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "18091046",
                  "id": "18091046",
                  "1fcoeff_weight": null,
                  "fbid_v2": "17841401291380282",
                  "follower_count": 7301283,
                  "full_name": "National Geographic TV",
                  "has_onboarded_to_text_post_app": null,
                  "is_active": null,
                  "is_private": false,
                  "is_verified": true,
                  "pk": "18091046",
                  "profile_pic_id": "3865691934048399589_18091046",
                  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                  "social_context": null,
                  "username": "natgeotv"
                }
              },
              "caption_add_on": null,
              "caption_is_edited": false,
              "carousel_last_edited_at": null,
              "client_cache_key": "Mzg2OTUyMzIyMzgyMjcxOTg5Ng==.3",
              "clips_attribution_info": null,
              "clips_karaoke_caption": null,
              "clips_captions": null,
              "clips_captions_translations_urls": null,
              "clips_tab_pinned_user_ids": [],
              "clips_text": null,
              "coauthor_producer_can_see_organic_insights": false,
              "coauthor_producers": [
                {
                  "__typename": "XDTUserDict",
                  "strong_id__": "10506924608",
                  "id": "10506924608",
                  "full_name": "James Cameron",
                  "is_private": false,
                  "is_verified": true,
                  "pk": "10506924608",
                  "profile_pic_id": "1964371814524155358_10506924608",
                  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                  "username": "jamescameronofficial"
                },
                {
                  "__typename": "XDTUserDict",
                  "strong_id__": "191074609",
                  "id": "191074609",
                  "full_name": "Hulu",
                  "is_private": false,
                  "is_verified": true,
                  "pk": "191074609",
                  "profile_pic_id": "3756416250542097738_191074609",
                  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                  "username": "hulu"
                },
                {
                  "__typename": "XDTUserDict",
                  "strong_id__": "1628164961",
                  "id": "1628164961",
                  "full_name": "Samuel Ramsey",
                  "is_private": false,
                  "is_verified": false,
                  "pk": "1628164961",
                  "profile_pic_id": "2453903210149049965_1628164961",
                  "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/...",
                  "username": "drsammygrams"
                }
              ],
              "code": "DWzTt7WE9uY",
              "comment_count": 170,
              "comment_inform_treatment": {
                "action_type": null,
                "should_have_inform_treatment": false,
                "text": "",
                "url": null
              },
              "comment_likes_enabled": true,
              "comment_threading_enabled": true,
              "comments_disabled": null,
              "community_notes_info": {
                "enable_submission_friction": false,
                "has_viewer_submitted_note": false,
                "note_submission_disabled": false
              },
              "creative_config": null,
              "creator_viewer_insights": null,
              "crosspost": null,
              "crosspost_metadata": {
                "fb_crosspost_deeplink_profile_id": null,
                "fb_crosspost_fbid": null,
                "fb_downstream_use_xpost_metadata": {
                  "downstream_use_xpost_deny_reason": "NONE"
                },
                "is_feedback_aggregated": null,
                "th_unified_feedback_row_tap_target_url": null,
                "unified_feedback_enabled": null
              },
              "deleted_reason": 0,
              "dominant_color": null,
              "fb_comment_count": null,
              "fb_like_count": null,
              "fb_play_count": null,
              "filter_type": 0,
              "fundraiser_tag": {
                "beneficiary_name": null,
                "beneficiary_username": null,
                "can_viewer_donate": null,
                "can_viewer_remove_fundraiser_tag": null,
                "contextual_title_str": null,
                "formatted_amount_raised": null,
                "formatted_fundraiser_progress_info_text": null,
                "formatted_goal_amount": null,
                "fundraiser_id": null,
                "fundraiser_owner_username": null,
                "fundraiser_title": null,
                "fundraiser_type": null,
                "has_standalone_fundraiser": false,
                "is_media_owner_fundraiser_owner": null,
                "progress_str": null,
                "show_fundraiser_owner_attribution": null,
                "thumbnail_display_url": null
              },
              "has_audio": true,
              "has_hidden_comments": null,
              "has_liked": false,
              "has_more_comments": true,
              "has_reshares": null,
              "has_shared_to_fb": 0,
              "has_tagged_users": true,
              "has_viewer_saved": null,
              "hide_view_all_comment_entrypoint": true,
              "ig_media_sharing_disabled": false,
              "ig_play_count": 420018,
              "igbio_product": null,
              "inline_composer_display_condition": null,
              "1finline_composer_imp_trigger_time": null,
              "invited_coauthor_producers": [],
              "is_artist_pick": false,
              "is_auto_created": null,
              "is_comments_gif_composer_enabled": false,
              "is_currently_promoting_by_sponsor": null,
              "is_cutout_sticker_allowed": false,
              "is_dash_eligible": 1,
              "is_eligible_for_media_note_recs_nux": null,
              "is_fb_only": null,
              "is_in_profile_grid": false,
              "is_organic_product_tagging_eligible": true,
              "is_paid_partnership": false,
              "is_post_live": null,
              "is_post_live_clips_media": false,
              "is_quiet_post": false,
              "is_reshare_of_text_post_app_media_in_ig": false,
              "is_reuse_allowed": false,
              "is_shared_from_basel": null,
              "is_third_party_downloads_eligible": false,
              "is_visual_reply_commenter_notice_enabled": true,
              "like_and_view_counts_disabled": false,
              "like_count": 5313,
              "media_attributions_data": [],
              "location": null,
              "mashup_info": null,
              "max_num_visible_preview_comments": 2,
              "media_notice": null,
              "media_overlay_info": null,
              "music_metadata": null,
              "mv_link": null,
              "number_of_qualities": 8,
              "original_media_has_visual_reply_media": false,
              "owner": {
                "__typename": "XDTUserDict",
                "strong_id__": "18091046",
                "id": "18091046",
                "can_see_quiet_post_attribution": true,
                "fbid_v2": "17841401291380282",
                "feed_post_reshare_disabled": false,
                "full_name": "National Geographic TV",
                "has_anonymous_profile_picture": false,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "pk": "18091046",
                "profile_pic_id": "3865691934048399589_18091046",
                "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
                "show_account_transparency_details": true,
                "transparency_product_enabled": false,
                "username": "natgeotv"
              },
              "photo_of_you": false,
              "play_count": 420018,
              "preview": null,
              "product_collection_tag": null,
              "product_suggestions": null,
              "product_tags": null,
              "profile_grid_control_enabled": false,
              "reshare_count": 387,
              "share_count_disabled": false,
              "shimmed_mv_link": null,
              "should_request_ads": false,
              "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
              "social_context": [],
              "sticker_translations_enabled": null,
              "subscribe_cta_visible": false,
              "threads_xpost_deny_reason": null,
              "top_likers": [],
              "translated_video_subtitles": null,
              "upcoming_event": null,
              "usertags": null,
              "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
              "1fvideo_duration": 76.28800201416016,
              "video_sticker_locales": [],
              "1fvideo_subtitles_confidence": null,
              "video_subtitles_enabled": null,
              "video_subtitles_locale": null,
              "video_subtitles_status": null,
              "video_subtitles_uri": null,
              "video_versions": [
                {
                  "height": 1280,
                  "id": "1317080756953513v",
                  "type": 101,
                  "url": "https://scontent-lax3-2.cdninstagram.com/...",
                  "width": 720
                }
              ],
              "view_count": null,
              "visibility": null,
              "visual_comment_reply_sticker_info": null,
              "visual_replies_info": null,
              "xpost_deny_reason": null,
              "xpost_deny_reason_enum": null,
              "floating_context_items": []
            }
          }
        ],
        "repost_next_max_id": "QVFCSG5IOHEtcG9fejFjTE14dEY0NXVlX1VoZWQ5b1ZCaDRkNHhpdDR1QXlodUNjcmZndkQtUFRpLWlWQ0Vta1pkc09ldlhMRGFvN0kxSDY3U1hKYmtGWA==",
        "repost_more_available": true
      }
    }
  },
  "extensions": {
    "is_final": true,
    "fulfilled_payloads": [
      {
        "label": "DeferrableSharedMedia",
        "path": [
          "1$fetch__XDTUserDict(id:$id)",
          "1$user_reposts_timeline(max_id:$max_id)",
          "repost_grid_items"
        ]
      },
      {
        "label": "DeferrableSharedMedia",
        "path": [
          "1$fetch__XDTUserDict(id:$id)",
          "1$user_reposts_timeline(max_id:$max_id)",
          "repost_grid_items"
        ]
      },
      {
        "label": "DeferrableSharedMedia",
        "path": [
          "1$fetch__XDTUserDict(id:$id)",
          "1$user_reposts_timeline(max_id:$max_id)",
          "repost_grid_items"
        ]
      }
    ],
    "server_metadata": {
      "request_start_time_ms": 1775669047333,
      "time_at_flush_ms": 1775669048592
    }
  },
  "status": "ok"
}
```

</details>

---

### GET /gql/user/web_profile_info

Get user profile info by user id (GraphQL web_profile_info)

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/web_profile_info?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_web_profile_info_gql(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/gql/user/web_profile_info",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/web_profile_info?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "gating": null,
  "fbid_v2": "17841400573960012",
  "is_memorialized": false,
  "is_private": false,
  "has_story_archive": null,
  "is_coppa_enforced": false,
  "supervision_info": null,
  "is_regulated_c18": false,
  "regulated_news_in_locations": null,
  "bio_links": [
    {
      "image_url": "",
      "is_pinned": false,
      "link_type": "external",
      "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPOTM2NjE5NzQzMzkyNDU5AAGn_v952RdNO6yMUCTFbgykw-5EG-3Au3ZiHUyUrer18pY5hJgZCZaldokedhM_aem_0m1d1pihdTPuz9GU7q0FNg&e=AT6yIGHJ_8Op_8vOKM_f6oJbouft3SY9QZyloeo7tPcqX4JSNuBOyDoTiDMRh5_sAj25ZyBd-Dnxe5EjKa5cWUEkPOCL6eYftFa_hZ9omt90Z20pVbfkUWQgWIJsS2W_o5qJYcjUNQWn",
      "media_accent_color_hex": "",
      "media_type": "none",
      "title": "",
      "url": "http://visitstore.bio/natgeo",
      "creation_source": "NONE"
    }
  ],
  "linked_fb_info": null,
  "text_post_app_badge_label": "natgeo",
  "show_text_post_app_badge": true,
  "username": "natgeo",
  "pk": "787132",
  "live_broadcast_visibility": null,
  "live_broadcast_id": null,
  "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/...",
  "hd_profile_pic_url_info": {
    "url": "https://scontent-lga3-3.cdninstagram.com/..."
  },
  "is_unpublished": false,
  "latest_reel_media": 1775659002,
  "has_profile_pic": null,
  "profile_pic_genai_tool_info": null,
  "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
  "full_name": "National Geographic",
  "is_verified": true,
  "show_account_transparency_details": true,
  "account_type": 2,
  "follower_count": 274988955,
  "mutual_followers_count": 0,
  "profile_context_links_with_user_ids": [],
  "profile_context_facepile_users": [],
  "address_street": "",
  "city_name": "",
  "is_business": true,
  "zip": "",
  "biography_with_entities": {
    "entities": []
  },
  "category": "",
  "should_show_category": false,
  "is_ring_creator": false,
  "show_ring_award": false,
  "ring_creator_metadata": {
    "profile_background_color": null
  },
  "account_badges": [],
  "ai_agent_type": null,
  "external_lynx_url": null,
  "external_url": null,
  "pronouns": [],
  "transparency_label": null,
  "transparency_product": null,
  "hide_creator_marketplace_badge": false,
  "id": "787132",
  "has_chaining": true,
  "remove_message_entrypoint": false,
  "is_embeds_disabled": false,
  "is_cannes": false,
  "is_professional_account": null,
  "following_count": 193,
  "media_count": 31529,
  "total_clips_count": 1,
  "latest_besties_reel_media": null,
  "reel_media_seen_timestamp": null
}
```

</details>

---

## Deprecated endpoints

These endpoints are deprecated — use the recommended alternatives. Retired ones respond with **410 Gone** and are never charged (see [Response Codes](../response-codes.md)); the rest still work but will be removed in a future version.

### ~~GET /gql/comment/likers~~

!!! warning
    WARNING: Preferable to use /gql/comment/likers/chunk

### ~~GET /gql/comments~~

!!! warning
    Use /v1/media/comments/chunk or /v2/media/comments instead

### ~~GET /gql/comments/chunk~~

!!! warning
    Use /v1/media/comments/chunk or /v2/media/comments instead

### ~~GET /gql/comments/threaded~~

!!! warning
    Use /v2/media/comments/replies instead

### ~~GET /gql/comments/threaded/chunk~~

!!! warning
    Use /v2/media/comments/replies instead

### ~~GET /gql/user/by/id~~

!!! warning
    User By Id

### ~~GET /gql/user/by/username~~

!!! warning
    Get user object by username (one request required)

### ~~GET /gql/user/followers~~

!!! warning
    WARNING: Use /v2/user/followers. Get a user followers (one request is required for every 46 followers)

### ~~GET /gql/user/following~~

!!! warning
    WARNING: Use /v2/user/following. Get a user following (one request is required for every 46 following)

### ~~GET /gql/user/related/profiles~~

!!! warning
    Prefer using v2/user/suggested/profiles as this endpoint will be completely deprecated soon

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-gql){ target=_blank }
