from django.contrib import admin

from . import models


@admin.register(models.TwitterHashtag)
class TwitterHashtagAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')


@admin.register(models.TwitterUser)
class TwitterUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'screen_name')


@admin.register(models.TwitterPost)
class TwitterPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'all_hashtags', 'like_count', 'retweet_count', 'reply_count')

    def all_hashtags(self, obj):
        return ', '.join(obj.hashtags.all().values_list('value', flat=True))
