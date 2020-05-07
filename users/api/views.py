from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
# from rest_framework.permissions import IsAdminUser

from users.api.serializers import FUserSerializer
from users.models import FrateUser

class FrateUsersView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = FUserSerializer
    def create(self, request):
    	print("data: ", request.data)

   