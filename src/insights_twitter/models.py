from django.db import models


class TwitterHashtag(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.value


class TwitterUser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    screen_name = models.CharField(max_length=64)


class TwitterPost(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
    )
    hashtags = models.ManyToManyField(
        TwitterHashtag,
        blank=True,
    )
    like_count = models.IntegerField()
    retweet_count = models.IntegerField()
    reply_count = models.IntegerField()

    def __str__(self):
        return self.id
