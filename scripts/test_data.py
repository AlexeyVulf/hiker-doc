"""Test data constants for the doc generator and response fetcher."""

API_BASE = "https://api.hikerapi.com"
USER_PK = "787132"
USER_USERNAME = "natgeo"
MEDIA_ID = "3776832898280228145"
MEDIA_PK = "3776832898280228145_787132"
MEDIA_CODE = "DRqAYKuAIUx"
MEDIA_URL = f"https://www.instagram.com/p/{MEDIA_CODE}/"
LOCATION_PK = "213131048"
HIGHLIGHT_ID = "18085475671830440"
COMMENT_ID = "17901801633335930"
HASHTAG_NAME = "love"
SEARCH_QUERY = "natgeo"
TRACK_ID = "797665381922277"
TRACK_CANONICAL_ID = "1218296241668996"

# Entities with rich data for endpoints that need non-empty responses
RICH_MEDIA_ID = "3691011991037807194"  # has comments
RICH_COMMENT_MEDIA_ID = "3864286541032633353"  # has comment replies
RICH_COMMENT_ID = "18142813870496178"  # has replies
RICH_COMMENT_LIKERS_MEDIA_ID = "18133609390533743"  # has comment likers
RICH_HIGHLIGHTS_USER_ID = "51089230684"  # has highlights
CLIP_MEDIA_ID = (
    "3973791230319739409"  # public reel with music, clean clips_metadata response
)
STORY_URL = f"https://www.instagram.com/stories/{USER_USERNAME}/3776832898280228145/"  # noqa: E501
SHARE_URL = f"https://www.instagram.com/p/{MEDIA_CODE}/"

