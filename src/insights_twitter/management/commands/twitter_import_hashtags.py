import time

from django.core.management import BaseCommand
from tqdm import tqdm

from insights.data import hashtags
from ... import api
from ...models import TwitterHashtag


class Command(BaseCommand):

    # TODO: Enable authentication if required
    # def add_arguments(self, parser):
    #     parser.add_argument('email', type=str)

    def handle(self, *args, **options):
        t0 = time.perf_counter()

        # TODO: Enable authentication if required
        # email = options['email']
        # user_id, user_key = api.twitter_get_user_credentials(email)

        count_instagram_hashtag_created = 0

        for hashtag in tqdm(hashtags):
            hashtag = hashtag[1:]  # remove # character

            try:
                twitter_hashtag = TwitterHashtag.objects.get(value=hashtag)
            except TwitterHashtag.DoesNotExist:
                twitter_hashtag = TwitterHashtag.objects.create(
                    value=hashtag,
                )
                count_instagram_hashtag_created += 1

        t = time.perf_counter() - t0
        self.stdout.write('Created {} new instagram hashtags'.format(count_instagram_hashtag_created))
        self.stdout.write('Done! (took {:.2f} seconds)'.format(t))
