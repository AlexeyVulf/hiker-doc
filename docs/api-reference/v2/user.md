# User Endpoints

Enhanced user data with pagination via page_id.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/a2/user`](#get-a2user) | [`/v2/user/by/id`](#get-v2userbyid) | [`/v2/user/by/username`](#get-v2userbyusername) | [`/v2/user/clips`](#get-v2userclips) | [`/v2/user/explore/businesses/by/id`](#get-v2userexplorebusinessesbyid) | [`/v2/user/followers`](#get-v2userfollowers) | [`/v2/user/following`](#get-v2userfollowing) | [`/v2/user/highlights`](#get-v2userhighlights) | [`/v2/user/highlights/by/username`](#get-v2userhighlightsbyusername) | [`/v2/user/stories`](#get-v2userstories) | [`/v2/user/stories/by/username`](#get-v2userstoriesbyusername) | [`/v2/user/suggested/profiles`](#get-v2usersuggestedprofiles) | [`/v2/user/tag/medias`](#get-v2usertagmedias) | [`/v2/userstream/by/id`](#get-v2userstreambyid) | [`/v2/userstream/by/username`](#get-v2userstreambyusername)

---

### GET /a2/user

Get user object

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/a2/user?username=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_a2(username="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/a2/user",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/a2/user?username=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "graphql": {
    "user": {
      "id": "787132",
      "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
      "full_name": "National Geographic",
      "edge_followed_by": {
        "count": 274988953
      },
      "edge_follow": {
        "count": 193
      },
      "profile_pic_url": "https://scontent-xxc1-1.cdninstagram.com/...",
      "profile_pic_url_hd": "https://scontent-xxc1-1.cdninstagram.com/...",
      "edge_owner_to_timeline_media": {
        "count": 31529,
        "edges": [
          {
            "node": {
              "id": "3865659729796199935",
              "shortcode": "DWllQsJCPX_",
              "display_url": "https://scontent-ord5-1.cdninstagram.com/...",
              "thumbnail_url": "https://scontent-ord5-1.cdninstagram.com/...",
              "video_url": "https://scontent-ord5-2.cdninstagram.com/...",
              "__typename": "GraphVideo",
              "product_type": "clips",
              "title": "",
              "video_duration": 60.10100173950195,
              "video_view_count": 0,
              "edge_media_to_caption": {
                "edges": [
                  {
                    "node": {
                      "text": "This Earth Month, step into wonder with National Geographic as we celebrate everything that makes our planet so extraordinary 🌍\n\nStream the National Geographic #EarthMonth collection all April long on @DisneyPlus. #StepIntoWonder"
                    }
                  }
                ]
              },
              "edge_media_to_comment": {
                "count": 236
              },
              "edge_liked_by": {
                "count": 35897
              },
              "edge_media_preview_like": {
                "count": 35897
              }
            }
          },
          {
            "node": {
              "id": "3844732796656436386",
              "shortcode": "DVbPBu5AESi",
              "display_url": "https://scontent-ord5-3.cdninstagram.com/...",
              "thumbnail_url": "https://scontent-ord5-3.cdninstagram.com/...",
              "video_url": "https://scontent-ord5-2.cdninstagram.com/...",
              "__typename": "GraphVideo",
              "product_type": "clips",
              "title": "",
              "video_duration": 60.07400131225586,
              "video_view_count": 0,
              "edge_media_to_caption": {
                "edges": [
                  {
                    "node": {
                      "text": "Small in size, but their impact on our planet is huge 🐝 Join @bertiegregory as he explores the weird and wonderful world of bees.\n\n#SecretsOfTheBees premieres Tuesday, March 31 at 8/7c on @natgeotv. Stream on @DisneyPlus and @hulu."
                    }
                  }
                ]
              },
              "edge_media_to_comment": {
                "count": 614
              },
              "edge_liked_by": {
                "count": 66087
              },
              "edge_media_preview_like": {
                "count": 66087
              }
            }
          },
          {
            "node": {
              "id": "3870670793969876810",
              "shortcode": "DW3YpRVDb9K",
              "display_url": null,
              "thumbnail_url": null,
              "video_url": null,
              "__typename": "GraphSidecar",
              "product_type": "carousel_container",
              "title": "",
              "video_duration": 0.0,
              "video_view_count": 0,
              "edge_media_to_caption": {
                "edges": [
                  {
                    "node": {
                      "text": "Whorls, hexagons, and half-moon patterns can be found throughout nature, formed by natural processes such as wind and crashing waves. After spending time along the seashore, photographer and conservationist Jon McCormack discovered that our planet's familiar shapes and designs have guided his work for years. To celebrate this, he set out on a journey to capture nature's intriguing forms at every scale.\n\nSee more of his work and learn about nature's patterns at the link in bio.\n\nPhotographs by @jonmccormackphoto, courtesy of Damiani’s upcoming book Jon McCormack: Patterns - Art of the Natural World"
                    }
                  }
                ]
              },
              "edge_media_to_comment": {
                "count": 118
              },
              "edge_liked_by": {
                "count": 43754
              },
              "edge_media_preview_like": {
                "count": 43754
              },
              "edge_sidecar_to_children": {
                "edges": [
                  {
                    "node": {
                      "__typename": "GraphImage",
                      "id": "3870670683399590370",
                      "shortcode": "DW3YnqWjRHi",
                      "display_url": "https://scontent-ord5-1.cdninstagram.com/...",
                      "thumbnail_url": "https://scontent-ord5-1.cdninstagram.com/...",
                      "video_url": null
                    }
                  },
                  {
                    "node": {
                      "__typename": "GraphImage",
                      "id": "3870670679968669302",
                      "shortcode": "DW3YnnKDV52",
                      "display_url": "https://scontent-ord5-1.cdninstagram.com/...",
                      "thumbnail_url": "https://scontent-ord5-1.cdninstagram.com/...",
                      "video_url": null
                    }
                  },
                  {
                    "node": {
                      "__typename": "GraphImage",
                      "id": "3870670694816531730",
                      "shortcode": "DW3Yn0_DcUS",
                      "display_url": "https://scontent-ord5-1.cdninstagram.com/...",
                      "thumbnail_url": "https://scontent-ord5-1.cdninstagram.com/...",
                      "video_url": null
                    }
                  }
                ]
              }
            }
          }
        ]
      }
    }
  }
}
```

</details>

---

### GET /v2/user/by/id

