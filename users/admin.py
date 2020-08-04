from django.contrib import admin
from users.models import FrateUser, FratePost, FrateFollower, FrateComment, Follower

# Register your models here.
admin.site.register(FrateUser)
admin.site.register(FratePost)
admin.site.register(FrateFollower)
admin.site.register(Follower)
admin.site.register(FrateComment)