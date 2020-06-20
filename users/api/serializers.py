from rest_framework import serializers
from users.models import FrateUser, FratePost

class FUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrateUser
        fields = ['id', 'Username', 'Password', 'Email']

class FPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FratePost
        fields = ['id', 'Username', 'Date', 'Filename', 'Category', 'Ratings', 'Caption']