Get user object by id. Returns a User object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/by/id?id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_by_id_v2(id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/user/by/id",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/by/id?id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "user": {
    "strong_id__": "787132",
    "pk": 787132,
    "id": "787132",
    "full_name": "National Geographic",
    "username": "natgeo",
    "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
    "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/...",
    "is_opal_enabled": false,
    "eligible_for_text_app_activation_badge": false,
    "highlights_tray_type": "DEFAULT",
    "account_type": 2,
    "bio_links": [
      {
        "link_id": 17954981494900183,
        "url": "http://visitstore.bio/natgeo",
        "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGne6enmrLohWZZw33KD8LdiuCUPVmQzGYwWJQl5pyZ9SQ-ycDh1ljIFltVsT4_aem_oz_zJSmTMWCh06cBY9lEbw&e=AT7e7KngvH2LmnDuWveGkojuxnpumetFtiICUMHTw0AH7L2P0M2i9Z05qd3ffembCYnGaAmLF7X-ueDbbUICBtsIzryjeJTVD4HqzmGSow",
        "link_type": "external",
        "title": "",
        "media_type": "none",
        "image_url": "",
        "icon_url": "",
        "media_accent_color_hex": "",
        "is_pinned": false,
        "is_verified": false,
        "open_external_url_with_in_app_browser": true,
        "click_id": "PAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGne6enmrLohWZZw33KD8LdiuCUPVmQzGYwWJQl5pyZ9SQ-ycDh1ljIFltVsT4_aem_oz_zJSmTMWCh06cBY9lEbw",
        "creation_source": "NONE"
      }
    ],
    "is_call_to_action_enabled": false,
    "is_business": true,
    "biography_with_entities": {
      "raw_text": "Step into wonder and find your inner explorer with National Geographic 🌎",
      "entities": []
    },
    "show_shoppable_feed": false,
    "seller_shoppable_feed_type": "none",
    "is_profile_picture_expansion_enabled": true,
    "show_schools_badge": null,
    "text_post_app_badge_label": "natgeo",
    "text_post_new_post_count": 5,
    "text_post_app_joiner_number": 672534,
    "text_post_app_joiner_number_label": "672,534",
    "recon_features": {
      "enable_recon_cta": true
    },
    "media_count": 31529,
    "trial_clips_rate_limiting": {
      "warning_title": "You can share one more trial reel",
      "at_limit_title": "You've reached the limit",
      "warning_body": "You've almost reached the limit. Once you share this trial reel, you'll need to wait up to 24 hours to start using trial reels again.",
      "at_limit_body": "You've shared the maximum number of trial reels allowed within 24 hours. You can share this reel to everyone now as a regular reel or wait up to 24 hours to share it as a trial reel.",
      "count": 20
    },
    "is_prime_onboarding_account": false,
    "is_onboarding_account": false,
    "show_ring_award": false,
    "ring_creator_metadata": {},
    "is_verified": true,
    "is_ring_creator": false,
    "is_private": false,
    "birthday_today_visibility_for_viewer": "NOT_VISIBLE",
    "following_count": 193,
    "follower_count": 274988955,
    "fbid_v2": 17841400573960012,
    "pk_id": "787132",
    "feed_post_reshare_disabled": false,
    "has_ever_selected_topics": false,
    "has_nme_badge": false,
    "third_party_downloads_enabled": 2,
    "show_fb_link_on_profile": false,
    "show_fb_page_link_on_profile": false,
    "can_hide_category": true,
    "can_hide_public_contacts": true,
    "primary_profile_link_type": 0,
    "is_recon_ad_cta_on_profile_eligible_with_viewer": true,
    "current_catalog_id": null,
    "mini_shop_seller_onboarding_status": null,
    "ads_incentive_expiration_date": null,
    "ads_page_id": null,
    "ads_page_name": null,
    "account_category": "",
    "can_add_fb_group_link_on_profile": false,
    "can_use_affiliate_partnership_messaging_as_creator": false,
    "can_use_affiliate_partnership_messaging_as_brand": false,
    "has_gen_ai_personas_for_profile_banner": false,
    "has_guides": false,
    "highlight_reshare_disabled": false,
    "include_direct_blacklist_status": true,
    "is_direct_roll_call_enabled": true,
    "is_eligible_for_meta_verified_links_in_reels": false,
    "is_eligible_for_post_boost_mv_upsell": false,
    "is_meta_verified_related_accounts_display_enabled": false,
    "is_new_to_instagram": false,
    "is_profile_broadcast_sharing_enabled": true,
    "is_secondary_account_creation": false,
    "profile_type": 0,
    "is_coppa_enforced": false,
    "is_auto_confirm_enabled_for_all_reciprocal_follow_requests": false,
    "views_on_grid_status": "SHOW_VIEWS_ON_GRID",
    "is_bestie": false,
    "latest_reel_media": 1775659002,
    "latest_besties_reel_media": 0,
    "account_badges": [],
    "has_highlight_reels": true,
    "is_creator_agent_enabled": false,
    "interop_messaging_user_fbid": 113671860027320,
    "profile_pic_id": "3865702555259028436_787132",
    "has_anonymous_profile_picture": false,
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
    "hd_profile_pic_url_info": {
      "height": 1080,
      "url": "https://scontent-lga3-2.cdninstagram.com/...",
      "width": 1080
    },
    "hd_profile_pic_versions": [
      {
        "height": 320,
        "url": "https://scontent-lga3-2.cdninstagram.com/...",
        "width": 320
      },
      {
        "height": 640,
        "url": "https://scontent-lga3-2.cdninstagram.com/...",
        "width": 640
      }
    ],
    "is_active_on_text_post_app": true,
    "is_cannes": false,
    "is_facebook_onboarded_charity": false,
    "is_favorite": false,
    "merchant_checkout_style": "none",
    "show_account_transparency_details": true,
    "transparency_product_enabled": false,
    "text_app_last_visited_time": null,
    "is_eligible_for_slide": false,
    "live_subscription_status": "default",
    "business_contact_method": "UNKNOWN",
    "category_id": "0",
    "city_id": "0",
    "city_name": "",
    "direct_messaging": "UNKNOWN",
    "instagram_location_id": "",
    "page_id": null,
    "public_email": "",
    "public_phone_country_code": "",
    "public_phone_number": "",
    "should_show_category": false,
    "should_show_public_contacts": true,
    "zip": "",
    "contact_phone_number": "",
    "has_music_on_profile": false,
    "has_videos": true,
    "has_views_fetching": true,
    "is_category_tappable": false,
    "is_eligible_for_creator_product_links": false,
    "is_eligible_for_lead_center": true,
    "is_eligible_for_schools_search_upsell": false,
    "is_eligible_for_smb_support_flow": true,
    "lead_details_app_id": "com.bloks.www.ig.smb.lead_gen.subpage",
    "num_of_admined_pages": null,
    "page_name": "National Geographic",
    "professional_conversion_suggested_account_type": 3,
    "profile_context": "",
    "smb_support_partner": null,
    "show_all_highlights_as_selected_in_management_screen": false,
    "trial_clips_enabled": false,
    "enable_add_school_in_edit_profile": false,
    "shopping_post_onboard_nux_type": null,
    "fb_page_call_to_action_id": "",
    "address_street": "",
    "is_profile_audio_call_enabled": false,
    "displayed_action_button_partner": null,
    "smb_delivery_partner": null,
    "smb_support_delivery_partner": null,
    "displayed_action_button_type": null,
    "category": "",
    "external_lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGnIgwUpGZSGvHU140ds2b-PG1LpSBtqA6coiUYqIBNRNEGbyu4WgyGpAbKVjw_aem_npWE-rWZ6v6OlJWps6TmOw&e=AT7SmDIM6gydO4reRckLvfG4H7YSEy0aJeGefP2e4k738EKAEB2Km9l9nv93aodcbEpYlj6HcX07y30LseKp-XY26XHB9wHqgikUPD_Utw",
    "external_url": "http://visitstore.bio/natgeo",
    "active_standalone_fundraisers": {
      "total_count": 0,
      "fundraisers": []
    },
    "additional_business_addresses": [],
    "allow_manage_memorialization": false,
    "auto_expand_chaining": false,
    "avatar_status": {
      "has_avatar": false
    },
    "broadcast_chat_preference_status": {
      "json_response": "{\"status\":\"ok\",\"status_code\":\"200\",\"is_broadcast_chat_creator\":true,\"notification_setting_type\":2}",
      "is_broadcast_chat_creator": true,
      "notification_setting_type": 2
    },
    "can_use_branded_content_discovery_as_brand": false,
    "can_use_branded_content_discovery_as_creator": false,
    "can_use_paid_partnership_messaging_as_creator": false,
    "chaining_upsell_cards": [],
    "charity_profile_fundraiser_info": {
      "pk": 787132,
      "has_active_fundraiser": false,
      "is_facebook_onboarded_charity": false,
      "consumption_sheet_config": {
        "can_viewer_donate": false,
        "currency": null,
        "donation_disabled_message": null,
        "donation_url": null,
        "has_viewer_donated": null,
        "privacy_disclaimer": null,
        "profile_fundraiser_id": null,
        "you_donated_message": null,
        "donation_amount_config": {
          "default_selected_donation_value": null,
          "donation_amount_selector_values": [],
          "maximum_donation_amount": null,
          "minimum_donation_amount": null,
          "prefill_amount": null,
          "user_currency": null
        }
      }
    },
    "creator_shopping_info": {
      "linked_merchant_accounts": []
    },
    "follow_friction_type": 0,
    "has_active_charity_business_profile_fundraiser": false,
    "has_chaining": true,
    "has_collab_collections": false,
    "has_exclusive_feed_content": false,
    "instagram_pk": "787132",
    "is_profile_search_enabled": false,
    "is_eligible_for_diverse_owned_business_info": false,
    "is_eligible_for_meta_verified_links_in_post": false,
    "is_eligible_for_meta_verified_enhanced_link_sheet": false,
    "is_eligible_for_meta_verified_enhanced_link_sheet_consumption": false,
    "is_eligible_for_meta_verified_multiple_addresses_creation": false,
    "is_eligible_for_meta_verified_multiple_addresses_consumption": false,
    "is_eligible_for_meta_verified_related_accounts": false,
    "meta_verified_related_accounts_count": 0,
    "is_eligible_to_display_diverse_owned_business_info": false,
    "is_eligible_to_host_profile_reels_ads": false,
    "is_favorite_for_clips": false,
    "is_favorite_for_highlights": false,
    "is_in_canada": false,
    "is_interest_account": true,
    "is_memorialized": false,
    "is_potential_business": false,
    "is_regulated_news_in_viewer_location": false,
    "is_remix_setting_enabled_for_posts": true,
    "is_remix_setting_enabled_for_reels": true,
    "is_regulated_c18": false,
    "profile_overlay_info": {
      "overlay_format": "NONE",
      "bloks_payload": null
    },
    "is_stories_teaser_muted": false,
    "is_supervision_features_enabled": false,
    "is_whatsapp_linked": false,
    "mutual_followers_count": 0,
    "nametag": {
      "available_theme_colors": [
        -1,
        7747834,
        13828293
      ],
      "background_image_url": "",
      "emoji": "😀",
      "emoji_color": 0,
      "gradient": 2,
      "is_background_image_blurred": false,
      "mode": 0,
      "selected_theme_color": -1,
      "selfie_sticker": 0,
      "selfie_url": "",
      "theme_color": {
        "available_theme_colors": [
          {
            "display_label": "Default",
            "int_value": -1
          },
          {
            "display_label": "Purple",
            "int_value": 7747834
          },
          {
            "display_label": "Lavender",
            "int_value": 13828293
          }
        ],
        "selected_theme_color": {
          "display_label": "Default",
          "int_value": -1
        }
      }
    },
    "not_meta_verified_friction_info": {
      "label_friction_content": "Not Meta Verified",
      "is_eligible_for_label_friction": false
    },
    "open_external_url_with_in_app_browser": true,
    "pinned_channels_info": {
      "has_public_channels": false,
      "pinned_channels_list": []
    },
    "profile_context_facepile_users": [],
    "profile_context_links_with_user_ids": [],
    "profile_pic_genai_tool_info": [],
    "pronouns": [],
    "relevant_news_regulation_locations": [],
    "remove_message_entrypoint": false,
    "request_contact_enabled": false,
    "show_blue_badge_on_main_profile": true,
    "show_ig_app_switcher_badge": true,
    "disable_profile_shop_cta": false,
    "show_text_post_app_badge": true,
    "show_text_post_app_switcher_badge": true,
    "spam_follower_setting_enabled": true,
    "total_ar_effects": 0,
    "total_clips_count": 1,
    "upcoming_events": [],
    "whatsapp_number": "",
    "recs_from_friends": {
      "enable_recs_from_friends": false,
      "recs_from_friends_entry_point_type": "banner"
    },
    "adjusted_banners_order": [],
    "has_visible_media_notes": true,
    "is_open_to_collab": false,
    "is_daily_limit_blocking": false,
    "threads_profile_glyph_url": "barcelona://user?username=natgeo&xmt=AQF05Pqewu4p0_W0p6g7mG0u2F5NeB8YbWSFBkLdotMO33E",
    "is_oregon_custom_gender_consented": false,
    "profile_reels_sorting_eligibility": "DISABLED",
    "nonpro_can_maybe_see_profile_hypercard": false,
    "should_show_tagged_tab": true,
    "posts_subscription_status": "default",
    "reels_subscription_status": "default",
    "stories_subscription_status": "default",
    "is_profile_wa_calling_enabled": false,
    "wa_calling_option_for_wa_linked": 0,
    "wa_calling_option_for_legacy_num": 0,
    "is_eligible_for_meta_verified_ig_self_profile_not_verified_badge": false,
    "has_private_collections": true,
    "is_guardian_r_account_cannes_pair": false,
    "can_see_support_inbox": null,
    "has_fan_club_subscriptions": false,
    "show_wa_link_on_profile": false,
    "meta_verified_benefits_info": {
      "active_meta_verified_benefits": [],
      "is_eligible_for_meta_verified_content_protection": false,
      "is_eligible_for_ig_meta_verified_label": false
    },
    "existing_user_age_collection_enabled": true,
    "has_public_tab_threads": true,
    "is_eligible_for_meta_verified_label": true,
    "is_favorite_for_stories": false,
    "is_parenting_account": false,
    "show_post_insights_entry_point": true,
    "short_drama_creator": null,
    "short_drama_series_playlist_id": null,
    "short_drama_series_episode_count": null,
    "short_drama_series_seed_media_id": null,
    "short_drama_series_title": null,
    "short_drama_role": "NONE",
    "short_drama_series_profiles": [],
    "short_drama_producer_account": null,
    "moonshot_joiner_number": null,
    "is_creator_marketplace_badge_visible": false,
    "creator_marketplace_accounts_reached_metric": null,
    "school_affiliated_account_viewer_status": null,
    "qa_freeform_banner": null,
    "qa_freeform_banner_available_prompts": [
      {
        "prompt": "CURRENT_OBSESSION",
        "display_text": "Current obsession"
      },
      {
        "prompt": "DREAM_DESTINATION",
        "display_text": "Dream destination"
      },
      {
        "prompt": "PLAYING",
        "display_text": "Playing"
      }
    ],
    "qa_freeform_banner_transparency": "The banner is visible to everyone on and off Instagram.",
    "can_message_pinned_carrera_interest_owner": true
  },
  "status": "ok"
}
```

</details>

---

### GET /v2/user/by/username

Get user object by username. Returns a User object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/by/username?username=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_by_username_v2(username="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/user/by/username",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/by/username?username=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "user": {
    "strong_id__": "787132",
    "pk": 787132,
    "id": "787132",
    "full_name": "National Geographic",
    "username": "natgeo",
    "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
    "profile_pic_url": "https://scontent-mia3-2.cdninstagram.com/...",
    "is_opal_enabled": false,
    "eligible_for_text_app_activation_badge": false,
    "highlights_tray_type": "DEFAULT",
    "account_type": 2,
    "bio_links": [
      {
        "link_id": 17954981494900183,
        "url": "http://visitstore.bio/natgeo",
        "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGnkFSR1HCzqfbC6GnfijBlotC6FEwprEUO0Y6OKnEA_36a9EVKpBExF9Q-4rY_aem_G0DwgvO2G-Mtq2_CtYq2NA&e=AT6I42Q3LVWBneB1QihtoJaOAfnbjh3dJoIo9eKvcBoqqmYlau5qPkt6P63LouBNerpMplIWxknXf_5fzXP4mRL51ebQnEawpDoQFaUPKQ",
        "link_type": "external",
        "title": "",
        "media_type": "none",
        "image_url": "",
        "icon_url": "",
        "media_accent_color_hex": "",
        "is_pinned": false,
        "is_verified": false,
        "open_external_url_with_in_app_browser": true,
        "click_id": "PAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGnkFSR1HCzqfbC6GnfijBlotC6FEwprEUO0Y6OKnEA_36a9EVKpBExF9Q-4rY_aem_G0DwgvO2G-Mtq2_CtYq2NA",
        "creation_source": "NONE"
      }
    ],
    "is_call_to_action_enabled": false,
    "is_business": true,
    "biography_with_entities": {
      "raw_text": "Step into wonder and find your inner explorer with National Geographic 🌎",
      "entities": []
    },
    "show_shoppable_feed": false,
    "seller_shoppable_feed_type": "none",
    "is_profile_picture_expansion_enabled": true,
    "show_schools_badge": null,
    "text_post_app_badge_label": "natgeo",
    "text_post_new_post_count": 5,
    "text_post_app_joiner_number": 672534,
    "text_post_app_joiner_number_label": "672,534",
    "recon_features": {
      "enable_recon_cta": true
    },
    "media_count": 31529,
    "trial_clips_rate_limiting": {
      "warning_title": "You can share one more trial reel",
      "at_limit_title": "You've reached the limit",
      "warning_body": "You've almost reached the limit. Once you share this trial reel, you'll need to wait up to 24 hours to start using trial reels again.",
      "at_limit_body": "You've shared the maximum number of trial reels allowed within 24 hours. You can share this reel to everyone now as a regular reel or wait up to 24 hours to share it as a trial reel.",
      "count": 20
    },
    "is_prime_onboarding_account": false,
    "is_onboarding_account": false,
    "show_ring_award": false,
    "ring_creator_metadata": {},
    "is_verified": true,
    "is_ring_creator": false,
    "is_private": false,
    "birthday_today_visibility_for_viewer": "NOT_VISIBLE",
    "following_count": 193,
    "follower_count": 274988955,
    "fbid_v2": 17841400573960012,
    "pk_id": "787132",
    "feed_post_reshare_disabled": false,
    "has_ever_selected_topics": false,
    "has_nme_badge": false,
    "third_party_downloads_enabled": 2,
    "show_fb_link_on_profile": false,
    "show_fb_page_link_on_profile": false,
    "can_hide_category": true,
    "can_hide_public_contacts": true,
    "primary_profile_link_type": 0,
    "is_recon_ad_cta_on_profile_eligible_with_viewer": true,
    "current_catalog_id": null,
    "mini_shop_seller_onboarding_status": null,
    "ads_incentive_expiration_date": null,
    "ads_page_id": null,
    "ads_page_name": null,
    "account_category": "",
    "can_add_fb_group_link_on_profile": false,
    "can_use_affiliate_partnership_messaging_as_creator": false,
    "can_use_affiliate_partnership_messaging_as_brand": false,
    "has_gen_ai_personas_for_profile_banner": false,
    "has_guides": false,
    "highlight_reshare_disabled": false,
    "include_direct_blacklist_status": true,
    "is_direct_roll_call_enabled": true,
    "is_eligible_for_meta_verified_links_in_reels": false,
    "is_eligible_for_post_boost_mv_upsell": false,
    "is_meta_verified_related_accounts_display_enabled": false,
    "is_new_to_instagram": false,
    "is_profile_broadcast_sharing_enabled": true,
    "is_secondary_account_creation": false,
    "profile_type": 0,
    "is_coppa_enforced": false,
    "is_auto_confirm_enabled_for_all_reciprocal_follow_requests": false,
    "views_on_grid_status": "SHOW_VIEWS_ON_GRID",
    "is_bestie": false,
    "latest_reel_media": 1775659002,
    "latest_besties_reel_media": 0,
    "account_badges": [],
    "has_highlight_reels": true,
    "is_creator_agent_enabled": false,
    "interop_messaging_user_fbid": 113671860027320,
    "profile_pic_id": "3865702555259028436_787132",
    "has_anonymous_profile_picture": false,
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
    "hd_profile_pic_url_info": {
      "height": 1080,
      "url": "https://scontent-mia3-2.cdninstagram.com/...",
      "width": 1080
    },
    "hd_profile_pic_versions": [
      {
        "height": 320,
        "url": "https://scontent-mia3-2.cdninstagram.com/...",
        "width": 320
      },
      {
        "height": 640,
        "url": "https://scontent-mia3-2.cdninstagram.com/...",
        "width": 640
      }
    ],
    "is_active_on_text_post_app": true,
    "is_cannes": false,
    "is_facebook_onboarded_charity": false,
    "is_favorite": false,
    "merchant_checkout_style": "none",
    "show_account_transparency_details": true,
    "transparency_product_enabled": false,
    "text_app_last_visited_time": null,
    "is_eligible_for_slide": false,
    "live_subscription_status": "default",
    "business_contact_method": "UNKNOWN",
    "category_id": "0",
    "city_id": "0",
    "city_name": "",
    "direct_messaging": "UNKNOWN",
    "instagram_location_id": "",
    "page_id": null,
    "public_email": "",
    "public_phone_country_code": "",
    "public_phone_number": "",
    "should_show_category": false,
    "should_show_public_contacts": true,
    "zip": "",
    "contact_phone_number": "",
    "has_music_on_profile": false,
    "has_videos": true,
    "has_views_fetching": true,
    "is_category_tappable": false,
    "is_eligible_for_creator_product_links": false,
    "is_eligible_for_lead_center": true,
    "is_eligible_for_schools_search_upsell": false,
    "is_eligible_for_smb_support_flow": true,
    "lead_details_app_id": "com.bloks.www.ig.smb.lead_gen.subpage",
    "num_of_admined_pages": null,
    "page_name": "National Geographic",
    "professional_conversion_suggested_account_type": 3,
    "profile_context": "",
    "smb_support_partner": null,
    "show_all_highlights_as_selected_in_management_screen": false,
    "trial_clips_enabled": false,
    "enable_add_school_in_edit_profile": false,
    "shopping_post_onboard_nux_type": null,
    "fb_page_call_to_action_id": "",
    "address_street": "",
    "is_profile_audio_call_enabled": false,
    "displayed_action_button_partner": null,
    "smb_delivery_partner": null,
    "smb_support_delivery_partner": null,
    "displayed_action_button_type": null,
    "category": "",
    "external_lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGnm_6iuVNOrgkWAoxRp4U6UbwtEt0I2Gczb4W_jHLq2TmsCqHUYulbqzPlDlY_aem_-O6ptuge92cQXiA-i3OUSw&e=AT7XtxASb3LWxjCtmAKtf2VMP1P7VcOQVQtOljalj8hh9iZ1L0zEG9owBRqXDgdu7K6tWEcosU_uAwg18lYkS63qX8Ch8suz2irfmUep6w",
    "external_url": "http://visitstore.bio/natgeo",
    "active_standalone_fundraisers": {
      "total_count": 0,
      "fundraisers": []
    },
    "additional_business_addresses": [],
    "allow_manage_memorialization": false,
    "auto_expand_chaining": false,
    "avatar_status": {
      "has_avatar": false
    },
    "broadcast_chat_preference_status": {
      "json_response": "{\"status\":\"ok\",\"status_code\":\"200\",\"is_broadcast_chat_creator\":true,\"notification_setting_type\":2}",
      "is_broadcast_chat_creator": true,
      "notification_setting_type": 2
    },
    "can_use_branded_content_discovery_as_brand": false,
    "can_use_branded_content_discovery_as_creator": false,
    "can_use_paid_partnership_messaging_as_creator": false,
    "chaining_upsell_cards": [],
    "charity_profile_fundraiser_info": {
      "pk": 787132,
      "has_active_fundraiser": false,
      "is_facebook_onboarded_charity": false,
      "consumption_sheet_config": {
        "can_viewer_donate": false,
        "currency": null,
        "donation_disabled_message": null,
        "donation_url": null,
        "has_viewer_donated": null,
        "privacy_disclaimer": null,
        "profile_fundraiser_id": null,
        "you_donated_message": null,
        "donation_amount_config": {
          "default_selected_donation_value": null,
          "donation_amount_selector_values": [],
          "maximum_donation_amount": null,
          "minimum_donation_amount": null,
          "prefill_amount": null,
          "user_currency": null
        }
      }
    },
    "creator_shopping_info": {
      "linked_merchant_accounts": []
    },
    "follow_friction_type": 0,
    "has_active_charity_business_profile_fundraiser": false,
    "has_chaining": true,
    "has_collab_collections": false,
    "has_exclusive_feed_content": false,
    "instagram_pk": "787132",
    "is_profile_search_enabled": false,
    "is_eligible_for_diverse_owned_business_info": false,
    "is_eligible_for_meta_verified_links_in_post": false,
    "is_eligible_for_meta_verified_enhanced_link_sheet": false,
    "is_eligible_for_meta_verified_enhanced_link_sheet_consumption": false,
    "is_eligible_for_meta_verified_multiple_addresses_creation": false,
    "is_eligible_for_meta_verified_multiple_addresses_consumption": false,
    "is_eligible_for_meta_verified_related_accounts": false,
    "meta_verified_related_accounts_count": 0,
    "is_eligible_to_display_diverse_owned_business_info": false,
    "is_eligible_to_host_profile_reels_ads": false,
    "is_favorite_for_clips": false,
    "is_favorite_for_highlights": false,
    "is_in_canada": false,
    "is_interest_account": true,
    "is_memorialized": false,
    "is_potential_business": false,
    "is_regulated_news_in_viewer_location": false,
    "is_remix_setting_enabled_for_posts": true,
    "is_remix_setting_enabled_for_reels": true,
    "is_regulated_c18": false,
    "profile_overlay_info": {
      "overlay_format": "NONE",
      "bloks_payload": null
    },
    "is_stories_teaser_muted": false,
    "is_supervision_features_enabled": false,
    "is_whatsapp_linked": false,
    "mutual_followers_count": 0,
    "nametag": {
      "available_theme_colors": [
        -1,
        7747834,
        13828293
      ],
      "background_image_url": "",
      "emoji": "😀",
      "emoji_color": 0,
      "gradient": 2,
      "is_background_image_blurred": false,
      "mode": 0,
      "selected_theme_color": -1,
      "selfie_sticker": 0,
      "selfie_url": "",
      "theme_color": {
        "available_theme_colors": [
          {
            "display_label": "Default",
            "int_value": -1
          },
          {
            "display_label": "Purple",
            "int_value": 7747834
          },
          {
            "display_label": "Lavender",
            "int_value": 13828293
          }
        ],
        "selected_theme_color": {
          "display_label": "Default",
          "int_value": -1
        }
      }
    },
    "not_meta_verified_friction_info": {
      "label_friction_content": "Not Meta Verified",
      "is_eligible_for_label_friction": false
    },
    "open_external_url_with_in_app_browser": true,
    "pinned_channels_info": {
      "has_public_channels": false,
      "pinned_channels_list": []
    },
    "profile_context_facepile_users": [],
    "profile_context_links_with_user_ids": [],
    "profile_pic_genai_tool_info": [],
    "pronouns": [],
    "relevant_news_regulation_locations": [],
    "remove_message_entrypoint": false,
    "request_contact_enabled": false,
    "show_blue_badge_on_main_profile": true,
    "show_ig_app_switcher_badge": true,
    "disable_profile_shop_cta": false,
    "show_text_post_app_badge": true,
    "show_text_post_app_switcher_badge": true,
    "spam_follower_setting_enabled": true,
    "total_ar_effects": 0,
    "total_clips_count": 1,
    "upcoming_events": [],
    "whatsapp_number": "",
    "recs_from_friends": {
      "enable_recs_from_friends": false,
      "recs_from_friends_entry_point_type": "banner"
    },
    "adjusted_banners_order": [],
    "has_visible_media_notes": true,
    "is_open_to_collab": false,
    "is_daily_limit_blocking": false,
    "threads_profile_glyph_url": "barcelona://user?username=natgeo&xmt=AQF0KHM_Z05WaAHrbXBIh4vKnd3XqMmqQeE__OOluggOS2k",
    "is_oregon_custom_gender_consented": false,
    "profile_reels_sorting_eligibility": "CHECK_VIEWER_QE",
    "nonpro_can_maybe_see_profile_hypercard": false,
    "should_show_tagged_tab": true,
    "posts_subscription_status": "default",
    "reels_subscription_status": "default",
    "stories_subscription_status": "default",
    "is_profile_wa_calling_enabled": false,
    "wa_calling_option_for_wa_linked": 0,
    "wa_calling_option_for_legacy_num": 0,
    "is_eligible_for_meta_verified_ig_self_profile_not_verified_badge": false,
    "has_private_collections": true,
    "is_guardian_r_account_cannes_pair": false,
    "can_see_support_inbox": null,
    "has_fan_club_subscriptions": false,
    "show_wa_link_on_profile": false,
    "meta_verified_benefits_info": {
      "active_meta_verified_benefits": [],
      "is_eligible_for_meta_verified_content_protection": false,
      "is_eligible_for_ig_meta_verified_label": false
    },
    "existing_user_age_collection_enabled": true,
    "has_public_tab_threads": true,
    "is_eligible_for_meta_verified_label": true,
    "is_favorite_for_stories": false,
    "is_parenting_account": false,
    "show_post_insights_entry_point": true,
    "short_drama_creator": null,
    "short_drama_series_playlist_id": null,
    "short_drama_series_episode_count": null,
    "short_drama_series_seed_media_id": null,
    "short_drama_series_title": null,
    "short_drama_role": "NONE",
    "short_drama_series_profiles": [],
    "short_drama_producer_account": null,
    "moonshot_joiner_number": null,
    "is_creator_marketplace_badge_visible": false,
    "creator_marketplace_accounts_reached_metric": null,
    "school_affiliated_account_viewer_status": null,
    "qa_freeform_banner": null,
    "qa_freeform_banner_available_prompts": [
      {
        "prompt": "CURRENT_OBSESSION",
        "display_text": "Current obsession"
      },
      {
        "prompt": "DREAM_DESTINATION",
        "display_text": "Dream destination"
      },
      {
        "prompt": "PLAYING",
        "display_text": "Playing"
      }
    ],
    "qa_freeform_banner_transparency": "The banner is visible to everyone on and off Instagram.",
    "can_message_pinned_carrera_interest_owner": true
  },
  "status": "ok"
}
```

</details>

---

### GET /v2/user/clips

