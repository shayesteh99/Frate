from django.contrib import admin
from users.models import FrateUser, FratePost, FrateFollower, FrateComment

# Register your models here.
admin.site.register(FrateUser)
admin.site.register(FratePost)
admin.site.register(FrateFollower)
admin.site.register(FrateComment)