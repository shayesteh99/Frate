from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from users.api.serializers import FUserSerializer, FPostSerializer
from users.models import FrateUser, FratePost

from rest_framework.response import Response

from datetime import datetime

class FrateUsersView(ListCreateAPIView):
    queryset = FrateUser.objects.all()
    serializer_class = FUserSerializer
    permission_classes = [AllowAny]

    def create(self, request):
    	email = request.data['Email']
    	username = request.data['Username']
    	password = request.data['Password']

    	m = FrateUser.objects.create(
    		Email = email,
    		Username = username,
    		Password = password
    		)
    	m.save()

    	return Response(data = {'Status': 1})

class FratePostsView(ListCreateAPIView):
    queryset = FratePost.objects.all()
    serializer_class = FPostSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        print(request.data)

        username = request.data['Username']
        filename = request.data['Filename']
        category = request.data['Category']
        ratings = request.data['Ratings']
        caption = request.data['Caption']
        dateobj = datetime.now()
        date = dateobj.strftime("%b %d, %Y")

        m = FratePost.objects.create(
            Username = username,
            Date = date,
            Filename = filename,
            Category = category,
            Ratings = ratings,
            Caption = caption
            )
        m.save()

        return Response(data = {'Status': 1})

    def update(self, request):
        print(request.data)
        

   