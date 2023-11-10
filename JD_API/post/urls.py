# --> post/urls.py

"""
Wire views up.
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from post import views

urlpatterns = [
    path("posts/", views.PostList.as_view()),
    path("posts/<int:pk>/", views.PostDetail.as_view()),
    path("posts/likes", views.LikeList.as_view()),
    path("posts/<int:pk>/", views.PostDetail.as_view()),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
