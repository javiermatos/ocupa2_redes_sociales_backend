from django.db import models


class InstagramHashtag(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.value


class InstagramUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=64)
    follower_count = models.IntegerField()
    media_count = models.IntegerField()

    def __str__(self):
        return self.username


class InstagramPost(models.Model):

    MEDIA_TYPE_CAROUSEL = 'CAROUSEL'
    MEDIA_TYPE_PHOTO = 'PHOTO'
    MEDIA_TYPE_VIDEO = 'VIDEO'
    MEDIA_TYPE_CHOICES = (
        MEDIA_TYPE_CAROUSEL,
        MEDIA_TYPE_PHOTO,
        MEDIA_TYPE_VIDEO,
    )

    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(
        InstagramUser,
        on_delete=models.CASCADE,
    )
    hashtags = models.ManyToManyField(
        InstagramHashtag,
        blank=True,
    )
    media_type = models.CharField(
        max_length=32,
        choices=[(c, c) for c in MEDIA_TYPE_CHOICES],
    )
    like_count = models.IntegerField()
    comments_count = models.IntegerField()

    def __str__(self):
        return self.id