ENDPOINT_PARAMS = {
    # System
    "/sys/balance": {},
    # User — v1
    "/v1/user/by/username": {"username": USER_USERNAME},
    "/v1/user/by/id": {"id": USER_PK},
    "/v1/user/by/url": {"url": f"https://www.instagram.com/{USER_USERNAME}/"},
    "/v1/user/about": {"id": USER_PK},
    "/v1/user/medias/chunk": {"user_id": USER_PK},
    "/v1/user/medias/pinned": {"user_id": USER_PK},
    "/v1/user/clips/chunk": {"user_id": USER_PK},
    "/v1/user/tag/medias/chunk": {"user_id": USER_PK},
    "/v1/user/stories": {"user_id": USER_PK},
    "/v1/user/stories/by/username": {"username": USER_USERNAME},
    "/v1/user/highlights": {"user_id": USER_PK},
    "/v1/user/highlights/by/username": {"username": USER_USERNAME},
    "/v1/user/search/followers": {"user_id": USER_PK, "query": SEARCH_QUERY},
    "/v1/user/search/following": {"user_id": USER_PK, "query": SEARCH_QUERY},
    "/v1/user/following/chunk": {"user_id": USER_PK},
    "/v1/user/followers/chunk": {"user_id": USER_PK},
    "/v1/user/clips": {"user_id": USER_PK},
    "/v1/user/followers": {"user_id": USER_PK},
    "/v1/user/following": {"user_id": USER_PK},
    "/v1/user/guides": {"user_id": USER_PK},
    "/v1/user/medias": {"user_id": USER_PK},
    "/v1/user/tag/medias": {"user_id": USER_PK},
    "/v1/user/videos": {"user_id": USER_PK},
    "/v1/user/videos/chunk": {"user_id": USER_PK},
    "/v1/user/web_profile_info": {"username": USER_USERNAME},
    # User — v2
    "/v2/user/by/username": {"username": USER_USERNAME},
    "/v2/user/by/id": {"id": USER_PK},
    "/v2/userstream/by/username": {"username": USER_USERNAME},
    "/v2/userstream/by/id": {"id": USER_PK},
    "/v2/user/stories": {"user_id": USER_PK},
    "/v2/user/stories/by/username": {"username": USER_USERNAME},
    "/v2/user/clips": {"user_id": USER_PK},
    "/v2/user/following": {"user_id": USER_PK},
    "/v2/user/followers": {"user_id": USER_PK},
    "/v2/user/tag/medias": {"user_id": USER_PK},
    "/v2/user/highlights": {"user_id": "1114341851"},
    "/v2/user/highlights/by/username": {"username": "nike"},
    "/v2/user/explore/businesses/by/id": {"user_id": USER_PK},
    "/v2/user/suggested/profiles": {"user_id": USER_PK},
    "/v2/user/medias": {"user_id": USER_PK},
    "/v2/user/videos": {"user_id": USER_PK},
    # User — a2
    "/a2/user": {"username": USER_USERNAME},
    # User — g2
    "/g2/user/followers": {"user_id": USER_PK},
    "/g2/user/following": {"user_id": USER_PK},
    "/g2/user/medias": {"user_id": USER_PK},
    # User — g1 (legacy public GraphQL)
    "/g1/user/followers": {"user_id": USER_PK},
    "/g1/user/following": {"user_id": USER_PK},
    # User — gql
    "/gql/user/about": {"id": USER_PK},
    "/gql/user/medias": {"user_id": USER_PK},
    "/gql/user/following/chunk": {"user_id": USER_PK},
    "/gql/user/followers/chunk": {"user_id": USER_PK},
    "/gql/user/reposts": {"user_id": USER_PK},
    "/gql/user/clips": {"user_id": USER_PK},
    "/gql/user/web_profile_info": {"user_id": USER_PK},
    "/gql/user/related/profiles": {"id": USER_PK},
    "/gql/user/by/id": {"id": USER_PK},
    "/gql/user/by/username": {"username": USER_USERNAME},
    "/gql/user/followers": {"user_id": USER_PK},
    "/gql/user/following": {"user_id": USER_PK},
    # Media — v1
    "/v1/media/by/id": {"id": MEDIA_ID},
    "/v1/media/by/code": {"code": MEDIA_CODE},
    "/v1/media/by/url": {"url": MEDIA_URL},
    "/v1/media/insight": {"media_id": MEDIA_ID},
    "/v1/media/comments/chunk": {"id": MEDIA_ID},
    "/v1/media/likers": {"id": MEDIA_ID},
    "/v1/media/user": {"media_id": MEDIA_ID},
    "/v1/media/oembed": {"url": MEDIA_URL},
    "/v1/media/code/from/pk": {"pk": MEDIA_ID},
    "/v1/media/pk/from/code": {"code": MEDIA_CODE},
    "/v1/media/pk/from/url": {"url": MEDIA_URL},
    "/v1/media/comments": {"id": MEDIA_ID},
    "/v1/media/download/photo": {"id": MEDIA_ID},
    "/v1/media/download/photo/by/url": {"url": MEDIA_URL},
    "/v1/media/download/video": {"id": MEDIA_ID},
    "/v1/media/download/video/by/url": {"url": MEDIA_URL},
    # Media — v2
    "/v2/media/info/by/id": {"id": MEDIA_ID},
    "/v2/media/info/by/code": {"code": MEDIA_CODE},
    "/v2/media/info/by/url": {"url": MEDIA_URL},
    "/v2/media/comments": {"id": RICH_MEDIA_ID},
    "/v2/media/comments/infos": {"media_ids": RICH_MEDIA_ID},
    "/v2/media/comments/replies": {
        "media_id": RICH_COMMENT_MEDIA_ID,
        "comment_id": RICH_COMMENT_ID,
    },
    "/v2/media/likers": {"id": MEDIA_ID},
    "/v3/media/likers": {"id": MEDIA_ID},
    "/v2/media/template": {"id": MEDIA_ID},
    "/v2/media/comment/offensive": {
        "media_id": MEDIA_ID,
        "comment": "test comment",
    },
    "/v2/media/by/code": {"code": MEDIA_CODE},
    "/v2/media/by/id": {"id": MEDIA_ID},
    "/v2/media/by/url": {"url": MEDIA_URL},
    # Media — gql
    "/gql/media/usertags": {"media_ids": MEDIA_ID},
    "/gql/media/clips_metadata": {"media_ids": CLIP_MEDIA_ID},
    "/gql/media/likers": {"media_id": MEDIA_ID},
    "/gql/comments/chunk": {"media_id": MEDIA_ID},
    "/gql/comments/threaded/chunk": {
        "media_id": MEDIA_ID,
        "comment_id": COMMENT_ID,
    },
    "/gql/comment/likers/chunk": {
        "comment_id": COMMENT_ID,
        "media_id": MEDIA_ID,
    },
    "/gql/comments": {"media_id": MEDIA_ID},
    "/gql/comment/likers": {"media_id": RICH_COMMENT_LIKERS_MEDIA_ID},
    "/gql/comments/threaded": {"media_id": MEDIA_ID, "comment_id": COMMENT_ID},
    # Story — v1
    "/v1/story/by/id": {"id": MEDIA_ID},
    "/v1/story/by/url": {"url": STORY_URL},
    "/v1/story/download": {"id": MEDIA_ID},
    "/v1/story/download/by/url": {"url": STORY_URL},
    "/v1/story/download/by/story/url": {"url": STORY_URL},
    # Story — v2
    "/v2/story/by/id": {"id": MEDIA_ID},
    "/v2/story/by/url": {"url": STORY_URL},
    # Highlight — v1
    "/v1/highlight/by/url": {
        "url": f"https://www.instagram.com/stories/highlights/{HIGHLIGHT_ID}/"
    },
    "/v1/highlight/by/id": {"id": HIGHLIGHT_ID},
    # Highlight — v2
    "/v2/highlight/by/id": {"id": HIGHLIGHT_ID},
    # Share — v1
    "/v1/share/by/code": {"code": "aGlnaGxpZ2h0OjE3ODkzMjA5ODI1MjgxMjIx"},
    "/v1/share/by/url": {"url": SHARE_URL},
    "/v1/share/reel/by/url": {"url": SHARE_URL},
    # Location — v1
    "/v1/location/by/id": {"id": LOCATION_PK},
    "/v1/location/medias/top": {"location_pk": LOCATION_PK},
    "/v1/location/medias/recent": {"location_pk": LOCATION_PK},
    "/v1/location/medias/top/chunk": {"location_pk": LOCATION_PK},
    "/v1/location/medias/recent/chunk": {"location_pk": LOCATION_PK},
    "/v1/location/search": {"lat": 40.7128, "lng": -74.0060},
    "/v1/location/guides": {"location_pk": LOCATION_PK},
    # Hashtag — v1
    "/v1/hashtag/by/name": {"name": HASHTAG_NAME},
    "/v1/hashtag/medias/top": {"name": HASHTAG_NAME},
    "/v1/hashtag/medias/top/chunk": {"name": HASHTAG_NAME},
    "/v1/hashtag/medias/top/recent/chunk": {"name": HASHTAG_NAME},
    "/v1/hashtag/medias/clips": {"name": HASHTAG_NAME},
    "/v1/hashtag/medias/clips/chunk": {"name": HASHTAG_NAME},
    "/v1/hashtag/medias/recent": {"name": HASHTAG_NAME},
    "/v1/hashtag/medias/recent/chunk": {"name": HASHTAG_NAME},
    # Hashtag — v2
    "/v2/hashtag/by/name": {"name": HASHTAG_NAME},
    "/v2/hashtag/medias/top": {"name": HASHTAG_NAME},
    "/v2/hashtag/medias/recent": {"name": HASHTAG_NAME},
    "/v2/hashtag/medias/clips": {"name": HASHTAG_NAME},
    # Track — v2
    "/v2/track/by/id": {"track_id": TRACK_ID},
    "/v2/track/stream/by/id": {"track_id": TRACK_ID},
    "/v2/track/by/canonical/id": {"canonical_id": TRACK_CANONICAL_ID},
    # Search — v1
    "/v1/search/hashtags": {"query": HASHTAG_NAME},
    "/v1/search/users": {"query": SEARCH_QUERY},
    "/v1/search/music": {"query": SEARCH_QUERY},
    "/v1/fbsearch/topsearch": {"query": SEARCH_QUERY},
    "/v1/fbsearch/places": {"query": SEARCH_QUERY},
    "/v1/fbsearch/topsearch/hashtags": {"query": HASHTAG_NAME},
    # Search — v2
    "/v2/fbsearch/topsearch": {"query": SEARCH_QUERY},
    "/v2/fbsearch/reels": {"query": SEARCH_QUERY},
    "/v2/fbsearch/accounts": {"query": SEARCH_QUERY},
    "/v2/fbsearch/places": {"query": SEARCH_QUERY},
    "/v2/search/music": {"query": SEARCH_QUERY},
    "/v2/search/hashtags": {"query": HASHTAG_NAME},
    "/v2/search/accounts": {"query": SEARCH_QUERY},
    "/v2/search/topsearch": {"query": SEARCH_QUERY},
    "/v2/search/reels": {"query": SEARCH_QUERY},
    "/v2/search/places": {"query": SEARCH_QUERY},
    # Search — v3
    "/v3/fbsearch/accounts": {"query": SEARCH_QUERY},
    "/v3/fbsearch/places": {"query": SEARCH_QUERY},
    "/v3/fbsearch/topsearch": {"query": SEARCH_QUERY},
    "/v3/fbsearch/reels": {"query": SEARCH_QUERY},
    # gql topsearch
    "/gql/topsearch": {"query": SEARCH_QUERY},
}

