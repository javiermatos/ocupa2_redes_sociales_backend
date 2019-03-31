import time

from django.core.management import BaseCommand
from tqdm import tqdm

from insights.data import hashtags
from ... import api
from ...models import InstagramHashtag


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('email', type=str)

    def handle(self, *args, **options):
        t0 = time.perf_counter()

        email = options['email']
        user_id, user_key = api.instagram_get_user_credentials(email)

        count_instagram_hashtag_created = 0

        for hashtag in tqdm(hashtags):
            hashtag = hashtag[1:]  # remove # character
            hashtag_id = api.instagram_get_hashtag_id(hashtag, user_id)

            try:
                instagram_hashtag = InstagramHashtag.objects.get(id=hashtag_id)
            except InstagramHashtag.DoesNotExist:
                instagram_hashtag = InstagramHashtag.objects.create(
                    id=hashtag_id,
                    value=hashtag,
                )
                count_instagram_hashtag_created += 1

        t = time.perf_counter() - t0
        self.stdout.write('Created {} new instagram hashtags'.format(count_instagram_hashtag_created))
        self.stdout.write('Done! (took {:.2f} seconds)'.format(t))
