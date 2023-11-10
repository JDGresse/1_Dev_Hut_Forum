# post/serializer.py

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Like


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fileds = ["id", "username", "posts"]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "body",
            "created_on",
        ]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "post", "liked_by", "liked_on"]
