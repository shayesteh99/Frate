from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.api.serializers import FUserSerializer
from users.models import FrateUser

class FrateUsersView(CreateAPIView):
    queryset = FrateUser.objects.all()
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

    def get(self, request):
        # fusers = []
        # for u in User.objects.all():
        #     a = {}
        #     a['Username'] = u.Username
        #     a['Password'] = u.Password
        #     a['Email'] = u.email
        #     fusers.append(a)
        serializer = FUserSerializer(FrateUser.objects.get())
        # fusers = [u for u in ]
        from rest_framework.response import Response
        return Response(serializer.data)

   