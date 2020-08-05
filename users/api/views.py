from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from users.api.serializers import FUserSerializer, FPostSerializer, FFollowerSerializer, FCommentSerializer
from users.models import FrateUser, FratePost, Follower, Comment

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
    		email = email,
    		username = username,
    		password = password
    		)
    	m.save()

    	return Response(data = {'Status': 1})

class FratePostsUpdateView(UpdateAPIView):
    queryset = FratePost.objects.all()
    serializer_class = FPostSerializer
    permission_classes = [AllowAny]

class FratePostsView(ListCreateAPIView, DestroyAPIView):
    queryset = FratePost.objects.all()
    serializer_class = FPostSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        print(request.data)

        username = request.data['Username']
        u = FrateUser.objects.get(id=username)

        filename = request.data['Filename']
        category = request.data['Category']
        ratings = request.data['Ratings']
        ratec = request.data['RateCount']
        caption = request.data['Caption']
        dateobj = datetime.now()
        date = dateobj.strftime("%b %d, %Y")

        m = FratePost.objects.create(
            username = u,
            date = date,
            filename = filename,
            category = category,
            ratings = ratings,
            rateCount = ratec,
            caption = caption
            )
        m.save()

        return Response(data = {'Status': 1})

class FrateFollowersView(ListCreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FFollowerSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        follower = request.data['Follower']
        following = request.data['Following']
        f1 = FrateUser.objects.get(id=follower)
        f2 = FrateUser.objects.get(id=following)

        m = Follower.objects.create(
            follower = f1,
            following = f2
            )
        m.save()

        return Response(data = {'Status': 1})

class FrateFollowersDeleteView(DestroyAPIView):
    queryset = Follower.objects.all()
    serializer_class = FFollowerSerializer
    permission_classes = [AllowAny]


class FrateCommentsView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = FCommentSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        username = request.data['Username']
        u = FrateUser.objects.get(id=username)

        comment = request.data['Comment']
        post = request.data['Post']
        p = FratePost.objects.get(id=post)


        m = Comment.objects.create(
            username = u,
            comment = comment,
            post = p
            )
        m.save()

        return Response(data = {'Status': 1})



   