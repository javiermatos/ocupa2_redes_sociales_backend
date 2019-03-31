from django.contrib import admin

from . import models


@admin.register(models.InstagramHashtag)
class InstagramHashtagAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')


@admin.register(models.InstagramUser)
class InstagramUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'follower_count', 'media_count')


@admin.register(models.InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'all_hashtags', 'media_type', 'like_count', 'comments_count')
    list_filter = ('media_type',)

    def all_hashtags(self, obj):
        return ', '.join(obj.hashtags.all().values_list('value', flat=True))
