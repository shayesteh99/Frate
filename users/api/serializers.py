from rest_framework import serializers
from users.models import FrateUser, FratePost, FrateFollower

class FUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrateUser
        fields = ['id', 'username', 'password', 'email']

class FPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FratePost
        fields = ['id', 'username', 'date', 'filename', 'category', 'ratings', 'caption']

class FFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrateFollower
        fields = ['id', 'follower', 'following']