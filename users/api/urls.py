
from django.contrib import admin
from django.urls import path, include
from users.api.views import FrateUsersView

urlpatterns = [
    path('login/', FrateUsersView.as_view(), name="callbackurl"),
]
