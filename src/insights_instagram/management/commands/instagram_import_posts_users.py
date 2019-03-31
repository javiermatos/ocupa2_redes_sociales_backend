import time

from django.core.management import BaseCommand
from tqdm import tqdm

from ... import api
from ...models import InstagramHashtag, InstagramPost, InstagramUser


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('email', type=str)

    def handle(self, *args, **options):
        t0 = time.perf_counter()

        email = options['email']
        user_id, user_key = api.instagram_get_user_credentials(email)

        count_instagram_post_created = 0
        count_instagram_user_created = 0

        for instagram_hashtag in InstagramHashtag.objects.all():
            post_data_overviews = api.instagram_get_posts_by_hashtag_id_top_media(instagram_hashtag.id, user_id)

            for post_data_overview in tqdm(post_data_overviews):

                try:
                    instagram_post = InstagramPost.objects.get(id=post_data_overview['id'])

                except InstagramPost.DoesNotExist:
                    post_data = api.instagram_get_post_metadata(post_data_overview['id'])

                    try:
                        instagram_user = InstagramUser.objects.get(id=post_data['userId'])

                    except InstagramUser.DoesNotExist:
                        user_data = api.instagram_get_user_metadata(post_data['userId'])

                        instagram_user = InstagramUser.objects.create(
                            id=user_data['id'],
                            username=user_data['username'],
                            follower_count=user_data['followerCount'],
                            media_count=user_data['mediaCount'],
                        )
                        count_instagram_user_created += 1

                    instagram_post = InstagramPost.objects.create(
                        id=post_data['id'],
                        user=instagram_user,
                        media_type=post_data['mediaType'],
                        like_count=post_data['likeCount'],
                        comments_count=post_data['commentsCount'],
                    )
                    count_instagram_post_created += 1

                if instagram_hashtag not in instagram_post.hashtags.all():
                    instagram_post.hashtags.add(instagram_hashtag)

        t = time.perf_counter() - t0
        self.stdout.write('Created {} new instagram users'.format(count_instagram_user_created))
        self.stdout.write('Created {} new instagram posts'.format(count_instagram_post_created))
        self.stdout.write('Done! (took {:.2f} seconds)'.format(t))
