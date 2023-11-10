# post/views.py

from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "posts": reverse("post-list", request=request, format=format),
            "likes": reverse("like-list", request=request, format=format),
        }
    )


class UserList(generics.ListAPIView):
    """
    List all the posts, or create a new post.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    List all the posts, or create a new post.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostList(APIView):
    """
    List all the posts, or create a new post.
    """

    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, format=None):
        posts = Post.objects.all()
        post_serializer = PostSerializer(posts, many=True)
        return Response({"posts": post_serializer.data})

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    """
    Retrieve a single post.
    """

    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


class LikeList(APIView):
    """
    List all the likes, or create a new like.

    """

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        likes = Like.objects.all()
        like_serializer = LikeSerializer(likes, many=True)
        return Response({"likes": like_serializer.data})

    def like(self, request):
        # [IsAuthenticatedOrReadOnly]
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


class LikeDetail(APIView):
    """
    Retrieve a single like.
    """

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Like.objects.get(pk=pk)
        except Like.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
