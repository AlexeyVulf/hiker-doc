# Media Endpoints

Get posts, comments, and media details.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v2/media/comment/offensive`](#get-v2mediacommentoffensive) | [`/v2/media/comments`](#get-v2mediacomments) | [`/v2/media/comments/replies`](#get-v2mediacommentsreplies) | [`/v2/media/info/by/code`](#get-v2mediainfobycode) | [`/v2/media/info/by/id`](#get-v2mediainfobyid) | [`/v2/media/info/by/url`](#get-v2mediainfobyurl) | [`/v2/media/likers`](#get-v2medialikers) | [`/v2/media/template`](#get-v2mediatemplate)

---

### GET /v2/media/comment/offensive

Whether to receive an offensive comment

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_id` | string | Yes | Media Id |
| `comment` | string | Yes | Comment |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/comment/offensive?media_id=3776832898280228145&comment=test comment"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_comment_offensive_v2(media_id="3776832898280228145", comment="test comment")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/media/comment/offensive",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"media_id": "3776832898280228145", "comment": "test comment"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/comment/offensive?media_id=3776832898280228145&comment=test comment",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "is_offensive": false,
    "text_language": "unknown",
    "status": "ok"
  },
  "next_page_id": null
}
```

</details>

---

### GET /v2/media/comments

Get comments on a media. Returns a list of Comment objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |
| `can_support_threading` | boolean | No | Can Support Threading |
| `safe_int` | boolean | No | Convert all big integers to strings |
| `page_id` | string | No | Page Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/comments?id=3691011991037807194"
    # Next page: add &page_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_comments_v2(id="3691011991037807194")
    # Next page: cl.media_comments_v2(id="3691011991037807194", page_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/media/comments",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "3691011991037807194"},
    )
    # Next page: add "page_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/comments?id=3691011991037807194",
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
    "can_view_more_preview_comments": false,
    "caption": {
      "bit_flags": 0,
      "content_type": "comment",
      "created_at": 1754223046,
      "created_at_for_fb_app": 1754223046,
      "created_at_utc": 1754223046,
      "did_report_as_spam": false,
      "is_covered": false,
      "is_created_by_media_owner": true,
      "is_ranked_comment": true,
      "media_id": 3691011991037807194,
      "pk": "17850017691525490",
      "private_reply_status": 0,
      "share_enabled": true,
      "status": "Active",
      "strong_id__": "17850017691525490",
      "text": "the way we still did a second round of picks after all the happy screaming…. 🫩🫩🫩",
      "type": 1,
      "user": {
        "fbid_v2": 17841401653390175,
        "full_name": "Adeline Tan ᐧ༚̮ᐧ",
        "id": "11255113",
        "is_private": false,
        "is_unpublished": false,
        "is_verified": false,
        "pk": 11255113,
        "pk_id": "11255113",
        "profile_pic_id": "1992089677481616027_11255113",
        "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/...",
        "strong_id__": "11255113",
        "username": "addie_ble"
      },
      "user_id": 11255113
    },
    "caption_is_edited": false,
    "comment_count": 551,
    "comment_cover_pos": "bottom",
    "comment_filter_param": "no_filter",
    "comment_likes_enabled": true,
    "comments": [
      {
        "bit_flags": 0,
        "comment_has_a_visual_reply_media": true,
        "comment_like_count": 13,
        "content_type": "comment",
        "created_at": 1754749758,
        "created_at_for_fb_app": 1754749758,
        "created_at_utc": 1754749758,
        "did_report_as_spam": false,
        "has_liked_comment": false,
        "has_disliked_comment": false,
        "inline_composer_display_condition": "never",
        "is_covered": false,
        "is_liked_by_media_owner": true,
        "is_pinned": true,
        "is_photo_comments_enabled_for_comment_author": false,
        "is_text_editable": false,
        "is_edited": false,
        "meta_ai_comment_type": "NONE",
        "is_ranked_comment": true,
        "keywords_data": [],
        "liked_by_media_coauthors": [],
        "other_preview_users": [],
        "media_id": 3691011991037807194,
        "pk": "18065401537979604",
        "preview_child_comments": [
          {
            "bit_flags": 0,
            "comment_like_count": 0,
            "content_type": "comment",
            "created_at": 1767006338,
            "created_at_utc": 1767006338,
            "created_at_for_fb_app": 1767006338,
            "did_report_as_spam": false,
            "has_liked_comment": false,
            "has_disliked_comment": false,
            "is_covered": false,
            "is_created_by_media_owner": true,
            "is_photo_comments_enabled_for_comment_author": false,
            "is_text_editable": false,
            "is_edited": false,
            "meta_ai_comment_type": "NONE",
            "is_ranked_comment": false,
            "liked_by_media_coauthors": [],
            "media_id": 3691011991037807194,
            "media_info": {
              "media": {
                "can_see_insights_as_brand": false,
                "caption": {
                  "__typename": "XDTCommentDict",
                  "strong_id__": "17905309164311566",
                  "pk": "17905309164311566",
                  "bit_flags": 0,
                  "content_type": "comment",
                  "created_at": 1767008635,
                  "created_at_utc": 1767008635,
                  "did_report_as_spam": false,
                  "is_covered": false,
                  "is_ranked_comment": false,
                  "media_id": 3798240616569105105,
                  "private_reply_status": 0,
                  "share_enabled": false,
                  "status": "Active",
                  "text": "RIP brackenfern I’ll always love you 🥀 \n\n#korea #family #vlog #jeju #travel",
                  "type": 1,
                  "user": {
                    "__typename": "XDTUserDict",
                    "strong_id__": "11255113",
                    "id": "11255113",
                    "fbid_v2": 17841401653390175,
                    "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                    "is_private": false,
                    "is_verified": false,
                    "pk": 11255113,
                    "profile_pic_id": "1992089677481616027_11255113",
                    "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/...",
                    "username": "addie_ble"
                  },
                  "user_id": 11255113
                },
                "clips_demotion_control": {
                  "confirmation_body": "We'll suggest fewer posts like this.",
                  "confirmation_icon": "none",
                  "confirmation_style": "bottomsheet",
                  "confirmation_title": "Post hidden",
                  "confirmation_title_style": "large_left",
                  "enable_word_wrapping": true,
                  "followup_options": [
                    {
                      "data": "author_id:11255113",
                      "demotion_control": {
                        "confirmation_body": "We won't suggest posts from addie_ble.",
                        "confirmation_icon": "eye-off-pano",
                        "confirmation_style": "bottomsheet",
                        "undo_style": "inline"
                      },
                      "id": "dislike_author",
                      "show_icon": true,
                      "text": "Don't suggest posts from addie_ble"
                    },
                    {
                      "id": "hide_all_specific_words",
                      "show_icon": true,
                      "text": "Don't suggest posts with certain words"
                    },
                    {
                      "id": "control_center",
                      "show_icon": true,
                      "text": "Manage content preferences"
                    }
                  ],
                  "title": "Not interested",
                  "title_style": "normal",
                  "undo_style": "top_right"
                },
                "coauthor_producer_can_see_organic_insights": false,
                "coauthor_producers": [],
                "comment_inform_treatment": {
                  "should_have_inform_treatment": false,
                  "text": ""
                },
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "deleted_reason": 0,
                "enable_media_notes_production": true,
                "enable_waist": true,
                "ig_play_count": 4128,
                "reshare_count": 3,
                "fundraiser_tag": {},
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "has_delayed_metadata": false,
                "has_more_comments": false,
                "hide_view_all_comment_entrypoint": true,
                "invited_coauthor_producers": [],
                "is_artist_pick": false,
                "is_cutout_sticker_allowed": true,
                "is_in_profile_grid": false,
                "is_organic_product_tagging_eligible": true,
                "is_paid_partnership": false,
                "is_reshare_of_text_post_app_media_in_ig": false,
                "is_reuse_allowed": true,
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "is_unified_video": false,
                "is_visual_reply_commenter_notice_enabled": true,
                "media_notes": {
                  "items": []
                },
                "mezql_token": "",
                "owner": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "11255113",
                  "id": "11255113",
                  "account_badges": [],
                  "biography": "⁽̨̡ ¨̮ ⁾̧̢ \n@dee_bakes 🍰\ntiktok: addieblesausage 🌭\nwork with me: adelinetan1996@gmail.com 🧚🏼‍♀️",
                  "can_see_quiet_post_attribution": true,
                  "fan_club_info": {},
                  "fbid_v2": 17841401653390175,
                  "feed_post_reshare_disabled": false,
                  "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                  "has_anonymous_profile_picture": false,
                  "interop_messaging_user_fbid": "113099470085044",
                  "is_favorite": false,
                  "is_private": false,
                  "is_unpublished": false,
                  "is_verified": false,
                  "pk": "11255113",
                  "profile_pic_id": "1992089677481616027_11255113",
                  "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/...",
                  "show_account_transparency_details": true,
                  "third_party_downloads_enabled": 2,
                  "transparency_product_enabled": false,
                  "username": "addie_ble",
                  "views_on_grid_status": "SHOW_VIEWS_ON_GRID"
                },
                "photo_of_you": false,
                "play_count": 4128,
                "profile_grid_control_enabled": false,
                "senders": [],
                "share_count_disabled": false,
                "is_social_ufi_disabled": false,
                "sharing_friction_info": {
                  "should_have_sharing_friction": false
                },
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "floating_context_items": [],
                "subscribe_cta_visible": false,
                "timeline_pinned_user_ids": [],
                "video_codec": "avc1.64001f",
                "video_sticker_locales": [],
                "video_subtitles_uri": "https://scontent-iad6-1.cdninstagram.com/...",
                "view_state_item_type": 128,
                "visual_comment_reply_sticker_info": [
                  {
                    "end_time_ms": 7200.9833333333,
                    "height": 0.14124688575434,
                    "is_fb_sticker": 0,
                    "is_hidden": 0,
                    "is_pinned": 0,
                    "is_sticker": 1,
                    "rotation": 0,
                    "start_time_ms": 0,
                    "vcr_sticker": {
                      "can_viewer_link_back_to_original_media_from_vcr": true,
                      "end_background_color": "#FFFFFF",
                      "end_time_ms": 7200.9833333333,
                      "original_comment_author": {
                        "__typename": "XDTUserDict",
                        "strong_id__": "4955997576",
                        "id": "4955997576",
                        "full_name": "Roselie Dumlao",
                        "is_private": true,
                        "is_verified": false,
                        "pk": "4955997576",
                        "profile_pic_id": "3832079386024340448_4955997576",
                        "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/...",
                        "username": "jangdan_ja_ju_ru"
                      },
                      "original_comment_id": "18065401537979604",
                      "original_comment_text": "Why did I scream as well ? Haha, as if I'm going with you guys 😂😂😂",
                      "original_media_id": "3691011991037807194",
                      "start_background_color": "#FFFFFF",
                      "start_time_ms": 0,
                      "text_color": ""
                    },
                    "width": 0.5873316831367,
                    "x": 0.5,
                    "y": 0.18525527831541,
                    "z": 0
                  }
                ],
                "visual_replies_info": {
                  "can_viewer_link_back_to_original_media_from_vcr": true,
                  "comment_info": {
                    "comment_id": "18065401537979604",
                    "commenter_username": "jangdan_ja_ju_ru"
                  },
                  "original_media": {
                    "pk": "3691011991037807194"
                  }
                },
                "top_likers": [],
                "__typename": "XDTMediaDict",
                "strong_id__": "3798240616569105105_11255113",
                "id": "3798240616569105105_11255113",
                "are_remixes_crosspostable": true,
                "can_viewer_reshare": true,
                "can_viewer_save": true,
                "caption_is_edited": true,
                "code": "DS2D7eCD-rR",
                "device_timestamp": 1767005556399135,
                "like_count": 57,
                "comment_count": 0,
                "filter_type": 0,
                "has_audio": true,
                "has_high_risk_gen_ai_inform_treatment": false,
                "has_liked": false,
                "has_shared_to_fb": 0,
                "has_views_fetching": true,
                "ig_media_sharing_disabled": false,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-iad3-1.cdninstagram.com/...",
                      "width": 640
                    },
                    "igtv_first_frame": {
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-iad3-1.cdninstagram.com/...",
                      "width": 640
                    }
                  },
                  "candidates": [
                    {
                      "height": 1280,
                      "scans_profile": "e15",
                      "url": "https://scontent-iad6-1.cdninstagram.com/...",
                      "width": 720
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 812,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_width": 1500,
                      "thumbnail_duration": 1.486980952381,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 156.133
                    }
                  }
                },
                "is_comments_gif_composer_enabled": true,
                "is_dash_eligible": 1,
                "is_post_live_clips_media": false,
                "is_quiet_post": false,
                "is_third_party_downloads_eligible": false,
                "like_and_view_counts_disabled": false,
                "media_type": 2,
                "number_of_qualities": 2,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo2LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiQVl4Vy1QS3VIV0tmb3NIRUFWczlsWDMzNzk4MjQwNjE2NTY5MTA1MTA1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTA3MjYwM3wzNzk4MjQwNjE2NTY5MTA1MTA1fDExMjU1MTEzfDgyMzU0ZWI0MGQwYmNjZDBmMTkyNWZhZGUwYWU1OTE1NDUyNDA0NTY1NmU4MjIxZDQ3NDNjYjRmMTMxZDViOTUifSwic2lnbmF0dXJlIjoiIn0=",
                "original_height": 1280,
                "original_media_has_visual_reply_media": false,
                "original_width": 720,
                "product_type": "clips",
                "taken_at": 1767006336,
                "user": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "11255113",
                  "id": "11255113",
                  "account_badges": [],
                  "fan_club_info": {},
                  "fbid_v2": 17841401653390175,
                  "feed_post_reshare_disabled": false,
                  "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                  "has_anonymous_profile_picture": false,
                  "interop_messaging_user_fbid": "113099470085044",
                  "is_facebook_onboarded_charity": false,
                  "is_favorite": false,
                  "is_private": false,
                  "is_unpublished": false,
                  "is_verified": false,
                  "merchant_checkout_style": "none",
                  "pk": 11255113,
                  "profile_pic_id": "1992089677481616027_11255113",
                  "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/...",
                  "seller_shoppable_feed_type": "none",
                  "show_account_transparency_details": true,
                  "show_shoppable_feed": false,
                  "third_party_downloads_enabled": 2,
                  "transparency_product_enabled": false,
                  "username": "addie_ble"
                },
                "video_subtitles_locale": "en_US",
                "__is_XDTMediaDict": true
              }
            },
            "parent_comment_id": "18065401537979604",
            "pk": "18389134726196231",
            "private_reply_status": 0,
            "replied_to_comment_id": "18065401537979604",
            "share_enabled": true,
            "status": "Active",
            "strong_id__": "18389134726196231",
            "text": "RIP brackenfern I’ll always love you 🥀 \n\n#korea #family #vlog #jeju #travel",
            "type": 2,
            "user": {
              "fbid_v2": 17841401653390175,
              "full_name": "Adeline Tan ᐧ༚̮ᐧ",
              "id": "11255113",
              "is_mentionable": true,
              "is_private": false,
              "is_verified": false,
              "pk": 11255113,
              "pk_id": "11255113",
              "profile_pic_id": "1992089677481616027_11255113",
              "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/...",
              "strong_id__": "11255113",
              "username": "addie_ble"
            },
            "user_id": 11255113
          }
        ],
        "private_reply_status": 0,
        "share_enabled": true,
        "status": "Active",
        "strong_id__": "18065401537979604",
        "text": "Why did I scream as well ? Haha, as if I'm going with you guys 😂😂😂",
        "type": 0,
        "user": {
          "fbid_v2": 17841404967299499,
          "full_name": "Roselie Dumlao",
          "id": "4955997576",
          "is_mentionable": false,
          "is_private": true,
          "is_verified": false,
          "pk": "4955997576",
          "pk_id": "4955997576",
          "profile_pic_id": "3832079386024340448_4955997576",
          "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/...",
          "strong_id__": "4955997576",
          "username": "jangdan_ja_ju_ru"
        },
        "user_id": 4955997576,
        "has_liked": false,
        "like_count": 13
      },
      {
        "bit_flags": 0,
        "comment_has_a_visual_reply_media": true,
        "comment_like_count": 2155,
        "content_type": "comment",
        "created_at": 1754310648,
        "created_at_for_fb_app": 1754310648,
        "created_at_utc": 1754310648,
        "did_report_as_spam": false,
        "has_liked_comment": false,
        "has_disliked_comment": false,
        "inline_composer_display_condition": "never",
        "is_covered": false,
        "is_pinned": true,
        "is_photo_comments_enabled_for_comment_author": false,
        "is_text_editable": false,
        "is_edited": false,
        "meta_ai_comment_type": "NONE",
        "is_ranked_comment": true,
        "keywords_data": [],
        "liked_by_media_coauthors": [],
        "other_preview_users": [],
        "media_id": 3691011991037807194,
        "pk": "18090010117735782",
        "preview_child_comments": [],
        "private_reply_status": 0,
        "share_enabled": true,
        "status": "Active",
        "strong_id__": "18090010117735782",
        "text": "Wait so none of y'all's parents stole the land of their siblings, thereby causing a forever-rift in the family?",
        "type": 0,
        "user": {
          "fbid_v2": 17841400810365572,
          "full_name": "Meenah Tariq",
          "id": "356635012",
          "is_mentionable": true,
          "is_private": false,
          "is_verified": false,
          "pk": "356635012",
          "pk_id": "356635012",
          "profile_pic_id": "3495891588465608853_356635012",
          "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/...",
          "strong_id__": "356635012",
          "username": "meenahtariq"
        },
        "user_id": 356635012,
        "has_liked": false,
        "like_count": 2155
      },
      {
        "bit_flags": 0,
        "comment_has_a_visual_reply_media": true,
        "comment_like_count": 340,
        "content_type": "comment",
        "created_at": 1757693209,
        "created_at_for_fb_app": 1757693209,
        "created_at_utc": 1757693209,
        "did_report_as_spam": false,
        "has_liked_comment": false,
        "has_disliked_comment": false,
        "inline_composer_display_condition": "never",
        "is_covered": false,
        "is_liked_by_media_owner": true,
        "is_pinned": true,
        "is_photo_comments_enabled_for_comment_author": false,
        "is_text_editable": false,
        "is_edited": false,
        "meta_ai_comment_type": "NONE",
        "is_ranked_comment": true,
        "keywords_data": [],
        "liked_by_media_coauthors": [],
        "other_preview_users": [],
        "media_id": 3691011991037807194,
        "pk": "17893429782322413",
        "preview_child_comments": [
          {
            "bit_flags": 0,
            "comment_like_count": 27,
            "content_type": "comment",
            "created_at": 1762860355,
            "created_at_utc": 1762860355,
            "created_at_for_fb_app": 1762860355,
            "did_report_as_spam": false,
            "has_liked_comment": false,
            "has_disliked_comment": false,
            "is_covered": false,
            "is_created_by_media_owner": true,
            "is_photo_comments_enabled_for_comment_author": false,
            "is_text_editable": false,
            "is_edited": false,
            "meta_ai_comment_type": "NONE",
            "is_ranked_comment": false,
            "liked_by_media_coauthors": [],
            "media_id": 3691011991037807194,
            "media_info": {
              "media": {
                "can_see_insights_as_brand": false,
                "caption": {
                  "__typename": "XDTCommentDict",
                  "strong_id__": "17920330227054327",
                  "pk": "17920330227054327",
                  "bit_flags": 0,
                  "content_type": "comment",
                  "created_at": 1762860353,
                  "created_at_utc": 1762860353,
                  "did_report_as_spam": false,
                  "is_covered": false,
                  "is_ranked_comment": false,
                  "media_id": 3763466966498528063,
                  "private_reply_status": 0,
                  "share_enabled": false,
                  "status": "Active",
                  "text": "I will always love u brackenfern…… 🥀❤️‍🩹\n\n#korea #travel #family #busan #jeju #holiday #vlog #cousins",
                  "type": 1,
                  "user": {
                    "__typename": "XDTUserDict",
                    "strong_id__": "11255113",
                    "id": "11255113",
                    "fbid_v2": 17841401653390175,
                    "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                    "is_private": false,
                    "is_verified": false,
                    "pk": 11255113,
                    "profile_pic_id": "1992089677481616027_11255113",
                    "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/...",
                    "username": "addie_ble"
                  },
                  "user_id": 11255113
                },
                "clips_demotion_control": {
                  "confirmation_body": "We'll suggest fewer posts like this.",
                  "confirmation_icon": "none",
                  "confirmation_style": "bottomsheet",
                  "confirmation_title": "Post hidden",
                  "confirmation_title_style": "large_left",
                  "enable_word_wrapping": true,
                  "followup_options": [
                    {
                      "data": "author_id:11255113",
                      "demotion_control": {
                        "confirmation_body": "We won't suggest posts from addie_ble.",
                        "confirmation_icon": "eye-off-pano",
                        "confirmation_style": "bottomsheet",
                        "undo_style": "inline"
                      },
                      "id": "dislike_author",
                      "show_icon": true,
                      "text": "Don't suggest posts from addie_ble"
                    },
                    {
                      "id": "hide_all_specific_words",
                      "show_icon": true,
                      "text": "Don't suggest posts with certain words"
                    },
                    {
                      "id": "control_center",
                      "show_icon": true,
                      "text": "Manage content preferences"
                    }
                  ],
                  "title": "Not interested",
                  "title_style": "normal",
                  "undo_style": "top_right"
                },
                "coauthor_producer_can_see_organic_insights": false,
                "coauthor_producers": [],
                "comment_inform_treatment": {
                  "should_have_inform_treatment": false,
                  "text": ""
                },
                "crosspost_metadata": {
                  "unified_feedback_enabled": true,
                  "is_feedback_aggregated": true,
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "deleted_reason": 0,
                "enable_media_notes_production": true,
                "enable_waist": true,
                "fb_comment_count": 0,
                "fb_like_count": 0,
                "fb_play_count": 3,
                "ig_play_count": 5380,
                "reshare_count": 9,
                "fundraiser_tag": {},
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "has_delayed_metadata": false,
                "has_more_comments": false,
                "hide_view_all_comment_entrypoint": true,
                "invited_coauthor_producers": [],
                "is_artist_pick": false,
                "is_cutout_sticker_allowed": true,
                "is_in_profile_grid": false,
                "is_organic_product_tagging_eligible": true,
                "is_paid_partnership": false,
                "is_reshare_of_text_post_app_media_in_ig": false,
                "is_reuse_allowed": true,
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "is_unified_video": false,
                "is_visual_reply_commenter_notice_enabled": true,
                "media_notes": {
                  "items": []
                },
                "mezql_token": "",
                "owner": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "11255113",
                  "id": "11255113",
                  "account_badges": [],
                  "biography": "⁽̨̡ ¨̮ ⁾̧̢ \n@dee_bakes 🍰\ntiktok: addieblesausage 🌭\nwork with me: adelinetan1996@gmail.com 🧚🏼‍♀️",
                  "can_see_quiet_post_attribution": true,
                  "fan_club_info": {},
                  "fbid_v2": 17841401653390175,
                  "feed_post_reshare_disabled": false,
                  "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                  "has_anonymous_profile_picture": false,
                  "interop_messaging_user_fbid": "113099470085044",
                  "is_favorite": false,
                  "is_private": false,
                  "is_unpublished": false,
                  "is_verified": false,
                  "pk": "11255113",
                  "profile_pic_id": "1992089677481616027_11255113",
                  "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/...",
                  "show_account_transparency_details": true,
                  "third_party_downloads_enabled": 2,
                  "transparency_product_enabled": false,
                  "username": "addie_ble",
                  "views_on_grid_status": "SHOW_VIEWS_ON_GRID"
                },
                "photo_of_you": false,
                "play_count": 5383,
                "profile_grid_control_enabled": false,
                "senders": [],
                "share_count_disabled": false,
                "is_social_ufi_disabled": false,
                "sharing_friction_info": {
                  "should_have_sharing_friction": false
                },
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "floating_context_items": [],
                "subscribe_cta_visible": false,
                "timeline_pinned_user_ids": [],
                "video_codec": "av01.0.04M.08.0.111.01.01.01.0",
                "video_sticker_locales": [],
                "video_subtitles_uri": "https://scontent-iad3-1.cdninstagram.com/...",
                "view_state_item_type": 128,
                "visual_comment_reply_sticker_info": [
                  {
                    "end_time_ms": 5601.6,
                    "height": 0.18095930232558,
                    "is_fb_sticker": 0,
                    "is_hidden": 0,
                    "is_pinned": 0,
                    "is_sticker": 1,
                    "rotation": 0,
                    "start_time_ms": 0,
                    "vcr_sticker": {
                      "can_viewer_link_back_to_original_media_from_vcr": true,
                      "end_background_color": "#FF81B1",
                      "end_time_ms": 5601.6,
                      "original_comment_author": {
                        "__typename": "XDTUserDict",
                        "strong_id__": "259645306",
                        "id": "259645306",
                        "full_name": "에밀리 ✨",
                        "is_private": false,
                        "is_verified": false,
                        "pk": "259645306",
                        "profile_pic_id": "3855655870168638939_259645306",
                        "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/...",
                        "username": "emilyrcrespo"
                      },
                      "original_comment_id": "17893429782322413",
                      "original_comment_text": "LETS GOOOOOO!! I shouted through the screen as if I were apart of this",
                      "original_media_id": "3691011991037807194",
                      "start_background_color": "#9658FF",
                      "start_time_ms": 0,
                      "text_color": ""
                    },
                    "width": 0.6077519379845,
                    "x": 0.5,
                    "y": 0.19513081395349,
                    "z": 0
                  }
                ],
                "visual_replies_info": {
                  "can_viewer_link_back_to_original_media_from_vcr": true,
                  "comment_info": {
                    "comment_id": "17893429782322413",
                    "commenter_username": "emilyrcrespo"
                  },
                  "original_media": {
                    "pk": "3691011991037807194"
                  }
                },
                "top_likers": [],
                "__typename": "XDTMediaDict",
                "strong_id__": "3763466966498528063_11255113",
                "id": "3763466966498528063_11255113",
                "are_remixes_crosspostable": true,
                "can_viewer_reshare": true,
                "can_viewer_save": true,
                "caption_is_edited": false,
                "code": "DQ6hUQuD8s_",
                "device_timestamp": 1762860209982184,
                "like_count": 94,
                "comment_count": 0,
                "filter_type": 0,
                "has_audio": true,
                "has_high_risk_gen_ai_inform_treatment": false,
                "has_liked": false,
                "has_shared_to_fb": 0,
                "has_views_fetching": true,
                "ig_media_sharing_disabled": false,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-iad3-2.cdninstagram.com/...",
                      "width": 640
                    },
                    "igtv_first_frame": {
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-iad3-2.cdninstagram.com/...",
                      "width": 640
                    }
                  },
                  "candidates": [
                    {
                      "height": 1280,
                      "scans_profile": "e15",
                      "url": "https://scontent-iad6-1.cdninstagram.com/...",
                      "width": 720
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 472,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_width": 1500,
                      "thumbnail_duration": 1.486980952381,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 156.133
                    }
                  }
                },
                "is_comments_gif_composer_enabled": true,
                "is_dash_eligible": 1,
                "is_post_live_clips_media": false,
                "is_quiet_post": false,
                "is_third_party_downloads_eligible": false,
                "like_and_view_counts_disabled": false,
                "media_type": 2,
                "number_of_qualities": 8,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo2LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiQVl4Vy1QS3VIV0tmb3NIRUFWczlsWDMzNzYzNDY2OTY2NDk4NTI4MDYzIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTA3MjYyOXwzNzYzNDY2OTY2NDk4NTI4MDYzfDExMjU1MTEzfDkwNTVmYTY3NzQ1YmQyOWVkNDVmODBjZDJhZjI4MDIwNzk5ZjUyYWJiZWYxYjY2NzkyNWIwYzA2MWJhNDUzMTgifSwic2lnbmF0dXJlIjoiIn0=",
                "original_height": 1920,
                "original_media_has_visual_reply_media": false,
                "original_width": 1080,
                "product_type": "clips",
                "taken_at": 1763031207,
                "user": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "11255113",
                  "id": "11255113",
                  "account_badges": [],
                  "fan_club_info": {},
                  "fbid_v2": 17841401653390175,
                  "feed_post_reshare_disabled": false,
                  "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                  "has_anonymous_profile_picture": false,
                  "interop_messaging_user_fbid": "113099470085044",
                  "is_facebook_onboarded_charity": false,
                  "is_favorite": false,
                  "is_private": false,
                  "is_unpublished": false,
                  "is_verified": false,
                  "merchant_checkout_style": "none",
                  "pk": 11255113,
                  "profile_pic_id": "1992089677481616027_11255113",
                  "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/...",
                  "seller_shoppable_feed_type": "none",
                  "show_account_transparency_details": true,
                  "show_shoppable_feed": false,
                  "third_party_downloads_enabled": 2,
                  "transparency_product_enabled": false,
                  "username": "addie_ble"
                },
                "video_subtitles_locale": "en_US",
                "__is_XDTMediaDict": true
              }
            },
            "parent_comment_id": "17893429782322413",
            "pk": "18086930504508184",
            "private_reply_status": 0,
            "replied_to_comment_id": "17893429782322413",
            "share_enabled": true,
            "status": "Active",
            "strong_id__": "18086930504508184",
            "text": "I will always love u brackenfern…… 🥀❤️‍🩹\n\n#korea #travel #family #busan #jeju #holiday #vlog #cousins",
            "type": 2,
            "user": {
              "fbid_v2": 17841401653390175,
              "full_name": "Adeline Tan ᐧ༚̮ᐧ",
              "id": "11255113",
              "is_mentionable": true,
              "is_private": false,
              "is_verified": false,
              "pk": 11255113,
              "pk_id": "11255113",
              "profile_pic_id": "1992089677481616027_11255113",
              "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/...",
              "strong_id__": "11255113",
              "username": "addie_ble"
            },
            "user_id": 11255113
          }
        ],
        "private_reply_status": 0,
        "share_enabled": true,
        "status": "Active",
        "strong_id__": "17893429782322413",
        "text": "LETS GOOOOOO!! I shouted through the screen as if I were apart of this",
        "type": 0,
        "user": {
          "fbid_v2": 17841401839184056,
          "full_name": "에밀리 ✨",
          "id": "259645306",
          "is_mentionable": true,
          "is_private": false,
          "is_verified": false,
          "pk": "259645306",
          "pk_id": "259645306",
          "profile_pic_id": "3855655870168638939_259645306",
          "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/...",
          "strong_id__": "259645306",
          "username": "emilyrcrespo"
        },
        "user_id": 259645306,
        "has_liked": false,
        "like_count": 340
      }
    ],
    "has_more_comments": false,
    "has_more_headload_comments": true,
    "initiate_at_top": true,
    "insert_new_comment_to_top": true,
    "is_ranked": true,
    "liked_by_media_owner_badge_enabled": true,
    "media_header_display": "none",
    "next_min_id": "{\"cached_comments_cursor\":\"17906257188216085\",\"bifilter_token\":\"GgYYeQBX4v_Bmcs_AGfi-oQPjD8AO8BGHgeOQAARdR_H-Ns_ABn8S53Bwz8A63vNEIdiQABJ35388jdAAO0c_cX6kT8A1GRlEWMuQAAEdH7y6Jo_AGhvUQdiiT8ASOG7jtqRPwAanwhxh_c_ALOy8XBNX0AAheNEpCSaPwAA\"}",
    "pinned_comment_count": 3,
    "quick_response_emojis": [
      {
        "unicode": "❤️"
      },
      {
        "unicode": "🙌"
      },
      {
        "unicode": "🔥"
      }
    ],
    "scroll_behavior": 1,
    "disclaimer_text": "addie_ble initially shared this reel to non-followers first on Aug 4, so some comments may be older than the reel's post date.",
    "filter_options": [],
    "sort_options": [],
    "preview_comments": [],
    "should_render_upsell": false,
    "foundation_improvements_enabled": true,
    "has_more_headload_fb_comments": false,
    "fb_comments": [],
    "ai_topic_filters": [],
    "status": "ok"
  },
  "next_page_id": "IntcImNhY2hlZF9jb21tZW50c19jdXJzb3JcIjpcIjE3OTA2MjU3MTg4MjE2MDg1XCIsXCJiaWZpbHRlcl90b2tlblwiOlwiR2dZWWVRQlg0dl9CbWNzX0FHZmktb1FQakQ4QU84QkdIZ2VPUUFBUmRSX0gtTnNfQUJuOFM1M0J3ejhBNjN2TkVJZGlRQUJKMzUzODhqZEFBTzBjX2NYNmtUOEExR1JsRVdNdVFBQUVkSDd5NkpvX0FHaHZVUWRpaVQ4QVNPRzdqdHFSUHdBYW53aHhoX2NfQUxPeThYQk5YMEFBaGVORXBDU2FQd0FBXCJ9Ig=="
}
```

