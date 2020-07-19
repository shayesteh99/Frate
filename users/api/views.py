from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from users.api.serializers import FUserSerializer, FPostSerializer, FFollowerSerializer, FCommentSerializer
from users.models import FrateUser, FratePost, FrateFollower, FrateComment

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

class FratePostsView(ListCreateAPIView, UpdateAPIView, DestroyAPIView):
    queryset = FratePost.objects.all()
    serializer_class = FPostSerializer
    permission_classes = [AllowAny]

    def delete(self, request):
        print(len(FratePost.objects))

    def create(self, request):
        print(request.data)

        username = request.data['Username']
        filename = request.data['Filename']
        category = request.data['Category']
        ratings = request.data['Ratings']
        ratec = request.data['RateCount']
        caption = request.data['Caption']
        dateobj = datetime.now()
        date = dateobj.strftime("%b %d, %Y")

        m = FratePost.objects.create(
            username = username,
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
    queryset = FrateFollower.objects.all()
    serializer_class = FFollowerSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        follower = request.data['Follower']
        following = request.data['Following']

        m = FrateFollower.objects.create(
            follower = follower,
            following = following
            )
        m.save()

        return Response(data = {'Status': 1})


class FrateCommentsView(ListCreateAPIView):
    queryset = FrateComment.objects.all()
    serializer_class = FCommentSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        username = request.data['Username']
        comment = request.data['Comment']
        postid = request.data['PostID']

        m = FrateComment.objects.create(
            username = username,
            comment = comment,
            postID = postid
            )
        m.save()

        return Response(data = {'Status': 1})


   