Get user clips. Returns a list of Media objects (Reels).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | No | Id of user account |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/clips?user_id=787132"
    # Next page: add &page_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_clips_v2(user_id="787132")
    # Next page: cl.user_clips_v2(user_id="787132", page_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/user/clips",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "page_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/clips?user_id=787132",
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
    "items": [
      {
        "media": {
          "strong_id__": "3870025531093850440_1029649300",
          "id": "3870025531093850440_1029649300",
          "disable_caption_and_comment": false,
          "fbid": 18064241420343903,
          "deleted_reason": 0,
          "client_cache_key": "Mzg3MDAyNTUzMTA5Mzg1MDQ0MA==.3",
          "integrity_review_decision": "pending",
          "pk": "3870025531093850440",
          "is_affiliate_commission_eligible": false,
          "has_delayed_metadata": false,
          "mezql_token": "",
          "should_request_ads": false,
          "has_privately_liked": false,
          "is_quiet_post": false,
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
                  4454,
                  8908,
                  13363
                ],
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-sof1-2.cdninstagram.com/...",
                "width": 640,
                "is_spatial_image": false
              },
              "igtv_first_frame": {
                "estimated_scans_sizes": [
                  4454,
                  8908,
                  13363
                ],
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-sof1-2.cdninstagram.com/...",
                "width": 640,
                "is_spatial_image": false
              },
              "smart_frame": null
            },
            "candidates": [
              {
                "estimated_scans_sizes": [
                  18248,
                  36496,
                  54745
                ],
                "height": 1333,
                "scans_profile": "e35",
                "url": "https://scontent-sof1-2.cdninstagram.com/...",
                "width": 750,
                "is_spatial_image": false
              }
            ],
            "scrubber_spritesheet_info_candidates": {
              "default": {
                "file_size_kb": 271,
                "max_thumbnails_per_sprite": 105,
                "rendered_width": 96,
                "sprite_height": 1232,
                "sprite_urls": [
                  "https://scontent-sof1-2.cdninstagram.com/v/t51.71878-15/661377490_4446710915609804_6368747692439450584_n.jpg?_nc_ht=scontent-sof1-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gEixL83Z5KiJ_iRMhIy4JCE9_C7GisHlLVTc2BONvjGxPHztmm3_6NKA1Z3dEYmE_Y&_nc_ohc=8YQN_m5Qfl0Q7kNvwEF_OU4&_nc_gid=ZzZyTEbgW85SzY4i4v6PEw&edm=ACHbZRIBAAAA&ccb=7-5&oh=00_Af0zXuY2rLjffwT-ALm1TPFaMtL48GgM7ktR24ezTOGrUw&oe=69DC46C6&_nc_sid=c024bc"
                ],
                "sprite_width": 1500,
                "thumbnail_duration": 0.578352380952381,
                "thumbnail_height": 176,
                "thumbnail_width": 100,
                "thumbnails_per_row": 15,
                "total_thumbnail_num_per_sprite": 105,
                "video_length": 60.727
              }
            }
          },
          "media_type": 2,
          "original_width": 720,
          "original_height": 1280,
          "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiOGY0M2QyZWY2ZjdjNDM1ZDgzM2QwNjdmMGNlM2NmYzIzODcwMDI1NTMxMDkzODUwNDQwIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTAxNDk3NHwzODcwMDI1NTMxMDkzODUwNDQwfDMyNjg5NTMzMTkwfDM5MzIwZGNlMTU4OGNhZDBlZTM0MDYxYzI0MGFmMTAxYTA5OTg0ZjE5ODgyZDM0MWJiNzFiNzQyYjUzYWE1MzIifSwic2lnbmF0dXJlIjoiIn0=",
          "music_metadata": null,
          "has_tagged_users": true,
          "clips_tab_pinned_user_ids": [],
          "original_lang_for_translations": "en",
          "is_open_to_public_submission": false,
          "is_social_ufi_disabled": false,
          "timeline_pinned_user_ids": [],
          "taken_at": 1775566804,
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
          "is_eligible_for_poe": false,
          "is_eligible_for_organic_eager_refresh": false,
          "commerce_integrity_review_decision": "",
          "is_reuse_allowed": false,
          "logging_info_token": "GCAyZWJhNGI0ZGMzOTE0ZmExYmU4ODZkZTU3N2Y0ZWNmYngDcnZhAA==",
          "boost_unavailable_identifier": null,
          "boost_unavailable_reason": null,
          "boost_unavailable_reason_v2": null,
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
              "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/..."
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
          "reshare_count": 11778,
          "ig_media_sharing_disabled": false,
          "media_repost_count": 1214,
          "view_state_item_type": 128,
          "like_count": 51261,
          "top_likers": [],
          "hidden_likes_string_variant": -1,
          "caption": {
            "strong_id__": "18064245098343903",
            "bit_flags": 0,
            "created_at": 1775566807,
            "created_at_utc": 1775566807,
            "did_report_as_spam": false,
            "is_ranked_comment": false,
            "pk": "18064245098343903",
            "share_enabled": false,
            "content_type": "comment",
            "media_id": 3870025531093850440,
            "status": "Active",
            "type": 1,
            "user_id": 1029649300,
            "text": "Intruder alert! 🚨 Murder Hornets eat bees and their larvae, but these Asian honey bees aren't going to let their hive be destroyed without a fight. \n\n#SecretsOfTheBees is now streaming on @DisneyPlus and @hulu",
            "user": {
              "strong_id__": "1029649300",
              "pk": 1029649300,
              "pk_id": "1029649300",
              "id": "1029649300",
              "is_unpublished": false,
              "fbid_v2": 17841400519016088,
              "username": "natgeoanimals",
              "full_name": "National Geographic Animals",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3865698702530758137_1029649300",
              "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/..."
            },
            "is_covered": false,
            "private_reply_status": 0
          },
          "comment_count": 499,
          "comment_inform_treatment": {
            "action_type": null,
            "should_have_inform_treatment": false,
            "text": "",
            "url": null
          },
          "is_photo_comments_composer_enabled_for_author": false,
          "hide_view_all_comment_entrypoint": true,
          "locations": [],
          "play_count": 2626058,
          "ig_play_count": 2626058,
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
          "video_duration": 60.736000061035156,
          "is_dash_eligible": 1,
          "video_versions": [
            {
              "bandwidth": 1579353,
              "height": 1280,
              "id": "4284559321859069v",
              "type": 101,
              "url": "https://scontent-sof1-2.cdninstagram.com/...",
              "url_expiration_timestamp_us": null,
              "width": 720,
              "fallback": null
            }
          ],
          "number_of_qualities": 7,
          "video_codec": "vp09.00.30.08.00.01.01.01.00",
          "sharing_friction_info": {
            "should_have_sharing_friction": false,
            "bloks_app_url": null,
            "sharing_friction_payload": null
          },
          "gen_ai_detection_method": {
            "detection_method": "NONE"
          },
          "clips_demotion_control": {
            "title": "Not interested",
            "enable_word_wrapping": true,
            "confirmation_icon": "none",
            "title_style": "normal",
            "confirmation_title": "Post hidden",
            "confirmation_body": "We'll suggest fewer posts like this.",
            "confirmation_title_style": "large_left",
            "undo_style": "top_right",
            "confirmation_style": "bottomsheet",
            "followup_options": [
              {
                "text": "Don't suggest posts from natgeoanimals",
                "style": null,
                "id": "dislike_author",
                "data": "author_id:1029649300",
                "show_icon": true,
                "demotion_control": {
                  "confirmation_style": "bottomsheet",
                  "confirmation_icon": "eye-off-pano",
                  "confirmation_body": "We won't suggest posts from natgeoanimals.",
                  "undo_style": "inline"
                },
                "subtitle": null
              },
              {
                "text": "Don't suggest posts with certain words",
                "id": "hide_all_specific_words",
                "show_icon": true,
                "data": null,
                "style": null,
                "demotion_control": null,
                "subtitle": null
              },
              {
                "text": "Manage content preferences",
                "id": "control_center",
                "show_icon": true,
                "data": null,
                "style": null,
                "demotion_control": null,
                "subtitle": null
              }
            ]
          },
          "user": {
            "pk": "1029649300",
            "id": "1029649300",
            "username": "natgeoanimals",
            "full_name": "National Geographic Animals",
            "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/...",
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
          "code": "DW1F7dciplI",
          "device_timestamp": 177556301582,
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
          "is_comments_gif_composer_enabled": false,
          "video_url": "https://scontent-sof1-2.cdninstagram.com/...",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                18248,
                36496,
                54745
              ],
              "height": 1333,
              "scans_profile": "e35",
              "url": "https://scontent-sof1-2.cdninstagram.com/...",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "thumbnail_url": "https://scontent-sof1-2.cdninstagram.com/...",
          "location": null,
          "usertags": [],
          "taken_at_ts": 1775566804,
          "sponsor_tags": []
        }
      },
      {
        "media": {
          "strong_id__": "3869494020385423326_787132",
          "id": "3869494020385423326_787132",
          "disable_caption_and_comment": false,
          "fbid": 18312636319285904,
          "deleted_reason": 0,
          "client_cache_key": "Mzg2OTQ5NDAyMDM4NTQyMzMyNg==.3",
          "integrity_review_decision": "pending",
          "pk": "3869494020385423326",
          "is_affiliate_commission_eligible": false,
          "has_delayed_metadata": false,
          "mezql_token": "",
          "should_request_ads": false,
          "has_privately_liked": false,
          "is_quiet_post": false,
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
                  3860,
                  7721,
                  11582
                ],
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-sof1-2.cdninstagram.com/...",
                "width": 640,
                "is_spatial_image": false
              },
              "igtv_first_frame": {
                "estimated_scans_sizes": [
                  3860,
                  7721,
                  11582
                ],
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-sof1-2.cdninstagram.com/...",
                "width": 640,
                "is_spatial_image": false
              },
              "smart_frame": null
            },
            "candidates": [
              {
                "estimated_scans_sizes": [
                  13479,
                  26958,
                  40438
                ],
                "height": 1333,
                "scans_profile": "e35",
                "url": "https://scontent-sof1-1.cdninstagram.com/...",
                "width": 750,
                "is_spatial_image": false
              }
            ],
            "scrubber_spritesheet_info_candidates": {
              "default": {
                "file_size_kb": 276,
                "max_thumbnails_per_sprite": 105,
                "rendered_width": 96,
                "sprite_height": 1232,
                "sprite_urls": [
                  "https://scontent-sof1-2.cdninstagram.com/v/t51.71878-15/660026027_948875084508987_6617144121092333726_n.jpg?_nc_ht=scontent-sof1-2.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gEixL83Z5KiJ_iRMhIy4JCE9_C7GisHlLVTc2BONvjGxPHztmm3_6NKA1Z3dEYmE_Y&_nc_ohc=a82HNH3lYl8Q7kNvwH4vWQp&_nc_gid=ZzZyTEbgW85SzY4i4v6PEw&edm=ACHbZRIBAAAA&ccb=7-5&oh=00_Af3Py_0FsMOaQd9x4YOIEsRFRy69gtKWmd61ieyeZkujRg&oe=69DC6F24&_nc_sid=c024bc"
                ],
                "sprite_width": 1500,
                "thumbnail_duration": 0.5279047619047619,
                "thumbnail_height": 176,
                "thumbnail_width": 100,
                "thumbnails_per_row": 15,
                "total_thumbnail_num_per_sprite": 105,
                "video_length": 55.43
              }
            }
          },
          "media_type": 2,
          "original_width": 720,
          "original_height": 1280,
          "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiOGY0M2QyZWY2ZjdjNDM1ZDgzM2QwNjdmMGNlM2NmYzIzODY5NDk0MDIwMzg1NDIzMzI2Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTAxNDk5MnwzODY5NDk0MDIwMzg1NDIzMzI2fDMyNjg5NTMzMTkwfGIzNjE5MDM0OGExMTA5MTliMmE5YTlhYjliZGUzNGEyZWQ5YjNjYzk0YjM5NzVkMGU5MTM4NjUzNzQ1MDM5Y2MifSwic2lnbmF0dXJlIjoiIn0=",
          "music_metadata": null,
          "has_tagged_users": true,
          "clips_tab_pinned_user_ids": [],
          "original_lang_for_translations": "en",
          "is_open_to_public_submission": false,
          "is_social_ufi_disabled": false,
          "timeline_pinned_user_ids": [],
          "taken_at": 1775502016,
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
          "is_reuse_allowed": false,
          "logging_info_token": "GCAyZWJhNGI0ZGMzOTE0ZmExYmU4ODZkZTU3N2Y0ZWNmYngDcnZhAA==",
          "boost_unavailable_identifier": null,
          "boost_unavailable_reason": null,
          "boost_unavailable_reason_v2": null,
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
              "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/..."
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
              "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/..."
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
          "reshare_count": 471,
          "ig_media_sharing_disabled": false,
          "media_repost_count": 169,
          "view_state_item_type": 128,
          "like_count": 11175,
          "top_likers": [],
          "hidden_likes_string_variant": -1,
          "caption": {
            "strong_id__": "18312640027285904",
            "bit_flags": 0,
            "created_at": 1775502018,
            "created_at_utc": 1775502018,
            "did_report_as_spam": false,
            "is_ranked_comment": false,
            "pk": "18312640027285904",
            "share_enabled": false,
            "content_type": "comment",
            "media_id": 3869494020385423326,
            "status": "Active",
            "type": 1,
            "user_id": 787132,
            "text": "In Hoppers, Piper Curda’s character Mabel explored her sense of wonder for the natural world with the help of hopping technology. For now, we still have to do it the old-fashioned way.\n\nSee Disney and Pixar’s new movie Hoppers, now playing, only in theaters, and step into wonder with National Geographic’s #EarthMonth collection on @DisneyPlus.",
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
              "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/..."
            },
            "is_covered": false,
            "private_reply_status": 0
          },
          "comment_count": 65,
          "comment_inform_treatment": {
            "action_type": null,
            "should_have_inform_treatment": false,
            "text": "",
            "url": null
          },
          "is_photo_comments_composer_enabled_for_author": false,
          "hide_view_all_comment_entrypoint": true,
          "locations": [],
          "play_count": 1496295,
          "ig_play_count": 1496295,
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
          "video_duration": 55.44499969482422,
          "is_dash_eligible": 1,
          "video_versions": [
            {
              "bandwidth": 1113315,
              "height": 1280,
              "id": "2358585431274531v",
              "type": 101,
              "url": "https://scontent-sof1-2.cdninstagram.com/...",
              "url_expiration_timestamp_us": null,
              "width": 720,
              "fallback": null
            }
          ],
          "number_of_qualities": 7,
          "video_codec": "vp09.00.31.08.00.01.01.01.00",
          "sharing_friction_info": {
            "should_have_sharing_friction": false,
            "bloks_app_url": null,
            "sharing_friction_payload": null
          },
          "gen_ai_detection_method": {
            "detection_method": "NONE"
          },
          "clips_demotion_control": {
            "title": "Not interested",
            "enable_word_wrapping": true,
            "confirmation_icon": "none",
            "title_style": "normal",
            "confirmation_title": "Post hidden",
            "confirmation_body": "We'll suggest fewer posts like this.",
            "confirmation_title_style": "large_left",
            "undo_style": "top_right",
            "confirmation_style": "bottomsheet",
            "followup_options": [
              {
                "text": "Don't suggest posts from natgeo",
                "style": null,
                "id": "dislike_author",
                "data": "author_id:787132",
                "show_icon": true,
                "demotion_control": {
                  "confirmation_style": "bottomsheet",
                  "confirmation_icon": "eye-off-pano",
                  "confirmation_body": "We won't suggest posts from natgeo.",
                  "undo_style": "inline"
                },
                "subtitle": null
              },
              {
                "text": "Don't suggest posts with certain words",
                "id": "hide_all_specific_words",
                "show_icon": true,
                "data": null,
                "style": null,
                "demotion_control": null,
                "subtitle": null
              },
              {
                "text": "Manage content preferences",
                "id": "control_center",
                "show_icon": true,
                "data": null,
                "style": null,
                "demotion_control": null,
                "subtitle": null
              }
            ]
          },
          "user": {
            "pk": "787132",
            "id": "787132",
            "username": "natgeo",
            "full_name": "National Geographic",
            "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/...",
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
          "code": "DWzNE9hkj_e",
          "device_timestamp": 1775502016,
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
          "is_comments_gif_composer_enabled": false,
          "video_url": "https://scontent-sof1-2.cdninstagram.com/...",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                13479,
                26958,
                40438
              ],
              "height": 1333,
              "scans_profile": "e35",
              "url": "https://scontent-sof1-1.cdninstagram.com/...",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "thumbnail_url": "https://scontent-sof1-1.cdninstagram.com/...",
          "location": null,
          "usertags": [],
          "taken_at_ts": 1775502016,
          "sponsor_tags": []
        }
      },
      {
        "media": {
          "strong_id__": "3868170261056492782_787132",
          "id": "3868170261056492782_787132",
          "disable_caption_and_comment": false,
          "fbid": 18083128910064008,
          "deleted_reason": 0,
          "client_cache_key": "Mzg2ODE3MDI2MTA1NjQ5Mjc4Mg==.3",
          "integrity_review_decision": "pending",
          "pk": "3868170261056492782",
          "is_affiliate_commission_eligible": false,
          "has_delayed_metadata": false,
          "mezql_token": "",
          "should_request_ads": false,
          "has_privately_liked": false,
          "is_quiet_post": false,
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
                  4541,
                  9082,
                  13624
                ],
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-sof1-2.cdninstagram.com/...",
                "width": 640,
                "is_spatial_image": false
              },
              "igtv_first_frame": {
                "estimated_scans_sizes": [
                  4541,
                  9082,
                  13624
                ],
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-sof1-2.cdninstagram.com/...",
                "width": 640,
                "is_spatial_image": false
              },
              "smart_frame": null
            },
            "candidates": [
              {
                "estimated_scans_sizes": [
                  18831,
                  37662,
                  56494
                ],
                "height": 1333,
                "scans_profile": "e35",
                "url": "https://scontent-sof1-2.cdninstagram.com/...",
                "width": 750,
                "is_spatial_image": false
              }
            ],
            "scrubber_spritesheet_info_candidates": {
              "default": {
                "file_size_kb": 274,
                "max_thumbnails_per_sprite": 105,
                "rendered_width": 96,
                "sprite_height": 1232,
                "sprite_urls": [
                  "https://scontent-sof1-1.cdninstagram.com/v/t51.71878-15/661407041_2382063302308753_1177647765954686603_n.jpg?_nc_ht=scontent-sof1-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gEixL83Z5KiJ_iRMhIy4JCE9_C7GisHlLVTc2BONvjGxPHztmm3_6NKA1Z3dEYmE_Y&_nc_ohc=n5iQezOC2T8Q7kNvwGr1iLN&_nc_gid=ZzZyTEbgW85SzY4i4v6PEw&edm=ACHbZRIBAAAA&ccb=7-5&oh=00_Af32Y5jPSqhW58Ktji_wtdUePBY_ktm3GGdN2Idb_BjR0A&oe=69DC5D1E&_nc_sid=c024bc"
                ],
                "sprite_width": 1500,
                "thumbnail_duration": 0.4560095238095238,
                "thumbnail_height": 176,
                "thumbnail_width": 100,
                "thumbnails_per_row": 15,
                "total_thumbnail_num_per_sprite": 105,
                "video_length": 47.881
              }
            }
          },
          "media_type": 2,
          "original_width": 720,
          "original_height": 1280,
          "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiOGY0M2QyZWY2ZjdjNDM1ZDgzM2QwNjdmMGNlM2NmYzIzODY4MTcwMjYxMDU2NDkyNzgyIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTAxNDk5M3wzODY4MTcwMjYxMDU2NDkyNzgyfDMyNjg5NTMzMTkwfDhiMjhjNWMwMDk2M2EzYmNlY2IxZWU4OGI5NjI1NjVhMzg1M2NhZjk4Mzg4Y2NkMTc0NmZlNWJmZDg2M2FmMDMifSwic2lnbmF0dXJlIjoiIn0=",
          "music_metadata": null,
          "has_tagged_users": true,
          "clips_tab_pinned_user_ids": [],
          "original_lang_for_translations": "en",
          "is_open_to_public_submission": false,
          "is_social_ufi_disabled": false,
          "timeline_pinned_user_ids": [],
          "taken_at": 1775404810,
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
          "is_reuse_allowed": false,
          "logging_info_token": "GCAyZWJhNGI0ZGMzOTE0ZmExYmU4ODZkZTU3N2Y0ZWNmYngDcnZhAA==",
          "boost_unavailable_identifier": null,
          "boost_unavailable_reason": null,
          "boost_unavailable_reason_v2": null,
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
              "profile_pic_url": "https://scontent-sof1-1.cdninstagram.com/..."
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
          "reshare_count": 154,
          "ig_media_sharing_disabled": false,
          "media_repost_count": 91,
          "view_state_item_type": 128,
          "like_count": 7490,
          "top_likers": [],
          "hidden_likes_string_variant": -1,
          "caption": {
            "strong_id__": "18083194658064008",
            "bit_flags": 0,
            "created_at": 1775404813,
            "created_at_utc": 1775404813,
            "did_report_as_spam": false,
            "is_ranked_comment": false,
            "pk": "18083194658064008",
            "share_enabled": false,
            "content_type": "comment",
            "media_id": 3868170261056492782,
            "status": "Active",
            "type": 1,
            "user_id": 787132,
            "text": "Spotted hyenas are a powerful example of the resilience and strength found in nature. For wildlife ecologist, conservation scientist, and National Geographic Explorer Dr. Christine Wilkinson (@christine_eleanor), these reminders are what wonder is all about. \n\n#StepIntoWonder with National Geographic’s #EarthMonth collection on @DisneyPlus.",
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
              "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/..."
            },
            "is_covered": false,
            "private_reply_status": 0
          },
          "comment_count": 78,
          "comment_inform_treatment": {
            "action_type": null,
            "should_have_inform_treatment": false,
            "text": "",
            "url": null
          },
          "is_photo_comments_composer_enabled_for_author": false,
          "hide_view_all_comment_entrypoint": true,
          "locations": [],
          "play_count": 1307792,
          "ig_play_count": 1307792,
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
          "video_duration": 47.893001556396484,
          "is_dash_eligible": 1,
          "video_versions": [
            {
              "bandwidth": 1064730,
              "height": 1280,
              "id": "799234956583164v",
              "type": 101,
              "url": "https://scontent-sof1-2.cdninstagram.com/...",
              "url_expiration_timestamp_us": null,
              "width": 720,
              "fallback": null
            }
          ],
          "number_of_qualities": 7,
          "video_codec": "vp09.00.31.08.00.01.01.01.00",
          "sharing_friction_info": {
            "should_have_sharing_friction": false,
            "bloks_app_url": null,
            "sharing_friction_payload": null
          },
          "gen_ai_detection_method": {
            "detection_method": "NONE"
          },
          "clips_demotion_control": {
            "title": "Not interested",
            "enable_word_wrapping": true,
            "confirmation_icon": "none",
            "title_style": "normal",
            "confirmation_title": "Post hidden",
            "confirmation_body": "We'll suggest fewer posts like this.",
            "confirmation_title_style": "large_left",
            "undo_style": "top_right",
            "confirmation_style": "bottomsheet",
            "followup_options": [
              {
                "text": "Don't suggest posts from natgeo",
                "style": null,
                "id": "dislike_author",
                "data": "author_id:787132",
                "show_icon": true,
                "demotion_control": {
                  "confirmation_style": "bottomsheet",
                  "confirmation_icon": "eye-off-pano",
                  "confirmation_body": "We won't suggest posts from natgeo.",
                  "undo_style": "inline"
                },
                "subtitle": null
              },
              {
                "text": "Don't suggest posts with certain words",
                "id": "hide_all_specific_words",
                "show_icon": true,
                "data": null,
                "style": null,
                "demotion_control": null,
                "subtitle": null
              },
              {
                "text": "Manage content preferences",
                "id": "control_center",
                "show_icon": true,
                "data": null,
                "style": null,
                "demotion_control": null,
                "subtitle": null
              }
            ]
          },
          "user": {
            "pk": "787132",
            "id": "787132",
            "username": "natgeo",
            "full_name": "National Geographic",
            "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/...",
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
          "code": "DWugFulAJTu",
          "device_timestamp": 1775404810,
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
          "is_comments_gif_composer_enabled": false,
          "video_url": "https://scontent-sof1-2.cdninstagram.com/...",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                18831,
                37662,
                56494
              ],
              "height": 1333,
              "scans_profile": "e35",
              "url": "https://scontent-sof1-2.cdninstagram.com/...",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "thumbnail_url": "https://scontent-sof1-2.cdninstagram.com/...",
          "location": null,
          "usertags": [],
          "taken_at_ts": 1775404810,
          "sponsor_tags": []
        }
      }
    ],
    "paging_info": {
      "max_id": "QVFDbDVDUGFoY2tWNW10Uk05N1NoTDE3Zk5GU2RvM1hINWRtdTB6TEFXZDlRbC1IeDZjYmRSdWlYT2x4VlU3X0FaWE5yRUtEdHBNYUJ5QkE1OVNsXzdqNw==",
      "more_available": true
    },
    "status": "ok"
  },
  "next_page_id": "QVFDbDVDUGFoY2tWNW10Uk05N1NoTDE3Zk5GU2RvM1hINWRtdTB6TEFXZDlRbC1IeDZjYmRSdWlYT2x4VlU3X0FaWE5yRUtEdHBNYUJ5QkE1OVNsXzdqNw=="
}
```

</details>

---

### GET /v2/user/explore/businesses/by/id

Get list of recommended accounts for business category of the user by his id. Returns recommended accounts.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/explore/businesses/by/id?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_explore_businesses_by_id_v2(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/user/explore/businesses/by/id",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/explore/businesses/by/id?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "category_id": 0,
  "items": [
    {
      "user": {
        "strong_id__": "5445218106",
        "pk": 5445218106,
        "pk_id": "5445218106",
        "fbid_v2": 17841405343200652,
        "third_party_downloads_enabled": 1,
        "can_hide_category": true,
        "can_hide_public_contacts": true,
        "id": "5445218106",
        "profile_pic_id": "1511834005069211669_5445218106",
        "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/...",
        "is_verified": false,
        "username": "the_scientist_magazine",
        "full_name": "The Scientist Magazine",
        "is_private": false,
        "has_anonymous_profile_picture": false,
        "latest_reel_media": 1775657053,
        "account_badges": [],
        "should_show_category": true,
        "category_id": "2233",
        "is_category_tappable": true,
        "should_show_public_contacts": true,
        "category": "Media/news company"
      },
      "media_previews": [
        {
          "media_id": 3865741383072792696,
          "media_fbid": 18074569283561933,
          "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/..."
        },
        {
          "media_id": 3844028826083372791,
          "media_fbid": 17955279509935029,
          "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/..."
        },
        {
          "media_id": 3823762571422659053,
          "media_fbid": 18164166292407419,
          "thumbnail_url": "https://scontent-lax3-2.cdninstagram.com/..."
        }
      ]
    },
    {
      "user": {
        "strong_id__": "41706552435",
        "pk": 41706552435,
        "pk_id": "41706552435",
        "fbid_v2": 17841441533073319,
        "third_party_downloads_enabled": 1,
        "can_hide_category": true,
        "can_hide_public_contacts": true,
        "id": "41706552435",
        "profile_pic_id": "3515614788425463673_41706552435",
        "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
        "is_verified": false,
        "username": "sciencex.physorg",
        "full_name": "Science X / Phys.org",
        "is_private": false,
        "has_anonymous_profile_picture": false,
        "latest_reel_media": 1775664429,
        "account_badges": [],
        "should_show_category": true,
        "category_id": "2233",
        "is_category_tappable": true,
        "should_show_public_contacts": false,
        "category": "Media/news company"
      },
      "media_previews": [
        {
          "media_id": 3870906408494091231,
          "media_fbid": 17951325804110134,
          "thumbnail_url": "https://scontent-lax3-2.cdninstagram.com/..."
        },
        {
          "media_id": 3870815828120322159,
          "media_fbid": 18195445549358591,
          "thumbnail_url": "https://scontent-lax3-2.cdninstagram.com/..."
        },
        {
          "media_id": 3870725212590124942,
          "media_fbid": 18078129377179314,
          "thumbnail_url": "https://scontent-lax3-2.cdninstagram.com/..."
        }
      ]
    },
    {
      "user": {
        "strong_id__": "68012770661",
        "pk": 68012770661,
        "pk_id": "68012770661",
        "fbid_v2": 17841467999841596,
        "third_party_downloads_enabled": 1,
        "can_hide_category": true,
        "can_hide_public_contacts": true,
        "id": "68012770661",
        "profile_pic_id": "3865708778020840707_68012770661",
        "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/...",
        "is_verified": false,
        "username": "natgeofamily",
        "full_name": "National Geographic Family",
        "is_private": false,
        "has_anonymous_profile_picture": false,
        "latest_reel_media": 1775653578,
        "account_badges": [],
        "should_show_category": true,
        "category_id": "191684877517919",
        "is_category_tappable": true,
        "should_show_public_contacts": false,
        "category": "Publisher"
      },
      "media_previews": [
        {
          "media_id": 3859246065955483507,
          "media_fbid": 18089268776270434,
          "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/..."
        },
        {
          "media_id": 3870269251261738850,
          "media_fbid": 18091692406918779,
          "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/..."
        },
        {
          "media_id": 3869291641157022329,
          "media_fbid": 17993445389947253,
          "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/..."
        }
      ]
    }
  ],
  "status": "ok"
}
```

