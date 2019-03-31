import time

from django.core.management import BaseCommand
from tqdm import tqdm

from ... import api
from ...models import TwitterHashtag, TwitterPost, TwitterUser


class Command(BaseCommand):

    # TODO: Enable authentication if required
    # def add_arguments(self, parser):
    #     parser.add_argument('email', type=str)

    def handle(self, *args, **options):
        t0 = time.perf_counter()

        # TODO: Enable authentication if required
        # email = options['email']
        # user_id, user_key = api.twitter_get_user_credentials(email)

        count_twitter_post_created = 0
        count_twitter_user_created = 0

        for twitter_hashtag in TwitterHashtag.objects.all():
            post_data_overviews = api.twitter_get_posts_by_hashtag(twitter_hashtag.value)

            for post_data_overview in tqdm(post_data_overviews):

                try:
                    twitter_post = TwitterPost.objects.get(id=post_data_overview['tweetId'])

                except TwitterPost.DoesNotExist:

                    try:
                        twitter_user = TwitterUser.objects.get(id=post_data_overview['userid'])

                    except TwitterUser.DoesNotExist:

                        twitter_user = TwitterUser.objects.create(
                            id=post_data_overview['userid'],
                            name=post_data_overview['name'],
                            screen_name=post_data_overview['screenName'],
                        )
                        count_twitter_user_created += 1

                    post_data = api.twitter_get_post_metadata(post_data_overview['tweetId'])

                    twitter_post = TwitterPost.objects.create(
                        id=post_data['id'],
                        user=twitter_user,
                        like_count=post_data['likeCount'],
                        retweet_count=post_data['retweetCount'],
                        reply_count=post_data['replyCount'],
                    )
                    count_twitter_post_created += 1

                if twitter_hashtag not in twitter_post.hashtags.all():
                    twitter_post.hashtags.add(twitter_hashtag)

        t = time.perf_counter() - t0
        self.stdout.write('Created {} new twitter users'.format(count_twitter_user_created))
        self.stdout.write('Created {} new twitter posts'.format(count_twitter_post_created))
        self.stdout.write('Done! (took {:.2f} seconds)'.format(t))
