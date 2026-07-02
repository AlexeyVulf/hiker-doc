# Hashtag Endpoints

Get hashtag info and media.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v2/hashtag/by/name`](#get-v2hashtagbyname) | [`/v2/hashtag/medias/recent`](#get-v2hashtagmediasrecent) | [`/v2/hashtag/medias/top`](#get-v2hashtagmediastop)

---

### GET /v2/hashtag/by/name

Get hashtag object by name. Returns a Hashtag object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Name |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/hashtag/by/name?name=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_by_name_v2(name="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/hashtag/by/name",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/hashtag/by/name?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "id": "17843826142012701",
  "name": "love",
  "media_count": 2147483647,
  "allow_muting_story": true,
  "subtitle": null,
  "follow_button_text": null,
  "show_follow_drop_down": false,
  "formatted_media_count": "2.1B",
  "is_trending": false,
  "hide_use_hashtag_button": false,
  "status": "ok",
  "allow_following": false,
  "profile_pic_url": null
}
```

</details>

---

### GET /v2/hashtag/medias/recent

Get hashtag chunk of recent medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Name |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/hashtag/medias/recent?name=love"
    # Next page: add &page_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_recent_v2(name="love")
    # Next page: cl.hashtag_medias_recent_v2(name="love", page_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/hashtag/medias/recent",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"name": "love"},
    )
    # Next page: add "page_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/hashtag/medias/recent?name=love",
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
    "sections": [
      {
        "layout_type": "media_grid",
        "feed_type": "media",
        "explore_item_info": {
          "num_columns": 3,
          "total_num_columns": 3,
          "aspect_ratio": 3.0,
          "autoplay": false
        },
        "layout_content": {
          "medias": [
            {
              "media": {
                "strong_id__": "3870771007451871805_375121505",
                "id": "3870771007451871805_375121505",
                "fbid": 18119849704714197,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDc3MTAwNzQ1MTg3MTgwNQ==.3",
                "integrity_review_decision": "pending",
                "pk": "3870771007451871805",
                "has_delayed_metadata": false,
                "mezql_token": "",
                "should_request_ads": false,
                "has_privately_liked": false,
                "collaborator_edit_eligibility": false,
                "share_count_disabled": false,
                "is_reshare_of_text_post_app_media_in_ig": false,
                "is_visual_reply_commenter_notice_enabled": true,
                "subtype_name_for_REST__": "XDTFeedMedia",
                "has_views_fetching_on_search_grid": false,
                "image_versions2": {
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        11766,
                        23532,
                        35299
                      ],
                      "height": 1101,
                      "scans_profile": "e35",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 1079,
                      "is_spatial_image": false
                    },
                    {
                      "estimated_scans_sizes": [
                        7924,
                        15848,
                        23772
                      ],
                      "height": 765,
                      "scans_profile": "e35",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 750,
                      "is_spatial_image": false
                    }
                  ]
                },
                "media_type": 1,
                "original_width": 1079,
                "original_height": 1101,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMjdiNTIzOWIyZTM0NGVlODkxMzExY2IzZTMzOTA4NDQzODcwNzcxMDA3NDUxODcxODA1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwODU3N3wzODcwNzcxMDA3NDUxODcxODA1fDMxMjMxODEwMDkzfGFkZDMwMTA2ODhjNjA4NTQ1ZjU2NjFjOWIwMDRiNzgxMDljNDNiYjQzN2E1N2RlMDQxMzYwZWZjOWE1YTY4OTAifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": {
                  "audio_type": null,
                  "music_canonical_id": "0",
                  "pinned_media_ids": null,
                  "music_info": null,
                  "original_sound_info": null
                },
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775651897,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
                  "in": []
                },
                "mashup_info": {
                  "can_toggle_mashups_allowed": false,
                  "formatted_mashups_count": null,
                  "has_been_mashed_up": false,
                  "has_nonmimicable_additional_audio": false,
                  "is_creator_requesting_mashup": false,
                  "is_light_weight_check": true,
                  "is_light_weight_reuse_allowed_check": true,
                  "is_pivot_page_available": false,
                  "is_reuse_allowed": false,
                  "mashup_type": null,
                  "mashups_allowed": false,
                  "mashups_allowed_for_carousel": false,
                  "non_privacy_filtered_mashups_media_count": 0,
                  "privacy_filtered_mashups_media_count": null,
                  "original_media": null
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "feed",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": false,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "commerce_integrity_review_decision": "",
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "product_suggestions": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 9,
                "like_count": 416,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18119849740714197",
                  "bit_flags": 0,
                  "created_at": 1775651899,
                  "created_at_utc": 1775651899,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18119849740714197",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870771007451871805,
                  "status": "Active",
                  "type": 1,
                  "user_id": 375121505,
                  "text": "Disney Princess irl",
                  "user": {
                    "strong_id__": "375121505",
                    "pk": 375121505,
                    "pk_id": "375121505",
                    "id": "375121505",
                    "is_unpublished": false,
                    "fbid_v2": 17841400525155861,
                    "username": "fallinginsociety",
                    "full_name": "FallingInSociety",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "1408922974837077103_375121505",
                    "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 5,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "shop_routing_user_id": null,
                "featured_products": [],
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "375121505",
                  "id": "375121505",
                  "username": "fallinginsociety",
                  "full_name": "FallingInSociety",
                  "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW3vbkaDLo9",
                "device_timestamp": 1775651897,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
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
                "is_comments_gif_composer_enabled": true,
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      11766,
                      23532,
                      35299
                    ],
                    "height": 1101,
                    "scans_profile": "e35",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 1079,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775651897,
                "sponsor_tags": [],
                "play_count": 0
              }
            },
            {
              "media": {
                "strong_id__": "3870855071546483116_375121505",
                "id": "3870855071546483116_375121505",
                "fbid": 18016114664675409,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDg1NTA3MTU0NjQ4MzExNg==.3",
                "integrity_review_decision": "pending",
                "pk": "3870855071546483116",
                "has_delayed_metadata": false,
                "mezql_token": "",
                "should_request_ads": false,
                "has_privately_liked": false,
                "collaborator_edit_eligibility": false,
                "share_count_disabled": false,
                "is_reshare_of_text_post_app_media_in_ig": false,
                "is_visual_reply_commenter_notice_enabled": true,
                "subtype_name_for_REST__": "XDTFeedMedia",
                "has_views_fetching_on_search_grid": false,
                "image_versions2": {
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        11957,
                        23915,
                        35873
                      ],
                      "height": 1440,
                      "scans_profile": "e35",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 1440,
                      "is_spatial_image": false
                    },
                    {
                      "estimated_scans_sizes": [
                        5887,
                        11774,
                        17661
                      ],
                      "height": 750,
                      "scans_profile": "e35",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 750,
                      "is_spatial_image": false
                    }
                  ]
                },
                "media_type": 1,
                "original_width": 1440,
                "original_height": 1440,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMjdiNTIzOWIyZTM0NGVlODkxMzExY2IzZTMzOTA4NDQzODcwODU1MDcxNTQ2NDgzMTE2Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwODYxNnwzODcwODU1MDcxNTQ2NDgzMTE2fDMxMjMxODEwMDkzfDk5NjU2YmFkNzdjY2EwZTQ0OWJmMTM1OWExN2QwNGY1OWU4MDQ5NTQ2MWI2MjMxNzUyMDkxMzBmNzQ4NmE3YWYifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": {
                  "audio_type": null,
                  "music_canonical_id": "0",
                  "pinned_media_ids": null,
                  "music_info": null,
                  "original_sound_info": null
                },
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775661908,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
                  "in": []
                },
                "mashup_info": {
                  "can_toggle_mashups_allowed": false,
                  "formatted_mashups_count": null,
                  "has_been_mashed_up": false,
                  "has_nonmimicable_additional_audio": false,
                  "is_creator_requesting_mashup": false,
                  "is_light_weight_check": true,
                  "is_light_weight_reuse_allowed_check": true,
                  "is_pivot_page_available": false,
                  "is_reuse_allowed": false,
                  "mashup_type": null,
                  "mashups_allowed": false,
                  "mashups_allowed_for_carousel": false,
                  "non_privacy_filtered_mashups_media_count": 0,
                  "privacy_filtered_mashups_media_count": null,
                  "original_media": null
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "feed",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": false,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "commerce_integrity_review_decision": "",
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "product_suggestions": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 12,
                "like_count": 325,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18016114685675409",
                  "bit_flags": 0,
                  "created_at": 1775661910,
                  "created_at_utc": 1775661910,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18016114685675409",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870855071546483116,
                  "status": "Active",
                  "type": 1,
                  "user_id": 375121505,
                  "text": "24 year olds deserve it",
                  "user": {
                    "strong_id__": "375121505",
                    "pk": 375121505,
                    "pk_id": "375121505",
                    "id": "375121505",
                    "is_unpublished": false,
                    "fbid_v2": 17841400525155861,
                    "username": "fallinginsociety",
                    "full_name": "FallingInSociety",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "1408922974837077103_375121505",
                    "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 3,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "shop_routing_user_id": null,
                "featured_products": [],
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "375121505",
                  "id": "375121505",
                  "username": "fallinginsociety",
                  "full_name": "FallingInSociety",
                  "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW4Ci3MjCGs",
                "device_timestamp": 1775661908,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
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
                "is_comments_gif_composer_enabled": true,
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      11957,
                      23915,
                      35873
                    ],
                    "height": 1440,
                    "scans_profile": "e35",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 1440,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775661908,
                "sponsor_tags": [],
                "play_count": 0
              }
            },
            {
              "media": {
                "strong_id__": "3870787133267296530_9816762",
                "id": "3870787133267296530_9816762",
                "fbid": 18099141781817244,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDc4NzEzMzI2NzI5NjUzMA==.3",
                "integrity_review_decision": "pending",
                "pk": "3870787133267296530",
                "has_delayed_metadata": false,
                "mezql_token": "",
                "should_request_ads": false,
                "has_privately_liked": false,
                "collaborator_edit_eligibility": false,
                "share_count_disabled": false,
                "is_reshare_of_text_post_app_media_in_ig": false,
                "is_visual_reply_commenter_notice_enabled": true,
                "subtype_name_for_REST__": "XDTFeedMedia",
                "has_views_fetching_on_search_grid": false,
                "image_versions2": {
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        9548,
                        19097,
                        28646
                      ],
                      "height": 1350,
                      "scans_profile": "e35",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 1080,
                      "is_spatial_image": false
                    },
                    {
                      "estimated_scans_sizes": [
                        6427,
                        12854,
                        19282
                      ],
                      "height": 938,
                      "scans_profile": "e35",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 750,
                      "is_spatial_image": false
                    }
                  ]
                },
                "media_type": 1,
                "original_width": 1080,
                "original_height": 1350,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMjdiNTIzOWIyZTM0NGVlODkxMzExY2IzZTMzOTA4NDQzODcwNzg3MTMzMjY3Mjk2NTMwIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwODYxNnwzODcwNzg3MTMzMjY3Mjk2NTMwfDMxMjMxODEwMDkzfDc2ODczNWI5ODg3NzBlYzlkN2VhZTgzMjdiOGQ4OTA2YmQ2MDQ2ODFmYTliNGJiMzE2ZDJkOThiNDU1YmVhY2IifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": {
                  "audio_type": null,
                  "music_canonical_id": "0",
                  "pinned_media_ids": null,
                  "music_info": null,
                  "original_sound_info": null
                },
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775653818,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
                  "in": []
                },
                "mashup_info": {
                  "can_toggle_mashups_allowed": false,
                  "formatted_mashups_count": null,
                  "has_been_mashed_up": false,
                  "has_nonmimicable_additional_audio": false,
                  "is_creator_requesting_mashup": false,
                  "is_light_weight_check": true,
                  "is_light_weight_reuse_allowed_check": true,
                  "is_pivot_page_available": false,
                  "is_reuse_allowed": false,
                  "mashup_type": null,
                  "mashups_allowed": false,
                  "mashups_allowed_for_carousel": false,
                  "non_privacy_filtered_mashups_media_count": 0,
                  "privacy_filtered_mashups_media_count": null,
                  "original_media": null
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "feed",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": false,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "commerce_integrity_review_decision": "",
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "product_suggestions": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 3,
                "like_count": 297,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18099141814817244",
                  "bit_flags": 0,
                  "created_at": 1775653820,
                  "created_at_utc": 1775653820,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18099141814817244",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870787133267296530,
                  "status": "Active",
                  "type": 1,
                  "user_id": 9816762,
                  "text": "the greatest human experience",
                  "user": {
                    "strong_id__": "9816762",
                    "pk": 9816762,
                    "pk_id": "9816762",
                    "id": "9816762",
                    "is_unpublished": false,
                    "fbid_v2": 17841400742860153,
                    "username": "nocap",
                    "full_name": "No Cap",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "2322865363225008074_9816762",
                    "profile_pic_url": "https://instagram.ftia13-1.fna.fbcdn.net/v/t51.2885-19/101552390_208306300166690_2852990751455838208_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=instagram.ftia13-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gHuxMmG5eWOFWR6MdjkGtC4rOVAIWHAlIzZ8CJ2g9w2TUdQ3SklFxRJoDjWxm2z53E&_nc_ohc=ytvnVM-Wer4Q7kNvwFHfysb&_nc_gid=IkdNGG7Wp88j1l4eqfa9DA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GAaRDQYiogYXdL0AAAAAAAD525cnbkULAAAB1501500j-ccb7-5&oh=00_Af1bFIR144rHpoRwdhTpp1dLntB3ciCg49Zg1pTICiMl0w&oe=69DC6F17&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 3,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "shop_routing_user_id": null,
                "featured_products": [],
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "9816762",
                  "id": "9816762",
                  "username": "nocap",
                  "full_name": "No Cap",
                  "profile_pic_url": "https://instagram.ftia13-1.fna.fbcdn.net/v/t51.2885-19/101552390_208306300166690_2852990751455838208_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=instagram.ftia13-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gHuxMmG5eWOFWR6MdjkGtC4rOVAIWHAlIzZ8CJ2g9w2TUdQ3SklFxRJoDjWxm2z53E&_nc_ohc=ytvnVM-Wer4Q7kNvwFHfysb&_nc_gid=IkdNGG7Wp88j1l4eqfa9DA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GAaRDQYiogYXdL0AAAAAAAD525cnbkULAAAB1501500j-ccb7-5&oh=00_Af1bFIR144rHpoRwdhTpp1dLntB3ciCg49Zg1pTICiMl0w&oe=69DC6F17&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW3zGOvjMES",
                "device_timestamp": 1775653818,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
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
                "is_comments_gif_composer_enabled": true,
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      9548,
                      19097,
                      28646
                    ],
                    "height": 1350,
                    "scans_profile": "e35",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 1080,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775653818,
                "sponsor_tags": [],
                "play_count": 0
              }
            }
          ]
        }
      },
      {
        "layout_type": "media_grid",
        "feed_type": "media",
        "explore_item_info": {
          "num_columns": 3,
          "total_num_columns": 3,
          "aspect_ratio": 3.0,
          "autoplay": false
        },
        "layout_content": {
          "medias": [
            {
              "media": {
                "strong_id__": "3870865595181294610_68182096424",
                "id": "3870865595181294610_68182096424",
                "disable_caption_and_comment": false,
                "fbid": 18088269698248526,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDg2NTU5NTE4MTI5NDYxMA==.3",
                "integrity_review_decision": "pending",
                "pk": "3870865595181294610",
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
                "is_third_party_downloads_eligible": true,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "estimated_scans_sizes": [
                        3420,
                        6841,
                        10261
                      ],
                      "height": 1138,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        3420,
                        6841,
                        10261
                      ],
                      "height": 1138,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        3420,
                        6841,
                        10261
                      ],
                      "height": 1138,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    }
                  ]
                },
                "media_type": 2,
                "original_width": 1076,
                "original_height": 1920,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMjdiNTIzOWIyZTM0NGVlODkxMzExY2IzZTMzOTA4NDQzODcwODY1NTk1MTgxMjk0NjEwIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwODYxNnwzODcwODY1NTk1MTgxMjk0NjEwfDMxMjMxODEwMDkzfGUzYmQwMzAyNGMzOWFkN2E0MzQyZDdhNDkwNzFiYzA4ZTRkODliZWU2OTI4NTkwNDYwNmNkYjUyYTUxMTZmYjkifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": false,
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775663284,
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
                "subscribe_cta_visible": false,
                "creative_config": {
                  "capture_type": "clips_v2",
                  "face_effect_id": null,
                  "failure_reason": null,
                  "attribution_user": null,
                  "creation_tool_info": [
                    {
                      "camera_tool": 97,
                      "duration_selector_seconds": 0,
                      "speed_selector": 0.0,
                      "color_filters": "",
                      "appearance_effect": 0,
                      "timer_selector_seconds": 0,
                      "magic_cut_start_time": 0.0,
                      "magic_cut_end_time": 0.0,
                      "effect_filter_name": ""
                    }
                  ],
                  "effect_configs": null,
                  "effect_preview": null,
                  "gen_ai_tool_info": null
                },
                "is_cutout_sticker_allowed": true,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 0,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 132,
                "like_count": 668,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18088269794248526",
                  "bit_flags": 0,
                  "created_at": 1775663285,
                  "created_at_utc": 1775663285,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18088269794248526",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870865595181294610,
                  "status": "Active",
                  "type": 1,
                  "user_id": 68182096424,
                  "has_translation": true,
                  "text": "Madam ji... Apke liye 2 line...🫶💝#dailymotivation #love #reelkarofeelkaro #sigma #video",
                  "user": {
                    "strong_id__": "68182096424",
                    "pk": 68182096424,
                    "pk_id": "68182096424",
                    "id": "68182096424",
                    "is_unpublished": false,
                    "fbid_v2": 17841468172722762,
                    "username": "pal_boy_krish_pal",
                    "full_name": "Sad 🥺 shayar 💔🥀",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3823783874106829968_68182096424",
                    "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 71,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "location": {
                  "pk": 235082047414982,
                  "name": "India : इंडिया",
                  "phone": "",
                  "website": "",
                  "category": "",
                  "hours": {},
                  "address": "",
                  "city": "",
                  "zip": null,
                  "lng": null,
                  "lat": null,
                  "external_id": "235082047414982",
                  "external_id_source": "facebook_places"
                },
                "locations": [],
                "play_count": 18556,
                "ig_play_count": 18556,
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
                "video_duration": 9.241000175476074,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 186744,
                    "height": 1280,
                    "id": "1268915285206999v",
                    "type": 101,
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "url_expiration_timestamp_us": null,
                    "width": 716,
                    "fallback": null
                  }
                ],
                "number_of_qualities": 4,
                "video_codec": "vp09.00.21.08.00.01.01.01.00",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "SELF_DISCLOSURE_FLOW"
                },
                "user": {
                  "pk": "68182096424",
                  "id": "68182096424",
                  "username": "pal_boy_krish_pal",
                  "full_name": "Sad 🥺 shayar 💔🥀",
                  "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW4E8AGD-QS",
                "device_timestamp": 827429536203318,
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
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      3420,
                      6841,
                      10261
                    ],
                    "height": 1138,
                    "scans_profile": "e15",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 640,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "usertags": [],
                "taken_at_ts": 1775663284,
                "sponsor_tags": []
              }
            },
            {
              "media": {
                "strong_id__": "3870782423390535263_195373995",
                "id": "3870782423390535263_195373995",
                "disable_caption_and_comment": false,
                "fbid": 18081427487526220,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDc4MjQyMzM5MDUzNTI2Mw==.3",
                "integrity_review_decision": "pending",
                "pk": "3870782423390535263",
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
                "is_third_party_downloads_eligible": true,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "estimated_scans_sizes": [
                        16942,
                        33884,
                        50826
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        16942,
                        33884,
                        50826
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        16942,
                        33884,
                        50826
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 459,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_urls": [
                        "https://scontent-otp1-1.cdninstagram.com/v/t51.71878-15/660790857_2373665619822205_8380873781116494925_n.jpg?_nc_ht=scontent-otp1-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gHuxMmG5eWOFWR6MdjkGtC4rOVAIWHAlIzZ8CJ2g9w2TUdQ3SklFxRJoDjWxm2z53E&_nc_ohc=dFTh4bF9nbYQ7kNvwHqE8Sj&_nc_gid=IkdNGG7Wp88j1l4eqfa9DA&edm=AMKDjl4BAAAA&ccb=7-5&oh=00_Af1Ag6FnMiehsXT9G8jmz7PyW56L-TfwJIyI5OM0ZXTp8w&oe=69DC7932&_nc_sid=472314"
                      ],
                      "sprite_width": 1500,
                      "thumbnail_duration": 0.10698095238095238,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 11.233
                    }
                  }
                },
                "media_type": 2,
                "original_width": 1080,
                "original_height": 1920,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMjdiNTIzOWIyZTM0NGVlODkxMzExY2IzZTMzOTA4NDQzODcwNzgyNDIzMzkwNTM1MjYzIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwODYxNnwzODcwNzgyNDIzMzkwNTM1MjYzfDMxMjMxODEwMDkzfGI5YWUxNmIwMGU0NzBkNjk1Njg5YmFlNjczMTY1Mzk5OGY4NDIwN2Y3ZWQ1NWE5MmNiNzYwNmJjMjI1YzBlNmMifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": false,
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775653218,
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
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": true,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 378,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 26,
                "like_count": 520,
                "fb_like_count": 73,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18081431078526220",
                  "bit_flags": 0,
                  "created_at": 1775653219,
                  "created_at_utc": 1775653219,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18081431078526220",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870782423390535263,
                  "status": "Active",
                  "type": 1,
                  "user_id": 195373995,
                  "text": "One day my love ♥️\n•\n•follow @affirmation_mastershop for more ✨\n•\n#relationship #soulmate #love #explore #relatable",
                  "user": {
                    "strong_id__": "195373995",
                    "pk": 195373995,
                    "pk_id": "195373995",
                    "id": "195373995",
                    "is_unpublished": false,
                    "fbid_v2": 17841401379853052,
                    "username": "affirmation_mastershop",
                    "full_name": "•Motivation | Success | Business•",
                    "is_private": false,
                    "is_verified": true,
                    "profile_pic_id": "3269410642393332923_195373995",
                    "profile_pic_url": "https://instagram.ftia13-1.fna.fbcdn.net/v/t51.2885-19/414190123_903159541161175_4561363514804565959_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44NTUuYzIifQ&_nc_ht=instagram.ftia13-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gHuxMmG5eWOFWR6MdjkGtC4rOVAIWHAlIzZ8CJ2g9w2TUdQ3SklFxRJoDjWxm2z53E&_nc_ohc=Cf8vjXcPRNEQ7kNvwGFFddM&_nc_gid=IkdNGG7Wp88j1l4eqfa9DA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GCsKsBjXXKA3azUDAMd3WhfzN00-bkULAAAB1501500j-ccb7-5&oh=00_Af28zA3OgKoxqv0hzo2fxm7udkhaj1AgNr_zMCoRjNdnMg&oe=69DC63B7&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 43,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "fb_comment_count": 3,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "play_count": 12337,
                "ig_play_count": 9360,
                "fb_play_count": 2977,
                "shop_routing_user_id": null,
                "featured_products": [],
                "are_remixes_crosspostable": true,
                "crosspost_metadata": {
                  "is_feedback_aggregated": true,
                  "unified_feedback_enabled": true,
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "is_eligible_for_autodub": false,
                "is_eligible_for_autodub_upsell": false,
                "video_sticker_locales": [],
                "has_audio": true,
                "video_duration": 11.232999801635742,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 1921190,
                    "height": 1280,
                    "id": "4297277253819204v",
                    "type": 101,
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  }
                ],
                "number_of_qualities": 8,
                "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "195373995",
                  "id": "195373995",
                  "username": "affirmation_mastershop",
                  "full_name": "•Motivation | Success | Business•",
                  "profile_pic_url": "https://instagram.ftia13-1.fna.fbcdn.net/v/t51.2885-19/414190123_903159541161175_4561363514804565959_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44NTUuYzIifQ&_nc_ht=instagram.ftia13-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gHuxMmG5eWOFWR6MdjkGtC4rOVAIWHAlIzZ8CJ2g9w2TUdQ3SklFxRJoDjWxm2z53E&_nc_ohc=Cf8vjXcPRNEQ7kNvwGFFddM&_nc_gid=IkdNGG7Wp88j1l4eqfa9DA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GCsKsBjXXKA3azUDAMd3WhfzN00-bkULAAAB1501500j-ccb7-5&oh=00_Af28zA3OgKoxqv0hzo2fxm7udkhaj1AgNr_zMCoRjNdnMg&oe=69DC63B7&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": true
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW3yBsVBL5f",
                "device_timestamp": 1775653218,
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
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      16942,
                      33884,
                      50826
                    ],
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 640,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775653218,
                "sponsor_tags": []
              }
            },
            {
              "media": {
                "strong_id__": "3870860512355504005_65598722808",
                "id": "3870860512355504005_65598722808",
                "disable_caption_and_comment": false,
                "fbid": 17944408656153547,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDg2MDUxMjM1NTUwNDAwNQ==.3",
                "integrity_review_decision": "pending",
                "pk": "3870860512355504005",
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
                "is_third_party_downloads_eligible": true,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "estimated_scans_sizes": [
                        9772,
                        19545,
                        29318
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        9772,
                        19545,
                        29318
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        9693,
                        19386,
                        29079
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 1031,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_urls": [
                        "https://scontent-otp1-1.cdninstagram.com/v/t51.71878-15/669651175_1424386019010433_5155631934091949423_n.jpg?_nc_ht=scontent-otp1-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gHuxMmG5eWOFWR6MdjkGtC4rOVAIWHAlIzZ8CJ2g9w2TUdQ3SklFxRJoDjWxm2z53E&_nc_ohc=dSLnotf1_GAQ7kNvwFWvxVA&_nc_gid=IkdNGG7Wp88j1l4eqfa9DA&edm=AMKDjl4BAAAA&ccb=7-5&oh=00_Af3a-m5Owd3MCpko6S9uod_SQ1RBGPBOnAO68h6TGPyrzw&oe=69DC4C3C&_nc_sid=472314"
                      ],
                      "sprite_width": 1500,
                      "thumbnail_duration": 0.24793333333333334,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 26.033
                    }
                  }
                },
                "media_type": 2,
                "original_width": 1080,
                "original_height": 1920,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMjdiNTIzOWIyZTM0NGVlODkxMzExY2IzZTMzOTA4NDQzODcwODYwNTEyMzU1NTA0MDA1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwODYxNnwzODcwODYwNTEyMzU1NTA0MDA1fDMxMjMxODEwMDkzfDZiZGU2NTNmZGQ3NTFjYTViMDNlMTJkMTg2NGI2MmQ0YTRlZDBiZjVjYTE2Mzg4NzZmNWViOWZiMzZjOGQ5NDYifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": false,
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775662593,
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
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": true,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 0,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 18,
                "like_count": 753,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "17944408788153547",
                  "bit_flags": 0,
                  "created_at": 1775662577,
                  "created_at_utc": 1775662577,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "17944408788153547",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870860512355504005,
                  "status": "Active",
                  "type": 1,
                  "user_id": 65598722808,
                  "text": "Grwm bro #broguy #zen #love #explorepage #explore",
                  "user": {
                    "strong_id__": "65598722808",
                    "pk": 65598722808,
                    "pk_id": "65598722808",
                    "id": "65598722808",
                    "is_unpublished": false,
                    "fbid_v2": 17841465604249840,
                    "username": "calthebaddie",
                    "full_name": "Cal Hegstrom",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3696876429471582434_65598722808",
                    "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 21,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "play_count": 7011,
                "ig_play_count": 7011,
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
                "video_duration": 26.033000946044922,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 2158516,
                    "height": 1280,
                    "id": "796052053563697v",
                    "type": 101,
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  }
                ],
                "number_of_qualities": 8,
                "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "65598722808",
                  "id": "65598722808",
                  "username": "calthebaddie",
                  "full_name": "Cal Hegstrom",
                  "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW4DyCWCU-F",
                "device_timestamp": 1775662548604018,
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
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      9693,
                      19386,
                      29079
                    ],
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 640,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775662593,
                "sponsor_tags": []
              }
            }
          ]
        }
      },
      {
        "layout_type": "media_grid",
        "feed_type": "media",
        "explore_item_info": {
          "num_columns": 3,
          "total_num_columns": 3,
          "aspect_ratio": 3.0,
          "autoplay": false
        },
        "layout_content": {
          "medias": [
            {
              "media": {
                "strong_id__": "3870768642929551615_45214193439",
                "id": "3870768642929551615_45214193439",
                "disable_caption_and_comment": false,
                "fbid": 18085640528032577,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDc2ODY0MjkyOTU1MTYxNQ==.3",
                "integrity_review_decision": "pending",
                "pk": "3870768642929551615",
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
                "is_third_party_downloads_eligible": true,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "estimated_scans_sizes": [
                        3038,
                        6077,
                        9115
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        3038,
                        6077,
                        9115
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        3332,
                        6665,
                        9998
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 516,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_urls": [
                        "https://scontent-otp1-1.cdninstagram.com/v/t51.71878-15/657947687_1455720549621280_2393358861707971551_n.jpg?_nc_ht=scontent-otp1-1.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gHuxMmG5eWOFWR6MdjkGtC4rOVAIWHAlIzZ8CJ2g9w2TUdQ3SklFxRJoDjWxm2z53E&_nc_ohc=F62VzUFmdYEQ7kNvwH0ISFc&_nc_gid=IkdNGG7Wp88j1l4eqfa9DA&edm=AMKDjl4BAAAA&ccb=7-5&oh=00_Af31ikj6W_bolfhcVpCl0S4G1wOW4otllXBpySS-2Xzxbw&oe=69DC5627&_nc_sid=472314"
                      ],
                      "sprite_width": 1500,
                      "thumbnail_duration": 0.2832571428571429,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 29.742
                    }
                  }
                },
                "media_type": 2,
                "original_width": 1080,
                "original_height": 1920,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMjdiNTIzOWIyZTM0NGVlODkxMzExY2IzZTMzOTA4NDQzODcwNzY4NjQyOTI5NTUxNjE1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwODYxNnwzODcwNzY4NjQyOTI5NTUxNjE1fDMxMjMxODEwMDkzfDAwMzIzODliOWU2ZGVjZWEzMzgzZjZiNjJkOTg5ZWRiOTY2MWMxMGY2MjA0MjI1ODEyMzMzZTVmYTk1MzdiODIifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": false,
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775651774,
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
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": true,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "commerce_integrity_review_decision": "",
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 10,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 13,
                "like_count": 1420,
                "fb_like_count": 675,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18085640600032577",
                  "bit_flags": 0,
                  "created_at": 1775651747,
                  "created_at_utc": 1775651747,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18085640600032577",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870768642929551615,
                  "status": "Active",
                  "type": 1,
                  "user_id": 45214193439,
                  "text": "❤️❤️❤️❤️jogi\n#instagram #trending #reels #love #reelitfeelit",
                  "user": {
                    "strong_id__": "45214193439",
                    "pk": 45214193439,
                    "pk_id": "45214193439",
                    "id": "45214193439",
                    "is_unpublished": false,
                    "fbid_v2": 17841445163181774,
                    "username": "bhoomika.ammu_official",
                    "full_name": "Roopa Ammu",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3853964456246227603_45214193439",
                    "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 19,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "fb_comment_count": 1,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "play_count": 16550,
                "ig_play_count": 10652,
                "fb_play_count": 5898,
                "shop_routing_user_id": null,
                "featured_products": [],
                "are_remixes_crosspostable": true,
                "crosspost_metadata": {
                  "is_feedback_aggregated": true,
                  "unified_feedback_enabled": true,
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "is_eligible_for_autodub": false,
                "is_eligible_for_autodub_upsell": false,
                "video_sticker_locales": [],
                "has_audio": true,
                "video_duration": 29.743999481201172,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 1477734,
                    "height": 1280,
                    "id": "2146509629455334v",
                    "type": 101,
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  }
                ],
                "number_of_qualities": 8,
                "video_codec": "av01.0.04M.08.0.111.01.01.01.0",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "45214193439",
                  "id": "45214193439",
                  "username": "bhoomika.ammu_official",
                  "full_name": "Roopa Ammu",
                  "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW3u5KRiWj_",
                "device_timestamp": 1775651593655136,
                "enable_media_notes_production": true,
                "filter_type": 810,
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
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      3332,
                      6665,
                      9998
                    ],
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 640,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775651774,
                "sponsor_tags": []
              }
            },
            {
              "media": {
                "strong_id__": "3870796725951067838_33660754057",
                "id": "3870796725951067838_33660754057",
                "disable_caption_and_comment": false,
                "fbid": 17993747885945714,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDc5NjcyNTk1MTA2NzgzOA==.3",
                "integrity_review_decision": "pending",
                "pk": "3870796725951067838",
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
                "is_third_party_downloads_eligible": true,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "estimated_scans_sizes": [
                        1347,
                        2695,
                        4042
                      ],
                      "height": 320,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        1347,
                        2695,
                        4042
                      ],
                      "height": 320,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        4891,
                        9782,
                        14674
                      ],
                      "height": 960,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 540,
                      "is_spatial_image": false
                    }
                  ]
                },
                "media_type": 2,
                "original_width": 1920,
                "original_height": 960,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMjdiNTIzOWIyZTM0NGVlODkxMzExY2IzZTMzOTA4NDQzODcwNzk2NzI1OTUxMDY3ODM4Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwODYxNnwzODcwNzk2NzI1OTUxMDY3ODM4fDMxMjMxODEwMDkzfDA0Nzk3Njg1NmFhNGFlZGE1ZWNlNGMzMjY0MjQzNWZiNjRkNGQzM2UyMTQ4YTZlN2M4ODE3Njc1NmJmYzRhMjYifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": false,
                "clips_tab_pinned_user_ids": [],
                "original_lang_for_translations": "pt",
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775655099,
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
                "subscribe_cta_visible": false,
                "creative_config": {
                  "capture_type": "clips_v2",
                  "face_effect_id": null,
                  "failure_reason": null,
                  "attribution_user": null,
                  "creation_tool_info": [
                    {
                      "camera_tool": 179,
                      "duration_selector_seconds": 0,
                      "speed_selector": 0.0,
                      "color_filters": "",
                      "appearance_effect": 0,
                      "timer_selector_seconds": 0,
                      "magic_cut_start_time": 0.0,
                      "magic_cut_end_time": 0.0,
                      "effect_filter_name": ""
                    },
                    {
                      "camera_tool": 97,
                      "duration_selector_seconds": 0,
                      "speed_selector": 0.0,
                      "color_filters": "",
                      "appearance_effect": 0,
                      "timer_selector_seconds": 0,
                      "magic_cut_start_time": 0.0,
                      "magic_cut_end_time": 0.0,
                      "effect_filter_name": ""
                    }
                  ],
                  "effect_configs": null,
                  "effect_preview": null,
                  "gen_ai_tool_info": null
                },
                "is_cutout_sticker_allowed": true,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 2,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 17,
                "like_count": 326,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "17993748008945714",
                  "bit_flags": 0,
                  "created_at": 1775655099,
                  "created_at_utc": 1775655099,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "17993748008945714",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870796725951067838,
                  "status": "Active",
                  "type": 1,
                  "user_id": 33660754057,
                  "has_translation": true,
                  "text": "Diário de uma Paixão (2004) prova que o tempo é o maior teste para o coracão Rvan Gosling e Rachel McAdams entregam uma química avassaladora como Noah e Allie, um casal separado pelas convenções sociais, mas unido por uma promessa que nem a distância, nem os anos conseguiram apagar. A direção de Nick Cassavetes transforma uma história de amor clássica em um estudo sobre a persistência da memória.\n\nO filme brilha ao mostrar que o amor verdadeiro não é apenas o fogo da iuventude, mas a escolha consciente de ficar, mesmo quando a mente começa a falhar. É uma obra emocionante que redefine o romance no cinema, merqulhando na alma de quem descobriu que, para certas conexões uma vida inteira ainda é pouco tempo. Uma licão de que o final de uma história pode ser tão bonito quanto o seu começo, desde que haja alguém para lê-la até o fim.\n.\n.\n.\n.\n.\n.\n#viral #reels #movies #love #explore",
                  "user": {
                    "strong_id__": "33660754057",
                    "pk": 33660754057,
                    "pk_id": "33660754057",
                    "id": "33660754057",
                    "is_unpublished": false,
                    "fbid_v2": 17841433661717594,
                    "username": "eodougllas",
                    "full_name": "D o u g l l a s",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3869675747422632731_33660754057",
                    "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 0,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "play_count": 2713,
                "ig_play_count": 2713,
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
                "video_subtitles_locale": "pt_BR",
                "video_sticker_locales": [],
                "has_audio": false,
                "video_duration": 60.0,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 0,
                    "height": 640,
                    "id": "2343379642794618v",
                    "type": 101,
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "url_expiration_timestamp_us": null,
                    "width": 1280,
                    "fallback": null
                  }
                ],
                "number_of_qualities": 8,
                "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "33660754057",
                  "id": "33660754057",
                  "username": "eodougllas",
                  "full_name": "D o u g l l a s",
                  "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW31R0oDva-",
                "device_timestamp": 40212274733240,
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
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      4891,
                      9782,
                      14674
                    ],
                    "height": 960,
                    "scans_profile": "e15",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 540,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775655099,
                "sponsor_tags": []
              }
            },
            {
              "media": {
                "strong_id__": "3870810258406906459_80079293147",
                "id": "3870810258406906459_80079293147",
                "disable_caption_and_comment": false,
                "fbid": 18436508572141899,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDgxMDI1ODQwNjkwNjQ1OQ==.3",
                "integrity_review_decision": "pending",
                "pk": "3870810258406906459",
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
                "is_third_party_downloads_eligible": true,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "estimated_scans_sizes": [
                        7312,
                        14624,
                        21937
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        7312,
                        14624,
                        21937
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        7312,
                        14624,
                        21937
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 788,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_urls": [
                        "https://scontent-otp1-1.cdninstagram.com/v/t51.71878-15/659803182_1238999864981400_5274167123944012537_n.jpg?_nc_ht=scontent-otp1-1.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gHuxMmG5eWOFWR6MdjkGtC4rOVAIWHAlIzZ8CJ2g9w2TUdQ3SklFxRJoDjWxm2z53E&_nc_ohc=c5P3bzW8GB8Q7kNvwFfC1sT&_nc_gid=IkdNGG7Wp88j1l4eqfa9DA&edm=AMKDjl4BAAAA&ccb=7-5&oh=00_Af1aE8YF5IyMs2nwsVqUpNhfIPL_ojU3vqC_S4goj1ZQzQ&oe=69DC7960&_nc_sid=472314"
                      ],
                      "sprite_width": 1500,
                      "thumbnail_duration": 0.1634952380952381,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 17.167
                    }
                  }
                },
                "media_type": 2,
                "original_width": 1080,
                "original_height": 1920,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMjdiNTIzOWIyZTM0NGVlODkxMzExY2IzZTMzOTA4NDQzODcwODEwMjU4NDA2OTA2NDU5Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwODYxNnwzODcwODEwMjU4NDA2OTA2NDU5fDMxMjMxODEwMDkzfGUyMWYzZDEwZDcyMGQxODgwNWYwMTQ2Mzc2NjUwYTRmZTlmZDExYWFhOGRiMmRjZTRjZjc0YWUxMmQ3YTEzODIifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": true,
                "clips_tab_pinned_user_ids": [],
                "original_lang_for_translations": "en",
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775656758,
                "photo_of_you": false,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [
                  {
                    "strong_id__": "6441686607",
                    "pk": 6441686607,
                    "pk_id": "6441686607",
                    "id": "6441686607",
                    "username": "hiba_jarvas",
                    "full_name": "Hiba jarvas",
                    "is_private": true,
                    "is_verified": false,
                    "profile_pic_id": "2774810643774319018_6441686607",
                    "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
                  }
                ],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "collab_follow_button_info": {
                  "show_follow_button": true,
                  "is_owner_in_author_exp": true
                },
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 65,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 5,
                "like_count": 616,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18436508806141899",
                  "bit_flags": 0,
                  "created_at": 1775656748,
                  "created_at_utc": 1775656748,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18436508806141899",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870810258406906459,
                  "status": "Active",
                  "type": 1,
                  "user_id": 80079293147,
                  "text": "Our first home🥹🤍. #father #love #reelviral #instgram #fyp",
                  "user": {
                    "strong_id__": "80079293147",
                    "pk": 80079293147,
                    "pk_id": "80079293147",
                    "id": "80079293147",
                    "is_unpublished": false,
                    "fbid_v2": 17841480074429911,
                    "username": "_moments.by.me_",
                    "full_name": "Rieewww",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3822356453873874657_80079293147",
                    "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 12,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "play_count": 13233,
                "ig_play_count": 13233,
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
                "video_duration": 17.180999755859375,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 1532780,
                    "height": 1280,
                    "id": "2147343469371331v",
                    "type": 101,
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  }
                ],
                "number_of_qualities": 8,
                "video_codec": "av01.0.04M.08.0.111.01.01.01.0",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "80079293147",
                  "id": "80079293147",
                  "username": "_moments.by.me_",
                  "full_name": "Rieewww",
                  "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW34WvtSBpb",
                "device_timestamp": 1775656559419070,
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
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      7312,
                      14624,
                      21937
                    ],
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 640,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775656758,
                "sponsor_tags": []
              }
            }
          ]
        }
      }
    ],
    "more_available": true,
    "next_max_id": "ae7c32cce452410cbd2772595ff4f094",
    "next_page": 1,
    "next_media_ids": [],
    "auto_load_more_enabled": true,
    "status": "ok"
  },
  "next_page_id": "WyJhZTdjMzJjY2U0NTI0MTBjYmQyNzcyNTk1ZmY0ZjA5NCIsW10sMV0="
}
```

</details>

---

### GET /v2/hashtag/medias/top

Get hashtag chunk of top medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Name |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/hashtag/medias/top?name=love"
    # Next page: add &page_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_top_v2(name="love")
    # Next page: cl.hashtag_medias_top_v2(name="love", page_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/hashtag/medias/top",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"name": "love"},
    )
    # Next page: add "page_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/hashtag/medias/top?name=love",
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
    "sections": [
      {
        "layout_type": "media_grid",
        "feed_type": "media",
        "explore_item_info": {
          "num_columns": 3,
          "total_num_columns": 3,
          "aspect_ratio": 3.0,
          "autoplay": false
        },
        "layout_content": {
          "medias": [
            {
              "media": {
                "strong_id__": "3870771007451871805_375121505",
                "id": "3870771007451871805_375121505",
                "fbid": 18119849704714197,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDc3MTAwNzQ1MTg3MTgwNQ==.3",
                "integrity_review_decision": "pending",
                "pk": "3870771007451871805",
                "has_delayed_metadata": false,
                "mezql_token": "",
                "should_request_ads": false,
                "has_privately_liked": false,
                "collaborator_edit_eligibility": false,
                "share_count_disabled": false,
                "is_reshare_of_text_post_app_media_in_ig": false,
                "is_visual_reply_commenter_notice_enabled": true,
                "subtype_name_for_REST__": "XDTFeedMedia",
                "has_views_fetching_on_search_grid": false,
                "image_versions2": {
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        11766,
                        23532,
                        35299
                      ],
                      "height": 1101,
                      "scans_profile": "e35",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 1079,
                      "is_spatial_image": false
                    },
                    {
                      "estimated_scans_sizes": [
                        7924,
                        15848,
                        23772
                      ],
                      "height": 765,
                      "scans_profile": "e35",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 750,
                      "is_spatial_image": false
                    }
                  ]
                },
                "media_type": 1,
                "original_width": 1079,
                "original_height": 1101,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiOTg3NzM3NWVlMjU3NDk0YjgwNDliZjAzMGJlNjVkZGEzODcwNzcxMDA3NDUxODcxODA1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwNDc4NHwzODcwNzcxMDA3NDUxODcxODA1fDMxMjMxODEwMDkzfDU2ZDFhMGY2N2UzZDllNGFjMDZiNDFmYWJkMjU5ZGY5YjBhYjc2MDQ2NmMwMjIwNjNkZGY3NDA5MzJjMDNkYTIifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": {
                  "audio_type": null,
                  "music_canonical_id": "0",
                  "pinned_media_ids": null,
                  "music_info": null,
                  "original_sound_info": null
                },
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775651897,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
                  "in": []
                },
                "mashup_info": {
                  "can_toggle_mashups_allowed": false,
                  "formatted_mashups_count": null,
                  "has_been_mashed_up": false,
                  "has_nonmimicable_additional_audio": false,
                  "is_creator_requesting_mashup": false,
                  "is_light_weight_check": true,
                  "is_light_weight_reuse_allowed_check": true,
                  "is_pivot_page_available": false,
                  "is_reuse_allowed": false,
                  "mashup_type": null,
                  "mashups_allowed": false,
                  "mashups_allowed_for_carousel": false,
                  "non_privacy_filtered_mashups_media_count": 0,
                  "privacy_filtered_mashups_media_count": null,
                  "original_media": null
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "feed",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": false,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "commerce_integrity_review_decision": "",
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "product_suggestions": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 9,
                "like_count": 416,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18119849740714197",
                  "bit_flags": 0,
                  "created_at": 1775651899,
                  "created_at_utc": 1775651899,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18119849740714197",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870771007451871805,
                  "status": "Active",
                  "type": 1,
                  "user_id": 375121505,
                  "text": "Disney Princess irl",
                  "user": {
                    "strong_id__": "375121505",
                    "pk": 375121505,
                    "pk_id": "375121505",
                    "id": "375121505",
                    "is_unpublished": false,
                    "fbid_v2": 17841400525155861,
                    "username": "fallinginsociety",
                    "full_name": "FallingInSociety",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "1408922974837077103_375121505",
                    "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 5,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "shop_routing_user_id": null,
                "featured_products": [],
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "375121505",
                  "id": "375121505",
                  "username": "fallinginsociety",
                  "full_name": "FallingInSociety",
                  "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW3vbkaDLo9",
                "device_timestamp": 1775651897,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
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
                "is_comments_gif_composer_enabled": true,
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      11766,
                      23532,
                      35299
                    ],
                    "height": 1101,
                    "scans_profile": "e35",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 1079,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775651897,
                "sponsor_tags": [],
                "play_count": 0
              }
            },
            {
              "media": {
                "strong_id__": "3870855071546483116_375121505",
                "id": "3870855071546483116_375121505",
                "fbid": 18016114664675409,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDg1NTA3MTU0NjQ4MzExNg==.3",
                "integrity_review_decision": "pending",
                "pk": "3870855071546483116",
                "has_delayed_metadata": false,
                "mezql_token": "",
                "should_request_ads": false,
                "has_privately_liked": false,
                "collaborator_edit_eligibility": false,
                "share_count_disabled": false,
                "is_reshare_of_text_post_app_media_in_ig": false,
                "is_visual_reply_commenter_notice_enabled": true,
                "subtype_name_for_REST__": "XDTFeedMedia",
                "has_views_fetching_on_search_grid": false,
                "image_versions2": {
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        11957,
                        23915,
                        35873
                      ],
                      "height": 1440,
                      "scans_profile": "e35",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 1440,
                      "is_spatial_image": false
                    },
                    {
                      "estimated_scans_sizes": [
                        5887,
                        11774,
                        17661
                      ],
                      "height": 750,
                      "scans_profile": "e35",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 750,
                      "is_spatial_image": false
                    }
                  ]
                },
                "media_type": 1,
                "original_width": 1440,
                "original_height": 1440,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiOTg3NzM3NWVlMjU3NDk0YjgwNDliZjAzMGJlNjVkZGEzODcwODU1MDcxNTQ2NDgzMTE2Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwNDg0NHwzODcwODU1MDcxNTQ2NDgzMTE2fDMxMjMxODEwMDkzfGMyZGU4M2Q0OTQ5MWQxZTY2YTY4NjA5NTMwM2RkMDNhNzJmMTk3YTJkM2NjODRkNjc3ZDNmYTNiZDAyYWQxZDMifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": {
                  "audio_type": null,
                  "music_canonical_id": "0",
                  "pinned_media_ids": null,
                  "music_info": null,
                  "original_sound_info": null
                },
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775661908,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
                  "in": []
                },
                "mashup_info": {
                  "can_toggle_mashups_allowed": false,
                  "formatted_mashups_count": null,
                  "has_been_mashed_up": false,
                  "has_nonmimicable_additional_audio": false,
                  "is_creator_requesting_mashup": false,
                  "is_light_weight_check": true,
                  "is_light_weight_reuse_allowed_check": true,
                  "is_pivot_page_available": false,
                  "is_reuse_allowed": false,
                  "mashup_type": null,
                  "mashups_allowed": false,
                  "mashups_allowed_for_carousel": false,
                  "non_privacy_filtered_mashups_media_count": 0,
                  "privacy_filtered_mashups_media_count": null,
                  "original_media": null
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "feed",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": false,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "commerce_integrity_review_decision": "",
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "product_suggestions": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 12,
                "like_count": 325,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18016114685675409",
                  "bit_flags": 0,
                  "created_at": 1775661910,
                  "created_at_utc": 1775661910,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18016114685675409",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870855071546483116,
                  "status": "Active",
                  "type": 1,
                  "user_id": 375121505,
                  "text": "24 year olds deserve it",
                  "user": {
                    "strong_id__": "375121505",
                    "pk": 375121505,
                    "pk_id": "375121505",
                    "id": "375121505",
                    "is_unpublished": false,
                    "fbid_v2": 17841400525155861,
                    "username": "fallinginsociety",
                    "full_name": "FallingInSociety",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "1408922974837077103_375121505",
                    "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 3,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "shop_routing_user_id": null,
                "featured_products": [],
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "375121505",
                  "id": "375121505",
                  "username": "fallinginsociety",
                  "full_name": "FallingInSociety",
                  "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW4Ci3MjCGs",
                "device_timestamp": 1775661908,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
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
                "is_comments_gif_composer_enabled": true,
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      11957,
                      23915,
                      35873
                    ],
                    "height": 1440,
                    "scans_profile": "e35",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 1440,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775661908,
                "sponsor_tags": [],
                "play_count": 0
              }
            },
            {
              "media": {
                "strong_id__": "3870860512355504005_65598722808",
                "id": "3870860512355504005_65598722808",
                "disable_caption_and_comment": false,
                "fbid": 17944408656153547,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDg2MDUxMjM1NTUwNDAwNQ==.3",
                "integrity_review_decision": "pending",
                "pk": "3870860512355504005",
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
                "is_third_party_downloads_eligible": true,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "estimated_scans_sizes": [
                        9772,
                        19545,
                        29318
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        9772,
                        19545,
                        29318
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        9693,
                        19386,
                        29079
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 1031,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_urls": [
                        "https://scontent-otp1-1.cdninstagram.com/v/t51.71878-15/669651175_1424386019010433_5155631934091949423_n.jpg?_nc_ht=scontent-otp1-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gHwR0z5-6Mti7yguikxBt2B8wv46H_AckcN_i8ps7w3R4hh-jGnQjsTvHyR3ESFZhg&_nc_ohc=dSLnotf1_GAQ7kNvwFWvxVA&_nc_gid=qsT5lUUkJDxaTYEgqW_Ntw&edm=AMKDjl4BAAAA&ccb=7-5&oh=00_Af3-6_ty82iYhYWlCxb31mupMYdndO027D-csCHqn6n91A&oe=69DC4C3C&_nc_sid=472314"
                      ],
                      "sprite_width": 1500,
                      "thumbnail_duration": 0.24793333333333334,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 26.033
                    }
                  }
                },
                "media_type": 2,
                "original_width": 1080,
                "original_height": 1920,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiOTg3NzM3NWVlMjU3NDk0YjgwNDliZjAzMGJlNjVkZGEzODcwODYwNTEyMzU1NTA0MDA1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwNDg0NHwzODcwODYwNTEyMzU1NTA0MDA1fDMxMjMxODEwMDkzfDcwNDg4OTM0YTI5YzA5Njg0ODQ0YzJiMzliNmE2N2YyNjU4ODdkZGQ4ODQ3YWUwYzhkZWY0YmNkMmI3OWNhNmEifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": false,
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775662593,
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
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": true,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 0,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 18,
                "like_count": 753,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "17944408788153547",
                  "bit_flags": 0,
                  "created_at": 1775662577,
                  "created_at_utc": 1775662577,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "17944408788153547",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870860512355504005,
                  "status": "Active",
                  "type": 1,
                  "user_id": 65598722808,
                  "text": "Grwm bro #broguy #zen #love #explorepage #explore",
                  "user": {
                    "strong_id__": "65598722808",
                    "pk": 65598722808,
                    "pk_id": "65598722808",
                    "id": "65598722808",
                    "is_unpublished": false,
                    "fbid_v2": 17841465604249840,
                    "username": "calthebaddie",
                    "full_name": "Cal Hegstrom",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3696876429471582434_65598722808",
                    "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 21,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "play_count": 7011,
                "ig_play_count": 7011,
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
                "video_duration": 26.033000946044922,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 2158516,
                    "height": 1280,
                    "id": "796052053563697v",
                    "type": 101,
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  }
                ],
                "number_of_qualities": 8,
                "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "65598722808",
                  "id": "65598722808",
                  "username": "calthebaddie",
                  "full_name": "Cal Hegstrom",
                  "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW4DyCWCU-F",
                "device_timestamp": 1775662548604018,
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
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      9693,
                      19386,
                      29079
                    ],
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 640,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775662593,
                "sponsor_tags": []
              }
            }
          ]
        }
      },
      {
        "layout_type": "media_grid",
        "feed_type": "media",
        "explore_item_info": {
          "num_columns": 3,
          "total_num_columns": 3,
          "aspect_ratio": 3.0,
          "autoplay": false
        },
        "layout_content": {
          "medias": [
            {
              "media": {
                "strong_id__": "3870817376287099396_77482241330",
                "id": "3870817376287099396_77482241330",
                "disable_caption_and_comment": false,
                "fbid": 18097732205024064,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDgxNzM3NjI4NzA5OTM5Ng==.3",
                "integrity_review_decision": "pending",
                "pk": "3870817376287099396",
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
                "is_third_party_downloads_eligible": true,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "estimated_scans_sizes": [
                        16459,
                        32918,
                        49377
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        16459,
                        32918,
                        49377
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        15586,
                        31173,
                        46760
                      ],
                      "height": 1280,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 720,
                      "is_spatial_image": false
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 627,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_urls": [
                        "https://scontent-otp1-1.cdninstagram.com/v/t51.71878-15/661601307_1289581033271498_730225288469970916_n.jpg?_nc_ht=scontent-otp1-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gHwR0z5-6Mti7yguikxBt2B8wv46H_AckcN_i8ps7w3R4hh-jGnQjsTvHyR3ESFZhg&_nc_ohc=jp3vIW0b3RoQ7kNvwG7t5J_&_nc_gid=qsT5lUUkJDxaTYEgqW_Ntw&edm=AMKDjl4BAAAA&ccb=7-5&oh=00_Af2a93kn1eWM6WUH1RKPcizV04DK7_cp5JVkabdsBXTfhQ&oe=69DC4DCC&_nc_sid=472314"
                      ],
                      "sprite_width": 1500,
                      "thumbnail_duration": 0.13443809523809525,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 14.116
                    }
                  }
                },
                "media_type": 2,
                "original_width": 1080,
                "original_height": 1920,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiOTg3NzM3NWVlMjU3NDk0YjgwNDliZjAzMGJlNjVkZGEzODcwODE3Mzc2Mjg3MDk5Mzk2Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwNDg0NHwzODcwODE3Mzc2Mjg3MDk5Mzk2fDMxMjMxODEwMDkzfGMzYmNjNzBhZTViNGQ5MjMzNGNkM2JlOTYxNWRlNTc3MTU4YmU3ZGQxZGRiZGQ3ZGM3OWJmNGE0MDQxZWM0OWMifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": false,
                "clips_tab_pinned_user_ids": [],
                "original_lang_for_translations": "en",
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775657471,
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
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": true,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "commerce_integrity_review_decision": "",
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 132,
                "like_count": 3,
                "top_likers": [
                  "domi_byr0"
                ],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18097732220024064",
                  "bit_flags": 0,
                  "created_at": 1775657434,
                  "created_at_utc": 1775657434,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18097732220024064",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870817376287099396,
                  "status": "Active",
                  "type": 1,
                  "user_id": 77482241330,
                  "text": "🎱🎱🎱\n•\n•\n•\n•\n#s1krr #bmw #ridersofinstagram #love #this",
                  "user": {
                    "strong_id__": "77482241330",
                    "pk": 77482241330,
                    "pk_id": "77482241330",
                    "id": "77482241330",
                    "is_unpublished": false,
                    "fbid_v2": 17841477319925280,
                    "username": "smv.1k",
                    "full_name": "",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3869602337917434777_77482241330",
                    "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 14,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "play_count": 18729,
                "ig_play_count": 18729,
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
                "video_subtitles_locale": "en_US",
                "video_subtitles_uri": "https://scontent-otp1-1.cdninstagram.com/...",
                "video_sticker_locales": [],
                "has_audio": true,
                "video_duration": 14.133000373840332,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 1286458,
                    "height": 1280,
                    "id": "2581576978905706v",
                    "type": 101,
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  }
                ],
                "number_of_qualities": 8,
                "video_codec": "av01.0.05M.08.0.110.01.01.01.0",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "77482241330",
                  "id": "77482241330",
                  "username": "smv.1k",
                  "full_name": "",
                  "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW35-UwAIoE",
                "device_timestamp": 1775657404818795,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
                "is_post_live_clips_media": false,
                "like_and_view_counts_disabled": true,
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
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      15586,
                      31173,
                      46760
                    ],
                    "height": 1280,
                    "scans_profile": "e15",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 720,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775657471,
                "sponsor_tags": []
              }
            },
            {
              "media": {
                "strong_id__": "3870787133267296530_9816762",
                "id": "3870787133267296530_9816762",
                "fbid": 18099141781817244,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDc4NzEzMzI2NzI5NjUzMA==.3",
                "integrity_review_decision": "pending",
                "pk": "3870787133267296530",
                "has_delayed_metadata": false,
                "mezql_token": "",
                "should_request_ads": false,
                "has_privately_liked": false,
                "collaborator_edit_eligibility": false,
                "share_count_disabled": false,
                "is_reshare_of_text_post_app_media_in_ig": false,
                "is_visual_reply_commenter_notice_enabled": true,
                "subtype_name_for_REST__": "XDTFeedMedia",
                "has_views_fetching_on_search_grid": false,
                "image_versions2": {
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        9548,
                        19097,
                        28646
                      ],
                      "height": 1350,
                      "scans_profile": "e35",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 1080,
                      "is_spatial_image": false
                    },
                    {
                      "estimated_scans_sizes": [
                        6427,
                        12854,
                        19282
                      ],
                      "height": 938,
                      "scans_profile": "e35",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 750,
                      "is_spatial_image": false
                    }
                  ]
                },
                "media_type": 1,
                "original_width": 1080,
                "original_height": 1350,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiOTg3NzM3NWVlMjU3NDk0YjgwNDliZjAzMGJlNjVkZGEzODcwNzg3MTMzMjY3Mjk2NTMwIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwNDg0NHwzODcwNzg3MTMzMjY3Mjk2NTMwfDMxMjMxODEwMDkzfDU4NjIyODk3N2Q4NDdiZDkwYjZkYTc1MDFjM2VmY2Y3M2U4ZjA2YmIzN2RmZGNiNDQ2MmEzYzI5NmJkYjg1MDEifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": {
                  "audio_type": null,
                  "music_canonical_id": "0",
                  "pinned_media_ids": null,
                  "music_info": null,
                  "original_sound_info": null
                },
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775653818,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
                  "in": []
                },
                "mashup_info": {
                  "can_toggle_mashups_allowed": false,
                  "formatted_mashups_count": null,
                  "has_been_mashed_up": false,
                  "has_nonmimicable_additional_audio": false,
                  "is_creator_requesting_mashup": false,
                  "is_light_weight_check": true,
                  "is_light_weight_reuse_allowed_check": true,
                  "is_pivot_page_available": false,
                  "is_reuse_allowed": false,
                  "mashup_type": null,
                  "mashups_allowed": false,
                  "mashups_allowed_for_carousel": false,
                  "non_privacy_filtered_mashups_media_count": 0,
                  "privacy_filtered_mashups_media_count": null,
                  "original_media": null
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "feed",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": false,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "commerce_integrity_review_decision": "",
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "product_suggestions": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 3,
                "like_count": 297,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18099141814817244",
                  "bit_flags": 0,
                  "created_at": 1775653820,
                  "created_at_utc": 1775653820,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18099141814817244",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870787133267296530,
                  "status": "Active",
                  "type": 1,
                  "user_id": 9816762,
                  "text": "the greatest human experience",
                  "user": {
                    "strong_id__": "9816762",
                    "pk": 9816762,
                    "pk_id": "9816762",
                    "id": "9816762",
                    "is_unpublished": false,
                    "fbid_v2": 17841400742860153,
                    "username": "nocap",
                    "full_name": "No Cap",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "2322865363225008074_9816762",
                    "profile_pic_url": "https://instagram.ftia13-1.fna.fbcdn.net/v/t51.2885-19/101552390_208306300166690_2852990751455838208_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=instagram.ftia13-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gHwR0z5-6Mti7yguikxBt2B8wv46H_AckcN_i8ps7w3R4hh-jGnQjsTvHyR3ESFZhg&_nc_ohc=ytvnVM-Wer4Q7kNvwFHfysb&_nc_gid=qsT5lUUkJDxaTYEgqW_Ntw&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GAaRDQYiogYXdL0AAAAAAAD525cnbkULAAAB1501500j-ccb7-5&oh=00_Af1NPSr3GxXw8QOpt_1RHJLpGE3iXAvvGRouGZdSws1lKg&oe=69DC6F17&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 3,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "shop_routing_user_id": null,
                "featured_products": [],
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "9816762",
                  "id": "9816762",
                  "username": "nocap",
                  "full_name": "No Cap",
                  "profile_pic_url": "https://instagram.ftia13-1.fna.fbcdn.net/v/t51.2885-19/101552390_208306300166690_2852990751455838208_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=instagram.ftia13-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gHwR0z5-6Mti7yguikxBt2B8wv46H_AckcN_i8ps7w3R4hh-jGnQjsTvHyR3ESFZhg&_nc_ohc=ytvnVM-Wer4Q7kNvwFHfysb&_nc_gid=qsT5lUUkJDxaTYEgqW_Ntw&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GAaRDQYiogYXdL0AAAAAAAD525cnbkULAAAB1501500j-ccb7-5&oh=00_Af1NPSr3GxXw8QOpt_1RHJLpGE3iXAvvGRouGZdSws1lKg&oe=69DC6F17&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW3zGOvjMES",
                "device_timestamp": 1775653818,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
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
                "is_comments_gif_composer_enabled": true,
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      9548,
                      19097,
                      28646
                    ],
                    "height": 1350,
                    "scans_profile": "e35",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 1080,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775653818,
                "sponsor_tags": [],
                "play_count": 0
              }
            },
            {
              "media": {
                "strong_id__": "3870865595181294610_68182096424",
                "id": "3870865595181294610_68182096424",
                "disable_caption_and_comment": false,
                "fbid": 18088269698248526,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDg2NTU5NTE4MTI5NDYxMA==.3",
                "integrity_review_decision": "pending",
                "pk": "3870865595181294610",
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
                "is_third_party_downloads_eligible": true,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "estimated_scans_sizes": [
                        3420,
                        6841,
                        10261
                      ],
                      "height": 1138,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        3420,
                        6841,
                        10261
                      ],
                      "height": 1138,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        3420,
                        6841,
                        10261
                      ],
                      "height": 1138,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    }
                  ]
                },
                "media_type": 2,
                "original_width": 1076,
                "original_height": 1920,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiOTg3NzM3NWVlMjU3NDk0YjgwNDliZjAzMGJlNjVkZGEzODcwODY1NTk1MTgxMjk0NjEwIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwNDg0NXwzODcwODY1NTk1MTgxMjk0NjEwfDMxMjMxODEwMDkzfDAxZGVjOGU1MDc0ZDYwODViMDhiMzFhZDFiYTFhN2NjOTlmMTAwZDkxNzZmZjJiMzhlMGMzYjllMmVlNjNhMGUifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": false,
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775663284,
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
                "subscribe_cta_visible": false,
                "creative_config": {
                  "capture_type": "clips_v2",
                  "face_effect_id": null,
                  "failure_reason": null,
                  "attribution_user": null,
                  "creation_tool_info": [
                    {
                      "camera_tool": 97,
                      "duration_selector_seconds": 0,
                      "speed_selector": 0.0,
                      "color_filters": "",
                      "appearance_effect": 0,
                      "timer_selector_seconds": 0,
                      "magic_cut_start_time": 0.0,
                      "magic_cut_end_time": 0.0,
                      "effect_filter_name": ""
                    }
                  ],
                  "effect_configs": null,
                  "effect_preview": null,
                  "gen_ai_tool_info": null
                },
                "is_cutout_sticker_allowed": true,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 0,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 132,
                "like_count": 668,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18088269794248526",
                  "bit_flags": 0,
                  "created_at": 1775663285,
                  "created_at_utc": 1775663285,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18088269794248526",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870865595181294610,
                  "status": "Active",
                  "type": 1,
                  "user_id": 68182096424,
                  "has_translation": true,
                  "text": "Madam ji... Apke liye 2 line...🫶💝#dailymotivation #love #reelkarofeelkaro #sigma #video",
                  "user": {
                    "strong_id__": "68182096424",
                    "pk": 68182096424,
                    "pk_id": "68182096424",
                    "id": "68182096424",
                    "is_unpublished": false,
                    "fbid_v2": 17841468172722762,
                    "username": "pal_boy_krish_pal",
                    "full_name": "Sad 🥺 shayar 💔🥀",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3823783874106829968_68182096424",
                    "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 71,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "location": {
                  "pk": 235082047414982,
                  "name": "India : इंडिया",
                  "phone": "",
                  "website": "",
                  "category": "",
                  "hours": {},
                  "address": "",
                  "city": "",
                  "zip": null,
                  "lng": null,
                  "lat": null,
                  "external_id": "235082047414982",
                  "external_id_source": "facebook_places"
                },
                "locations": [],
                "play_count": 18556,
                "ig_play_count": 18556,
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
                "video_duration": 9.241000175476074,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 186744,
                    "height": 1280,
                    "id": "1268915285206999v",
                    "type": 101,
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "url_expiration_timestamp_us": null,
                    "width": 716,
                    "fallback": null
                  }
                ],
                "number_of_qualities": 4,
                "video_codec": "vp09.00.21.08.00.01.01.01.00",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "SELF_DISCLOSURE_FLOW"
                },
                "user": {
                  "pk": "68182096424",
                  "id": "68182096424",
                  "username": "pal_boy_krish_pal",
                  "full_name": "Sad 🥺 shayar 💔🥀",
                  "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW4E8AGD-QS",
                "device_timestamp": 827429536203318,
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
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      3420,
                      6841,
                      10261
                    ],
                    "height": 1138,
                    "scans_profile": "e15",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 640,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "usertags": [],
                "taken_at_ts": 1775663284,
                "sponsor_tags": []
              }
            }
          ]
        }
      },
      {
        "layout_type": "media_grid",
        "feed_type": "media",
        "explore_item_info": {
          "num_columns": 3,
          "total_num_columns": 3,
          "aspect_ratio": 3.0,
          "autoplay": false
        },
        "layout_content": {
          "medias": [
            {
              "media": {
                "strong_id__": "3870782423390535263_195373995",
                "id": "3870782423390535263_195373995",
                "disable_caption_and_comment": false,
                "fbid": 18081427487526220,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDc4MjQyMzM5MDUzNTI2Mw==.3",
                "integrity_review_decision": "pending",
                "pk": "3870782423390535263",
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
                "is_third_party_downloads_eligible": true,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "estimated_scans_sizes": [
                        16942,
                        33884,
                        50826
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        16942,
                        33884,
                        50826
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        16942,
                        33884,
                        50826
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 459,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_urls": [
                        "https://scontent-otp1-1.cdninstagram.com/v/t51.71878-15/660790857_2373665619822205_8380873781116494925_n.jpg?_nc_ht=scontent-otp1-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gHwR0z5-6Mti7yguikxBt2B8wv46H_AckcN_i8ps7w3R4hh-jGnQjsTvHyR3ESFZhg&_nc_ohc=dFTh4bF9nbYQ7kNvwHqE8Sj&_nc_gid=qsT5lUUkJDxaTYEgqW_Ntw&edm=AMKDjl4BAAAA&ccb=7-5&oh=00_Af02LU5pS-5wqWmtRbvrQHafWoMkC2YykVvsoOXNlggR1Q&oe=69DC7932&_nc_sid=472314"
                      ],
                      "sprite_width": 1500,
                      "thumbnail_duration": 0.10698095238095238,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 11.233
                    }
                  }
                },
                "media_type": 2,
                "original_width": 1080,
                "original_height": 1920,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiOTg3NzM3NWVlMjU3NDk0YjgwNDliZjAzMGJlNjVkZGEzODcwNzgyNDIzMzkwNTM1MjYzIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwNDg0NXwzODcwNzgyNDIzMzkwNTM1MjYzfDMxMjMxODEwMDkzfGQ3YWE3NmUyYjE1ZjliYjExOWJkYzA5N2JjYTVmZTNkOTZjY2E5YTBkYzFiNDQ5YzdhMGQ5MjFhYmMxY2ZiNGUifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": false,
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775653218,
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
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": true,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 378,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 26,
                "like_count": 520,
                "fb_like_count": 73,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18081431078526220",
                  "bit_flags": 0,
                  "created_at": 1775653219,
                  "created_at_utc": 1775653219,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18081431078526220",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870782423390535263,
                  "status": "Active",
                  "type": 1,
                  "user_id": 195373995,
                  "text": "One day my love ♥️\n•\n•follow @affirmation_mastershop for more ✨\n•\n#relationship #soulmate #love #explore #relatable",
                  "user": {
                    "strong_id__": "195373995",
                    "pk": 195373995,
                    "pk_id": "195373995",
                    "id": "195373995",
                    "is_unpublished": false,
                    "fbid_v2": 17841401379853052,
                    "username": "affirmation_mastershop",
                    "full_name": "•Motivation | Success | Business•",
                    "is_private": false,
                    "is_verified": true,
                    "profile_pic_id": "3269410642393332923_195373995",
                    "profile_pic_url": "https://instagram.ftia13-1.fna.fbcdn.net/v/t51.2885-19/414190123_903159541161175_4561363514804565959_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44NTUuYzIifQ&_nc_ht=instagram.ftia13-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gHwR0z5-6Mti7yguikxBt2B8wv46H_AckcN_i8ps7w3R4hh-jGnQjsTvHyR3ESFZhg&_nc_ohc=Cf8vjXcPRNEQ7kNvwGFFddM&_nc_gid=qsT5lUUkJDxaTYEgqW_Ntw&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GCsKsBjXXKA3azUDAMd3WhfzN00-bkULAAAB1501500j-ccb7-5&oh=00_Af0k_0Bw6-a5CHcwOhLnh1jU3U6urCwxO1odpheI4DKRhg&oe=69DC63B7&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 43,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "fb_comment_count": 3,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "play_count": 12320,
                "ig_play_count": 9357,
                "fb_play_count": 2963,
                "shop_routing_user_id": null,
                "featured_products": [],
                "are_remixes_crosspostable": true,
                "crosspost_metadata": {
                  "is_feedback_aggregated": true,
                  "unified_feedback_enabled": true,
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "is_eligible_for_autodub": false,
                "is_eligible_for_autodub_upsell": false,
                "video_sticker_locales": [],
                "has_audio": true,
                "video_duration": 11.232999801635742,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 1921190,
                    "height": 1280,
                    "id": "4297277253819204v",
                    "type": 101,
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  }
                ],
                "number_of_qualities": 8,
                "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "195373995",
                  "id": "195373995",
                  "username": "affirmation_mastershop",
                  "full_name": "•Motivation | Success | Business•",
                  "profile_pic_url": "https://instagram.ftia13-1.fna.fbcdn.net/v/t51.2885-19/414190123_903159541161175_4561363514804565959_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44NTUuYzIifQ&_nc_ht=instagram.ftia13-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gHwR0z5-6Mti7yguikxBt2B8wv46H_AckcN_i8ps7w3R4hh-jGnQjsTvHyR3ESFZhg&_nc_ohc=Cf8vjXcPRNEQ7kNvwGFFddM&_nc_gid=qsT5lUUkJDxaTYEgqW_Ntw&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GCsKsBjXXKA3azUDAMd3WhfzN00-bkULAAAB1501500j-ccb7-5&oh=00_Af0k_0Bw6-a5CHcwOhLnh1jU3U6urCwxO1odpheI4DKRhg&oe=69DC63B7&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": true
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW3yBsVBL5f",
                "device_timestamp": 1775653218,
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
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      16942,
                      33884,
                      50826
                    ],
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 640,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775653218,
                "sponsor_tags": []
              }
            },
            {
              "media": {
                "strong_id__": "3870804372502703203_1426659339",
                "id": "3870804372502703203_1426659339",
                "disable_caption_and_comment": false,
                "fbid": 18575765008015381,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDgwNDM3MjUwMjcwMzIwMw==.3",
                "integrity_review_decision": "pending",
                "pk": "3870804372502703203",
                "is_affiliate_commission_eligible": false,
                "has_delayed_metadata": false,
                "mezql_token": "",
                "should_request_ads": false,
                "has_privately_liked": false,
                "collaborator_edit_eligibility": false,
                "share_count_disabled": false,
                "is_reshare_of_text_post_app_media_in_ig": false,
                "is_visual_reply_commenter_notice_enabled": true,
                "translated_langs_for_autodub": [
                  "mr",
                  "kn",
                  "en"
                ],
                "subtype_name_for_REST__": "XDTClipsMedia",
                "is_third_party_downloads_eligible": true,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "estimated_scans_sizes": [
                        14939,
                        29878,
                        44818
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        14939,
                        29878,
                        44818
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        15171,
                        30342,
                        45514
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 438,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_urls": [
                        "https://scontent-otp1-1.cdninstagram.com/v/t51.71878-15/657748489_2147344586107150_5689865079221968025_n.jpg?_nc_ht=scontent-otp1-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gHwR0z5-6Mti7yguikxBt2B8wv46H_AckcN_i8ps7w3R4hh-jGnQjsTvHyR3ESFZhg&_nc_ohc=QCYkb7DLkd4Q7kNvwFRYJl8&_nc_gid=qsT5lUUkJDxaTYEgqW_Ntw&edm=AMKDjl4BAAAA&ccb=7-5&oh=00_Af1gim25J5_R7Ev8-nMJ7rsmtQ66BR_sQmXddZ0Vk_Csiw&oe=69DC5B36&_nc_sid=472314"
                      ],
                      "sprite_width": 1500,
                      "thumbnail_duration": 0.5647619047619047,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 59.3
                    }
                  }
                },
                "media_cropping_info": {
                  "four_by_three_crop": {
                    "crop_left": 0.0,
                    "crop_right": 1.0,
                    "crop_top": 0.0,
                    "crop_bottom": 0.7496790757381258
                  }
                },
                "media_type": 2,
                "original_width": 1080,
                "original_height": 1920,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiOTg3NzM3NWVlMjU3NDk0YjgwNDliZjAzMGJlNjVkZGEzODcwODA0MzcyNTAyNzAzMjAzIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwNDg0NXwzODcwODA0MzcyNTAyNzAzMjAzfDMxMjMxODEwMDkzfDUxZmI2N2U1OTE0ZDc1OWQ2M2Y3NTljZDk2YjhkZjFhYmFjNjVjNTdlYmQyZjFkZGY3ZTI1MzM4YjNkNGRjZWUifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": false,
                "clips_tab_pinned_user_ids": [],
                "original_lang_for_translations": "te",
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775656212,
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
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": true,
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
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 96,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 15,
                "like_count": 748,
                "fb_like_count": 9,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18575765320015381",
                  "bit_flags": 0,
                  "created_at": 1775655966,
                  "created_at_utc": 1775655966,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18575765320015381",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870804372502703203,
                  "status": "Active",
                  "type": 1,
                  "user_id": 1426659339,
                  "text": "If this is on your feed… it’s not random. It’s a reminder.… \n\n#loveyourself #respectyourself #rjkajal #kajaltalks #love",
                  "user": {
                    "strong_id__": "1426659339",
                    "pk": 1426659339,
                    "pk_id": "1426659339",
                    "id": "1426659339",
                    "is_unpublished": false,
                    "fbid_v2": 17841401060192291,
                    "username": "kajalrj",
                    "full_name": "RJ Kajal️️️️️️",
                    "is_private": false,
                    "is_verified": true,
                    "profile_pic_id": "3435656723797656694_1426659339",
                    "profile_pic_url": "https://instagram.ftia13-1.fna.fbcdn.net/v/t51.2885-19/455738881_2466174476925406_6091587945073964807_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=instagram.ftia13-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gHwR0z5-6Mti7yguikxBt2B8wv46H_AckcN_i8ps7w3R4hh-jGnQjsTvHyR3ESFZhg&_nc_ohc=2nQ1y-6XiGUQ7kNvwFoO1En&_nc_gid=qsT5lUUkJDxaTYEgqW_Ntw&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GAEGKhveuab9_MIIAAd3LyD2qolUbkULAAAB1501500j-ccb7-5&oh=00_Af2v46osCuJpDCZzGpSxDyUbYAEcnHhicoYZFK9vlDnUuA&oe=69DC7C52&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 34,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "fb_comment_count": 0,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "play_count": 46307,
                "ig_play_count": 45416,
                "fb_play_count": 891,
                "shop_routing_user_id": null,
                "featured_products": [],
                "are_remixes_crosspostable": true,
                "crosspost_metadata": {
                  "is_feedback_aggregated": true,
                  "unified_feedback_enabled": true,
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "is_eligible_for_autodub": false,
                "is_eligible_for_autodub_upsell": false,
                "video_subtitles_locale": "en_US",
                "video_subtitles_uri": "https://scontent-otp1-1.cdninstagram.com/...",
                "video_sticker_locales": [],
                "has_audio": true,
                "video_duration": 59.301998138427734,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 808203,
                    "height": 1280,
                    "id": "1608421213789232v",
                    "type": 101,
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  }
                ],
                "number_of_qualities": 5,
                "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "1426659339",
                  "id": "1426659339",
                  "username": "kajalrj",
                  "full_name": "RJ Kajal️️️️️️",
                  "profile_pic_url": "https://instagram.ftia13-1.fna.fbcdn.net/v/t51.2885-19/455738881_2466174476925406_6091587945073964807_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=instagram.ftia13-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gHwR0z5-6Mti7yguikxBt2B8wv46H_AckcN_i8ps7w3R4hh-jGnQjsTvHyR3ESFZhg&_nc_ohc=2nQ1y-6XiGUQ7kNvwFoO1En&_nc_gid=qsT5lUUkJDxaTYEgqW_Ntw&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GAEGKhveuab9_MIIAAd3LyD2qolUbkULAAAB1501500j-ccb7-5&oh=00_Af2v46osCuJpDCZzGpSxDyUbYAEcnHhicoYZFK9vlDnUuA&oe=69DC7C52&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": true
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW33BGCDWxj",
                "device_timestamp": 1775655723146134,
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
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      15171,
                      30342,
                      45514
                    ],
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 640,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775656212,
                "sponsor_tags": []
              }
            },
            {
              "media": {
                "strong_id__": "3870810258406906459_80079293147",
                "id": "3870810258406906459_80079293147",
                "disable_caption_and_comment": false,
                "fbid": 18436508572141899,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDgxMDI1ODQwNjkwNjQ1OQ==.3",
                "integrity_review_decision": "pending",
                "pk": "3870810258406906459",
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
                "is_third_party_downloads_eligible": true,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "estimated_scans_sizes": [
                        7312,
                        14624,
                        21937
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        7312,
                        14624,
                        21937
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        7312,
                        14624,
                        21937
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-otp1-1.cdninstagram.com/...",
                      "width": 640,
                      "is_spatial_image": false
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 788,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_urls": [
                        "https://scontent-otp1-1.cdninstagram.com/v/t51.71878-15/659803182_1238999864981400_5274167123944012537_n.jpg?_nc_ht=scontent-otp1-1.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gHwR0z5-6Mti7yguikxBt2B8wv46H_AckcN_i8ps7w3R4hh-jGnQjsTvHyR3ESFZhg&_nc_ohc=c5P3bzW8GB8Q7kNvwFfC1sT&_nc_gid=qsT5lUUkJDxaTYEgqW_Ntw&edm=AMKDjl4BAAAA&ccb=7-5&oh=00_Af3O8jSpFr3RXAUlBcmr7mPqDcCUHwgIEc5ieS0ukG6hGw&oe=69DC7960&_nc_sid=472314"
                      ],
                      "sprite_width": 1500,
                      "thumbnail_duration": 0.1634952380952381,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 17.167
                    }
                  }
                },
                "media_type": 2,
                "original_width": 1080,
                "original_height": 1920,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiOTg3NzM3NWVlMjU3NDk0YjgwNDliZjAzMGJlNjVkZGEzODcwODEwMjU4NDA2OTA2NDU5Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTIwNDg0NXwzODcwODEwMjU4NDA2OTA2NDU5fDMxMjMxODEwMDkzfGQzNzIxMjhmNWNjNmM1NTUwZTU0ZTMwNzdiY2Y4NmZkODRlYjdhNzMyZjI3YzM3ZDNkNTcyMjI5NzNlYmNiNDEifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": true,
                "clips_tab_pinned_user_ids": [],
                "original_lang_for_translations": "en",
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775656758,
                "photo_of_you": false,
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
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [
                  {
                    "strong_id__": "6441686607",
                    "pk": 6441686607,
                    "pk_id": "6441686607",
                    "id": "6441686607",
                    "username": "hiba_jarvas",
                    "full_name": "Hiba jarvas",
                    "is_private": true,
                    "is_verified": false,
                    "profile_pic_id": "2774810643774319018_6441686607",
                    "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
                  }
                ],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "collab_follow_button_info": {
                  "show_follow_button": true,
                  "is_owner_in_author_exp": true
                },
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 65,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 5,
                "like_count": 616,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18436508806141899",
                  "bit_flags": 0,
                  "created_at": 1775656748,
                  "created_at_utc": 1775656748,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18436508806141899",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870810258406906459,
                  "status": "Active",
                  "type": 1,
                  "user_id": 80079293147,
                  "text": "Our first home🥹🤍. #father #love #reelviral #instgram #fyp",
                  "user": {
                    "strong_id__": "80079293147",
                    "pk": 80079293147,
                    "pk_id": "80079293147",
                    "id": "80079293147",
                    "is_unpublished": false,
                    "fbid_v2": 17841480074429911,
                    "username": "_moments.by.me_",
                    "full_name": "Rieewww",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3822356453873874657_80079293147",
                    "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 12,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "play_count": 13219,
                "ig_play_count": 13219,
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
                "video_duration": 17.180999755859375,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 1532780,
                    "height": 1280,
                    "id": "2147343469371331v",
                    "type": 101,
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  }
                ],
                "number_of_qualities": 8,
                "video_codec": "av01.0.04M.08.0.111.01.01.01.0",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "80079293147",
                  "id": "80079293147",
                  "username": "_moments.by.me_",
                  "full_name": "Rieewww",
                  "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW34WvtSBpb",
                "device_timestamp": 1775656559419070,
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
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      7312,
                      14624,
                      21937
                    ],
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-otp1-1.cdninstagram.com/...",
                    "width": 640,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775656758,
                "sponsor_tags": []
              }
            }
          ]
        }
      }
    ],
    "more_available": true,
    "next_max_id": "87626e0cf46b4c7ca5bbc1359f05e087",
    "next_page": 1,
    "next_media_ids": [],
    "auto_load_more_enabled": true,
    "status": "ok"
  },
  "next_page_id": "WyI4NzYyNmUwY2Y0NmI0YzdjYTViYmMxMzU5ZjA1ZTA4NyIsW10sMV0="
}
```

</details>

---

## Deprecated endpoints

These endpoints are still available but will be removed in a future version. Use the recommended alternatives.

### ~~GET /v2/hashtag/medias/clips~~

!!! warning
    Switch to /v2/fbsearch/reels — this endpoint will be deprecated soon. It currently returns all media types, not just reels.

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v2-hashtags){ target=_blank }