</details>

---

### GET /v2/user/followers

Get part (one page) of followers users with cursor. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | No | Id of user account |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/followers?user_id=787132"
    # Next page: add &page_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_followers_v2(user_id="787132")
    # Next page: cl.user_followers_v2(user_id="787132", page_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/user/followers",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "page_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/followers?user_id=787132",
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
        "pk": "32456705511",
        "id": "32456705511",
        "username": "was_wildanimalssurvival",
        "full_name": "Wild Animals Survival",
        "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false,
        "account_badges": null,
        "fbid_v2": null,
        "has_anonymous_profile_picture": null,
        "latest_reel_media": 0,
        "pk_id": null,
        "profile_pic_id": null,
        "strong_id__": null,
        "third_party_downloads_enabled": null,
        "reel": {
          "id": "32456705511",
          "expiring_at": 1775755421,
          "has_pride_media": false,
          "latest_reel_media": 0,
          "seen": null,
          "owner": {
            "__typename": "GraphUser",
            "id": "32456705511",
            "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/...",
            "username": "was_wildanimalssurvival"
          }
        },
        "followed_by_viewer": false,
        "follows_viewer": false,
        "requested_by_viewer": false
      },
      {
        "pk": "39324947303",
        "id": "39324947303",
        "username": "jeans.jcs",
        "full_name": "Jean",
        "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": true,
        "is_verified": false,
        "account_badges": null,
        "fbid_v2": null,
        "has_anonymous_profile_picture": null,
        "latest_reel_media": null,
        "pk_id": null,
        "profile_pic_id": null,
        "strong_id__": null,
        "third_party_downloads_enabled": null,
        "reel": {
          "id": "39324947303",
          "expiring_at": 1775755421,
          "has_pride_media": false,
          "latest_reel_media": null,
          "seen": null,
          "owner": {
            "__typename": "GraphUser",
            "id": "39324947303",
            "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/...",
            "username": "jeans.jcs"
          }
        },
        "followed_by_viewer": false,
        "follows_viewer": false,
        "requested_by_viewer": false
      },
      {
        "pk": "37609441463",
        "id": "37609441463",
        "username": "megisbe",
        "full_name": "Megan",
        "profile_pic_url": "https://instagram.fcau13-1.fna.fbcdn.net/v/t51.2885-19/573323465_1219825463302212_7278921664109726296_n.png?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=instagram.fcau13-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gFG1WWORGUVMDLlSZa4UBnzz8IU32EqmT98EaBar_qlpeMiyD0-VB4jJSFnF0FJ0h0&_nc_ohc=xpiLrADWZlUQ7kNvwE0zbQd&_nc_gid=lGpAp1TvpxZhEpZB_CvmXg&edm=AL4D0a4BAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.3-ccb7-5&oh=00_Af2v4WZQ3jpjxa7RMWvRxqp3PmaJjBeywfbWvaisFJpcGw&oe=69DC6EAA&_nc_sid=9e8221",
        "profile_pic_url_hd": null,
        "is_private": true,
        "is_verified": false,
        "account_badges": null,
        "fbid_v2": null,
        "has_anonymous_profile_picture": null,
        "latest_reel_media": null,
        "pk_id": null,
        "profile_pic_id": null,
        "strong_id__": null,
        "third_party_downloads_enabled": null,
        "reel": {
          "id": "37609441463",
          "expiring_at": 1775755421,
          "has_pride_media": false,
          "latest_reel_media": null,
          "seen": null,
          "owner": {
            "__typename": "GraphUser",
            "id": "37609441463",
            "profile_pic_url": "https://instagram.fcau13-1.fna.fbcdn.net/v/t51.2885-19/573323465_1219825463302212_7278921664109726296_n.png?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=instagram.fcau13-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gFG1WWORGUVMDLlSZa4UBnzz8IU32EqmT98EaBar_qlpeMiyD0-VB4jJSFnF0FJ0h0&_nc_ohc=xpiLrADWZlUQ7kNvwE0zbQd&_nc_gid=lGpAp1TvpxZhEpZB_CvmXg&edm=AL4D0a4BAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.3-ccb7-5&oh=00_Af2v4WZQ3jpjxa7RMWvRxqp3PmaJjBeywfbWvaisFJpcGw&oe=69DC6EAA&_nc_sid=9e8221",
            "username": "megisbe"
          }
        },
        "followed_by_viewer": false,
        "follows_viewer": false,
        "requested_by_viewer": false
      }
    ],
    "big_list": null,
    "page_size": null,
    "next_max_id": null,
    "has_more": null,
    "should_limit_list_of_followers": null,
    "use_clickable_see_more": null,
    "show_spam_follow_request_tab": null,
    "status": null
  },
  "next_page_id": "QVFETUZtTGJraVZqMzJ1TU0tMENvNVBsbEVWUUMzOHJDcUxLZWs3WjV1Rjg3TzdfMFZBeVpVS2Z6QlNWNDFKS1kwS25tNUpnRldNVzdsTHBaS3J1WTVMSQ=="
}
```

</details>

---

### GET /v2/user/following

Get part (one page) of following users. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | No | Id of user account |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/following?user_id=787132"
    # Next page: add &page_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_following_v2(user_id="787132")
    # Next page: cl.user_following_v2(user_id="787132", page_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/user/following",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "page_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/following?user_id=787132",
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
        "strong_id__": "14331657700",
        "pk": "14331657700",
        "pk_id": "14331657700",
        "id": "14331657700",
        "fbid_v2": 17841414211021457,
        "third_party_downloads_enabled": 1,
        "profile_pic_id": "2073867961613189688_14331657700",
        "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/...",
        "is_verified": false,
        "username": "natgeomagjp",
        "full_name": "ナショナルジオグラフィック日本版",
        "is_private": false,
        "has_anonymous_profile_picture": false,
        "account_badges": [],
        "latest_reel_media": 0,
        "is_favorite": false
      },
      {
        "strong_id__": "8958735",
        "pk": "8958735",
        "pk_id": "8958735",
        "id": "8958735",
        "fbid_v2": 17841401882050139,
        "third_party_downloads_enabled": 2,
        "profile_pic_id": "3354861487016662033_8958735",
        "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/...",
        "is_verified": true,
        "username": "christiehemmklok",
        "full_name": "Christie Hemm Klok",
        "is_private": false,
        "has_anonymous_profile_picture": false,
        "account_badges": [],
        "latest_reel_media": 0,
        "is_favorite": false
      },
      {
        "strong_id__": "2558720332",
        "pk": "2558720332",
        "pk_id": "2558720332",
        "id": "2558720332",
        "fbid_v2": 17841402409979840,
        "third_party_downloads_enabled": 1,
        "profile_pic_id": "3358229400727377822_2558720332",
        "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/...",
        "is_verified": true,
        "username": "natgeouk",
        "full_name": "National Geographic UK",
        "is_private": false,
        "has_anonymous_profile_picture": false,
        "account_badges": [],
        "latest_reel_media": 0,
        "is_favorite": false
      }
    ],
    "big_list": true,
    "page_size": 25,
    "next_max_id": "25",
    "has_more": true,
    "should_limit_list_of_followers": false,
    "use_clickable_see_more": false,
    "follow_ranking_token": "5de8222f07044483a35fc76341d21637|38589907806|osr",
    "status": "ok"
  },
  "next_page_id": "25"
}
```

</details>

---

### GET /v2/user/highlights

⚠️ Billing: 2 requests per call. Returns a list of Highlight objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `amount` | integer | No | Amount |
| `force` | boolean | No | Skip account privacy check |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/highlights?user_id=1114341851"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_highlights_v2(user_id="1114341851")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/user/highlights",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "1114341851"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/highlights?user_id=1114341851",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "tray": [
      {
        "strong_id__": "highlight:18415168747119768",
        "id": "highlight:18415168747119768",
        "reel_type": "highlight_reel",
        "title": "Australia 25",
        "created_at": 1760617676,
        "is_pinned_highlight": false,
        "prefetch_count": 0,
        "highlight_reel_type": "DEFAULT",
        "is_converted_to_clips": false,
        "is_nux": false,
        "can_gif_quick_reply": true,
        "can_reshare": true,
        "is_archived": false,
        "cover_media": {
          "crop_rect": [
            0,
            0.21843291995490413,
            1
          ],
          "media_id": "3738052766552968887_1114341851",
          "upload_id": null,
          "cropped_image_version": {
            "height": 150,
            "scans_profile": "",
            "url": "https://scontent-vie1-1.cdninstagram.com/...",
            "width": 150
          },
          "full_image_version": null
        },
        "ranked_position": -1760617676,
        "seen_ranked_position": -1760617676,
        "media_count": 100,
        "updated_timestamp": 1760617676,
        "latest_reel_media": 1760084710,
        "seen": null,
        "can_reply": true,
        "can_react_with_avatar": false,
        "contains_stitched_media_blocked_by_rm": false,
        "user": {
          "strong_id__": "1114341851",
          "pk": "1114341851",
          "pk_id": "1114341851",
          "id": "1114341851",
          "username": "nilova.mila",
          "full_name": "Mila Nilova | Путешествия, Семья, Дом, Творчество, Хоумскулинг",
          "is_private": false,
          "is_verified": false,
          "profile_pic_id": "3798513769124094296_1114341851",
          "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/...",
          "account_badges": [],
          "interop_messaging_user_fbid": 115919179800872,
          "is_creator_agent_enabled": false
        },
        "pk": "18415168747119768",
        "items": []
      },
      {
        "strong_id__": "highlight:17977344911917324",
        "id": "highlight:17977344911917324",
        "reel_type": "highlight_reel",
        "title": "Australia 25",
        "created_at": 1759698558,
        "is_pinned_highlight": false,
        "prefetch_count": 0,
        "highlight_reel_type": "DEFAULT",
        "is_converted_to_clips": false,
        "is_nux": false,
        "can_gif_quick_reply": true,
        "can_reshare": true,
        "is_archived": false,
        "cover_media": {
          "crop_rect": [
            0,
            0.26942567567567566,
            1
          ],
          "media_id": "3735181374413487831_1114341851",
          "upload_id": null,
          "cropped_image_version": {
            "height": 150,
            "scans_profile": "",
            "url": "https://scontent-vie1-1.cdninstagram.com/...",
            "width": 150
          },
          "full_image_version": null
        },
        "ranked_position": -1759698558,
        "seen_ranked_position": -1759698558,
        "media_count": 80,
        "updated_timestamp": 1759698558,
        "latest_reel_media": 1759656472,
        "seen": null,
        "can_reply": true,
        "can_react_with_avatar": false,
        "contains_stitched_media_blocked_by_rm": false,
        "user": {
          "strong_id__": "1114341851",
          "pk": "1114341851",
          "pk_id": "1114341851",
          "id": "1114341851",
          "username": "nilova.mila",
          "full_name": "Mila Nilova | Путешествия, Семья, Дом, Творчество, Хоумскулинг",
          "is_private": false,
          "is_verified": false,
          "profile_pic_id": "3798513769124094296_1114341851",
          "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/...",
          "account_badges": [],
          "interop_messaging_user_fbid": 115919179800872,
          "is_creator_agent_enabled": false
        },
        "pk": "17977344911917324",
        "items": []
      },
      {
        "strong_id__": "highlight:17934466041066904",
        "id": "highlight:17934466041066904",
        "reel_type": "highlight_reel",
        "title": "Australia 25",
        "created_at": 1759322098,
        "is_pinned_highlight": false,
        "prefetch_count": 0,
        "highlight_reel_type": "DEFAULT",
        "is_converted_to_clips": false,
        "is_nux": false,
        "can_gif_quick_reply": true,
        "can_reshare": true,
        "is_archived": false,
        "cover_media": {
          "crop_rect": [
            0,
            0.3217905405405405,
            1
          ],
          "media_id": "3732226846084715516_1114341851",
          "upload_id": null,
          "cropped_image_version": {
            "height": 150,
            "scans_profile": "",
            "url": "https://scontent-vie1-1.cdninstagram.com/...",
            "width": 150
          },
          "full_image_version": null
        },
        "ranked_position": -1759322098,
        "seen_ranked_position": -1759322098,
        "media_count": 100,
        "updated_timestamp": 1759322098,
        "latest_reel_media": 1759239851,
        "seen": null,
        "can_reply": true,
        "can_react_with_avatar": false,
        "contains_stitched_media_blocked_by_rm": false,
        "user": {
          "strong_id__": "1114341851",
          "pk": "1114341851",
          "pk_id": "1114341851",
          "id": "1114341851",
          "username": "nilova.mila",
          "full_name": "Mila Nilova | Путешествия, Семья, Дом, Творчество, Хоумскулинг",
          "is_private": false,
          "is_verified": false,
          "profile_pic_id": "3798513769124094296_1114341851",
          "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/...",
          "account_badges": [],
          "interop_messaging_user_fbid": 115919179800872,
          "is_creator_agent_enabled": false
        },
        "pk": "17934466041066904",
        "items": []
      }
    ],
    "last_paginated_highlights_node_edited_at_ts": null,
    "has_fetched_all_remaining_highlights": null,
    "suggested_highlights": {},
    "cursor": "QVFEUUNmaU95a2g4a1A1R0pjRlpzZGhHdjMyYnYwbjVaNlFDWWxxWUdTQVZaak9fWDg2NVNrQzdCeVpvQlV4S1pSbWYzQ3J4aThUY1hYUXB0R1FCRFVDSg==",
    "highlights_tray_type": "DEFAULT",
    "status": "ok"
  },
  "next_page_id": null
}
```

</details>

---

### GET /v2/user/highlights/by/username

⚠️ Billing: 3 requests per call. Returns a list of Highlight objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |
| `amount` | integer | No | Amount |
| `force` | boolean | No | Skip account privacy check |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/highlights/by/username?username=nike"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_highlights_by_username_v2(username="nike")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/user/highlights/by/username",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"username": "nike"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/highlights/by/username?username=nike",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "tray": [
      {
        "strong_id__": "highlight:17975319242920589",
        "id": "highlight:17975319242920589",
        "reel_type": "highlight_reel",
        "title": "Just Do It",
        "created_at": 1757529224,
        "is_pinned_highlight": false,
        "prefetch_count": 0,
        "highlight_reel_type": "DEFAULT",
        "is_converted_to_clips": false,
        "is_nux": false,
        "can_gif_quick_reply": true,
        "can_reshare": true,
        "is_archived": false,
        "cover_media": {
          "crop_rect": null,
          "media_id": null,
          "upload_id": null,
          "cropped_image_version": {
            "height": 150,
            "scans_profile": "",
            "url": "https://scontent-lax7-1.cdninstagram.com/...",
            "width": 150
          },
          "full_image_version": null
        },
        "ranked_position": -1758300565,
        "seen_ranked_position": -1758300565,
        "media_count": 49,
        "updated_timestamp": 1758300565,
        "latest_reel_media": 1758300505,
        "seen": null,
        "can_reply": true,
        "can_react_with_avatar": false,
        "contains_stitched_media_blocked_by_rm": false,
        "user": {
          "strong_id__": "13460080",
          "pk": "13460080",
          "pk_id": "13460080",
          "id": "13460080",
          "username": "nike",
          "full_name": "Nike",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3727349705534754477_13460080",
          "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/...",
          "account_badges": [],
          "interop_messaging_user_fbid": 113294420064920,
          "is_creator_agent_enabled": false
        },
        "pk": "17975319242920589",
        "items": []
      }
    ],
    "last_paginated_highlights_node_edited_at_ts": null,
    "has_fetched_all_remaining_highlights": null,
    "suggested_highlights": {},
    "cursor": null,
    "highlights_tray_type": "DEFAULT",
    "status": "ok"
  },
  "next_page_id": null
}
```

</details>

---

### GET /v2/user/stories

