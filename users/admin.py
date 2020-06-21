from django.contrib import admin
from users.models import FrateUser, FratePost

# Register your models here.
admin.site.register(FrateUser)
admin.site.register(FratePost)