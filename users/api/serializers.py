from rest_framework import serializers
from users.models import FrateUser, FratePost, FrateFollower, FrateComment

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

class FCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrateComment
        fields = ['id', 'username', 'comment', 'postID']