⚠️ Billing: 2 requests per call. Returns a list of Story objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `force` | boolean | No | Skip account privacy check |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/stories?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_stories_v2(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/user/stories",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/stories?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "broadcast": null,
  "reel": {
    "id": 787132,
    "strong_id__": "787132",
    "latest_reel_media": 1775659002,
    "seen": 0,
    "can_reply": false,
    "can_gif_quick_reply": true,
    "can_reshare": true,
    "reel_type": "user_reel",
    "ad_expiry_timestamp_in_millis": null,
    "is_cta_sticker_available": null,
    "should_treat_link_sticker_as_cta": null,
    "pool_refresh_ttl_in_sec": null,
    "can_react_with_avatar": false,
    "prefetch_count": 0,
    "expiring_at": 1775745402,
    "user": {
      "strong_id__": "787132",
      "pk": 787132,
      "pk_id": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "is_private": false,
      "is_ring_creator": false,
      "show_ring_award": false,
      "is_verified": true,
      "profile_pic_id": "3865702555259028436_787132",
      "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/...",
      "interop_messaging_user_fbid": 113671860027320,
      "is_creator_agent_enabled": false,
      "transparency_product_enabled": false,
      "is_screenshot_blocking_enabled": false
    },
    "items": [
      {
        "strong_id__": "3870828041672894129_787132",
        "id": "3870828041672894129_787132",
        "expiring_at": 1775745075,
        "pk": 3870828041672894129,
        "is_visual_reply_commenter_notice_enabled": true,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_reel_media": true,
        "fbid": 18311197711278628,
        "mezql_token": "",
        "should_request_ads": false,
        "is_terminal_video_segment": false,
        "integrity_review_decision": "pending",
        "client_cache_key": "Mzg3MDgyODA0MTY3Mjg5NDEyOQ==.3",
        "has_privately_liked": false,
        "user": {
          "strong_id__": "787132",
          "id": "787132",
          "pk": 787132,
          "fbid_v2": 17841400573960012,
          "pk_id": "787132",
          "eligible_for_text_app_activation_badge": false,
          "account_type": 2,
          "is_private": false,
          "account_badges": [],
          "full_name": "National Geographic",
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/...",
          "username": "natgeo",
          "user_activation_info": {}
        },
        "shop_routing_user_id": null,
        "subscribe_cta_visible": false,
        "commenting_disabled_for_viewer": true,
        "hide_view_all_comment_entrypoint": false,
        "caption": null,
        "is_dash_eligible": 1,
        "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
        "number_of_qualities": 8,
        "video_versions": [
          {
            "bandwidth": 1746448,
            "height": 1280,
            "id": "26262506683371587v",
            "type": 101,
            "url": "https://scontent-iad6-1.cdninstagram.com/...",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          }
        ],
        "video_duration": 14.965999603271484,
        "has_audio": true,
        "can_see_insights_as_brand": false,
        "media_type": 2,
        "original_media_type": 2,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "sharing_friction_info": {
          "bloks_app_url": null,
          "should_have_sharing_friction": false,
          "sharing_friction_payload": null
        },
        "has_translation": false,
        "sponsor_tags": [
          {
            "permission": false,
            "sponsor_id": null,
            "username": null,
            "is_pending": false,
            "sponsor": {
              "strong_id__": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/...",
              "is_unpublished": false,
              "follower_count": 34037491
            }
          }
        ],
        "coauthor_producers": [],
        "media_overlay_info": null,
        "profile_grid_control_enabled": false,
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                3902,
                7804,
                11707
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-iad6-1.cdninstagram.com/...",
              "width": 640,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                3902,
                7804,
                11707
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-iad6-1.cdninstagram.com/...",
              "width": 640,
              "is_spatial_image": false
            }
          ]
        },
        "original_width": 1080,
        "original_height": 1920,
        "is_paid_partnership": true,
        "music_metadata": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiZGMyMmU0YTE2ZjQ2NGViOGI5ZGI5MDgzZTEzMDdkZTUzODcwODI4MDQxNjcyODk0MTI5Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTAxMjkxOXwzODcwODI4MDQxNjcyODk0MTI5fDI5NzcyMzAwODI0fGUwMTA5YWNhZjJmYTFlNzU5ZTkzYjc0MmViYTI2YjQ4MGE2ZmFlNzg3N2ZiMzMxYjMzZWRmZjMxNDc0MWEzNTYifSwic2lnbmF0dXJlIjoiIn0=",
        "ig_media_sharing_disabled": false,
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "creative_config": null,
        "cutout_sticker_info": [],
        "can_hype": false,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "is_open_to_public_submission": false,
        "media_attributions_data": [],
        "taken_at": 1775658675,
        "product_type": "story",
        "has_liked": false,
        "can_viewer_save": false,
        "is_organic_product_tagging_eligible": true,
        "device_timestamp": 1775658676503732,
        "code": "DW38ZhqiKax",
        "caption_is_edited": false,
        "original_media_has_visual_reply_media": false,
        "is_quicksnap_recap": false,
        "deleted_reason": 0,
        "is_story_image_with_music": false,
        "filter_type": 0,
        "archive_story_deletion_ts": 0,
        "can_send_prompt": false,
        "is_arirang_prize": false,
        "is_first_take": false,
        "is_from_ayt_clips_inspiration": false,
        "is_from_discovery_surface": false,
        "is_rollcall_v2": false,
        "supports_reel_reactions": true,
        "is_photo_mash_story": false,
        "can_reshare": true,
        "can_reply": false,
        "can_mention_back": false,
        "can_play_spotify_audio": false,
        "is_superlative": false,
        "show_one_tap_fb_share_tooltip": true,
        "can_mention_share": false,
        "is_viewer_mentioned": false,
        "wearables_creator_tools_info": [],
        "wearable_shared_media_resolutions": [],
        "reel_mentions": [
          {
            "end_time_ms": 86400.0,
            "height": 0.0,
            "id": "1517189826474103",
            "is_fb_sticker": 0,
            "is_hidden": 0,
            "is_pinned": 0,
            "is_sticker": 1,
            "rotation": 0.0,
            "start_time_ms": 0.0,
            "width": 0.0,
            "x": 0.0,
            "y": 0.0,
            "z": 0,
            "user": {
              "strong_id__": "304662892",
              "id": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/..."
            }
          }
        ]
      },
      {
        "strong_id__": "3870828324352170239_787132",
        "id": "3870828324352170239_787132",
        "expiring_at": 1775745104,
        "pk": 3870828324352170239,
        "is_visual_reply_commenter_notice_enabled": true,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_reel_media": true,
        "fbid": 18358102888233883,
        "mezql_token": "",
        "should_request_ads": false,
        "is_terminal_video_segment": false,
        "integrity_review_decision": "pending",
        "client_cache_key": "Mzg3MDgyODMyNDM1MjE3MDIzOQ==.3",
        "has_privately_liked": false,
        "user": {
          "strong_id__": "787132",
          "id": "787132",
          "pk": 787132,
          "fbid_v2": 17841400573960012,
          "pk_id": "787132",
          "eligible_for_text_app_activation_badge": false,
          "account_type": 2,
          "is_private": false,
          "account_badges": [],
          "full_name": "National Geographic",
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/...",
          "username": "natgeo",
          "user_activation_info": {}
        },
        "shop_routing_user_id": null,
        "subscribe_cta_visible": false,
        "commenting_disabled_for_viewer": true,
        "hide_view_all_comment_entrypoint": false,
        "caption": null,
        "is_dash_eligible": 1,
        "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
        "number_of_qualities": 8,
        "video_versions": [
          {
            "bandwidth": 1384222,
            "height": 1280,
            "id": "953910417580528v",
            "type": 101,
            "url": "https://scontent-iad6-1.cdninstagram.com/...",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          }
        ],
        "video_duration": 14.965999603271484,
        "has_audio": true,
        "can_see_insights_as_brand": false,
        "media_type": 2,
        "original_media_type": 2,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "sharing_friction_info": {
          "bloks_app_url": null,
          "should_have_sharing_friction": false,
          "sharing_friction_payload": null
        },
        "has_translation": false,
        "sponsor_tags": [
          {
            "permission": false,
            "sponsor_id": null,
            "username": null,
            "is_pending": false,
            "sponsor": {
              "strong_id__": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/...",
              "is_unpublished": false,
              "follower_count": 34037491
            }
          }
        ],
        "coauthor_producers": [],
        "media_overlay_info": null,
        "profile_grid_control_enabled": false,
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                2437,
                4875,
                7313
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-iad6-1.cdninstagram.com/...",
              "width": 640,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                2437,
                4875,
                7313
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-iad6-1.cdninstagram.com/...",
              "width": 640,
              "is_spatial_image": false
            }
          ]
        },
        "original_width": 1080,
        "original_height": 1920,
        "is_paid_partnership": true,
        "music_metadata": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiZGMyMmU0YTE2ZjQ2NGViOGI5ZGI5MDgzZTEzMDdkZTUzODcwODI4MzI0MzUyMTcwMjM5Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTAxMjkxOXwzODcwODI4MzI0MzUyMTcwMjM5fDI5NzcyMzAwODI0fDZjM2U2YTRjZWE5YWNjYWE5MDQ5MDliMTZjMDUwNjZhMmMwNTc2Y2ZmYmM5MDFmNWEwMzM4OGY5OWVkMjE0MWYifSwic2lnbmF0dXJlIjoiIn0=",
        "ig_media_sharing_disabled": false,
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "creative_config": null,
        "cutout_sticker_info": [],
        "can_hype": false,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "is_open_to_public_submission": false,
        "media_attributions_data": [],
        "taken_at": 1775658704,
        "product_type": "story",
        "has_liked": false,
        "can_viewer_save": false,
        "is_organic_product_tagging_eligible": true,
        "device_timestamp": 1775658704503734,
        "code": "DW38do7iBj_",
        "caption_is_edited": false,
        "original_media_has_visual_reply_media": false,
        "is_quicksnap_recap": false,
        "deleted_reason": 0,
        "is_story_image_with_music": false,
        "filter_type": 0,
        "archive_story_deletion_ts": 0,
        "can_send_prompt": false,
        "is_arirang_prize": false,
        "is_first_take": false,
        "is_from_ayt_clips_inspiration": false,
        "is_from_discovery_surface": false,
        "is_rollcall_v2": false,
        "supports_reel_reactions": true,
        "is_photo_mash_story": false,
        "can_reshare": true,
        "can_reply": false,
        "can_mention_back": false,
        "can_play_spotify_audio": false,
        "is_superlative": false,
        "show_one_tap_fb_share_tooltip": true,
        "can_mention_share": false,
        "is_viewer_mentioned": false,
        "wearables_creator_tools_info": [],
        "wearable_shared_media_resolutions": [],
        "reel_mentions": [
          {
            "end_time_ms": 86400.0,
            "height": 0.0,
            "id": "968400145722533",
            "is_fb_sticker": 0,
            "is_hidden": 0,
            "is_pinned": 0,
            "is_sticker": 1,
            "rotation": 0.0,
            "start_time_ms": 0.0,
            "width": 0.0,
            "x": 0.0,
            "y": 0.0,
            "z": 0,
            "user": {
              "strong_id__": "304662892",
              "id": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/..."
            }
          }
        ]
      },
      {
        "strong_id__": "3870828687528621445_787132",
        "id": "3870828687528621445_787132",
        "expiring_at": 1775745136,
        "pk": 3870828687528621445,
        "is_visual_reply_commenter_notice_enabled": true,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_reel_media": true,
        "fbid": 18519178861076290,
        "mezql_token": "",
        "should_request_ads": false,
        "is_terminal_video_segment": false,
        "integrity_review_decision": "pending",
        "client_cache_key": "Mzg3MDgyODY4NzUyODYyMTQ0NQ==.3",
        "has_privately_liked": false,
        "user": {
          "strong_id__": "787132",
          "id": "787132",
          "pk": 787132,
          "fbid_v2": 17841400573960012,
          "pk_id": "787132",
          "eligible_for_text_app_activation_badge": false,
          "account_type": 2,
          "is_private": false,
          "account_badges": [],
          "full_name": "National Geographic",
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/...",
          "username": "natgeo",
          "user_activation_info": {}
        },
        "shop_routing_user_id": null,
        "subscribe_cta_visible": false,
        "commenting_disabled_for_viewer": true,
        "hide_view_all_comment_entrypoint": false,
        "caption": null,
        "is_dash_eligible": 1,
        "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
        "number_of_qualities": 8,
        "video_versions": [
          {
            "bandwidth": 1699428,
            "height": 1280,
            "id": "1446825286910099v",
            "type": 101,
            "url": "https://scontent-iad6-1.cdninstagram.com/...",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          }
        ],
        "video_duration": 13.732999801635742,
        "has_audio": true,
        "can_see_insights_as_brand": false,
        "media_type": 2,
        "original_media_type": 2,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "sharing_friction_info": {
          "bloks_app_url": null,
          "should_have_sharing_friction": false,
          "sharing_friction_payload": null
        },
        "has_translation": false,
        "sponsor_tags": [
          {
            "permission": false,
            "sponsor_id": null,
            "username": null,
            "is_pending": false,
            "sponsor": {
              "strong_id__": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/...",
              "is_unpublished": false,
              "follower_count": 34037491
            }
          }
        ],
        "coauthor_producers": [],
        "media_overlay_info": null,
        "profile_grid_control_enabled": false,
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                2419,
                4839,
                7259
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-iad6-1.cdninstagram.com/...",
              "width": 640,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                2419,
                4839,
                7259
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-iad6-1.cdninstagram.com/...",
              "width": 640,
              "is_spatial_image": false
            }
          ]
        },
        "original_width": 1080,
        "original_height": 1920,
        "is_paid_partnership": true,
        "music_metadata": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiZGMyMmU0YTE2ZjQ2NGViOGI5ZGI5MDgzZTEzMDdkZTUzODcwODI4Njg3NTI4NjIxNDQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTAxMjkxOXwzODcwODI4Njg3NTI4NjIxNDQ1fDI5NzcyMzAwODI0fDQ0YWYyZWJhNmJmNDc0NDI0MTBhNTIxM2Q1NDY0MWRhMjQ1Y2UwMWEzNGQxODgwNjZjMzhiMjljNWQwYWUxM2IifSwic2lnbmF0dXJlIjoiIn0=",
        "ig_media_sharing_disabled": false,
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "creative_config": null,
        "cutout_sticker_info": [],
        "can_hype": false,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "is_open_to_public_submission": false,
        "media_attributions_data": [],
        "taken_at": 1775658736,
        "product_type": "story",
        "has_liked": false,
        "can_viewer_save": false,
        "is_organic_product_tagging_eligible": true,
        "device_timestamp": 1775658736503736,
        "code": "DW38i7KiPWF",
        "caption_is_edited": false,
        "original_media_has_visual_reply_media": false,
        "is_quicksnap_recap": false,
        "deleted_reason": 0,
        "is_story_image_with_music": false,
        "filter_type": 0,
        "archive_story_deletion_ts": 0,
        "can_send_prompt": false,
        "is_arirang_prize": false,
        "is_first_take": false,
        "is_from_ayt_clips_inspiration": false,
        "is_from_discovery_surface": false,
        "is_rollcall_v2": false,
        "supports_reel_reactions": true,
        "is_photo_mash_story": false,
        "can_reshare": true,
        "can_reply": false,
        "can_mention_back": false,
        "can_play_spotify_audio": false,
        "is_superlative": false,
        "show_one_tap_fb_share_tooltip": true,
        "can_mention_share": false,
        "is_viewer_mentioned": false,
        "wearables_creator_tools_info": [],
        "wearable_shared_media_resolutions": [],
        "reel_mentions": [
          {
            "end_time_ms": 86400.0,
            "height": 0.0,
            "id": "983436374123185",
            "is_fb_sticker": 0,
            "is_hidden": 0,
            "is_pinned": 0,
            "is_sticker": 1,
            "rotation": 0.0,
            "start_time_ms": 0.0,
            "width": 0.0,
            "x": 0.0,
            "y": 0.0,
            "z": 0,
            "user": {
              "strong_id__": "304662892",
              "id": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/..."
            }
          }
        ]
      }
    ],
    "is_nux": false,
    "has_besties_media": false,
    "media_count": 7,
    "media_ids": [
      3870828041672894129,
      3870828324352170239,
      3870828687528621445
    ],
    "has_fan_club_media": false,
    "show_fan_club_stories_teaser": false,
    "is_cacheable": true,
    "disabled_reply_types": [
      "story_remix_reply",
      "story_selfie_reply",
      "story_voice_reply"
    ],
    "is_archived": false,
    "show_expiration_tray_signal": false
  },
  "unviewable_authors_info": null,
  "status": "ok"
}
```

</details>

---

### GET /v2/user/stories/by/username

⚠️ Billing: 3 requests per call. Returns a list of Story objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |
| `force` | boolean | No | Skip account privacy check |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/stories/by/username?username=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_stories_by_username_v2(username="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/user/stories/by/username",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/stories/by/username?username=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "broadcast": null,
  "reel": {
    "id": 787132,
    "strong_id__": "787132",
    "latest_reel_media": 1775659002,
    "seen": 0,
    "can_reply": false,
    "can_gif_quick_reply": true,
    "can_reshare": true,
    "reel_type": "user_reel",
    "ad_expiry_timestamp_in_millis": null,
    "is_cta_sticker_available": null,
    "should_treat_link_sticker_as_cta": null,
    "pool_refresh_ttl_in_sec": null,
    "can_react_with_avatar": false,
    "prefetch_count": 0,
    "expiring_at": 1775745402,
    "user": {
      "strong_id__": "787132",
      "pk": 787132,
      "pk_id": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "is_private": false,
      "is_ring_creator": false,
      "show_ring_award": false,
      "is_verified": true,
      "profile_pic_id": "3865702555259028436_787132",
      "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/...",
      "interop_messaging_user_fbid": 113671860027320,
      "is_creator_agent_enabled": false,
      "transparency_product_enabled": false,
      "is_screenshot_blocking_enabled": false
    },
    "items": [
      {
        "strong_id__": "3870828041672894129_787132",
        "id": "3870828041672894129_787132",
        "expiring_at": 1775745075,
        "pk": 3870828041672894129,
        "is_visual_reply_commenter_notice_enabled": true,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_reel_media": true,
        "fbid": 18311197711278628,
        "mezql_token": "",
        "should_request_ads": false,
        "is_terminal_video_segment": false,
        "integrity_review_decision": "pending",
        "client_cache_key": "Mzg3MDgyODA0MTY3Mjg5NDEyOQ==.3",
        "has_privately_liked": false,
        "user": {
          "strong_id__": "787132",
          "id": "787132",
          "pk": 787132,
          "fbid_v2": 17841400573960012,
          "pk_id": "787132",
          "eligible_for_text_app_activation_badge": false,
          "account_type": 2,
          "is_private": false,
          "account_badges": [],
          "full_name": "National Geographic",
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/...",
          "username": "natgeo",
          "user_activation_info": {}
        },
        "shop_routing_user_id": null,
        "subscribe_cta_visible": false,
        "commenting_disabled_for_viewer": true,
        "hide_view_all_comment_entrypoint": false,
        "caption": null,
        "is_dash_eligible": 1,
        "video_codec": "vp09.00.21.08.00.01.01.01.00",
        "number_of_qualities": 3,
        "video_versions": [
          {
            "bandwidth": 1746448,
            "height": 1280,
            "id": "26262506683371587v",
            "type": 101,
            "url": "https://scontent-lga3-1.cdninstagram.com/...",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          }
        ],
        "video_duration": 15.0,
        "has_audio": true,
        "can_see_insights_as_brand": false,
        "media_type": 2,
        "original_media_type": 2,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "sharing_friction_info": {
          "bloks_app_url": null,
          "should_have_sharing_friction": false,
          "sharing_friction_payload": null
        },
        "has_translation": false,
        "sponsor_tags": [
          {
            "permission": false,
            "sponsor_id": null,
            "username": null,
            "is_pending": false,
            "sponsor": {
              "strong_id__": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/...",
              "is_unpublished": false,
              "follower_count": 34037491
            }
          }
        ],
        "coauthor_producers": [],
        "media_overlay_info": null,
        "profile_grid_control_enabled": false,
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                3902,
                7804,
                11707
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-lga3-3.cdninstagram.com/...",
              "width": 640,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                3902,
                7804,
                11707
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-lga3-3.cdninstagram.com/...",
              "width": 640,
              "is_spatial_image": false
            }
          ]
        },
        "original_width": 720,
        "original_height": 1280,
        "is_paid_partnership": true,
        "music_metadata": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiZDJmYjJlMmU0MWNjNDA3NmExNGQ2NjFiZmUzMDZhYWMzODcwODI4MDQxNjcyODk0MTI5Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTAxNDA0MXwzODcwODI4MDQxNjcyODk0MTI5fDM5MDg5NjM1NjUwfDJmZDZiNzMwYTIxNDk2ZTA4ZWQ5NjQ4MjMwMzM3NTA3M2Q0MzNhYjE4MzhlZmFmMThiYWZjYjlhY2VlOWExNmUifSwic2lnbmF0dXJlIjoiIn0=",
        "ig_media_sharing_disabled": false,
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "creative_config": null,
        "cutout_sticker_info": [],
        "can_hype": false,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "is_open_to_public_submission": false,
        "media_attributions_data": [],
        "taken_at": 1775658675,
        "product_type": "story",
        "has_liked": false,
        "can_viewer_save": false,
        "is_organic_product_tagging_eligible": true,
        "device_timestamp": 1775658676503732,
        "code": "DW38ZhqiKax",
        "caption_is_edited": false,
        "original_media_has_visual_reply_media": false,
        "is_quicksnap_recap": false,
        "deleted_reason": 0,
        "is_story_image_with_music": false,
        "filter_type": 0,
        "archive_story_deletion_ts": 0,
        "can_send_prompt": false,
        "is_arirang_prize": false,
        "is_first_take": false,
        "is_from_ayt_clips_inspiration": false,
        "is_from_discovery_surface": false,
        "is_rollcall_v2": false,
        "supports_reel_reactions": true,
        "is_photo_mash_story": false,
        "can_reshare": true,
        "can_reply": false,
        "can_mention_back": false,
        "can_play_spotify_audio": false,
        "is_superlative": false,
        "show_one_tap_fb_share_tooltip": true,
        "can_mention_share": false,
        "is_viewer_mentioned": false,
        "wearables_creator_tools_info": [],
        "wearable_shared_media_resolutions": [],
        "reel_mentions": [
          {
            "end_time_ms": 86400.0,
            "height": 0.0,
            "id": "1517189826474103",
            "is_fb_sticker": 0,
            "is_hidden": 0,
            "is_pinned": 0,
            "is_sticker": 1,
            "rotation": 0.0,
            "start_time_ms": 0.0,
            "width": 0.0,
            "x": 0.0,
            "y": 0.0,
            "z": 0,
            "user": {
              "strong_id__": "304662892",
              "id": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/..."
            }
          }
        ]
      },
      {
        "strong_id__": "3870828324352170239_787132",
        "id": "3870828324352170239_787132",
        "expiring_at": 1775745104,
        "pk": 3870828324352170239,
        "is_visual_reply_commenter_notice_enabled": true,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_reel_media": true,
        "fbid": 18358102888233883,
        "mezql_token": "",
        "should_request_ads": false,
        "is_terminal_video_segment": false,
        "integrity_review_decision": "pending",
        "client_cache_key": "Mzg3MDgyODMyNDM1MjE3MDIzOQ==.3",
        "has_privately_liked": false,
        "user": {
          "strong_id__": "787132",
          "id": "787132",
          "pk": 787132,
          "fbid_v2": 17841400573960012,
          "pk_id": "787132",
          "eligible_for_text_app_activation_badge": false,
          "account_type": 2,
          "is_private": false,
          "account_badges": [],
          "full_name": "National Geographic",
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/...",
          "username": "natgeo",
          "user_activation_info": {}
        },
        "shop_routing_user_id": null,
        "subscribe_cta_visible": false,
        "commenting_disabled_for_viewer": true,
        "hide_view_all_comment_entrypoint": false,
        "caption": null,
        "is_dash_eligible": 1,
        "video_codec": "vp09.00.21.08.00.01.01.01.00",
        "number_of_qualities": 3,
        "video_versions": [
          {
            "bandwidth": 1384222,
            "height": 1280,
            "id": "953910417580528v",
            "type": 101,
            "url": "https://scontent-lga3-2.cdninstagram.com/...",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          }
        ],
        "video_duration": 15.0,
        "has_audio": true,
        "can_see_insights_as_brand": false,
        "media_type": 2,
        "original_media_type": 2,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "sharing_friction_info": {
          "bloks_app_url": null,
          "should_have_sharing_friction": false,
          "sharing_friction_payload": null
        },
        "has_translation": false,
        "sponsor_tags": [
          {
            "permission": false,
            "sponsor_id": null,
            "username": null,
            "is_pending": false,
            "sponsor": {
              "strong_id__": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/...",
              "is_unpublished": false,
              "follower_count": 34037491
            }
          }
        ],
        "coauthor_producers": [],
        "media_overlay_info": null,
        "profile_grid_control_enabled": false,
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                2437,
                4875,
                7313
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-lga3-3.cdninstagram.com/...",
              "width": 640,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                2437,
                4875,
                7313
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-lga3-3.cdninstagram.com/...",
              "width": 640,
              "is_spatial_image": false
            }
          ]
        },
        "original_width": 720,
        "original_height": 1280,
        "is_paid_partnership": true,
        "music_metadata": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiZDJmYjJlMmU0MWNjNDA3NmExNGQ2NjFiZmUzMDZhYWMzODcwODI4MzI0MzUyMTcwMjM5Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTAxNDA0MXwzODcwODI4MzI0MzUyMTcwMjM5fDM5MDg5NjM1NjUwfDg5ZmEwNmEyN2ZjODQ3NmE5MDY3MzJiYTMxNmRlNjJmZmJhZDZmN2QyOTA3Yjg1NDM4NTY5M2YxOTJkYjgzZjkifSwic2lnbmF0dXJlIjoiIn0=",
        "ig_media_sharing_disabled": false,
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "creative_config": null,
        "cutout_sticker_info": [],
        "can_hype": false,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "is_open_to_public_submission": false,
        "media_attributions_data": [],
        "taken_at": 1775658704,
        "product_type": "story",
        "has_liked": false,
        "can_viewer_save": false,
        "is_organic_product_tagging_eligible": true,
        "device_timestamp": 1775658704503734,
        "code": "DW38do7iBj_",
        "caption_is_edited": false,
        "original_media_has_visual_reply_media": false,
        "is_quicksnap_recap": false,
        "deleted_reason": 0,
        "is_story_image_with_music": false,
        "filter_type": 0,
        "archive_story_deletion_ts": 0,
        "can_send_prompt": false,
        "is_arirang_prize": false,
        "is_first_take": false,
        "is_from_ayt_clips_inspiration": false,
        "is_from_discovery_surface": false,
        "is_rollcall_v2": false,
        "supports_reel_reactions": true,
        "is_photo_mash_story": false,
        "can_reshare": true,
        "can_reply": false,
        "can_mention_back": false,
        "can_play_spotify_audio": false,
        "is_superlative": false,
        "show_one_tap_fb_share_tooltip": true,
        "can_mention_share": false,
        "is_viewer_mentioned": false,
        "wearables_creator_tools_info": [],
        "wearable_shared_media_resolutions": [],
        "reel_mentions": [
          {
            "end_time_ms": 86400.0,
            "height": 0.0,
            "id": "968400145722533",
            "is_fb_sticker": 0,
            "is_hidden": 0,
            "is_pinned": 0,
            "is_sticker": 1,
            "rotation": 0.0,
            "start_time_ms": 0.0,
            "width": 0.0,
            "x": 0.0,
            "y": 0.0,
            "z": 0,
            "user": {
              "strong_id__": "304662892",
              "id": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/..."
            }
          }
        ]
      },
      {
        "strong_id__": "3870828687528621445_787132",
        "id": "3870828687528621445_787132",
        "expiring_at": 1775745136,
        "pk": 3870828687528621445,
        "is_visual_reply_commenter_notice_enabled": true,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_reel_media": true,
        "fbid": 18519178861076290,
        "mezql_token": "",
        "should_request_ads": false,
        "is_terminal_video_segment": false,
        "integrity_review_decision": "pending",
        "client_cache_key": "Mzg3MDgyODY4NzUyODYyMTQ0NQ==.3",
        "has_privately_liked": false,
        "user": {
          "strong_id__": "787132",
          "id": "787132",
          "pk": 787132,
          "fbid_v2": 17841400573960012,
          "pk_id": "787132",
          "eligible_for_text_app_activation_badge": false,
          "account_type": 2,
          "is_private": false,
          "account_badges": [],
          "full_name": "National Geographic",
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/...",
          "username": "natgeo",
          "user_activation_info": {}
        },
        "shop_routing_user_id": null,
        "subscribe_cta_visible": false,
        "commenting_disabled_for_viewer": true,
        "hide_view_all_comment_entrypoint": false,
        "caption": null,
        "is_dash_eligible": 1,
        "video_codec": "vp09.00.21.08.00.01.01.01.00",
        "number_of_qualities": 3,
        "video_versions": [
          {
            "bandwidth": 1699428,
            "height": 1280,
            "id": "1446825286910099v",
            "type": 101,
            "url": "https://scontent-lga3-3.cdninstagram.com/...",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          }
        ],
        "video_duration": 13.765999794006348,
        "has_audio": true,
        "can_see_insights_as_brand": false,
        "media_type": 2,
        "original_media_type": 2,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "sharing_friction_info": {
          "bloks_app_url": null,
          "should_have_sharing_friction": false,
          "sharing_friction_payload": null
        },
        "has_translation": false,
        "sponsor_tags": [
          {
            "permission": false,
            "sponsor_id": null,
            "username": null,
            "is_pending": false,
            "sponsor": {
              "strong_id__": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/...",
              "is_unpublished": false,
              "follower_count": 34037491
            }
          }
        ],
        "coauthor_producers": [],
        "media_overlay_info": null,
        "profile_grid_control_enabled": false,
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                2419,
                4839,
                7259
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-lga3-3.cdninstagram.com/...",
              "width": 640,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                2419,
                4839,
                7259
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-lga3-3.cdninstagram.com/...",
              "width": 640,
              "is_spatial_image": false
            }
          ]
        },
        "original_width": 720,
        "original_height": 1280,
        "is_paid_partnership": true,
        "music_metadata": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiZDJmYjJlMmU0MWNjNDA3NmExNGQ2NjFiZmUzMDZhYWMzODcwODI4Njg3NTI4NjIxNDQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTAxNDA0MXwzODcwODI4Njg3NTI4NjIxNDQ1fDM5MDg5NjM1NjUwfGRmYzlhZDhlODBiZDY0MWNhZDE4Njk0YzM0ZThiZDk5ZDhjZDZkMjQ2Mjc4Y2YwOGQzOGY3MjQ1ZmY5ZGFlODMifSwic2lnbmF0dXJlIjoiIn0=",
        "ig_media_sharing_disabled": false,
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "creative_config": null,
        "cutout_sticker_info": [],
        "can_hype": false,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "is_open_to_public_submission": false,
        "media_attributions_data": [],
        "taken_at": 1775658736,
        "product_type": "story",
        "has_liked": false,
        "can_viewer_save": false,
        "is_organic_product_tagging_eligible": true,
        "device_timestamp": 1775658736503736,
        "code": "DW38i7KiPWF",
        "caption_is_edited": false,
        "original_media_has_visual_reply_media": false,
        "is_quicksnap_recap": false,
        "deleted_reason": 0,
        "is_story_image_with_music": false,
        "filter_type": 0,
        "archive_story_deletion_ts": 0,
        "can_send_prompt": false,
        "is_arirang_prize": false,
        "is_first_take": false,
        "is_from_ayt_clips_inspiration": false,
        "is_from_discovery_surface": false,
        "is_rollcall_v2": false,
        "supports_reel_reactions": true,
        "is_photo_mash_story": false,
        "can_reshare": true,
        "can_reply": false,
        "can_mention_back": false,
        "can_play_spotify_audio": false,
        "is_superlative": false,
        "show_one_tap_fb_share_tooltip": true,
        "can_mention_share": false,
        "is_viewer_mentioned": false,
        "wearables_creator_tools_info": [],
        "wearable_shared_media_resolutions": [],
        "reel_mentions": [
          {
            "end_time_ms": 86400.0,
            "height": 0.0,
            "id": "983436374123185",
            "is_fb_sticker": 0,
            "is_hidden": 0,
            "is_pinned": 0,
            "is_sticker": 1,
            "rotation": 0.0,
            "start_time_ms": 0.0,
            "width": 0.0,
            "x": 0.0,
            "y": 0.0,
            "z": 0,
            "user": {
              "strong_id__": "304662892",
              "id": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/..."
            }
          }
        ]
      }
    ],
    "is_nux": false,
    "has_besties_media": false,
    "media_count": 7,
    "media_ids": [
      3870828041672894129,
      3870828324352170239,
      3870828687528621445
    ],
    "has_fan_club_media": false,
    "show_fan_club_stories_teaser": false,
    "is_cacheable": true,
    "disabled_reply_types": [
      "story_remix_reply",
      "story_selfie_reply",
      "story_voice_reply"
    ],
    "is_archived": false,
    "show_expiration_tray_signal": false
  },
  "unviewable_authors_info": null,
  "status": "ok"
}
```

