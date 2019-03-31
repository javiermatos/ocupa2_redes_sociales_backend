import requests
from django.conf import settings


def twitter_get_user_credentials(email):
    response = requests.get(
        settings.TWITTER_API_URL + '/get/key',
        params={
            'email': email,
        },
    )
    data = response.json()
    return data['userid'], data['key']


def twitter_get_posts_by_hashtag(hashtag):
    response = requests.get(
        settings.TWITTER_API_URL + '/search/tweets.json',
        params={
            'q': hashtag,
        }
    )
    data = response.json()
    return data


def twitter_get_post_metadata(post_id):
    response = requests.get(
        settings.TWITTER_API_URL + '/statuses/retweets/{}.json'.format(post_id),
    )
    data = response.json()
    post_metadata, *rest = data
    return post_metadata
