
from django.contrib import admin
from django.urls import path, include
from users.api.views import FrateUsersView, FratePostsView

urlpatterns = [
    path('login/', FrateUsersView.as_view(), name="users"),
    path('posts/', FratePostsView.as_view(), name="posts"),
]