</details>

---

### GET /v2/user/suggested/profiles

Fetch suggested users details by target_id.

expand_suggestion=True for more detailed response

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `expand_suggestion` | boolean | No | Expand Suggestion |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/suggested/profiles?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_suggested_profiles_v2(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/user/suggested/profiles",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/suggested/profiles?user_id=787132",
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
      "strong_id__": "373961533",
      "pk": 373961533,
      "pk_id": "373961533",
      "id": "373961533",
      "username": "rainforestalliance",
      "full_name": "Rainforest Alliance",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3778293340623238872_373961533",
      "profile_pic_url": "https://scontent-prg1-1.cdninstagram.com/...",
      "chaining_info": {
        "sources": "",
        "algorithm": null
      },
      "profile_chaining_secondary_label": "Rainforest Alliance",
      "social_context": "Rainforest Alliance"
    },
    {
      "strong_id__": "6860189",
      "pk": 6860189,
      "pk_id": "6860189",
      "id": "6860189",
      "username": "lilbieber",
      "full_name": "Justin Bieber",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3723351201745598446_6860189",
      "profile_pic_url": "https://scontent-prg1-1.cdninstagram.com/...",
      "chaining_info": {
        "sources": "",
        "algorithm": null
      },
      "profile_chaining_secondary_label": "Justin Bieber",
      "social_context": "Justin Bieber"
    },
    {
      "strong_id__": "305701719",
      "pk": 305701719,
      "pk_id": "305701719",
      "id": "305701719",
      "username": "jlo",
      "full_name": "Jennifer Lopez",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3832165777018273796_305701719",
      "profile_pic_url": "https://scontent-prg1-1.cdninstagram.com/...",
      "chaining_info": {
        "sources": "",
        "algorithm": null
      },
      "profile_chaining_secondary_label": "Jennifer Lopez",
      "social_context": "Jennifer Lopez"
    }
  ],
  "is_backup": false,
  "is_recommend_account": false,
  "chaining_upsell_cards": [],
  "follow_ranking_token": "1dcf20a616fb4cfc9d3b7cc930d94ab2|35147819905|chaining",
  "status": "ok"
}
```

</details>

---

### GET /v2/user/tag/medias

Get usertag medias

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | No | Id of user account |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/tag/medias?user_id=787132"
    # Next page: add &page_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_tag_medias_v2(user_id="787132")
    # Next page: cl.user_tag_medias_v2(user_id="787132", page_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/user/tag/medias",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    # Next page: add "page_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/tag/medias?user_id=787132",
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
    "num_results": 21,
    "more_available": true,
    "items": [
      {
        "strong_id__": "1929261108986102451_429173",
        "id": "1929261108986102451_429173",
        "fbid": 18006729904037433,
        "deleted_reason": 0,
        "client_cache_key": "MTkyOTI2MTEwODk4NjEwMjQ1MQ==.3",
        "integrity_review_decision": "approved",
        "pk": "1929261108986102451",
        "has_delayed_metadata": false,
        "mezql_token": "",
        "should_request_ads": false,
        "has_privately_liked": false,
        "is_quiet_post": false,
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
                50179,
                100358,
                150537
              ],
              "height": 1334,
              "scans_profile": "e35",
              "url": "https://scontent-sjc3-1.cdninstagram.com/...",
              "width": 1080,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                33759,
                67518,
                101277
              ],
              "height": 926,
              "scans_profile": "e35",
              "url": "https://scontent-sjc3-1.cdninstagram.com/...",
              "width": 750,
              "is_spatial_image": false
            }
          ]
        },
        "media_type": 1,
        "original_width": 1080,
        "original_height": 1334,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiNTAzMjZhNTg1MjFkNDdhMDk0Mjk1MDhkNDM0Yzg5ZTAxOTI5MjYxMTA4OTg2MTAyNDUxIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTAyMjQ4NHwxOTI5MjYxMTA4OTg2MTAyNDUxfDM4ODQxODE0NjI4fDljYmZiMWY2YjA2ODJkM2JiNWRhZTQyMGI4ODU1OTg2YzFkMjU3NTVmNzlkMDgxZGQzM2ZiZDFlOWQ4ZDBkYjcifSwic2lnbmF0dXJlIjoiIn0=",
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
        "taken_at": 1544205867,
        "usertags": [
          {
            "user": {
              "pk": "1709655155",
              "id": "1709655155",
              "username": "fromwhereidrone",
              "full_name": "From Where I Drone®",
              "profile_pic_url": "https://scontent-sjc3-1.cdninstagram.com/...",
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
              "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/...",
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
              "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/...",
              "profile_pic_url_hd": null,
              "is_private": false,
              "is_verified": false
            },
            "x": 0.9319999814000001,
            "y": 0.0912000015
          }
        ],
        "photo_of_you": false,
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
        "is_reuse_allowed": false,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "coauthor_producers": [],
        "coauthor_producer_can_see_organic_insights": false,
        "invited_coauthor_producers": [],
        "product_suggestions": [],
        "igbio_product": null,
        "is_paid_partnership": false,
        "reshare_count": 11,
        "ig_media_sharing_disabled": false,
        "media_repost_count": 2,
        "like_count": 14016,
        "top_likers": [],
        "hidden_likes_string_variant": -1,
        "caption": {
          "strong_id__": "18006729967037433",
          "bit_flags": 0,
          "created_at": 1544205875,
          "created_at_utc": 1544205875,
          "did_report_as_spam": false,
          "is_ranked_comment": false,
          "pk": "18006729967037433",
          "share_enabled": false,
          "content_type": "comment",
          "media_id": 1929261108986102451,
          "status": "Active",
          "type": 1,
          "user_id": 429173,
          "text": "Vardzia is a cave monastery site located in southern Georgia. It is excavated from the slopes of the Erusheti Mountain on the left side of the Kura River. Oh Georgia, I miss you when I look at these images 😭 #georgia #exploregeorgia #MavicPro\n.\n.\n.\n.\n.\n#mymavic #awesome_earthpix #collectivelycreate #exploretocreate #livefolk #beautifuldestinations #iglifecz #folkcreative #exklusive_shot #AGameOfTones #igerscz #discoverglobe #QueekyGrams #ourplanetdaily #adventureculture #welivetoexplore #stayandwander #dnescestujem #droneofficial #droneoftheday #dronesdaily #dji #fromwhereidrone #earthofficial #natgeo #MavicPro @beautifuldestinations @roamtheplanet @earthofficial @earthpix @folkmagazine @liveoutdoor.s @awesomeglobe @awesome.earth @djiglobal @fromwhereidrone @dronestagr.am @droneoftheday @droneofficial @earthstoke @livefolk @global_hotshotz @vzcomood @artofvisuals @majestic_earth_ @folkvibe @welivetoexplore @lastingvisuals @mountainsphoto @theglobewanderer @tentree @awesome.earth @awesomeglobe @ourplanetdaily",
          "user": {
            "strong_id__": "429173",
            "pk": 429173,
            "pk_id": "429173",
            "id": "429173",
            "is_unpublished": false,
            "fbid_v2": 17841401355190006,
            "username": "hynecheck",
            "full_name": "Hynek Hampl",
            "is_private": false,
            "is_verified": false,
            "profile_pic_id": "3301920468198178307_429173",
            "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/..."
          },
          "is_covered": false,
          "private_reply_status": 0
        },
        "comment_count": 579,
        "can_view_more_preview_comments": false,
        "preview_comments": [],
        "comment_likes_enabled": true,
        "comment_inform_treatment": {
          "action_type": null,
          "should_have_inform_treatment": false,
          "text": "",
          "url": null
        },
        "is_photo_comments_composer_enabled_for_author": false,
        "hide_view_all_comment_entrypoint": true,
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
          "pk": "429173",
          "id": "429173",
          "username": "hynecheck",
          "full_name": "Hynek Hampl",
          "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/...",
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
        "caption_is_edited": true,
        "code": "BrGHMHIF8Kz",
        "device_timestamp": 1544205867,
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
              50179,
              100358,
              150537
            ],
            "height": 1334,
            "scans_profile": "e35",
            "url": "https://scontent-sjc3-1.cdninstagram.com/...",
            "width": 1080,
            "is_spatial_image": false
          }
        ],
        "thumbnail_url": "https://scontent-sjc3-1.cdninstagram.com/...",
        "taken_at_ts": 1544205867,
        "sponsor_tags": [],
        "play_count": 0
      },
      {
        "strong_id__": "1929229904589027835_276524869",
        "id": "1929229904589027835_276524869",
        "fbid": 17989037833125917,
        "deleted_reason": 0,
        "client_cache_key": "MTkyOTIyOTkwNDU4OTAyNzgzNQ==.3",
        "integrity_review_decision": "approved",
        "pk": "1929229904589027835",
        "has_delayed_metadata": false,
        "mezql_token": "",
        "should_request_ads": false,
        "has_privately_liked": false,
        "is_quiet_post": false,
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
                16232,
                32464,
                48696
              ],
              "height": 720,
              "scans_profile": "e35",
              "url": "https://scontent-sjc3-1.cdninstagram.com/...",
              "width": 1080,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                10923,
                21846,
                32769
              ],
              "height": 500,
              "scans_profile": "e35",
              "url": "https://scontent-sjc3-1.cdninstagram.com/...",
              "width": 750,
              "is_spatial_image": false
            }
          ]
        },
        "media_type": 1,
        "original_width": 1080,
        "original_height": 720,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiNTAzMjZhNTg1MjFkNDdhMDk0Mjk1MDhkNDM0Yzg5ZTAxOTI5MjI5OTA0NTg5MDI3ODM1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTAyMjUwN3wxOTI5MjI5OTA0NTg5MDI3ODM1fDM4ODQxODE0NjI4fDQ3Yjk5ZDExNWJiZGQ4NWQxYjUwMjA2ZTllNDI5M2E3N2EwNjA5MWFkYWMyOWY0YWE5YTUzYzFhN2E0MTBmMDcifSwic2lnbmF0dXJlIjoiIn0=",
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
        "taken_at": 1544202148,
        "usertags": [
          {
            "user": {
              "pk": "1029649300",
              "id": "1029649300",
              "username": "natgeoanimals",
              "full_name": "National Geographic Animals",
              "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/...",
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
              "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/...",
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
              "profile_pic_url": "https://scontent-sjc3-1.cdninstagram.com/...",
              "profile_pic_url_hd": null,
              "is_private": false,
              "is_verified": false
            },
            "x": 0.5,
            "y": 0.5
          }
        ],
        "photo_of_you": false,
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
        "commerce_integrity_review_decision": "approved",
        "is_reuse_allowed": false,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "coauthor_producers": [],
        "coauthor_producer_can_see_organic_insights": false,
        "invited_coauthor_producers": [],
        "product_suggestions": [],
        "igbio_product": null,
        "is_paid_partnership": false,
        "reshare_count": 1,
        "ig_media_sharing_disabled": false,
        "media_repost_count": 1,
        "like_count": 6172,
        "top_likers": [],
        "hidden_likes_string_variant": -1,
        "caption": {
          "strong_id__": "17989037887125917",
          "bit_flags": 0,
          "created_at": 1544202155,
          "created_at_utc": 1544202155,
          "did_report_as_spam": false,
          "is_ranked_comment": false,
          "pk": "17989037887125917",
          "share_enabled": false,
          "content_type": "comment",
          "media_id": 1929229904589027835,
          "status": "Active",
          "type": 1,
          "user_id": 276524869,
          "text": "No helmet needed once your on Cát Bà Island.\n.\nCát Bà Island || Vietnam\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\nShot on EOS T3i and SIGMA 85mm F1.4 EX DG HSM\nISO 100 | f/1.4 | 1/2000\n——\n#vietnam #vietnamese #vietnamesefood #vietnamflashback #vietnamesegirl #vietnamtravel #vietnamtrip #vietnamesehair #vietnamwar #vietnamesecuisine #vietnamflashbacks #vietnamesecoffee #vietnamfood #Canon #canonphotography #canonphoto #canon6d #canoneos #canonusa #canon70d #canon5dmarkiii #canon5d #canonaustralia #canonphotos #canon7d #canon60d #canon700d #canon5dmarkiv #canonphotographer #canoncanada",
          "user": {
            "strong_id__": "276524869",
            "pk": 276524869,
            "pk_id": "276524869",
            "id": "276524869",
            "is_unpublished": false,
            "fbid_v2": 17841401346074320,
            "username": "samuellemieux",
            "full_name": "Samuel Lemieux",
            "is_private": false,
            "is_verified": false,
            "profile_pic_id": "3460593955377529534_276524869",
            "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/..."
          },
          "is_covered": false,
          "private_reply_status": 0
        },
        "comment_count": 182,
        "can_view_more_preview_comments": false,
        "preview_comments": [],
        "comment_likes_enabled": true,
        "comment_inform_treatment": {
          "action_type": null,
          "should_have_inform_treatment": false,
          "text": "",
          "url": null
        },
        "is_photo_comments_composer_enabled_for_author": false,
        "hide_view_all_comment_entrypoint": true,
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
          "pk": "276524869",
          "id": "276524869",
          "username": "samuellemieux",
          "full_name": "Samuel Lemieux",
          "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/...",
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
        "caption_is_edited": true,
        "code": "BrGAGBxFvn7",
        "device_timestamp": 1544202148,
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
              16232,
              32464,
              48696
            ],
            "height": 720,
            "scans_profile": "e35",
            "url": "https://scontent-sjc3-1.cdninstagram.com/...",
            "width": 1080,
            "is_spatial_image": false
          }
        ],
        "thumbnail_url": "https://scontent-sjc3-1.cdninstagram.com/...",
        "taken_at_ts": 1544202148,
        "sponsor_tags": [],
        "play_count": 0
      },
      {
        "strong_id__": "1929198769279088926_1423130965",
        "id": "1929198769279088926_1423130965",
        "fbid": 17992565425118532,
        "deleted_reason": 0,
        "client_cache_key": "MTkyOTE5ODc2OTI3OTA4ODkyNg==.3",
        "integrity_review_decision": "approved",
        "pk": "1929198769279088926",
        "has_delayed_metadata": false,
        "mezql_token": "",
        "should_request_ads": false,
        "has_privately_liked": false,
        "is_quiet_post": false,
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
                25149,
                50299,
                75448
              ],
              "height": 716,
              "scans_profile": "e35",
              "url": "https://scontent-sjc6-1.cdninstagram.com/...",
              "width": 1080,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                16919,
                33839,
                50759
              ],
              "height": 497,
              "scans_profile": "e35",
              "url": "https://scontent-sjc6-1.cdninstagram.com/...",
              "width": 750,
              "is_spatial_image": false
            }
          ]
        },
        "media_type": 1,
        "original_width": 1080,
        "original_height": 716,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiNTAzMjZhNTg1MjFkNDdhMDk0Mjk1MDhkNDM0Yzg5ZTAxOTI5MTk4NzY5Mjc5MDg4OTI2Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2OTAyMjUwOHwxOTI5MTk4NzY5Mjc5MDg4OTI2fDM4ODQxODE0NjI4fGNiNzM2YTExNzNlYTlmNjM2YjBiYzZjMGRjODhmNTlkMThlYjkzM2ExNjA5MDdiYmRiODE2NTJlYTQyZWIzNmMifSwic2lnbmF0dXJlIjoiIn0=",
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
        "taken_at": 1544198436,
        "usertags": [
          {
            "user": {
              "pk": "20388776",
              "id": "20388776",
              "username": "visittheusa",
              "full_name": "Visit The USA",
              "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/...",
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
              "profile_pic_url": "https://scontent-sjc3-1.cdninstagram.com/...",
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
              "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/...",
              "profile_pic_url_hd": null,
              "is_private": false,
              "is_verified": true
            },
            "x": 0.5124999881,
            "y": 0.267295599
          }
        ],
        "photo_of_you": false,
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
        "is_eligible_for_poe": true,
        "is_eligible_for_organic_eager_refresh": false,
        "commerce_integrity_review_decision": "approved",
        "is_reuse_allowed": false,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "coauthor_producers": [],
        "coauthor_producer_can_see_organic_insights": false,
        "invited_coauthor_producers": [],
        "product_suggestions": [],
        "igbio_product": null,
        "is_paid_partnership": false,
        "reshare_count": 3,
        "ig_media_sharing_disabled": false,
        "media_repost_count": 1,
        "like_count": 5581,
        "top_likers": [],
        "hidden_likes_string_variant": -1,
        "caption": {
          "strong_id__": "17992565452118532",
          "bit_flags": 0,
          "created_at": 1544198440,
          "created_at_utc": 1544198440,
          "did_report_as_spam": false,
          "is_ranked_comment": false,
          "pk": "17992565452118532",
          "share_enabled": false,
          "content_type": "comment",
          "media_id": 1929198769279088926,
          "status": "Active",
          "type": 1,
          "user_id": 1423130965,
          "has_translation": true,
          "text": "☀️Warme Sonnenstrahlen, herrliche Seeluft und weicher Sandstrand - erlebt den ewigen Sommer in Florida😍 Die rund 700 Kilometer lange Landzunge zwischen dem Atlantik und dem Golf von Mexiko wird auch Sunshine State genannt und wird seinem Namen auf jeden Fall gerecht - rund 300 Sonnentage im Jahr kann man in dem US-Bundeststaat genießen.🏝#mycanusa #sunshinestate #visitflorida #florida #exploremore #visittheusa",
          "user": {
            "strong_id__": "1423130965",
            "pk": 1423130965,
            "pk_id": "1423130965",
            "id": "1423130965",
            "is_unpublished": false,
            "fbid_v2": 17841400808972236,
            "username": "canusatouristik",
            "full_name": "CANUSA TOURISTIK 🇺🇸 & 🇨🇦",
            "is_private": false,
            "is_verified": false,
            "profile_pic_id": "2600837206099067919_1423130965",
            "profile_pic_url": "https://scontent-sjc3-1.cdninstagram.com/..."
          },
          "is_covered": false,
          "private_reply_status": 0,
          "text_translation": "☀️Warm sun rays, wonderful sea air and soft sandy beach - experience eternal summer in Florida😍 The 700-kilometer-long landline between the Atlantic and the Gulf of Mexico is also called the Sunshine State and it certainly lives up to its name - around 300 sunny days a year you can enjoy enjoying the U.S. state. 🏝#mycanusa #visitflorida #exploremore #visittheusa"
        },
        "comment_count": 204,
        "can_view_more_preview_comments": false,
        "preview_comments": [],
        "comment_likes_enabled": true,
        "comment_inform_treatment": {
          "action_type": null,
          "should_have_inform_treatment": false,
          "text": "",
          "url": null
        },
        "is_photo_comments_composer_enabled_for_author": false,
        "hide_view_all_comment_entrypoint": true,
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
          "pk": "1423130965",
          "id": "1423130965",
          "username": "canusatouristik",
          "full_name": "CANUSA TOURISTIK 🇺🇸 & 🇨🇦",
          "profile_pic_url": "https://scontent-sjc3-1.cdninstagram.com/...",
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
        "caption_is_edited": true,
        "code": "BrF5A8wADke",
        "device_timestamp": 1544198436,
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
              25149,
              50299,
              75448
            ],
            "height": 716,
            "scans_profile": "e35",
            "url": "https://scontent-sjc6-1.cdninstagram.com/...",
            "width": 1080,
            "is_spatial_image": false
          }
        ],
        "thumbnail_url": "https://scontent-sjc6-1.cdninstagram.com/...",
        "taken_at_ts": 1544198436,
        "sponsor_tags": [],
        "play_count": 0
      }
    ],
    "auto_load_more_enabled": true,
    "next_max_id": 1926933891264902156,
    "new_photos": [],
    "requires_review": false,
    "total_count": 1123,
    "status": "ok"
  },
  "next_page_id": "1926933891264902156"
}
```

