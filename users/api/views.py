from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.api.serializers import FUserSerializer
from users.models import FrateUser

class FrateUsersView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = FUserSerializer
    permission_classes = [AllowAny]

    def create(self, request):
    	print("data: ", request.data)
    	username = request.data['Username']
    	password = request.data['Password']

   