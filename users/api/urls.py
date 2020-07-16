
from django.contrib import admin
from django.urls import path, include
from users.api.views import FrateUsersView, FratePostsView, FrateFollowersView, FrateCommentsView

urlpatterns = [
    path('login/', FrateUsersView.as_view(), name="users"),
    path('posts/', FratePostsView.as_view(), name="posts"),
    path('followers/', FrateFollowersView.as_view(), name="followers"),
    path('comments/', FrateCommentsView.as_view(), name="comments"),
]