</details>

---

### GET /v2/userstream/by/id

Get userstream (info) by id. Returns user stream data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/userstream/by/id?id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.userstream_by_id_v2(id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/userstream/by/id",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/userstream/by/id?id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "stream_rows": [
    {
      "user": {
        "strong_id__": "787132",
        "pk": 787132,
        "id": "787132",
        "full_name": "National Geographic",
        "username": "natgeo",
        "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
        "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/..."
      },
      "status": "ok"
    },
    {
      "user": {
        "strong_id__": "787132",
        "id": "787132",
        "pk": 787132,
        "is_opal_enabled": false,
        "eligible_for_text_app_activation_badge": false,
        "highlights_tray_type": "DEFAULT",
        "account_type": 2,
        "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/...",
        "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
        "bio_links": [
          {
            "link_id": 17954981494900183,
            "url": "http://visitstore.bio/natgeo",
            "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGn7sa0ZbkTFk-SAS1u9Z-LRSNm4GPdIoNSzuOP4uE153tXNbiSgIN5-SAP0X4_aem_yZt27foys9vwTQ-MC75Pgg&e=AT5hEg7JJvYPe5-i4xkpXJjRGqMRpjVADgv6nV9wDvDEhNo1cJKGMlVpCJUVou3nnN1MP37Fcs2A98ZWZCE3iZQ-G4q4f6hpAoyUDrljYw",
            "link_type": "external",
            "title": "",
            "media_type": "none",
            "image_url": "",
            "icon_url": "",
            "media_accent_color_hex": "",
            "is_pinned": false,
            "is_verified": false,
            "open_external_url_with_in_app_browser": true,
            "creation_source": "NONE"
          }
        ],
        "is_call_to_action_enabled": false,
        "is_business": true,
        "biography_with_entities": {
          "raw_text": "Step into wonder and find your inner explorer with National Geographic 🌎",
          "entities": []
        },
        "is_profile_picture_expansion_enabled": true,
        "show_schools_badge": null,
        "text_post_app_badge_label": "natgeo",
        "text_post_new_post_count": 5,
        "text_post_app_joiner_number": 672534,
        "text_post_app_joiner_number_label": "672,534",
        "recon_features": {
          "enable_recon_cta": true
        },
        "media_count": 31529,
        "trial_clips_rate_limiting": {
          "warning_title": "You can share one more trial reel",
          "at_limit_title": "You've reached the limit",
          "warning_body": "You've almost reached the limit. Once you share this trial reel, you'll need to wait up to 24 hours to start using trial reels again.",
          "at_limit_body": "You've shared the maximum number of trial reels allowed within 24 hours. You can share this reel to everyone now as a regular reel or wait up to 24 hours to share it as a trial reel.",
          "count": 20
        },
        "is_prime_onboarding_account": false,
        "is_onboarding_account": false,
        "show_ring_award": false,
        "ring_creator_metadata": {},
        "is_verified": true,
        "is_ring_creator": false,
        "is_private": false,
        "username": "natgeo",
        "full_name": "National Geographic",
        "birthday_today_visibility_for_viewer": "NOT_VISIBLE",
        "following_count": 193,
        "follower_count": 274988954
      },
      "status": "ok"
    },
    {
      "user": {
        "strong_id__": "787132",
        "id": "787132",
        "fbid_v2": 17841400573960012,
        "pk_id": "787132",
        "pk": 787132,
        "eligible_for_text_app_activation_badge": false,
        "feed_post_reshare_disabled": false,
        "has_ever_selected_topics": false,
        "has_nme_badge": false,
        "third_party_downloads_enabled": 2,
        "show_fb_link_on_profile": false,
        "show_fb_page_link_on_profile": false,
        "can_hide_category": true,
        "can_hide_public_contacts": true,
        "is_opal_enabled": false,
        "primary_profile_link_type": 0,
        "is_recon_ad_cta_on_profile_eligible_with_viewer": true,
        "account_type": 2,
        "highlights_tray_type": "DEFAULT",
        "current_catalog_id": null,
        "mini_shop_seller_onboarding_status": null,
        "ads_incentive_expiration_date": null,
        "ads_page_id": null,
        "ads_page_name": null,
        "account_category": "",
        "can_add_fb_group_link_on_profile": false,
        "can_use_affiliate_partnership_messaging_as_creator": false,
        "can_use_affiliate_partnership_messaging_as_brand": false,
        "has_gen_ai_personas_for_profile_banner": false,
        "has_guides": false,
        "highlight_reshare_disabled": false,
        "include_direct_blacklist_status": true,
        "is_direct_roll_call_enabled": true,
        "is_eligible_for_meta_verified_links_in_reels": false,
        "is_eligible_for_post_boost_mv_upsell": false,
        "is_meta_verified_related_accounts_display_enabled": false,
        "is_new_to_instagram": false,
        "is_profile_broadcast_sharing_enabled": true,
        "is_secondary_account_creation": false,
        "profile_type": 0,
        "is_coppa_enforced": false,
        "is_auto_confirm_enabled_for_all_reciprocal_follow_requests": false,
        "views_on_grid_status": "SHOW_VIEWS_ON_GRID",
        "is_bestie": false,
        "latest_reel_media": 1775659002,
        "latest_besties_reel_media": 0,
        "is_ring_creator": false,
        "account_badges": [],
        "has_highlight_reels": true,
        "is_creator_agent_enabled": false,
        "is_private": false,
        "interop_messaging_user_fbid": 113671860027320,
        "is_verified": true,
        "profile_pic_id": "3865702555259028436_787132",
        "has_anonymous_profile_picture": false,
        "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/...",
        "username": "natgeo",
        "full_name": "National Geographic",
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
        "hd_profile_pic_url_info": {
          "height": 1080,
          "url": "https://scontent-sof1-2.cdninstagram.com/...",
          "width": 1080
        },
        "hd_profile_pic_versions": [
          {
            "height": 320,
            "url": "https://scontent-sof1-2.cdninstagram.com/...",
            "width": 320
          },
          {
            "height": 640,
            "url": "https://scontent-sof1-2.cdninstagram.com/...",
            "width": 640
          }
        ],
        "is_active_on_text_post_app": true,
        "is_cannes": false,
        "is_facebook_onboarded_charity": false,
        "is_favorite": false,
        "show_account_transparency_details": true,
        "transparency_product_enabled": false,
        "text_app_last_visited_time": null,
        "text_post_app_joiner_number": 672534,
        "follower_count": 274988954,
        "following_count": 193,
        "is_eligible_for_slide": false,
        "live_subscription_status": "default",
        "business_contact_method": "UNKNOWN",
        "category_id": "0",
        "city_id": "0",
        "city_name": "",
        "direct_messaging": "UNKNOWN",
        "instagram_location_id": "",
        "page_id": null,
        "public_email": "",
        "public_phone_country_code": "",
        "public_phone_number": "",
        "should_show_category": false,
        "should_show_public_contacts": true,
        "zip": "",
        "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
        "biography_with_entities": {
          "raw_text": "Step into wonder and find your inner explorer with National Geographic 🌎",
          "entities": []
        },
        "contact_phone_number": "",
        "has_music_on_profile": false,
        "has_videos": true,
        "has_views_fetching": true,
        "is_call_to_action_enabled": false,
        "is_category_tappable": false,
        "is_eligible_for_creator_product_links": false,
        "is_eligible_for_lead_center": true,
        "is_eligible_for_schools_search_upsell": false,
        "is_eligible_for_smb_support_flow": true,
        "lead_details_app_id": "com.bloks.www.ig.smb.lead_gen.subpage",
        "num_of_admined_pages": null,
        "page_name": "National Geographic",
        "professional_conversion_suggested_account_type": 3,
        "profile_context": "",
        "smb_support_partner": null,
        "ring_creator_metadata": {},
        "text_post_app_joiner_number_label": "672,534",
        "is_onboarding_account": false,
        "recon_features": {
          "enable_recon_cta": true
        },
        "text_post_app_badge_label": "natgeo",
        "is_business": true,
        "is_prime_onboarding_account": false,
        "is_profile_picture_expansion_enabled": true,
        "show_all_highlights_as_selected_in_management_screen": false,
        "show_schools_badge": null,
        "text_post_new_post_count": 5,
        "trial_clips_enabled": false,
        "enable_add_school_in_edit_profile": false,
        "shopping_post_onboard_nux_type": null,
        "fb_page_call_to_action_id": "",
        "address_street": "",
        "is_profile_audio_call_enabled": false,
        "displayed_action_button_partner": null,
        "smb_delivery_partner": null,
        "smb_support_delivery_partner": null,
        "displayed_action_button_type": null,
        "category": "",
        "external_lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGnxJI2zSJ43Em4zUT1JcKLJvpJNZqIlg736wQfNykG06kdT_R36_ln2QHdFKw_aem_zbWv6PS3n0hxA-AnnTvwLQ&e=AT710uEnqVmhqdrPBWzi6HGjVUpxFXtkteon4yElFdNGJwDIbRRR_3XjSPkfPKqwrKbwc8E4oQ6GZXkEBIO1WP3gDuE9zF0I0_iXizWUfw",
        "external_url": "http://visitstore.bio/natgeo",
        "active_standalone_fundraisers": {
          "total_count": 0,
          "fundraisers": []
        },
        "additional_business_addresses": [],
        "allow_manage_memorialization": false,
        "auto_expand_chaining": false,
        "avatar_status": {
          "has_avatar": false
        },
        "bio_links": [
          {
            "link_id": 17954981494900183,
            "url": "http://visitstore.bio/natgeo",
            "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGn7sa0ZbkTFk-SAS1u9Z-LRSNm4GPdIoNSzuOP4uE153tXNbiSgIN5-SAP0X4_aem_yZt27foys9vwTQ-MC75Pgg&e=AT5hEg7JJvYPe5-i4xkpXJjRGqMRpjVADgv6nV9wDvDEhNo1cJKGMlVpCJUVou3nnN1MP37Fcs2A98ZWZCE3iZQ-G4q4f6hpAoyUDrljYw",
            "link_type": "external",
            "title": "",
            "media_type": "none",
            "image_url": "",
            "icon_url": "",
            "media_accent_color_hex": "",
            "is_pinned": false,
            "is_verified": false,
            "open_external_url_with_in_app_browser": true,
            "creation_source": "NONE"
          }
        ],
        "broadcast_chat_preference_status": {
          "json_response": "{\"status\":\"ok\",\"status_code\":\"200\",\"is_broadcast_chat_creator\":true,\"notification_setting_type\":2}",
          "is_broadcast_chat_creator": true,
          "notification_setting_type": 2
        },
        "can_use_branded_content_discovery_as_brand": false,
        "can_use_branded_content_discovery_as_creator": false,
        "can_use_paid_partnership_messaging_as_creator": false,
        "chaining_upsell_cards": [],
        "charity_profile_fundraiser_info": {
          "pk": 787132,
          "has_active_fundraiser": false,
          "is_facebook_onboarded_charity": false,
          "consumption_sheet_config": {
            "can_viewer_donate": false,
            "currency": null,
            "donation_disabled_message": null,
            "donation_url": null,
            "has_viewer_donated": null,
            "privacy_disclaimer": null,
            "profile_fundraiser_id": null,
            "you_donated_message": null,
            "donation_amount_config": {
              "default_selected_donation_value": null,
              "donation_amount_selector_values": [],
              "maximum_donation_amount": null,
              "minimum_donation_amount": null,
              "prefill_amount": null,
              "user_currency": null
            }
          }
        },
        "follow_friction_type": 0,
        "has_active_charity_business_profile_fundraiser": false,
        "has_chaining": true,
        "has_collab_collections": false,
        "has_exclusive_feed_content": false,
        "instagram_pk": "787132",
        "is_profile_search_enabled": false,
        "is_eligible_for_meta_verified_links_in_post": false,
        "is_eligible_for_meta_verified_enhanced_link_sheet": false,
        "is_eligible_for_meta_verified_enhanced_link_sheet_consumption": false,
        "is_eligible_for_meta_verified_multiple_addresses_creation": false,
        "is_eligible_for_meta_verified_multiple_addresses_consumption": false,
        "is_eligible_for_meta_verified_related_accounts": false,
        "meta_verified_related_accounts_count": 0,
        "is_eligible_to_host_profile_reels_ads": false,
        "is_favorite_for_clips": false,
        "is_favorite_for_highlights": false,
        "is_in_canada": false,
        "is_interest_account": true,
        "is_memorialized": false,
        "is_potential_business": false,
        "is_regulated_news_in_viewer_location": false,
        "is_remix_setting_enabled_for_posts": true,
        "is_remix_setting_enabled_for_reels": true,
        "is_regulated_c18": false,
        "profile_overlay_info": {
          "overlay_format": "NONE",
          "bloks_payload": null
        },
        "is_stories_teaser_muted": false,
        "is_supervision_features_enabled": false,
        "is_whatsapp_linked": false,
        "media_count": 31529,
        "mutual_followers_count": 0,
        "nametag": {
          "available_theme_colors": [
            -1,
            7747834,
            13828293
          ],
          "background_image_url": "",
          "emoji": "😀",
          "emoji_color": 0,
          "gradient": 2,
          "is_background_image_blurred": false,
          "mode": 0,
          "selected_theme_color": -1,
          "selfie_sticker": 0,
          "selfie_url": "",
          "theme_color": {
            "available_theme_colors": [
              {
                "display_label": "Default",
                "int_value": -1
              },
              {
                "display_label": "Purple",
                "int_value": 7747834
              },
              {
                "display_label": "Lavender",
                "int_value": 13828293
              }
            ],
            "selected_theme_color": {
              "display_label": "Default",
              "int_value": -1
            }
          }
        },
        "not_meta_verified_friction_info": {
          "label_friction_content": "Not Meta Verified",
          "is_eligible_for_label_friction": false
        },
        "open_external_url_with_in_app_browser": true,
        "pinned_channels_info": {
          "has_public_channels": false,
          "pinned_channels_list": []
        },
        "profile_context_facepile_users": [],
        "profile_context_links_with_user_ids": [],
        "profile_pic_genai_tool_info": [],
        "pronouns": [],
        "relevant_news_regulation_locations": [],
        "remove_message_entrypoint": false,
        "request_contact_enabled": false,
        "show_blue_badge_on_main_profile": true,
        "show_ig_app_switcher_badge": true,
        "disable_profile_shop_cta": true,
        "show_text_post_app_badge": true,
        "show_text_post_app_switcher_badge": true,
        "spam_follower_setting_enabled": true,
        "total_ar_effects": 0,
        "total_clips_count": 1,
        "upcoming_events": [],
        "whatsapp_number": "",
        "recs_from_friends": {
          "enable_recs_from_friends": false,
          "recs_from_friends_entry_point_type": "banner"
        },
        "adjusted_banners_order": [],
        "has_visible_media_notes": true,
        "is_open_to_collab": false,
        "is_daily_limit_blocking": false,
        "threads_profile_glyph_url": "barcelona://user?username=natgeo&xmt=AQF0zjHzpItgqi9lp1jtnFzuAEMoSz-c4MXKFxefjPNTaao",
        "is_oregon_custom_gender_consented": false,
        "profile_reels_sorting_eligibility": "CHECK_VIEWER_QE",
        "nonpro_can_maybe_see_profile_hypercard": false,
        "should_show_tagged_tab": true,
        "posts_subscription_status": "default",
        "reels_subscription_status": "default",
        "stories_subscription_status": "default",
        "is_profile_wa_calling_enabled": false,
        "wa_calling_option_for_wa_linked": 0,
        "wa_calling_option_for_legacy_num": 0,
        "birthday_today_visibility_for_viewer": "NOT_VISIBLE",
        "is_eligible_for_meta_verified_ig_self_profile_not_verified_badge": false,
        "has_private_collections": true,
        "is_guardian_r_account_cannes_pair": false,
        "can_see_support_inbox": null,
        "has_fan_club_subscriptions": false,
        "show_wa_link_on_profile": false,
        "meta_verified_benefits_info": {
          "active_meta_verified_benefits": [],
          "is_eligible_for_meta_verified_content_protection": false,
          "is_eligible_for_ig_meta_verified_label": false
        },
        "existing_user_age_collection_enabled": true,
        "has_public_tab_threads": true,
        "is_eligible_for_meta_verified_label": true,
        "is_favorite_for_stories": false,
        "is_parenting_account": false,
        "show_post_insights_entry_point": true,
        "short_drama_creator": null,
        "short_drama_series_playlist_id": null,
        "short_drama_series_episode_count": null,
        "short_drama_series_seed_media_id": null,
        "short_drama_series_title": null,
        "short_drama_role": "NONE",
        "short_drama_series_profiles": [],
        "short_drama_producer_account": null,
        "moonshot_joiner_number": null,
        "is_creator_marketplace_badge_visible": false,
        "creator_marketplace_accounts_reached_metric": null,
        "school_affiliated_account_viewer_status": null,
        "qa_freeform_banner": null,
        "qa_freeform_banner_available_prompts": [
          {
            "prompt": "CURRENT_OBSESSION",
            "display_text": "Current obsession"
          },
          {
            "prompt": "DREAM_DESTINATION",
            "display_text": "Dream destination"
          },
          {
            "prompt": "PLAYING",
            "display_text": "Playing"
          }
        ],
        "qa_freeform_banner_transparency": "The banner is visible to everyone on and off Instagram.",
        "can_message_pinned_carrera_interest_owner": true
      },
      "status": "ok"
    }
  ]
}
```

</details>

---

### GET /v2/userstream/by/username

Get userstream (info) by username. Returns user stream data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/userstream/by/username?username=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.userstream_by_username_v2(username="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/userstream/by/username",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/userstream/by/username?username=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "stream_rows": [
    {
      "user": {
        "strong_id__": "787132",
        "pk": 787132,
        "id": "787132",
        "full_name": "National Geographic",
        "username": "natgeo",
        "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
        "profile_pic_url": "https://scontent-prg1-1.cdninstagram.com/..."
      },
      "status": "ok"
    },
    {
      "user": {
        "strong_id__": "787132",
        "id": "787132",
        "pk": 787132,
        "is_opal_enabled": false,
        "eligible_for_text_app_activation_badge": false,
        "highlights_tray_type": "DEFAULT",
        "account_type": 2,
        "profile_pic_url": "https://scontent-prg1-1.cdninstagram.com/...",
        "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
        "bio_links": [
          {
            "link_id": 17954981494900183,
            "url": "http://visitstore.bio/natgeo",
            "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGn6ql2xXb9C45w3X6g5IQpElfbMRLG7-FUKNnP5AQOZiSr1T_LXrEdy0oil-Q_aem_FlpPcj2zT6XrKmHBfy4HJA&e=AT6V1luiBan_PCoL_5Ayx2CIwWx7087zsEEnPY7Sfy1oR8zdte_tx2HEZSmAxXfPO6Zo4WcKLMidAlHjxl9cSoAqNRf7CEpHYuJV4gi4gw",
            "link_type": "external",
            "title": "",
            "media_type": "none",
            "image_url": "",
            "icon_url": "",
            "media_accent_color_hex": "",
            "is_pinned": false,
            "is_verified": false,
            "open_external_url_with_in_app_browser": true,
            "click_id": "PAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGn6ql2xXb9C45w3X6g5IQpElfbMRLG7-FUKNnP5AQOZiSr1T_LXrEdy0oil-Q_aem_FlpPcj2zT6XrKmHBfy4HJA",
            "creation_source": "NONE"
          }
        ],
        "is_call_to_action_enabled": false,
        "is_business": true,
        "biography_with_entities": {
          "raw_text": "Step into wonder and find your inner explorer with National Geographic 🌎",
          "entities": []
        },
        "is_profile_picture_expansion_enabled": true,
        "show_schools_badge": null,
        "text_post_app_badge_label": "natgeo",
        "text_post_new_post_count": 5,
        "text_post_app_joiner_number": 672534,
        "text_post_app_joiner_number_label": "672,534",
        "recon_features": {
          "enable_recon_cta": true
        },
        "media_count": 31529,
        "trial_clips_rate_limiting": {
          "warning_title": "You can share one more trial reel",
          "at_limit_title": "You've reached the limit",
          "warning_body": "You've almost reached the limit. Once you share this trial reel, you'll need to wait up to 24 hours to start using trial reels again.",
          "at_limit_body": "You've shared the maximum number of trial reels allowed within 24 hours. You can share this reel to everyone now as a regular reel or wait up to 24 hours to share it as a trial reel.",
          "count": 20
        },
        "is_prime_onboarding_account": false,
        "is_onboarding_account": false,
        "show_ring_award": false,
        "ring_creator_metadata": {},
        "is_verified": true,
        "is_ring_creator": false,
        "is_private": false,
        "username": "natgeo",
        "full_name": "National Geographic",
        "birthday_today_visibility_for_viewer": "NOT_VISIBLE",
        "following_count": 193,
        "follower_count": 274988954
      },
      "status": "ok"
    },
    {
      "user": {
        "strong_id__": "787132",
        "id": "787132",
        "fbid_v2": 17841400573960012,
        "pk_id": "787132",
        "pk": 787132,
        "eligible_for_text_app_activation_badge": false,
        "feed_post_reshare_disabled": false,
        "has_ever_selected_topics": false,
        "has_nme_badge": false,
        "third_party_downloads_enabled": 2,
        "show_fb_link_on_profile": false,
        "show_fb_page_link_on_profile": false,
        "can_hide_category": true,
        "can_hide_public_contacts": true,
        "is_opal_enabled": false,
        "primary_profile_link_type": 0,
        "is_recon_ad_cta_on_profile_eligible_with_viewer": true,
        "account_type": 2,
        "highlights_tray_type": "DEFAULT",
        "current_catalog_id": null,
        "mini_shop_seller_onboarding_status": null,
        "ads_incentive_expiration_date": null,
        "ads_page_id": null,
        "ads_page_name": null,
        "account_category": "",
        "can_add_fb_group_link_on_profile": false,
        "can_use_affiliate_partnership_messaging_as_creator": false,
        "can_use_affiliate_partnership_messaging_as_brand": false,
        "has_gen_ai_personas_for_profile_banner": false,
        "has_guides": false,
        "highlight_reshare_disabled": false,
        "include_direct_blacklist_status": true,
        "is_direct_roll_call_enabled": true,
        "is_eligible_for_meta_verified_links_in_reels": false,
        "is_eligible_for_post_boost_mv_upsell": false,
        "is_meta_verified_related_accounts_display_enabled": false,
        "is_new_to_instagram": false,
        "is_profile_broadcast_sharing_enabled": true,
        "is_secondary_account_creation": false,
        "profile_type": 0,
        "is_coppa_enforced": false,
        "is_auto_confirm_enabled_for_all_reciprocal_follow_requests": false,
        "views_on_grid_status": "SHOW_VIEWS_ON_GRID",
        "is_bestie": false,
        "latest_reel_media": 1775659002,
        "latest_besties_reel_media": 0,
        "is_ring_creator": false,
        "account_badges": [],
        "has_highlight_reels": true,
        "is_creator_agent_enabled": false,
        "is_private": false,
        "interop_messaging_user_fbid": 113671860027320,
        "is_verified": true,
        "profile_pic_id": "3865702555259028436_787132",
        "has_anonymous_profile_picture": false,
        "profile_pic_url": "https://scontent-prg1-1.cdninstagram.com/...",
        "username": "natgeo",
        "full_name": "National Geographic",
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
        "hd_profile_pic_url_info": {
          "height": 1080,
          "url": "https://scontent-prg1-1.cdninstagram.com/...",
          "width": 1080
        },
        "hd_profile_pic_versions": [
          {
            "height": 320,
            "url": "https://scontent-prg1-1.cdninstagram.com/...",
            "width": 320
          },
          {
            "height": 640,
            "url": "https://scontent-prg1-1.cdninstagram.com/...",
            "width": 640
          }
        ],
        "is_active_on_text_post_app": true,
        "is_cannes": false,
        "is_facebook_onboarded_charity": false,
        "is_favorite": false,
        "show_account_transparency_details": true,
        "transparency_product_enabled": false,
        "text_app_last_visited_time": null,
        "text_post_app_joiner_number": 672534,
        "follower_count": 274988954,
        "following_count": 193,
        "is_eligible_for_slide": false,
        "live_subscription_status": "default",
        "business_contact_method": "UNKNOWN",
        "category_id": "0",
        "city_id": "0",
        "city_name": "",
        "direct_messaging": "UNKNOWN",
        "instagram_location_id": "",
        "page_id": null,
        "public_email": "",
        "public_phone_country_code": "",
        "public_phone_number": "",
        "should_show_category": false,
        "should_show_public_contacts": true,
        "zip": "",
        "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
        "biography_with_entities": {
          "raw_text": "Step into wonder and find your inner explorer with National Geographic 🌎",
          "entities": []
        },
        "contact_phone_number": "",
        "has_music_on_profile": false,
        "has_videos": true,
        "has_views_fetching": true,
        "is_call_to_action_enabled": false,
        "is_category_tappable": false,
        "is_eligible_for_creator_product_links": false,
        "is_eligible_for_lead_center": true,
        "is_eligible_for_schools_search_upsell": false,
        "is_eligible_for_smb_support_flow": true,
        "lead_details_app_id": "com.bloks.www.ig.smb.lead_gen.subpage",
        "num_of_admined_pages": null,
        "page_name": "National Geographic",
        "professional_conversion_suggested_account_type": 3,
        "profile_context": "",
        "smb_support_partner": null,
        "ring_creator_metadata": {},
        "text_post_app_joiner_number_label": "672,534",
        "is_onboarding_account": false,
        "recon_features": {
          "enable_recon_cta": true
        },
        "text_post_app_badge_label": "natgeo",
        "is_business": true,
        "is_prime_onboarding_account": false,
        "is_profile_picture_expansion_enabled": true,
        "show_all_highlights_as_selected_in_management_screen": false,
        "show_schools_badge": null,
        "text_post_new_post_count": 5,
        "trial_clips_enabled": false,
        "enable_add_school_in_edit_profile": false,
        "shopping_post_onboard_nux_type": null,
        "fb_page_call_to_action_id": "",
        "address_street": "",
        "is_profile_audio_call_enabled": false,
        "displayed_action_button_partner": null,
        "smb_delivery_partner": null,
        "smb_support_delivery_partner": null,
        "displayed_action_button_type": null,
        "category": "",
        "external_lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGn3Ou-fXIntyS_T9eO5VYa1prvUk9vW_RW4QahLbzXa3CvtSFshmQ3GHufyKc_aem_g3Lbh1UQnyfQOTw4eLW0uQ&e=AT5DjGUaY8A9j_fDrDtN7EPahCiFuXQWOL3ebP7rDGfCNBABSqwuRd5xoSh-lmYrIniY-irfWtxxOQBP1lY8PaENrFFlCWHx28qpZb0qSg",
        "external_url": "http://visitstore.bio/natgeo",
        "active_standalone_fundraisers": {
          "total_count": 0,
          "fundraisers": []
        },
        "additional_business_addresses": [],
        "allow_manage_memorialization": false,
        "auto_expand_chaining": false,
        "avatar_status": {
          "has_avatar": false
        },
        "bio_links": [
          {
            "link_id": 17954981494900183,
            "url": "http://visitstore.bio/natgeo",
            "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGn6ql2xXb9C45w3X6g5IQpElfbMRLG7-FUKNnP5AQOZiSr1T_LXrEdy0oil-Q_aem_FlpPcj2zT6XrKmHBfy4HJA&e=AT6V1luiBan_PCoL_5Ayx2CIwWx7087zsEEnPY7Sfy1oR8zdte_tx2HEZSmAxXfPO6Zo4WcKLMidAlHjxl9cSoAqNRf7CEpHYuJV4gi4gw",
            "link_type": "external",
            "title": "",
            "media_type": "none",
            "image_url": "",
            "icon_url": "",
            "media_accent_color_hex": "",
            "is_pinned": false,
            "is_verified": false,
            "open_external_url_with_in_app_browser": true,
            "click_id": "PAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGn6ql2xXb9C45w3X6g5IQpElfbMRLG7-FUKNnP5AQOZiSr1T_LXrEdy0oil-Q_aem_FlpPcj2zT6XrKmHBfy4HJA",
            "creation_source": "NONE"
          }
        ],
        "broadcast_chat_preference_status": {
          "json_response": "{\"status\":\"ok\",\"status_code\":\"200\",\"is_broadcast_chat_creator\":true,\"notification_setting_type\":2}",
          "is_broadcast_chat_creator": true,
          "notification_setting_type": 2
        },
        "can_use_branded_content_discovery_as_brand": false,
        "can_use_branded_content_discovery_as_creator": false,
        "can_use_paid_partnership_messaging_as_creator": false,
        "chaining_upsell_cards": [],
        "charity_profile_fundraiser_info": {
          "pk": 787132,
          "has_active_fundraiser": false,
          "is_facebook_onboarded_charity": false,
          "consumption_sheet_config": {
            "can_viewer_donate": false,
            "currency": null,
            "donation_disabled_message": null,
            "donation_url": null,
            "has_viewer_donated": null,
            "privacy_disclaimer": null,
            "profile_fundraiser_id": null,
            "you_donated_message": null,
            "donation_amount_config": {
              "default_selected_donation_value": null,
              "donation_amount_selector_values": [],
              "maximum_donation_amount": null,
              "minimum_donation_amount": null,
              "prefill_amount": null,
              "user_currency": null
            }
          }
        },
        "follow_friction_type": 0,
        "has_active_charity_business_profile_fundraiser": false,
        "has_chaining": true,
        "has_collab_collections": false,
        "has_exclusive_feed_content": false,
        "instagram_pk": "787132",
        "is_profile_search_enabled": false,
        "is_eligible_for_meta_verified_links_in_post": false,
        "is_eligible_for_meta_verified_enhanced_link_sheet": false,
        "is_eligible_for_meta_verified_enhanced_link_sheet_consumption": false,
        "is_eligible_for_meta_verified_multiple_addresses_creation": false,
        "is_eligible_for_meta_verified_multiple_addresses_consumption": false,
        "is_eligible_for_meta_verified_related_accounts": false,
        "meta_verified_related_accounts_count": 0,
        "is_eligible_to_host_profile_reels_ads": false,
        "is_favorite_for_clips": false,
        "is_favorite_for_highlights": false,
        "is_in_canada": false,
        "is_interest_account": true,
        "is_memorialized": false,
        "is_potential_business": false,
        "is_regulated_news_in_viewer_location": false,
        "is_remix_setting_enabled_for_posts": true,
        "is_remix_setting_enabled_for_reels": true,
        "is_regulated_c18": false,
        "profile_overlay_info": {
          "overlay_format": "NONE",
          "bloks_payload": null
        },
        "is_stories_teaser_muted": false,
        "is_supervision_features_enabled": false,
        "is_whatsapp_linked": false,
        "media_count": 31529,
        "mutual_followers_count": 0,
        "nametag": {
          "available_theme_colors": [
            -1,
            7747834,
            13828293
          ],
          "background_image_url": "",
          "emoji": "😀",
          "emoji_color": 0,
          "gradient": 2,
          "is_background_image_blurred": false,
          "mode": 0,
          "selected_theme_color": -1,
          "selfie_sticker": 0,
          "selfie_url": "",
          "theme_color": {
            "available_theme_colors": [
              {
                "display_label": "Default",
                "int_value": -1
              },
              {
                "display_label": "Purple",
                "int_value": 7747834
              },
              {
                "display_label": "Lavender",
                "int_value": 13828293
              }
            ],
            "selected_theme_color": {
              "display_label": "Default",
              "int_value": -1
            }
          }
        },
        "not_meta_verified_friction_info": {
          "label_friction_content": "Not Meta Verified",
          "is_eligible_for_label_friction": false
        },
        "open_external_url_with_in_app_browser": true,
        "pinned_channels_info": {
          "has_public_channels": false,
          "pinned_channels_list": []
        },
        "profile_context_facepile_users": [],
        "profile_context_links_with_user_ids": [],
        "profile_pic_genai_tool_info": [],
        "pronouns": [],
        "relevant_news_regulation_locations": [],
        "remove_message_entrypoint": false,
        "request_contact_enabled": false,
        "show_blue_badge_on_main_profile": true,
        "show_ig_app_switcher_badge": true,
        "disable_profile_shop_cta": true,
        "show_text_post_app_badge": true,
        "show_text_post_app_switcher_badge": true,
        "spam_follower_setting_enabled": true,
        "total_ar_effects": 0,
        "total_clips_count": 1,
        "upcoming_events": [],
        "whatsapp_number": "",
        "recs_from_friends": {
          "enable_recs_from_friends": false,
          "recs_from_friends_entry_point_type": "banner"
        },
        "adjusted_banners_order": [],
        "has_visible_media_notes": true,
        "is_open_to_collab": false,
        "is_daily_limit_blocking": false,
        "threads_profile_glyph_url": "barcelona://user?username=natgeo&xmt=AQF0zccKrgOIQgOnQin_GhdZPpFEu1Vn0kzLeyk81TqME2M",
        "is_oregon_custom_gender_consented": false,
        "profile_reels_sorting_eligibility": "DISABLED",
        "nonpro_can_maybe_see_profile_hypercard": false,
        "should_show_tagged_tab": true,
        "posts_subscription_status": "default",
        "reels_subscription_status": "default",
        "stories_subscription_status": "default",
        "is_profile_wa_calling_enabled": false,
        "wa_calling_option_for_wa_linked": 0,
        "wa_calling_option_for_legacy_num": 0,
        "birthday_today_visibility_for_viewer": "NOT_VISIBLE",
        "is_eligible_for_meta_verified_ig_self_profile_not_verified_badge": false,
        "has_private_collections": true,
        "is_guardian_r_account_cannes_pair": false,
        "can_see_support_inbox": null,
        "has_fan_club_subscriptions": false,
        "show_wa_link_on_profile": false,
        "meta_verified_benefits_info": {
          "active_meta_verified_benefits": [],
          "is_eligible_for_meta_verified_content_protection": false,
          "is_eligible_for_ig_meta_verified_label": false
        },
        "existing_user_age_collection_enabled": true,
        "has_public_tab_threads": true,
        "is_eligible_for_meta_verified_label": true,
        "is_favorite_for_stories": false,
        "is_parenting_account": false,
        "show_post_insights_entry_point": true,
        "short_drama_creator": null,
        "short_drama_series_playlist_id": null,
        "short_drama_series_episode_count": null,
        "short_drama_series_seed_media_id": null,
        "short_drama_series_title": null,
        "short_drama_role": "NONE",
        "short_drama_series_profiles": [],
        "short_drama_producer_account": null,
        "moonshot_joiner_number": null,
        "is_creator_marketplace_badge_visible": false,
        "creator_marketplace_accounts_reached_metric": null,
        "school_affiliated_account_viewer_status": null,
        "qa_freeform_banner": null,
        "qa_freeform_banner_available_prompts": [
          {
            "prompt": "CURRENT_OBSESSION",
            "display_text": "Current obsession"
          },
          {
            "prompt": "DREAM_DESTINATION",
            "display_text": "Dream destination"
          },
          {
            "prompt": "PLAYING",
            "display_text": "Playing"
          }
        ],
        "qa_freeform_banner_transparency": "The banner is visible to everyone on and off Instagram.",
        "can_message_pinned_carrera_interest_owner": true
      },
      "status": "ok"
    }
  ]
}
```

</details>

---

## Deprecated endpoints

These endpoints are deprecated — use the recommended alternatives. Retired ones respond with **410 Gone** and are never charged (see [Response Codes](../response-codes.md)); the rest still work but will be removed in a future version.

### ~~GET /v2/user/medias~~

!!! warning
    Prefer /gql/user/medias - this endpoint will be deprecated

### ~~GET /v2/user/videos~~

!!! warning
    Prefer using /v2/user/clips or /v2/user/medias instead

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v2-user){ target=_blank }
