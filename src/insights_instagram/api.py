import requests
from django.conf import settings


def instagram_get_user_credentials(email):
    response = requests.get(
        settings.INSTAGRAM_API_URL + '/get/key',
        params={
            'email': email,
        },
    )
    data = response.json()
    return data['userid'], data['key']


def instagram_get_hashtag_id(hashtag, user_id):
    response = requests.get(
        settings.INSTAGRAM_API_URL + '/ig_hashtag_search',
        params={
            'q': hashtag,
            'user_id': user_id,
        },
    )
    data = response.json()
    return data['id']


SEARCH_CRITERION_RECENT_MEDIA = 'recent_media'
SEARCH_CRITERION_TOP_MEDIA = 'top_media'


def instagram_get_posts_by_hashtag_id(hashtag_id, search_criterion, user_id):
    response = requests.get(
        settings.INSTAGRAM_API_URL + '/{}/{}'.format(hashtag_id, search_criterion),
        params={
            'user_id': user_id,
        },
    )
    data = response.json()
    return data['data']


def instagram_get_posts_by_hashtag_id_recent_media(hashtag_id, user_id):
    return instagram_get_posts_by_hashtag_id(hashtag_id, SEARCH_CRITERION_RECENT_MEDIA, user_id)


def instagram_get_posts_by_hashtag_id_top_media(hashtag_id, user_id):
    return instagram_get_posts_by_hashtag_id(hashtag_id, SEARCH_CRITERION_TOP_MEDIA, user_id)


POST_METADATA_FIELDS = ('id', 'username', 'media_type', 'like_count', 'comments_count')


def instagram_get_post_metadata(post_id, fields=POST_METADATA_FIELDS):
    response = requests.get(
        settings.INSTAGRAM_API_URL + '/media/{}'.format(post_id),
        params={
            'fields': ','.join(fields),
        },
    )
    data = response.json()
    post_metadata, *rest = data
    return post_metadata


USER_METADATA_FIELDS = ('id', 'username', 'follower_count', 'media_count')


def instagram_get_user_metadata(user_id, fields=USER_METADATA_FIELDS):
    response = requests.get(
        settings.INSTAGRAM_API_URL + '/{}'.format(user_id),
        params={
            'fields': ','.join(fields),
        },
    )
    data = response.json()
    user_metadata, *rest = data
    return user_metadata