SDK_METHODS = {
    # System — no SDK method
    # User — v1
    "/v1/user/by/username": "user_by_username_v1",
    "/v1/user/by/id": "user_by_id_v1",
    "/v1/user/by/url": "user_by_url_v1",
    "/v1/user/about": "user_about_v1",
    "/v1/user/medias/chunk": "user_medias_chunk_v1",
    "/v1/user/medias/pinned": "user_medias_pinned_v1",
    "/v1/user/clips/chunk": "user_clips_chunk_v1",
    "/v1/user/tag/medias/chunk": "user_tag_medias_chunk_v1",
    "/v1/user/stories": "user_stories_v1",
    "/v1/user/stories/by/username": "user_stories_by_username_v1",
    "/v1/user/highlights": "user_highlights_v1",
    "/v1/user/highlights/by/username": "user_highlights_by_username_v1",
    "/v1/user/search/followers": "user_search_followers_v1",
    "/v1/user/search/following": "user_search_following_v1",
    "/v1/user/following/chunk": "user_following_chunk_v1",
    "/v1/user/followers/chunk": "user_followers_chunk_v1",
    # User — v2
    "/v2/user/by/username": "user_by_username_v2",
    "/v2/user/by/id": "user_by_id_v2",
    "/v2/userstream/by/username": "userstream_by_username_v2",
    "/v2/userstream/by/id": "userstream_by_id_v2",
    "/v2/user/stories": "user_stories_v2",
    "/v2/user/stories/by/username": "user_stories_by_username_v2",
    "/v2/user/clips": "user_clips_v2",
    "/v2/user/following": "user_following_v2",
    "/v2/user/followers": "user_followers_v2",
    "/v2/user/tag/medias": "user_tag_medias_v2",
    "/v2/user/highlights": "user_highlights_v2",
    "/v2/user/highlights/by/username": "user_highlights_by_username_v2",
    "/v2/user/explore/businesses/by/id": "user_explore_businesses_by_id_v2",
    "/v2/user/suggested/profiles": "user_suggested_profiles_v2",
    # User — a2
    "/a2/user": "user_a2",
    # User — gql
    "/gql/user/medias": "user_medias_gql",
    "/gql/user/following/chunk": "user_following_chunk_gql",
    "/gql/user/followers/chunk": "user_followers_chunk_gql",
    "/gql/user/reposts": "user_reposts_gql",
    "/gql/user/clips": "user_clips_gql",
    "/gql/user/web_profile_info": "user_web_profile_info_gql",
    # Media — v1
    "/v1/media/by/id": "media_by_id_v1",
    "/v1/media/by/code": "media_by_code_v1",
    "/v1/media/by/url": "media_by_url_v1",
    "/v1/media/insight": "media_insight_v1",
    "/v1/media/comments/chunk": "media_comments_chunk_v1",
    "/v1/media/likers": "media_likers_v1",
    "/v1/media/user": "media_user_v1",
    "/v1/media/oembed": "media_oembed_v1",
    "/v1/media/code/from/pk": "media_code_from_pk_v1",
    "/v1/media/pk/from/code": "media_pk_from_code_v1",
    "/v1/media/pk/from/url": "media_pk_from_url_v1",
    # Media — v2
    "/v2/media/info/by/id": "media_info_by_id_v2",
    "/v2/media/info/by/code": "media_info_by_code_v2",
    "/v2/media/info/by/url": "media_info_by_url_v2",
    "/v2/media/comments": "media_comments_v2",
    "/v2/media/comments/replies": "media_comments_replies_v2",
    "/v2/media/likers": "media_likers_v2",
    "/v2/media/template": "media_template_v2",
    "/v2/media/comment/offensive": "media_comment_offensive_v2",
    # Media — gql
    "/gql/media/usertags": "media_usertags_gql",
    "/gql/media/likers": "media_likers_gql",
    "/gql/comments/chunk": "comments_chunk_gql",
    "/gql/comments/threaded/chunk": "comments_threaded_chunk_gql",
    "/gql/comment/likers/chunk": "comment_likers_chunk_gql",
    # Story — v1
    "/v1/story/by/id": "story_by_id_v1",
    "/v1/story/by/url": "story_by_url_v1",
    "/v1/story/download": "story_download_v1",
    "/v1/story/download/by/url": "story_download_by_url_v1",
    "/v1/story/download/by/story/url": "story_download_by_story_url_v1",
    # Story — v2
    "/v2/story/by/id": "story_by_id_v2",
    "/v2/story/by/url": "story_by_url_v2",
    # Highlight — v1
    "/v1/highlight/by/url": "highlight_by_url_v1",
    # Highlight — v2
    "/v2/highlight/by/id": "highlight_by_id_v2",
    # Share — v1
    "/v1/share/by/code": "share_by_code_v1",
    "/v1/share/by/url": "share_by_url_v1",
    "/v1/share/reel/by/url": "share_reel_by_url_v1",
    # Location — v1
    "/v1/location/by/id": "location_by_id_v1",
    "/v1/location/medias/top": "location_medias_top_v1",
    "/v1/location/medias/recent": "location_medias_recent_v1",
    "/v1/location/medias/top/chunk": "location_medias_top_chunk_v1",
    "/v1/location/medias/recent/chunk": "location_medias_recent_chunk_v1",
    "/v1/location/search": "location_search_v1",
    "/v1/location/guides": "location_guides_v1",
    # Hashtag — v1
    "/v1/hashtag/by/name": "hashtag_by_name_v1",
    "/v1/hashtag/medias/top": "hashtag_medias_top_v1",
    "/v1/hashtag/medias/top/chunk": "hashtag_medias_top_chunk_v1",
    "/v1/hashtag/medias/top/recent/chunk": (  # noqa: E501
        "hashtag_medias_top_recent_chunk_v1"
    ),
    "/v1/hashtag/medias/clips": "hashtag_medias_clips_v1",
    "/v1/hashtag/medias/clips/chunk": "hashtag_medias_clips_chunk_v1",
    # Hashtag — v2
    "/v2/hashtag/by/name": "hashtag_by_name_v2",
    "/v2/hashtag/medias/top": "hashtag_medias_top_v2",
    "/v2/hashtag/medias/recent": "hashtag_medias_recent_v2",
    # Track — v2
    "/v2/track/by/id": "track_by_id_v2",
    "/v2/track/stream/by/id": "track_stream_by_id_v2",
    "/v2/track/by/canonical/id": "track_by_canonical_id_v2",
    # Search — v1
    "/v1/search/hashtags": "search_hashtags_v1",
    "/v1/search/users": "search_users_v1",
    "/v1/search/music": "search_music_v1",
    "/v1/fbsearch/topsearch": "fbsearch_topsearch_v1",
    "/v1/fbsearch/places": "fbsearch_places_v1",
    "/v1/fbsearch/topsearch/hashtags": "fbsearch_topsearch_hashtags_v1",
    # Search — v2
    "/v2/fbsearch/topsearch": "fbsearch_topsearch_v2",
    "/v2/fbsearch/reels": "fbsearch_reels_v2",
    "/v2/fbsearch/accounts": "fbsearch_accounts_v2",
    "/v2/fbsearch/places": "fbsearch_places_v2",
    "/v2/search/music": "search_music_v2",
    "/v2/search/hashtags": "search_hashtags_v2",
    # Search — v3
    "/v3/fbsearch/accounts": "fbsearch_accounts_v3",
    "/v3/fbsearch/places": "fbsearch_places_v3",
    # gql topsearch
    "/gql/topsearch": "topsearch_gql",
}
