
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from users.api.views import FrateUsersView, FratePostsView, FrateFollowersView, FrateCommentsView, FratePostsUpdateView, FrateFollowersDeleteView

urlpatterns = [
    path('login/', FrateUsersView.as_view(), name="users"),
    path('posts/', FratePostsView.as_view(), name="posts"),
    url(r'^posts/(?P<pk>\d+)/$', FratePostsUpdateView.as_view(), name="update posts"),
    path('followers/', FrateFollowersView.as_view(), name="followers"),
    url(r'^followers/(?P<pk>\d+)/$', FrateFollowersDeleteView.as_view(), name="delete followers"),
    path('comments/', FrateCommentsView.as_view(), name="comments"),
    
]
