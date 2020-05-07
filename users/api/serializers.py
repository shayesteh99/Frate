from rest_framework import serializers
from users.models import FrateUser

class FUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrateUser
        fields = ['id']