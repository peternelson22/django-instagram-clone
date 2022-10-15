from django.contrib import admin
from .models import LikePost, Profile, Post, FollowersCount

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