</details>

---

### GET /v2/media/comments/replies

Get media comment replies with pagination by min_id. Returns a list of Comment objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_id` | string | Yes | Media Id |
| `comment_id` | string | Yes | Comment Id |
| `min_id` | string | No | Min Id |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/comments/replies?media_id=3864286541032633353&comment_id=18142813870496178"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_comments_replies_v2(media_id="3864286541032633353", comment_id="18142813870496178")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/media/comments/replies",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"media_id": "3864286541032633353", "comment_id": "18142813870496178"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/comments/replies?media_id=3864286541032633353&comment_id=18142813870496178",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "child_comment_count": 6,
  "child_comments": [
    {
      "bit_flags": 0,
      "child_comment_index": 0,
      "comment_like_count": 0,
      "content_type": "comment",
      "created_at": 1775154407,
      "created_at_for_fb_app": 1775154407,
      "created_at_utc": 1775154407,
      "did_report_as_spam": false,
      "has_disliked_comment": false,
      "has_liked_comment": false,
      "is_covered": false,
      "is_photo_comments_enabled_for_comment_author": false,
      "is_text_editable": false,
      "is_edited": false,
      "meta_ai_comment_type": "NONE",
      "is_ranked_comment": false,
      "liked_by_media_coauthors": [],
      "media_id": 3864286541032633353,
      "media_info": {
        "media": {
          "can_see_insights_as_brand": false,
          "clips_demotion_control": {
            "confirmation_body": "We'll suggest fewer posts like this.",
            "confirmation_icon": "none",
            "confirmation_style": "bottomsheet",
            "confirmation_title": "Post hidden",
            "confirmation_title_style": "large_left",
            "enable_word_wrapping": true,
            "followup_options": [
              {
                "data": "author_id:6752523055",
                "demotion_control": {
                  "confirmation_body": "We won't suggest posts from caldeironuria70.",
                  "confirmation_icon": "eye-off-pano",
                  "confirmation_style": "bottomsheet",
                  "undo_style": "inline"
                },
                "id": "dislike_author",
                "show_icon": true,
                "text": "Don't suggest posts from caldeironuria70"
              },
              {
                "id": "hide_all_specific_words",
                "show_icon": true,
                "text": "Don't suggest posts with certain words"
              },
              {
                "id": "control_center",
                "show_icon": true,
                "text": "Manage content preferences"
              }
            ],
            "title": "Not interested",
            "title_style": "normal",
            "undo_style": "top_right"
          },
          "coauthor_producer_can_see_organic_insights": false,
          "coauthor_producers": [],
          "comment_inform_treatment": {
            "should_have_inform_treatment": false,
            "text": ""
          },
          "crosspost_metadata": {
            "fb_downstream_use_xpost_metadata": {
              "downstream_use_xpost_deny_reason": "NONE"
            }
          },
          "deleted_reason": 0,
          "enable_media_notes_production": true,
          "enable_waist": true,
          "ig_play_count": 83,
          "fundraiser_tag": {},
          "gen_ai_detection_method": {
            "detection_method": "NONE"
          },
          "has_delayed_metadata": false,
          "has_more_comments": false,
          "hide_view_all_comment_entrypoint": true,
          "invited_coauthor_producers": [],
          "is_artist_pick": false,
          "is_cutout_sticker_allowed": true,
          "is_in_profile_grid": false,
          "is_organic_product_tagging_eligible": true,
          "is_paid_partnership": false,
          "is_reshare_of_text_post_app_media_in_ig": false,
          "is_reuse_allowed": true,
          "is_tagged_media_shared_to_viewer_profile_grid": false,
          "is_unified_video": false,
          "is_visual_reply_commenter_notice_enabled": true,
          "media_notes": {
            "items": []
          },
          "mezql_token": "",
          "owner": {
            "__typename": "XDTUserDict",
            "strong_id__": "6752523055",
            "id": "6752523055",
            "account_badges": [],
            "biography": "Galega de  pura cepa",
            "can_see_quiet_post_attribution": true,
            "fan_club_info": {},
            "fbid_v2": 17841406811654065,
            "feed_post_reshare_disabled": false,
            "full_name": "Nuria Taboada",
            "has_anonymous_profile_picture": false,
            "interop_messaging_user_fbid": "110265577029021",
            "is_favorite": false,
            "is_private": false,
            "is_unpublished": false,
            "is_verified": false,
            "pk": "6752523055",
            "profile_pic_id": "3869835622605851526_6752523055",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
            "show_account_transparency_details": true,
            "third_party_downloads_enabled": 1,
            "transparency_product_enabled": false,
            "username": "caldeironuria70",
            "views_on_grid_status": "SHOW_VIEWS_ON_GRID"
          },
          "play_count": 83,
          "profile_grid_control_enabled": false,
          "senders": [],
          "share_count_disabled": false,
          "is_social_ufi_disabled": false,
          "sharing_friction_info": {
            "should_have_sharing_friction": false
          },
          "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
          "floating_context_items": [],
          "subscribe_cta_visible": false,
          "timeline_pinned_user_ids": [],
          "video_codec": "avc1.64001f",
          "video_sticker_locales": [],
          "view_state_item_type": 128,
          "visual_comment_reply_sticker_info": [
            {
              "end_time_ms": 38677,
              "height": 0.178125,
              "is_fb_sticker": 0,
              "is_hidden": 0,
              "is_pinned": 0,
              "is_sticker": 1,
              "rotation": 0,
              "start_time_ms": 0,
              "vcr_sticker": {
                "can_viewer_link_back_to_original_media_from_vcr": true,
                "end_background_color": "#ffffff",
                "end_time_ms": 38677,
                "original_comment_author": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "46193898922",
                  "id": "46193898922",
                  "full_name": "Natalia Vega Garcia",
                  "is_private": false,
                  "is_verified": false,
                  "pk": "46193898922",
                  "profile_pic_id": "2518281128395959898_46193898922",
                  "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
                  "username": "vegagarcianatalia"
                },
                "original_comment_id": "18142813870496178",
                "original_comment_text": "Ya está bien tapar estás palabras: violación y violencia etc",
                "original_media_id": "3864286541032633353",
                "start_background_color": "#ffffff",
                "start_time_ms": 0,
                "text_color": ""
              },
              "width": 0.7222222,
              "x": 0.5,
              "y": 0.29453126,
              "z": 0
            }
          ],
          "visual_replies_info": {
            "can_viewer_link_back_to_original_media_from_vcr": true,
            "comment_info": {
              "comment_id": "18142813870496178",
              "commenter_username": "vegagarcianatalia"
            },
            "original_media": {
              "pk": "3864286541032633353"
            }
          },
          "top_likers": [],
          "__typename": "XDTMediaDict",
          "strong_id__": "3866597721931422240_6752523055",
          "id": "3866597721931422240_6752523055",
          "are_remixes_crosspostable": true,
          "can_viewer_reshare": true,
          "can_viewer_save": true,
          "caption_is_edited": false,
          "code": "DWo6iRZDpog",
          "device_timestamp": 11031814077916,
          "like_count": 0,
          "comment_count": 0,
          "filter_type": 0,
          "has_audio": true,
          "has_high_risk_gen_ai_inform_treatment": false,
          "has_liked": false,
          "has_shared_to_fb": 0,
          "has_views_fetching": true,
          "ig_media_sharing_disabled": false,
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
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw6-1.cdninstagram.com/...",
                "width": 640
              }
            ],
            "scrubber_spritesheet_info_candidates": {
              "default": {
                "file_size_kb": 598,
                "max_thumbnails_per_sprite": 105,
                "rendered_width": 96,
                "sprite_height": 1232,
                "sprite_width": 1500,
                "thumbnail_duration": 0.5044,
                "thumbnail_height": 176,
                "thumbnail_width": 100,
                "thumbnails_per_row": 15,
                "total_thumbnail_num_per_sprite": 105,
                "video_length": 52.962
              }
            }
          },
          "is_comments_gif_composer_enabled": true,
          "is_dash_eligible": 1,
          "is_post_live_clips_media": false,
          "is_quiet_post": false,
          "is_third_party_downloads_eligible": true,
          "like_and_view_counts_disabled": false,
          "media_type": 2,
          "number_of_qualities": 2,
          "organic_tracking_token": "eyJ2ZXJzaW9uIjo2LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiQVVlcHZtRlZaRmJkTDlJaTRITU5mYzgzODY2NTk3NzIxOTMxNDIyMjQwIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTA3NTI0M3wzODY2NTk3NzIxOTMxNDIyMjQwfDY3NTI1MjMwNTV8ZTg3MTg3MWY0Yjk2ZjNiYTc1ZjI1N2VkMjBmM2ZmNjFlM2UwMTA5YjA0MjAwZmFhN2VhYTBkN2Q2ZmI1ZGVjNCJ9LCJzaWduYXR1cmUiOiIifQ==",
          "original_height": 1280,
          "original_media_has_visual_reply_media": false,
          "original_width": 720,
          "product_type": "clips",
          "taken_at": 1775154422,
          "user": {
            "__typename": "XDTUserDict",
            "strong_id__": "6752523055",
            "id": "6752523055",
            "account_badges": [],
            "fan_club_info": {},
            "fbid_v2": 17841406811654065,
            "feed_post_reshare_disabled": false,
            "full_name": "Nuria Taboada",
            "has_anonymous_profile_picture": false,
            "interop_messaging_user_fbid": "110265577029021",
            "is_facebook_onboarded_charity": false,
            "is_favorite": false,
            "is_private": false,
            "is_unpublished": false,
            "is_verified": false,
            "merchant_checkout_style": "none",
            "pk": 6752523055,
            "profile_pic_id": "3869835622605851526_6752523055",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
            "seller_shoppable_feed_type": "none",
            "show_account_transparency_details": true,
            "show_shoppable_feed": false,
            "third_party_downloads_enabled": 1,
            "transparency_product_enabled": false,
            "username": "caldeironuria70"
          },
          "video_subtitles_locale": "es_CL",
          "__is_XDTMediaDict": true
        }
      },
      "parent_comment_id": "18142813870496178",
      "pk": "18061290119485558",
      "private_reply_status": 0,
      "replied_to_comment_id": "18142813870496178",
      "share_enabled": true,
      "status": "Active",
      "strong_id__": "18061290119485558",
      "text": "@vegagarcianatalia",
      "type": 2,
      "user": {
        "fbid_v2": 17841406811654065,
        "full_name": "Nuria Taboada",
        "id": "6752523055",
        "is_mentionable": true,
        "is_private": false,
        "is_verified": false,
        "pk": 6752523055,
        "pk_id": "6752523055",
        "profile_pic_id": "3869835622605851526_6752523055",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
        "strong_id__": "6752523055",
        "username": "caldeironuria70"
      },
      "user_id": 6752523055
    },
    {
      "bit_flags": 0,
      "child_comment_index": 1,
      "comment_like_count": 0,
      "content_type": "comment",
      "created_at": 1775154575,
      "created_at_for_fb_app": 1775154575,
      "created_at_utc": 1775154575,
      "did_report_as_spam": false,
      "has_disliked_comment": false,
      "has_liked_comment": false,
      "is_covered": false,
      "is_photo_comments_enabled_for_comment_author": false,
      "is_text_editable": false,
      "is_edited": false,
      "meta_ai_comment_type": "NONE",
      "is_ranked_comment": false,
      "liked_by_media_coauthors": [],
      "media_id": 3864286541032633353,
      "media_info": {
        "media": {
          "can_see_insights_as_brand": false,
          "clips_demotion_control": {
            "confirmation_body": "We'll suggest fewer posts like this.",
            "confirmation_icon": "none",
            "confirmation_style": "bottomsheet",
            "confirmation_title": "Post hidden",
            "confirmation_title_style": "large_left",
            "enable_word_wrapping": true,
            "followup_options": [
              {
                "data": "author_id:6752523055",
                "demotion_control": {
                  "confirmation_body": "We won't suggest posts from caldeironuria70.",
                  "confirmation_icon": "eye-off-pano",
                  "confirmation_style": "bottomsheet",
                  "undo_style": "inline"
                },
                "id": "dislike_author",
                "show_icon": true,
                "text": "Don't suggest posts from caldeironuria70"
              },
              {
                "id": "hide_all_specific_words",
                "show_icon": true,
                "text": "Don't suggest posts with certain words"
              },
              {
                "id": "control_center",
                "show_icon": true,
                "text": "Manage content preferences"
              }
            ],
            "title": "Not interested",
            "title_style": "normal",
            "undo_style": "top_right"
          },
          "coauthor_producer_can_see_organic_insights": false,
          "coauthor_producers": [],
          "comment_inform_treatment": {
            "should_have_inform_treatment": false,
            "text": ""
          },
          "crosspost_metadata": {
            "fb_downstream_use_xpost_metadata": {
              "downstream_use_xpost_deny_reason": "NONE"
            }
          },
          "deleted_reason": 0,
          "enable_media_notes_production": true,
          "enable_waist": true,
          "ig_play_count": 148,
          "fundraiser_tag": {},
          "gen_ai_detection_method": {
            "detection_method": "NONE"
          },
          "has_delayed_metadata": false,
          "has_more_comments": false,
          "hide_view_all_comment_entrypoint": true,
          "invited_coauthor_producers": [],
          "is_artist_pick": false,
          "is_cutout_sticker_allowed": true,
          "is_in_profile_grid": false,
          "is_organic_product_tagging_eligible": true,
          "is_paid_partnership": false,
          "is_reshare_of_text_post_app_media_in_ig": false,
          "is_reuse_allowed": true,
          "is_tagged_media_shared_to_viewer_profile_grid": false,
          "is_unified_video": false,
          "is_visual_reply_commenter_notice_enabled": true,
          "media_notes": {
            "items": []
          },
          "mezql_token": "",
          "owner": {
            "__typename": "XDTUserDict",
            "strong_id__": "6752523055",
            "id": "6752523055",
            "account_badges": [],
            "biography": "Galega de  pura cepa",
            "can_see_quiet_post_attribution": true,
            "fan_club_info": {},
            "fbid_v2": 17841406811654065,
            "feed_post_reshare_disabled": false,
            "full_name": "Nuria Taboada",
            "has_anonymous_profile_picture": false,
            "interop_messaging_user_fbid": "110265577029021",
            "is_favorite": false,
            "is_private": false,
            "is_unpublished": false,
            "is_verified": false,
            "pk": "6752523055",
            "profile_pic_id": "3869835622605851526_6752523055",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
            "show_account_transparency_details": true,
            "third_party_downloads_enabled": 1,
            "transparency_product_enabled": false,
            "username": "caldeironuria70",
            "views_on_grid_status": "SHOW_VIEWS_ON_GRID"
          },
          "play_count": 148,
          "profile_grid_control_enabled": false,
          "senders": [],
          "share_count_disabled": false,
          "is_social_ufi_disabled": false,
          "sharing_friction_info": {
            "should_have_sharing_friction": false
          },
          "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
          "floating_context_items": [],
          "subscribe_cta_visible": false,
          "timeline_pinned_user_ids": [],
          "video_codec": "avc1.64001f",
          "video_sticker_locales": [],
          "view_state_item_type": 128,
          "visual_comment_reply_sticker_info": [
            {
              "end_time_ms": 38886,
              "height": 0.178125,
              "is_fb_sticker": 0,
              "is_hidden": 0,
              "is_pinned": 0,
              "is_sticker": 1,
              "rotation": 0,
              "start_time_ms": 0,
              "vcr_sticker": {
                "can_viewer_link_back_to_original_media_from_vcr": true,
                "end_background_color": "#ffffff",
                "end_time_ms": 38886,
                "original_comment_author": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "46193898922",
                  "id": "46193898922",
                  "full_name": "Natalia Vega Garcia",
                  "is_private": false,
                  "is_verified": false,
                  "pk": "46193898922",
                  "profile_pic_id": "2518281128395959898_46193898922",
                  "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
                  "username": "vegagarcianatalia"
                },
                "original_comment_id": "18142813870496178",
                "original_comment_text": "Ya está bien tapar estás palabras: violación y violencia etc",
                "original_media_id": "3864286541032633353",
                "start_background_color": "#ffffff",
                "start_time_ms": 0,
                "text_color": ""
              },
              "width": 0.7222222,
              "x": 0.5,
              "y": 0.29453126,
              "z": 0
            }
          ],
          "visual_replies_info": {
            "can_viewer_link_back_to_original_media_from_vcr": true,
            "comment_info": {
              "comment_id": "18142813870496178",
              "commenter_username": "vegagarcianatalia"
            },
            "original_media": {
              "pk": "3864286541032633353"
            }
          },
          "top_likers": [],
          "__typename": "XDTMediaDict",
          "strong_id__": "3866599194518014185_6752523055",
          "id": "3866599194518014185_6752523055",
          "are_remixes_crosspostable": true,
          "can_viewer_reshare": true,
          "can_viewer_save": true,
          "caption_is_edited": false,
          "code": "DWo63s2Dsjp",
          "device_timestamp": 11217188893707,
          "like_count": 0,
          "comment_count": 0,
          "filter_type": 0,
          "has_audio": true,
          "has_high_risk_gen_ai_inform_treatment": false,
          "has_liked": false,
          "has_shared_to_fb": 0,
          "has_views_fetching": true,
          "ig_media_sharing_disabled": false,
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
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw5-2.cdninstagram.com/...",
                "width": 640
              }
            ],
            "scrubber_spritesheet_info_candidates": {
              "default": {
                "file_size_kb": 583,
                "max_thumbnails_per_sprite": 105,
                "rendered_width": 96,
                "sprite_height": 1232,
                "sprite_width": 1500,
                "thumbnail_duration": 0.37078095238095,
                "thumbnail_height": 176,
                "thumbnail_width": 100,
                "thumbnails_per_row": 15,
                "total_thumbnail_num_per_sprite": 105,
                "video_length": 38.932
              }
            }
          },
          "is_comments_gif_composer_enabled": true,
          "is_dash_eligible": 1,
          "is_post_live_clips_media": false,
          "is_quiet_post": false,
          "is_third_party_downloads_eligible": true,
          "like_and_view_counts_disabled": false,
          "media_type": 2,
          "number_of_qualities": 2,
          "organic_tracking_token": "eyJ2ZXJzaW9uIjo2LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiQVVlcHZtRlZaRmJkTDlJaTRITU5mYzgzODY2NTk5MTk0NTE4MDE0MTg1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTA3NTI0NXwzODY2NTk5MTk0NTE4MDE0MTg1fDY3NTI1MjMwNTV8MzhmYjk1NjQ5ZjAxZjNmYTMyNjliNGM5ZjlhMTM2MTcwYjJjNTQ0ZmIwOTNkMDBlZDAxMGQ4NTE0YmNjMjJmMiJ9LCJzaWduYXR1cmUiOiIifQ==",
          "original_height": 1280,
          "original_media_has_visual_reply_media": false,
          "original_width": 720,
          "product_type": "clips",
          "taken_at": 1775154589,
          "user": {
            "__typename": "XDTUserDict",
            "strong_id__": "6752523055",
            "id": "6752523055",
            "account_badges": [],
            "fan_club_info": {},
            "fbid_v2": 17841406811654065,
            "feed_post_reshare_disabled": false,
            "full_name": "Nuria Taboada",
            "has_anonymous_profile_picture": false,
            "interop_messaging_user_fbid": "110265577029021",
            "is_facebook_onboarded_charity": false,
            "is_favorite": false,
            "is_private": false,
            "is_unpublished": false,
            "is_verified": false,
            "merchant_checkout_style": "none",
            "pk": 6752523055,
            "profile_pic_id": "3869835622605851526_6752523055",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
            "seller_shoppable_feed_type": "none",
            "show_account_transparency_details": true,
            "show_shoppable_feed": false,
            "third_party_downloads_enabled": 1,
            "transparency_product_enabled": false,
            "username": "caldeironuria70"
          },
          "video_subtitles_locale": "es_CL",
          "__is_XDTMediaDict": true
        }
      },
      "parent_comment_id": "18142813870496178",
      "pk": "18121513129619994",
      "private_reply_status": 0,
      "replied_to_comment_id": "18142813870496178",
      "share_enabled": true,
      "status": "Active",
      "strong_id__": "18121513129619994",
      "text": "@vegagarcianatalia",
      "type": 2,
      "user": {
        "fbid_v2": 17841406811654065,
        "full_name": "Nuria Taboada",
        "id": "6752523055",
        "is_mentionable": true,
        "is_private": false,
        "is_verified": false,
        "pk": 6752523055,
        "pk_id": "6752523055",
        "profile_pic_id": "3869835622605851526_6752523055",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
        "strong_id__": "6752523055",
        "username": "caldeironuria70"
      },
      "user_id": 6752523055
    },
    {
      "bit_flags": 0,
      "child_comment_index": 2,
      "comment_like_count": 0,
      "content_type": "comment",
      "created_at": 1775154735,
      "created_at_for_fb_app": 1775154735,
      "created_at_utc": 1775154735,
      "did_report_as_spam": false,
      "has_disliked_comment": false,
      "has_liked_comment": false,
      "is_covered": false,
      "is_photo_comments_enabled_for_comment_author": false,
      "is_text_editable": false,
      "is_edited": false,
      "meta_ai_comment_type": "NONE",
      "is_ranked_comment": false,
      "liked_by_media_coauthors": [],
      "media_id": 3864286541032633353,
      "media_info": {
        "media": {
          "can_see_insights_as_brand": false,
          "clips_demotion_control": {
            "confirmation_body": "We'll suggest fewer posts like this.",
            "confirmation_icon": "none",
            "confirmation_style": "bottomsheet",
            "confirmation_title": "Post hidden",
            "confirmation_title_style": "large_left",
            "enable_word_wrapping": true,
            "followup_options": [
              {
                "data": "author_id:6752523055",
                "demotion_control": {
                  "confirmation_body": "We won't suggest posts from caldeironuria70.",
                  "confirmation_icon": "eye-off-pano",
                  "confirmation_style": "bottomsheet",
                  "undo_style": "inline"
                },
                "id": "dislike_author",
                "show_icon": true,
                "text": "Don't suggest posts from caldeironuria70"
              },
              {
                "id": "hide_all_specific_words",
                "show_icon": true,
                "text": "Don't suggest posts with certain words"
              },
              {
                "id": "control_center",
                "show_icon": true,
                "text": "Manage content preferences"
              }
            ],
            "title": "Not interested",
            "title_style": "normal",
            "undo_style": "top_right"
          },
          "coauthor_producer_can_see_organic_insights": false,
          "coauthor_producers": [],
          "comment_inform_treatment": {
            "should_have_inform_treatment": false,
            "text": ""
          },
          "crosspost_metadata": {
            "fb_downstream_use_xpost_metadata": {
              "downstream_use_xpost_deny_reason": "NONE"
            }
          },
          "deleted_reason": 0,
          "enable_media_notes_production": true,
          "enable_waist": true,
          "ig_play_count": 17,
          "fundraiser_tag": {},
          "gen_ai_detection_method": {
            "detection_method": "NONE"
          },
          "has_delayed_metadata": false,
          "has_more_comments": false,
          "hide_view_all_comment_entrypoint": true,
          "invited_coauthor_producers": [],
          "is_artist_pick": false,
          "is_cutout_sticker_allowed": true,
          "is_in_profile_grid": false,
          "is_organic_product_tagging_eligible": true,
          "is_paid_partnership": false,
          "is_reshare_of_text_post_app_media_in_ig": false,
          "is_reuse_allowed": true,
          "is_tagged_media_shared_to_viewer_profile_grid": false,
          "is_unified_video": false,
          "is_visual_reply_commenter_notice_enabled": true,
          "media_notes": {
            "items": []
          },
          "mezql_token": "",
          "owner": {
            "__typename": "XDTUserDict",
            "strong_id__": "6752523055",
            "id": "6752523055",
            "account_badges": [],
            "biography": "Galega de  pura cepa",
            "can_see_quiet_post_attribution": true,
            "fan_club_info": {},
            "fbid_v2": 17841406811654065,
            "feed_post_reshare_disabled": false,
            "full_name": "Nuria Taboada",
            "has_anonymous_profile_picture": false,
            "interop_messaging_user_fbid": "110265577029021",
            "is_favorite": false,
            "is_private": false,
            "is_unpublished": false,
            "is_verified": false,
            "pk": "6752523055",
            "profile_pic_id": "3869835622605851526_6752523055",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
            "show_account_transparency_details": true,
            "third_party_downloads_enabled": 1,
            "transparency_product_enabled": false,
            "username": "caldeironuria70",
            "views_on_grid_status": "SHOW_VIEWS_ON_GRID"
          },
          "play_count": 17,
          "profile_grid_control_enabled": false,
          "senders": [],
          "share_count_disabled": false,
          "is_social_ufi_disabled": false,
          "sharing_friction_info": {
            "should_have_sharing_friction": false
          },
          "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
          "floating_context_items": [],
          "subscribe_cta_visible": false,
          "timeline_pinned_user_ids": [],
          "video_codec": "avc1.64001f",
          "video_sticker_locales": [],
          "view_state_item_type": 128,
          "visual_comment_reply_sticker_info": [
            {
              "end_time_ms": 38677,
              "height": 0.178125,
              "is_fb_sticker": 0,
              "is_hidden": 0,
              "is_pinned": 0,
              "is_sticker": 1,
              "rotation": 0,
              "start_time_ms": 0,
              "vcr_sticker": {
                "can_viewer_link_back_to_original_media_from_vcr": true,
                "end_background_color": "#ffffff",
                "end_time_ms": 38677,
                "original_comment_author": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "46193898922",
                  "id": "46193898922",
                  "full_name": "Natalia Vega Garcia",
                  "is_private": false,
                  "is_verified": false,
                  "pk": "46193898922",
                  "profile_pic_id": "2518281128395959898_46193898922",
                  "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
                  "username": "vegagarcianatalia"
                },
                "original_comment_id": "18142813870496178",
                "original_comment_text": "Ya está bien tapar estás palabras: violación y violencia etc",
                "original_media_id": "3864286541032633353",
                "start_background_color": "#ffffff",
                "start_time_ms": 0,
                "text_color": ""
              },
              "width": 0.7222222,
              "x": 0.5,
              "y": 0.29453126,
              "z": 0
            }
          ],
          "visual_replies_info": {
            "can_viewer_link_back_to_original_media_from_vcr": true,
            "comment_info": {
              "comment_id": "18142813870496178",
              "commenter_username": "vegagarcianatalia"
            },
            "original_media": {
              "pk": "3864286541032633353"
            }
          },
          "top_likers": [],
          "__typename": "XDTMediaDict",
          "strong_id__": "3866600359091686055_6752523055",
          "id": "3866600359091686055_6752523055",
          "are_remixes_crosspostable": true,
          "can_viewer_reshare": true,
          "can_viewer_save": true,
          "caption_is_edited": false,
          "code": "DWo7IpcDsqn",
          "device_timestamp": 11341063266541,
          "like_count": 0,
          "comment_count": 0,
          "filter_type": 0,
          "has_audio": true,
          "has_high_risk_gen_ai_inform_treatment": false,
          "has_liked": false,
          "has_shared_to_fb": 0,
          "has_views_fetching": true,
          "ig_media_sharing_disabled": false,
          "image_versions2": {
            "additional_candidates": {
              "first_frame": {
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw5-1.cdninstagram.com/...",
                "width": 640
              },
              "igtv_first_frame": {
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw5-1.cdninstagram.com/...",
                "width": 640
              }
            },
            "candidates": [
              {
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw5-1.cdninstagram.com/...",
                "width": 640
              }
            ],
            "scrubber_spritesheet_info_candidates": {
              "default": {
                "file_size_kb": 669,
                "max_thumbnails_per_sprite": 105,
                "rendered_width": 96,
                "sprite_height": 1232,
                "sprite_width": 1500,
                "thumbnail_duration": 0.50617142857143,
                "thumbnail_height": 176,
                "thumbnail_width": 100,
                "thumbnails_per_row": 15,
                "total_thumbnail_num_per_sprite": 105,
                "video_length": 53.148
              }
            }
          },
          "is_comments_gif_composer_enabled": true,
          "is_dash_eligible": 1,
          "is_post_live_clips_media": false,
          "is_quiet_post": false,
          "is_third_party_downloads_eligible": true,
          "like_and_view_counts_disabled": false,
          "media_type": 2,
          "number_of_qualities": 2,
          "organic_tracking_token": "eyJ2ZXJzaW9uIjo2LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiQVVlcHZtRlZaRmJkTDlJaTRITU5mYzgzODY2NjAwMzU5MDkxNjg2MDU1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTA3NTI0NnwzODY2NjAwMzU5MDkxNjg2MDU1fDY3NTI1MjMwNTV8NmEwZDJhNmM4MWQxYjE4YzRlYzZhOWU5ODA3ZmU4ZjUwZjRjNTM3YjEzMGI4NDc4ZGE4ZmE4ODk4MzliNWZmMiJ9LCJzaWduYXR1cmUiOiIifQ==",
          "original_height": 1280,
          "original_media_has_visual_reply_media": false,
          "original_width": 720,
          "product_type": "clips",
          "taken_at": 1775154752,
          "user": {
            "__typename": "XDTUserDict",
            "strong_id__": "6752523055",
            "id": "6752523055",
            "account_badges": [],
            "fan_club_info": {},
            "fbid_v2": 17841406811654065,
            "feed_post_reshare_disabled": false,
            "full_name": "Nuria Taboada",
            "has_anonymous_profile_picture": false,
            "interop_messaging_user_fbid": "110265577029021",
            "is_facebook_onboarded_charity": false,
            "is_favorite": false,
            "is_private": false,
            "is_unpublished": false,
            "is_verified": false,
            "merchant_checkout_style": "none",
            "pk": 6752523055,
            "profile_pic_id": "3869835622605851526_6752523055",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
            "seller_shoppable_feed_type": "none",
            "show_account_transparency_details": true,
            "show_shoppable_feed": false,
            "third_party_downloads_enabled": 1,
            "transparency_product_enabled": false,
            "username": "caldeironuria70"
          },
          "video_subtitles_locale": "es_CL",
          "__is_XDTMediaDict": true
        }
      },
      "parent_comment_id": "18142813870496178",
      "pk": "18088027280262150",
      "private_reply_status": 0,
      "replied_to_comment_id": "18142813870496178",
      "share_enabled": true,
      "status": "Active",
      "strong_id__": "18088027280262150",
      "text": "@vegagarcianatalia",
      "type": 2,
      "user": {
        "fbid_v2": 17841406811654065,
        "full_name": "Nuria Taboada",
        "id": "6752523055",
        "is_mentionable": true,
        "is_private": false,
        "is_verified": false,
        "pk": 6752523055,
        "pk_id": "6752523055",
        "profile_pic_id": "3869835622605851526_6752523055",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
        "strong_id__": "6752523055",
        "username": "caldeironuria70"
      },
      "user_id": 6752523055
    }
  ],
  "has_more_head_child_comments": false,
  "has_more_tail_child_comments": false,
  "is_ranked_replies": false,
  "liked_by_media_owner_badge_enabled": true,
  "parent_comment": {
    "bit_flags": 0,
    "comment_has_a_visual_reply_media": true,
    "comment_like_count": 2,
    "content_type": "comment",
    "created_at": 1774989022,
    "created_at_for_fb_app": 1774989022,
    "created_at_utc": 1774989022,
    "did_report_as_spam": false,
    "has_disliked_comment": false,
    "has_liked_comment": false,
    "has_translation": true,
    "is_covered": false,
    "is_photo_comments_enabled_for_comment_author": false,
    "is_text_editable": false,
    "is_edited": false,
    "meta_ai_comment_type": "NONE",
    "is_ranked_comment": false,
    "liked_by_media_coauthors": [],
    "media_id": 3864286541032633353,
    "pk": "18142813870496178",
    "private_reply_status": 0,
    "share_enabled": true,
    "status": "Active",
    "strong_id__": "18142813870496178",
    "text": "Ya está bien tapar estás palabras: violación y violencia etc",
    "type": 0,
    "user": {
      "fbid_v2": 17841446167674237,
      "full_name": "Natalia Vega Garcia",
      "id": "46193898922",
      "is_mentionable": true,
      "is_private": false,
      "is_verified": false,
      "pk": 46193898922,
      "pk_id": "46193898922",
      "profile_pic_id": "2518281128395959898_46193898922",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/...",
      "strong_id__": "46193898922",
      "username": "vegagarcianatalia"
    },
    "user_id": 46193898922
  },
  "status": "ok"
}
```

