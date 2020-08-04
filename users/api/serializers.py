from rest_framework import serializers
from users.models import FrateUser, FratePost, Comment, Follower

class FUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrateUser
        fields = ['id', 'username', 'password', 'email']

class FPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FratePost
        fields = ['id', 'username', 'date', 'filename', 'category', 'ratings', 'rateCount', 'caption']

class FFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['id', 'follower', 'following']

class FCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'username', 'comment', 'postID']