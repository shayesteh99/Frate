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
    	email = request.data['Email']
    	username = request.data['Username']
    	password = request.data['Password']


    	from users.models import FrateUser
    	m = FrateUser.objects.create(
    		Email = email,
    		Username = username,
    		Password = password
    		)
    	m.save()

    	from rest_framework.response import Response

    	return Response(data = {'Status': 1})

    def get(seld, request):
        pass

   