</details>

---

### GET /v2/media/info/by/code

Get media object

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `code` | string | Yes | Code |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/info/by/code?code=DRqAYKuAIUx"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_info_by_code_v2(code="DRqAYKuAIUx")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/media/info/by/code",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"code": "DRqAYKuAIUx"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/info/by/code?code=DRqAYKuAIUx",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "media_or_ad": {
    "strong_id__": "3776832898280228145_787132",
    "id": "3776832898280228145_787132",
    "disable_caption_and_comment": false,
    "fbid": 18065011277571522,
    "deleted_reason": 0,
    "client_cache_key": "Mzc3NjgzMjg5ODI4MDIyODE0NQ==.3",
    "integrity_review_decision": "pending",
    "pk": 3776832898280228145,
    "is_affiliate_commission_eligible": false,
    "has_delayed_metadata": false,
    "mezql_token": "",
    "should_request_ads": false,
    "has_privately_liked": false,
    "collaborator_edit_eligibility": false,
    "share_count_disabled": false,
    "is_reshare_of_text_post_app_media_in_ig": false,
    "is_visual_reply_commenter_notice_enabled": true,
    "translated_langs_for_autodub": [],
    "subtype_name_for_REST__": "XDTClipsMedia",
    "is_third_party_downloads_eligible": false,
    "image_versions2": {
      "additional_candidates": {
        "first_frame": {
          "estimated_scans_sizes": [
            6839,
            13678,
            20517
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-atl3-3.cdninstagram.com/...",
          "width": 640,
          "is_spatial_image": false
        },
        "igtv_first_frame": {
          "estimated_scans_sizes": [
            6839,
            13678,
            20517
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-atl3-3.cdninstagram.com/...",
          "width": 640,
          "is_spatial_image": false
        },
        "smart_frame": null
      },
      "candidates": [
        {
          "estimated_scans_sizes": [
            27870,
            55740,
            83610
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-atl3-2.cdninstagram.com/...",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "scrubber_spritesheet_info_candidates": {
        "default": {
          "file_size_kb": 428,
          "max_thumbnails_per_sprite": 105,
          "rendered_width": 96,
          "sprite_height": 1232,
          "sprite_urls": [
            "https://scontent-atl3-1.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gE5D5xkzJlD4HI6mVcFfzCe7h-0GlKcY4mDDdaZkUyD_K9KJChiMhKk0wU-gwG1JQA&_nc_ohc=7fRK9vLZo4UQ7kNvwFFclfX&_nc_gid=EuHlGg-baE-_SoN-Nv9UmA&edm=AEcnVisBAAAA&ccb=7-5&oh=00_Af0LAiSbAWj2_DToWIXbI9BAiNzzs6h75NRUw9e6GF2wCg&oe=69DC4C8A&_nc_sid=55bbed"
          ],
          "sprite_width": 1500,
          "thumbnail_duration": 0.2125047619047619,
          "thumbnail_height": 176,
          "thumbnail_width": 100,
          "thumbnails_per_row": 15,
          "total_thumbnail_num_per_sprite": 105,
          "video_length": 22.313
        }
      }
    },
    "media_type": 2,
    "original_width": 720,
    "original_height": 1280,
    "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMTk4Mjg4YzAyNmRiNGU1YWExNTQ0YTcwYTc1ZWEyYTMzNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTA2OTU0MXwzNzc2ODMyODk4MjgwMjI4MTQ1fDM1MTQ2MDMyODk3fGI4NGE5NDMxZGFiOGMyNTE2ZmRhZWJhNGVlYjIzM2IxNjczNmU5MjAzMTQ1MzI4MzJjZmRhNjdhODQzOTk0ZmYifSwic2lnbmF0dXJlIjoiIn0=",
    "music_metadata": null,
    "has_tagged_users": false,
    "clips_tab_pinned_user_ids": [],
    "is_open_to_public_submission": false,
    "is_social_ufi_disabled": false,
    "timeline_pinned_user_ids": [],
    "taken_at": 1764453631,
    "can_see_insights_as_brand": false,
    "fundraiser_tag": {
      "has_standalone_fundraiser": false
    },
    "fb_user_tags": {
      "in": []
    },
    "media_overlay_info": null,
    "is_in_profile_grid": false,
    "profile_grid_control_enabled": false,
    "is_artist_pick": false,
    "media_notes": {
      "items": []
    },
    "product_type": "clips",
    "social_context": [],
    "subscribe_cta_visible": false,
    "creative_config": null,
    "is_cutout_sticker_allowed": false,
    "cutout_sticker_info": [],
    "is_tagged_media_shared_to_viewer_profile_grid": false,
    "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
    "meta_ai_suggested_prompts": [],
    "gen_ai_chat_with_ai_cta_info": null,
    "can_reply": false,
    "floating_context_items": [],
    "is_eligible_content_for_post_roll_ad": false,
    "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
    "eligible_insights_entrypoints": "NONE",
    "media_attributions_data": [],
    "media_ui_attributions_data": [],
    "media_ui_attributions_data_v2": [],
    "creator_product_link_infos": [],
    "is_eligible_for_poe": true,
    "is_eligible_for_organic_eager_refresh": false,
    "commerce_integrity_review_decision": "",
    "prefetch_instructions": {
      "should_force_new_preload_chaining": false
    },
    "boost_unavailable_identifier": null,
    "boost_unavailable_reason": null,
    "boost_unavailable_reason_v2": null,
    "coauthor_producers": [],
    "coauthor_producer_can_see_organic_insights": false,
    "invited_coauthor_producers": [],
    "igbio_product": null,
    "is_paid_partnership": false,
    "reshare_count": 8346,
    "ig_media_sharing_disabled": false,
    "media_repost_count": 4442,
    "like_count": 135428,
    "top_likers": [],
    "hidden_likes_string_variant": -1,
    "caption": {
      "strong_id__": "18065011298571522",
      "bit_flags": 0,
      "created_at": 1764453632,
      "created_at_utc": 1764453632,
      "did_report_as_spam": false,
      "is_ranked_comment": false,
      "pk": "18065011298571522",
      "share_enabled": false,
      "content_type": "comment",
      "media_id": 3776832898280228145,
      "status": "Active",
      "type": 1,
      "user_id": 787132,
      "text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
      "user": {
        "strong_id__": "787132",
        "pk": 787132,
        "pk_id": "787132",
        "id": "787132",
        "is_unpublished": false,
        "fbid_v2": 17841400573960012,
        "username": "natgeo",
        "full_name": "National Geographic",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865702555259028436_787132",
        "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/..."
      },
      "is_covered": false,
      "private_reply_status": 0,
      "text_translation": "Even the heaviest rain feels peaceful here. \n\n #HostilePlanet is now streaming on @DisneyPlus."
    },
    "comment_count": 485,
    "comment_inform_treatment": {
      "action_type": null,
      "should_have_inform_treatment": false,
      "text": "",
      "url": null
    },
    "is_photo_comments_composer_enabled_for_author": false,
    "hide_view_all_comment_entrypoint": true,
    "locations": [],
    "play_count": 2866123,
    "ig_play_count": 2866123,
    "shop_routing_user_id": null,
    "featured_products": [],
    "are_remixes_crosspostable": true,
    "crosspost_metadata": {
      "fb_downstream_use_xpost_metadata": {
        "downstream_use_xpost_deny_reason": "NONE"
      }
    },
    "is_eligible_for_autodub": false,
    "is_eligible_for_autodub_upsell": false,
    "video_sticker_locales": [],
    "has_audio": true,
    "video_duration": 22.31399917602539,
    "is_dash_eligible": 1,
    "video_versions": [
      {
        "bandwidth": 2315752,
        "height": 1280,
        "id": "1525428988604088v",
        "type": 101,
        "url": "https://scontent-atl3-2.cdninstagram.com/...",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      }
    ],
    "number_of_qualities": 7,
    "video_codec": "vp09.00.30.08.00.02.02.01.00",
    "sharing_friction_info": {
      "should_have_sharing_friction": false,
      "bloks_app_url": null,
      "sharing_friction_payload": null
    },
    "gen_ai_detection_method": {
      "detection_method": "NONE"
    },
    "user": {
      "strong_id__": "787132",
      "fbid_v2": 17841400573960012,
      "feed_post_reshare_disabled": false,
      "id": "787132",
      "is_unpublished": false,
      "pk": 787132,
      "pk_id": "787132",
      "third_party_downloads_enabled": 2,
      "eligible_for_text_app_activation_badge": false,
      "account_type": 2,
      "account_badges": [],
      "fan_club_info": {
        "autosave_to_exclusive_highlight": null,
        "connected_member_count": null,
        "fan_club_id": null,
        "fan_club_name": null,
        "has_created_ssc": null,
        "has_enough_subscribers_for_ssc": null,
        "is_fan_club_gifting_eligible": null,
        "is_fan_club_referral_eligible": null,
        "is_free_trial_eligible": null,
        "largest_public_bc_id": null,
        "subscriber_count": null,
        "should_show_playlists_in_profile_tab": null,
        "fan_consideration_page_revamp_eligiblity": null
      },
      "full_name": "National Geographic",
      "has_anonymous_profile_picture": false,
      "is_favorite": false,
      "is_private": false,
      "is_ring_creator": false,
      "show_ring_award": false,
      "is_verified": true,
      "profile_pic_id": "3865702555259028436_787132",
      "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/...",
      "show_account_transparency_details": true,
      "transparency_product_enabled": false,
      "username": "natgeo",
      "latest_reel_media": 1775659002,
      "user_activation_info": {}
    },
    "community_notes_info": {
      "has_viewer_submitted_note": false,
      "note_submission_disabled": false,
      "enable_submission_friction": false,
      "is_eligible_for_request_a_note": true
    },
    "has_high_risk_gen_ai_inform_treatment": false,
    "caption_is_edited": false,
    "code": "DRqAYKuAIUx",
    "device_timestamp": 1764453587369,
    "enable_media_notes_production": true,
    "filter_type": 0,
    "has_views_fetching": true,
    "is_post_live_clips_media": false,
    "like_and_view_counts_disabled": false,
    "original_media_has_visual_reply_media": false,
    "report_info": {
      "has_viewer_submitted_report": false
    },
    "is_organic_product_tagging_eligible": true,
    "can_viewer_reshare": true,
    "has_shared_to_fb": 0,
    "media_reposter_bottomsheet_enabled": false,
    "has_liked": false,
    "can_viewer_save": true,
    "is_comments_gif_composer_enabled": false
  },
  "status": "ok"
}
```

</details>

---

### GET /v2/media/info/by/id

Get media object

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/info/by/id?id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_info_by_id_v2(id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/media/info/by/id",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/info/by/id?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "media_or_ad": {
    "strong_id__": "3776832898280228145_787132",
    "id": "3776832898280228145_787132",
    "disable_caption_and_comment": false,
    "fbid": 18065011277571522,
    "deleted_reason": 0,
    "client_cache_key": "Mzc3NjgzMjg5ODI4MDIyODE0NQ==.3",
    "integrity_review_decision": "pending",
    "pk": 3776832898280228145,
    "is_affiliate_commission_eligible": false,
    "has_delayed_metadata": false,
    "mezql_token": "",
    "should_request_ads": false,
    "has_privately_liked": false,
    "collaborator_edit_eligibility": false,
    "share_count_disabled": false,
    "is_reshare_of_text_post_app_media_in_ig": false,
    "is_visual_reply_commenter_notice_enabled": true,
    "translated_langs_for_autodub": [],
    "subtype_name_for_REST__": "XDTClipsMedia",
    "is_third_party_downloads_eligible": false,
    "image_versions2": {
      "additional_candidates": {
        "first_frame": {
          "estimated_scans_sizes": [
            6839,
            13678,
            20517
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-iad6-1.cdninstagram.com/...",
          "width": 640,
          "is_spatial_image": false
        },
        "igtv_first_frame": {
          "estimated_scans_sizes": [
            6839,
            13678,
            20517
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-iad6-1.cdninstagram.com/...",
          "width": 640,
          "is_spatial_image": false
        },
        "smart_frame": null
      },
      "candidates": [
        {
          "estimated_scans_sizes": [
            27870,
            55740,
            83610
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-iad6-1.cdninstagram.com/...",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "scrubber_spritesheet_info_candidates": {
        "default": {
          "file_size_kb": 428,
          "max_thumbnails_per_sprite": 105,
          "rendered_width": 96,
          "sprite_height": 1232,
          "sprite_urls": [
            "https://scontent-iad3-2.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gGJ7SlNLbNn6dZWTdPFRew5d0KjqnRdY2Tqg3gDP9aBKp1ys7eMA6Goq7QnIgbrnjk&_nc_ohc=7fRK9vLZo4UQ7kNvwH1hH_-&_nc_gid=6HdQyFFJPpFiY4pw7pv6QQ&edm=AEcnVisBAAAA&ccb=7-5&oh=00_Af2lPqbjIqVYm8UnpZ7n5RSvqwyT9JkOh2retOyU_D54lw&oe=69DC4C8A&_nc_sid=55bbed"
          ],
          "sprite_width": 1500,
          "thumbnail_duration": 0.2125047619047619,
          "thumbnail_height": 176,
          "thumbnail_width": 100,
          "thumbnails_per_row": 15,
          "total_thumbnail_num_per_sprite": 105,
          "video_length": 22.313
        }
      }
    },
    "media_type": 2,
    "original_width": 720,
    "original_height": 1280,
    "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiOTRjMGRjMmJjNzU1NDBmYWFiZWNiZWQ3YWU5NjM5Y2IzNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTA2ODU2NnwzNzc2ODMyODk4MjgwMjI4MTQ1fDMyOTQwMjU0MDYyfDZkNTRiZjMyN2UwZDM3OWQzZDVhN2MzMGQzMjFhYTU5MWQxZjllYTBmYzhhOWY0NDQ3YTA3NDc0ZDM3ZmQ2ZmUifSwic2lnbmF0dXJlIjoiIn0=",
    "music_metadata": null,
    "has_tagged_users": false,
    "clips_tab_pinned_user_ids": [],
    "is_open_to_public_submission": false,
    "is_social_ufi_disabled": false,
    "timeline_pinned_user_ids": [],
    "taken_at": 1764453631,
    "can_see_insights_as_brand": false,
    "fundraiser_tag": {
      "has_standalone_fundraiser": false
    },
    "fb_user_tags": {
      "in": []
    },
    "media_overlay_info": null,
    "is_in_profile_grid": false,
    "profile_grid_control_enabled": false,
    "is_artist_pick": false,
    "media_notes": {
      "items": []
    },
    "product_type": "clips",
    "social_context": [],
    "subscribe_cta_visible": false,
    "creative_config": null,
    "is_cutout_sticker_allowed": false,
    "cutout_sticker_info": [],
    "is_tagged_media_shared_to_viewer_profile_grid": false,
    "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
    "meta_ai_suggested_prompts": [],
    "gen_ai_chat_with_ai_cta_info": null,
    "can_reply": false,
    "floating_context_items": [],
    "is_eligible_content_for_post_roll_ad": false,
    "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
    "eligible_insights_entrypoints": "NONE",
    "media_attributions_data": [],
    "media_ui_attributions_data": [],
    "media_ui_attributions_data_v2": [],
    "creator_product_link_infos": [],
    "is_eligible_for_poe": true,
    "is_eligible_for_organic_eager_refresh": false,
    "commerce_integrity_review_decision": "",
    "prefetch_instructions": {
      "should_force_new_preload_chaining": false
    },
    "boost_unavailable_identifier": null,
    "boost_unavailable_reason": null,
    "boost_unavailable_reason_v2": null,
    "coauthor_producers": [],
    "coauthor_producer_can_see_organic_insights": false,
    "invited_coauthor_producers": [],
    "igbio_product": null,
    "is_paid_partnership": false,
    "reshare_count": 8346,
    "ig_media_sharing_disabled": false,
    "media_repost_count": 4442,
    "like_count": 135428,
    "top_likers": [],
    "hidden_likes_string_variant": -1,
    "caption": {
      "strong_id__": "18065011298571522",
      "bit_flags": 0,
      "created_at": 1764453632,
      "created_at_utc": 1764453632,
      "did_report_as_spam": false,
      "is_ranked_comment": false,
      "pk": "18065011298571522",
      "share_enabled": false,
      "content_type": "comment",
      "media_id": 3776832898280228145,
      "status": "Active",
      "type": 1,
      "user_id": 787132,
      "text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
      "user": {
        "strong_id__": "787132",
        "pk": 787132,
        "pk_id": "787132",
        "id": "787132",
        "is_unpublished": false,
        "fbid_v2": 17841400573960012,
        "username": "natgeo",
        "full_name": "National Geographic",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865702555259028436_787132",
        "profile_pic_url": "https://scontent-xxc1-1.cdninstagram.com/..."
      },
      "is_covered": false,
      "private_reply_status": 0,
      "text_translation": "Even the heaviest rain feels peaceful here. \n\n #HostilePlanet is now streaming on @DisneyPlus."
    },
    "comment_count": 485,
    "comment_inform_treatment": {
      "action_type": null,
      "should_have_inform_treatment": false,
      "text": "",
      "url": null
    },
    "is_photo_comments_composer_enabled_for_author": false,
    "hide_view_all_comment_entrypoint": true,
    "locations": [],
    "play_count": 2866123,
    "ig_play_count": 2866123,
    "shop_routing_user_id": null,
    "featured_products": [],
    "are_remixes_crosspostable": true,
    "crosspost_metadata": {
      "fb_downstream_use_xpost_metadata": {
        "downstream_use_xpost_deny_reason": "NONE"
      }
    },
    "is_eligible_for_autodub": false,
    "is_eligible_for_autodub_upsell": false,
    "video_sticker_locales": [],
    "has_audio": true,
    "video_duration": 22.31399917602539,
    "is_dash_eligible": 1,
    "video_versions": [
      {
        "bandwidth": 2315752,
        "height": 1280,
        "id": "1525428988604088v",
        "type": 101,
        "url": "https://scontent-iad6-1.cdninstagram.com/...",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      }
    ],
    "number_of_qualities": 7,
    "video_codec": "vp09.00.30.08.00.02.02.01.00",
    "sharing_friction_info": {
      "should_have_sharing_friction": false,
      "bloks_app_url": null,
      "sharing_friction_payload": null
    },
    "gen_ai_detection_method": {
      "detection_method": "NONE"
    },
    "user": {
      "strong_id__": "787132",
      "fbid_v2": 17841400573960012,
      "feed_post_reshare_disabled": false,
      "id": "787132",
      "is_unpublished": false,
      "pk": 787132,
      "pk_id": "787132",
      "third_party_downloads_enabled": 2,
      "eligible_for_text_app_activation_badge": false,
      "account_type": 2,
      "account_badges": [],
      "fan_club_info": {
        "autosave_to_exclusive_highlight": null,
        "connected_member_count": null,
        "fan_club_id": null,
        "fan_club_name": null,
        "has_created_ssc": null,
        "has_enough_subscribers_for_ssc": null,
        "is_fan_club_gifting_eligible": null,
        "is_fan_club_referral_eligible": null,
        "is_free_trial_eligible": null,
        "largest_public_bc_id": null,
        "subscriber_count": null,
        "should_show_playlists_in_profile_tab": null,
        "fan_consideration_page_revamp_eligiblity": null
      },
      "full_name": "National Geographic",
      "has_anonymous_profile_picture": false,
      "is_favorite": false,
      "is_private": false,
      "is_ring_creator": false,
      "show_ring_award": false,
      "is_verified": true,
      "profile_pic_id": "3865702555259028436_787132",
      "profile_pic_url": "https://scontent-xxc1-1.cdninstagram.com/...",
      "show_account_transparency_details": true,
      "transparency_product_enabled": false,
      "username": "natgeo",
      "latest_reel_media": 1775659002,
      "user_activation_info": {}
    },
    "community_notes_info": {
      "has_viewer_submitted_note": false,
      "note_submission_disabled": false,
      "enable_submission_friction": false,
      "is_eligible_for_request_a_note": true
    },
    "has_high_risk_gen_ai_inform_treatment": false,
    "caption_is_edited": false,
    "code": "DRqAYKuAIUx",
    "device_timestamp": 1764453587369,
    "enable_media_notes_production": true,
    "filter_type": 0,
    "has_views_fetching": true,
    "is_post_live_clips_media": false,
    "like_and_view_counts_disabled": false,
    "original_media_has_visual_reply_media": false,
    "report_info": {
      "has_viewer_submitted_report": false
    },
    "is_organic_product_tagging_eligible": true,
    "can_viewer_reshare": true,
    "has_shared_to_fb": 0,
    "media_reposter_bottomsheet_enabled": false,
    "has_liked": false,
    "can_viewer_save": true,
    "is_comments_gif_composer_enabled": false
  },
  "status": "ok"
}
```

</details>

---

### GET /v2/media/info/by/url

Get media object

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/info/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_info_by_url_v2(url="https://www.instagram.com/p/DRqAYKuAIUx/")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/media/info/by/url",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/p/DRqAYKuAIUx/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/info/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "media_or_ad": {
    "strong_id__": "3776832898280228145_787132",
    "id": "3776832898280228145_787132",
    "disable_caption_and_comment": false,
    "fbid": 18065011277571522,
    "deleted_reason": 0,
    "client_cache_key": "Mzc3NjgzMjg5ODI4MDIyODE0NQ==.3",
    "integrity_review_decision": "pending",
    "pk": 3776832898280228145,
    "is_affiliate_commission_eligible": false,
    "has_delayed_metadata": false,
    "mezql_token": "",
    "should_request_ads": false,
    "has_privately_liked": false,
    "collaborator_edit_eligibility": false,
    "share_count_disabled": false,
    "is_reshare_of_text_post_app_media_in_ig": false,
    "is_visual_reply_commenter_notice_enabled": true,
    "translated_langs_for_autodub": [],
    "subtype_name_for_REST__": "XDTClipsMedia",
    "is_third_party_downloads_eligible": false,
    "image_versions2": {
      "additional_candidates": {
        "first_frame": {
          "estimated_scans_sizes": [
            6839,
            13678,
            20517
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-lga3-1.cdninstagram.com/...",
          "width": 640,
          "is_spatial_image": false
        },
        "igtv_first_frame": {
          "estimated_scans_sizes": [
            6839,
            13678,
            20517
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-lga3-1.cdninstagram.com/...",
          "width": 640,
          "is_spatial_image": false
        },
        "smart_frame": null
      },
      "candidates": [
        {
          "estimated_scans_sizes": [
            27870,
            55740,
            83610
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-lga3-2.cdninstagram.com/...",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "scrubber_spritesheet_info_candidates": {
        "default": {
          "file_size_kb": 428,
          "max_thumbnails_per_sprite": 105,
          "rendered_width": 96,
          "sprite_height": 1232,
          "sprite_urls": [
            "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gFgByIqzz4nb9OdZ0q1QKfh3hpPGwi8u7fLUsafJlj76Tx1ZzIepmWogLnvd-FJ9l0&_nc_ohc=7fRK9vLZo4UQ7kNvwFd0e2e&_nc_gid=9n0M10odfRZRdpekxkuIlw&edm=AEcnVisBAAAA&ccb=7-5&oh=00_Af2kCgLAsL58XXV-n33_mTST-XseZF0Bt8ctJH90qyHq8A&oe=69DC4C8A&_nc_sid=55bbed"
          ],
          "sprite_width": 1500,
          "thumbnail_duration": 0.2125047619047619,
          "thumbnail_height": 176,
          "thumbnail_width": 100,
          "thumbnails_per_row": 15,
          "total_thumbnail_num_per_sprite": 105,
          "video_length": 22.313
        }
      }
    },
    "media_type": 2,
    "original_width": 720,
    "original_height": 1280,
    "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiNjhkZGY2NjlmODRjNDZhNDg5OTU3YTcyMGY2ZmFkMDQzNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTA3MDQzNHwzNzc2ODMyODk4MjgwMjI4MTQ1fDM5MDg5NjM1NjUwfDliYjQ5NDlkYzQxZDY0YzAwM2M1YzZmYWE0MmI5M2E0NjJjY2VhOTcwYmFjOWVlNDFmNDg1NGMxMzQyNDI0ZWUifSwic2lnbmF0dXJlIjoiIn0=",
    "music_metadata": null,
    "has_tagged_users": false,
    "clips_tab_pinned_user_ids": [],
    "is_open_to_public_submission": false,
    "is_social_ufi_disabled": false,
    "timeline_pinned_user_ids": [],
    "taken_at": 1764453631,
    "can_see_insights_as_brand": false,
    "fundraiser_tag": {
      "has_standalone_fundraiser": false
    },
    "fb_user_tags": {
      "in": []
    },
    "media_overlay_info": null,
    "is_in_profile_grid": false,
    "profile_grid_control_enabled": false,
    "is_artist_pick": false,
    "media_notes": {
      "items": []
    },
    "product_type": "clips",
    "social_context": [],
    "subscribe_cta_visible": false,
    "creative_config": null,
    "is_cutout_sticker_allowed": false,
    "cutout_sticker_info": [],
    "is_tagged_media_shared_to_viewer_profile_grid": false,
    "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
    "meta_ai_suggested_prompts": [],
    "gen_ai_chat_with_ai_cta_info": null,
    "can_reply": false,
    "floating_context_items": [],
    "is_eligible_content_for_post_roll_ad": false,
    "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
    "eligible_insights_entrypoints": "NONE",
    "media_attributions_data": [],
    "media_ui_attributions_data": [],
    "media_ui_attributions_data_v2": [],
    "creator_product_link_infos": [],
    "is_eligible_for_poe": true,
    "is_eligible_for_organic_eager_refresh": false,
    "commerce_integrity_review_decision": "",
    "prefetch_instructions": {
      "should_force_new_preload_chaining": false
    },
    "boost_unavailable_identifier": null,
    "boost_unavailable_reason": null,
    "boost_unavailable_reason_v2": null,
    "coauthor_producers": [],
    "coauthor_producer_can_see_organic_insights": false,
    "invited_coauthor_producers": [],
    "igbio_product": null,
    "is_paid_partnership": false,
    "reshare_count": 8346,
    "ig_media_sharing_disabled": false,
    "media_repost_count": 4442,
    "like_count": 135428,
    "top_likers": [],
    "hidden_likes_string_variant": -1,
    "caption": {
      "strong_id__": "18065011298571522",
      "bit_flags": 0,
      "created_at": 1764453632,
      "created_at_utc": 1764453632,
      "did_report_as_spam": false,
      "is_ranked_comment": false,
      "pk": "18065011298571522",
      "share_enabled": false,
      "content_type": "comment",
      "media_id": 3776832898280228145,
      "status": "Active",
      "type": 1,
      "user_id": 787132,
      "text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
      "user": {
        "strong_id__": "787132",
        "pk": 787132,
        "pk_id": "787132",
        "id": "787132",
        "is_unpublished": false,
        "fbid_v2": 17841400573960012,
        "username": "natgeo",
        "full_name": "National Geographic",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865702555259028436_787132",
        "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/..."
      },
      "is_covered": false,
      "private_reply_status": 0,
      "text_translation": "Even the heaviest rain feels peaceful here. \n\n #HostilePlanet is now streaming on @DisneyPlus."
    },
    "comment_count": 485,
    "comment_inform_treatment": {
      "action_type": null,
      "should_have_inform_treatment": false,
      "text": "",
      "url": null
    },
    "is_photo_comments_composer_enabled_for_author": false,
    "hide_view_all_comment_entrypoint": true,
    "locations": [],
    "play_count": 2866123,
    "ig_play_count": 2866123,
    "shop_routing_user_id": null,
    "featured_products": [],
    "are_remixes_crosspostable": true,
    "crosspost_metadata": {
      "fb_downstream_use_xpost_metadata": {
        "downstream_use_xpost_deny_reason": "NONE"
      }
    },
    "is_eligible_for_autodub": false,
    "is_eligible_for_autodub_upsell": false,
    "video_sticker_locales": [],
    "has_audio": true,
    "video_duration": 22.31399917602539,
    "is_dash_eligible": 1,
    "video_versions": [
      {
        "bandwidth": 2315752,
        "height": 1280,
        "id": "1525428988604088v",
        "type": 101,
        "url": "https://scontent-lga3-3.cdninstagram.com/...",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      }
    ],
    "number_of_qualities": 7,
    "video_codec": "vp09.00.30.08.00.02.02.01.00",
    "sharing_friction_info": {
      "should_have_sharing_friction": false,
      "bloks_app_url": null,
      "sharing_friction_payload": null
    },
    "gen_ai_detection_method": {
      "detection_method": "NONE"
    },
    "user": {
      "strong_id__": "787132",
      "fbid_v2": 17841400573960012,
      "feed_post_reshare_disabled": false,
      "id": "787132",
      "is_unpublished": false,
      "pk": 787132,
      "pk_id": "787132",
      "third_party_downloads_enabled": 2,
      "eligible_for_text_app_activation_badge": false,
      "account_type": 2,
      "account_badges": [],
      "fan_club_info": {
        "autosave_to_exclusive_highlight": null,
        "connected_member_count": null,
        "fan_club_id": null,
        "fan_club_name": null,
        "has_created_ssc": null,
        "has_enough_subscribers_for_ssc": null,
        "is_fan_club_gifting_eligible": null,
        "is_fan_club_referral_eligible": null,
        "is_free_trial_eligible": null,
        "largest_public_bc_id": null,
        "subscriber_count": null,
        "should_show_playlists_in_profile_tab": null,
        "fan_consideration_page_revamp_eligiblity": null
      },
      "full_name": "National Geographic",
      "has_anonymous_profile_picture": false,
      "is_favorite": false,
      "is_private": false,
      "is_ring_creator": false,
      "show_ring_award": false,
      "is_verified": true,
      "profile_pic_id": "3865702555259028436_787132",
      "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/...",
      "show_account_transparency_details": true,
      "transparency_product_enabled": false,
      "username": "natgeo",
      "latest_reel_media": 1775659002,
      "user_activation_info": {}
    },
    "community_notes_info": {
      "has_viewer_submitted_note": false,
      "note_submission_disabled": false,
      "enable_submission_friction": false,
      "is_eligible_for_request_a_note": true
    },
    "has_high_risk_gen_ai_inform_treatment": false,
    "caption_is_edited": false,
    "code": "DRqAYKuAIUx",
    "device_timestamp": 1764453587369,
    "enable_media_notes_production": true,
    "filter_type": 0,
    "has_views_fetching": true,
    "is_post_live_clips_media": false,
    "like_and_view_counts_disabled": false,
    "original_media_has_visual_reply_media": false,
    "report_info": {
      "has_viewer_submitted_report": false
    },
    "is_organic_product_tagging_eligible": true,
    "can_viewer_reshare": true,
    "has_shared_to_fb": 0,
    "media_reposter_bottomsheet_enabled": false,
    "has_liked": false,
    "can_viewer_save": true,
    "is_comments_gif_composer_enabled": false
  },
  "status": "ok"
}
```

</details>

---

### GET /v2/media/likers

Get user's likers. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/likers?id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_likers_v2(id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/media/likers",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/likers?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "users": [
    {
      "strong_id__": "1469722832",
      "pk": 1469722832,
      "pk_id": "1469722832",
      "id": "1469722832",
      "full_name": "🅙orge Delgado 🦖",
      "is_private": true,
      "is_verified": false,
      "profile_pic_id": "3011497359763514020_1469722832",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/...",
      "username": "jorge10.ds",
      "is_new": false,
      "latest_reel_media": 0
    },
    {
      "strong_id__": "48158574428",
      "pk": 48158574428,
      "pk_id": "48158574428",
      "id": "48158574428",
      "full_name": "",
      "is_private": true,
      "is_verified": false,
      "profile_pic_id": "3861336032742852912_48158574428",
      "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/...",
      "username": "only_looking_at_fashionpeople",
      "is_new": false,
      "latest_reel_media": 0
    },
    {
      "strong_id__": "77145556919",
      "pk": 77145556919,
      "pk_id": "77145556919",
      "id": "77145556919",
      "full_name": "張心瑋",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3832460928504522162_77145556919",
      "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
      "username": "xin.wei.chang261891",
      "is_new": false,
      "latest_reel_media": 1775634127
    }
  ],
  "user_count": 135428,
  "status": "ok"
}
```

</details>

---

### GET /v2/media/template

Get media template

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/template?id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_template_v2(id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/media/template",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/template?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "items": [
    {
      "media": {
        "strong_id__": "3776832898280228145_787132",
        "id": "3776832898280228145_787132",
        "pk": 3776832898280228145,
        "fbid": 18065011277571522,
        "media_type": 2,
        "like_and_view_counts_disabled": false,
        "code": "DRqAYKuAIUx",
        "taken_at": 1764453631,
        "product_type": "clips",
        "caption_is_edited": false,
        "can_viewer_reshare": true,
        "can_viewer_save": true,
        "comment_count": 485,
        "are_remixes_crosspostable": true,
        "video_versions": [
          {
            "url": "https://scontent-lga3-3.cdninstagram.com/...",
            "height": 1280,
            "width": 720,
            "type": 101,
            "id": "1525428988604088v",
            "bandwidth": 2315752
          }
        ],
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                27870,
                55740,
                83610
              ],
              "height": 1333,
              "scans_profile": "e35",
              "url": "https://scontent-lga3-2.cdninstagram.com/...",
              "width": 750
            }
          ],
          "additional_candidates": {
            "first_frame": {
              "estimated_scans_sizes": [
                6839,
                13678,
                20517
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-lga3-1.cdninstagram.com/...",
              "width": 640
            },
            "igtv_first_frame": {
              "estimated_scans_sizes": [
                6839,
                13678,
                20517
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-lga3-1.cdninstagram.com/...",
              "width": 640
            }
          },
          "scrubber_spritesheet_info_candidates": {
            "default": {
              "sprite_urls": [
                "https://scontent-lga3-3.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_cat=102&ccb=7-5&_nc_sid=efdbef&_nc_ohc=pyZiGYy3BegQ7kNvwFooX4U&_nc_oc=AdqaiKLAjbusHNSsaPE6rj7UQj4L0TIEPBjOJtwLhjyBNIZ_dILGjd2zo0wYb_3Rn_Y&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=R_Aani4DZtr5O2ImInLgtg&_nc_ss=7a3ba&oh=00_Af1e6AEya_KXaqV5PF7NXwqeJGihPm1KEGo6ZhME32BYtQ&oe=69DC4C8A"
              ],
              "file_size_kb": 428,
              "max_thumbnails_per_sprite": 105,
              "rendered_width": 96,
              "sprite_height": 1232,
              "sprite_width": 1500,
              "thumbnail_duration": 0.21250476190476,
              "thumbnail_height": 176,
              "thumbnail_width": 100,
              "thumbnails_per_row": 15,
              "total_thumbnail_num_per_sprite": 105,
              "video_length": 22.313
            }
          }
        },
        "has_audio": true,
        "like_count": 135428,
        "locations": [],
        "is_dash_eligible": 1,
        "is_unified_video": true,
        "community_notes_info": {
          "has_viewer_submitted_note": false,
          "note_submission_disabled": false,
          "enable_submission_friction": false,
          "is_eligible_for_request_a_note": true
        },
        "enable_media_notes_production": true,
        "play_count": 2866123,
        "ig_play_count": 2866123,
        "is_third_party_downloads_eligible": false,
        "original_width": 720,
        "original_height": 1280,
        "is_reuse_allowed": false,
        "has_shared_to_fb": 0,
        "reshare_count": 8346,
        "has_privately_liked": false,
        "ig_media_sharing_disabled": false,
        "original_media_has_visual_reply_media": false,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo2LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiQXRURkZDenphY25CUkx2UXVTYW1kZVIzNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTA3OTA5MHwzNzc2ODMyODk4MjgwMjI4MTQ1fDc4NzEzMnxhZjE4YWNmZGRlMTYyYzliYTNiNDVlODg5MTc3NGViZDU4NTNjZThkYmEzZjcxZjE3ZDg3YWVmMzI2NTMzOWFmIn0sInNpZ25hdHVyZSI6IiJ9",
        "has_views_fetching": true,
        "video_duration": 22.314,
        "is_post_live_clips_media": false,
        "is_quiet_post": false,
        "is_comments_gif_composer_enabled": false,
        "has_high_risk_gen_ai_inform_treatment": false,
        "clips_tab_pinned_user_ids": [],
        "collaborator_edit_eligibility": false,
        "number_of_qualities": 7,
        "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
        "is_artist_pick": false,
        "translated_langs_for_autodub": [],
        "subtype_name_for_REST__": "XDTClipsMedia",
        "is_eligible_for_poe": true,
        "eligible_insights_entrypoints": "NONE",
        "clips_demotion_control": {
          "confirmation_body": "We'll suggest fewer posts like this.",
          "confirmation_icon": "none",
          "confirmation_style": "bottomsheet",
          "confirmation_title": "Post hidden",
          "confirmation_title_style": "large_left",
          "enable_word_wrapping": true,
          "followup_options": [
            {
              "data": "author_id:787132",
              "demotion_control": {
                "confirmation_body": "We won't suggest posts from natgeo.",
                "confirmation_icon": "eye-off-pano",
                "confirmation_style": "bottomsheet",
                "undo_style": "inline"
              },
              "id": "dislike_author",
              "show_icon": true,
              "text": "Don't suggest posts from natgeo"
            },
            {
              "id": "hide_all_specific_words",
              "show_icon": true,
              "text": "Don't suggest posts with certain words"
            },
            {
              "id": "control_center",
              "show_icon": true,
              "text": "Manage content preferences"
            }
          ],
          "title": "Not interested",
          "title_style": "normal",
          "undo_style": "top_right"
        },
        "hidden_likes_string_variant": -1,
        "is_social_ufi_disabled": false,
        "client_cache_key": "Mzc3NjgzMjg5ODI4MDIyODE0NQ==.3",
        "can_reply": false,
        "media_repost_count": 4442,
        "media_attributions_data": [],
        "media_ui_attributions_data": [],
        "creator_product_link_infos": [],
        "can_view_more_preview_comments": false,
        "video_codec": "vp09.00.30.08.00.02.02.01.00",
        "mezql_token": "",
        "has_tagged_users": false,
        "is_eligible_content_for_post_roll_ad": false,
        "is_cutout_sticker_allowed": false,
        "is_photo_comments_composer_enabled_for_author": false,
        "hide_view_all_comment_entrypoint": true,
        "has_liked": false,
        "is_organic_product_tagging_eligible": true,
        "view_state_item_type": 128,
        "top_likers": [],
        "video_sticker_locales": [],
        "is_paid_partnership": false,
        "is_in_profile_grid": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "integrity_review_decision": "pending",
        "has_delayed_metadata": false,
        "filter_type": 0,
        "deleted_reason": 0,
        "device_timestamp": 1764453587369,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "timeline_pinned_user_ids": [],
        "is_open_to_public_submission": false,
        "profile_grid_control_enabled": false,
        "can_see_insights_as_brand": false,
        "media_reposter_bottomsheet_enabled": false,
        "coauthor_producer_can_see_organic_insights": false,
        "share_count_disabled": false,
        "is_visual_reply_commenter_notice_enabled": true,
        "should_request_ads": false,
        "subscribe_cta_visible": false,
        "commerce_integrity_review_decision": "",
        "sharing_friction_info": {
          "should_have_sharing_friction": false
        },
        "media_notes": {
          "items": []
        },
        "fb_user_tags": {
          "in": []
        },
        "coauthor_producers": [],
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "cutout_sticker_info": [],
        "invited_coauthor_producers": [],
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "floating_context_items": [],
        "comment_inform_treatment": {
          "should_have_inform_treatment": false,
          "text": ""
        },
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "caption": {
          "strong_id__": "18065011298571522",
          "pk": "18065011298571522",
          "bit_flags": 0,
          "content_type": "comment",
          "created_at": 1764453632,
          "created_at_utc": 1764453632,
          "did_report_as_spam": false,
          "is_covered": false,
          "is_ranked_comment": false,
          "media_id": 3776832898280228145,
          "private_reply_status": 0,
          "share_enabled": false,
          "status": "Active",
          "text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
          "type": 1,
          "user": {
            "id": "787132",
            "pk": 787132,
            "pk_id": "787132",
            "username": "natgeo",
            "full_name": "National Geographic",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3865702555259028436_787132",
            "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/...",
            "fbid_v2": 17841400573960012,
            "is_unpublished": false,
            "strong_id__": "787132"
          },
          "user_id": 787132
        },
        "report_info": {
          "has_viewer_submitted_report": false
        },
        "meta_ai_suggested_prompts": [],
        "user": {
          "id": "787132",
          "pk": 787132,
          "pk_id": "787132",
          "fbid_v2": 17841400573960012,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/...",
          "username": "natgeo",
          "full_name": "National Geographic",
          "is_private": false,
          "is_unpublished": false,
          "is_verified": true,
          "is_ring_creator": false,
          "show_ring_award": false,
          "account_badges": [],
          "account_type": 2,
          "has_anonymous_profile_picture": false,
          "latest_reel_media": 1775659002,
          "is_embeds_disabled": false,
          "strong_id__": "787132",
          "eligible_for_text_app_activation_badge": false,
          "interop_messaging_user_fbid": "113671860027320",
          "show_account_transparency_details": true,
          "transparency_product_enabled": false,
          "third_party_downloads_enabled": 2,
          "feed_post_reshare_disabled": false,
          "is_favorite": false,
          "fan_club_info": {},
          "user_activation_info": {}
        }
      }
    }
  ],
  "metadata": {
    "template_clips_media_creator": "natgeo",
    "clips_count": "1 reel",
    "image_versions2": {
      "additional_candidates": {
        "first_frame": {
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-lga3-1.cdninstagram.com/...",
          "width": 640
        },
        "igtv_first_frame": {
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-lga3-1.cdninstagram.com/...",
          "width": 640
        }
      },
      "candidates": [
        {
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-lga3-2.cdninstagram.com/...",
          "width": 750
        }
      ],
      "scrubber_spritesheet_info_candidates": {
        "default": {
          "file_size_kb": 428,
          "max_thumbnails_per_sprite": 105,
          "rendered_width": 96,
          "sprite_height": 1232,
          "sprite_width": 1500,
          "thumbnail_duration": 0.21250476190476,
          "thumbnail_height": 176,
          "thumbnail_width": 100,
          "thumbnails_per_row": 15,
          "total_thumbnail_num_per_sprite": 105,
          "video_length": 22.313
        }
      }
    },
    "template_title": "Original template"
  },
  "paging_info": {
    "max_id": "GhbilITg1eCA6mgmnK7_4a1nFAI0AikIGAAaCDoGGQwA",
    "more_available": true
  },
  "status": "ok",
  "status_code": "200"
}
```

</details>

---

## Deprecated endpoints

These endpoints are deprecated — use the recommended alternatives. Retired ones respond with **410 Gone** and are never charged (see [Response Codes](../response-codes.md)); the rest still work but will be removed in a future version.

### ~~GET /v2/media/by/code~~

!!! warning
    Prefer using /v2/media/info/by/code as this endpoint will be completely deprecated soon

### ~~GET /v2/media/by/id~~

!!! warning
    Prefer using /v2/media/info/by/id as this endpoint will be completely deprecated soon

### ~~GET /v2/media/by/url~~

!!! warning
    Prefer using /v2/media/info/by/url as this endpoint will be completely deprecated soon

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v2-media){ target=_blank }
