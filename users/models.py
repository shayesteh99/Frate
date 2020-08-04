from django.db import models

# Create your models here.

class FrateUser(models.Model):
	email = models.EmailField()
	username = models.CharField(max_length = 50)
	password = models.CharField(max_length = 20)

class FratePost(models.Model):
	username = models.CharField(max_length = 50)
	date = models.CharField(max_length = 20)
	filename = models.CharField(max_length = 500)
	category = models.IntegerField()
	ratings = models.CharField(max_length = 20)
	rateCount = models.CharField(max_length = 10, default = "0")
	caption = models.CharField(max_length = 100, blank = True)

class Follower(models.Model):
	follower = models.ForeignKey(FrateUser, on_delete = models.CASCADE, related_name = 'followings')
	following = models.ForeignKey(FrateUser, on_delete = models.CASCADE, related_name = 'followers')

# class Comment(models.Model):
# 	username = models.CharField(max_length = 50)
# 	comment = models.CharField(max_length = 100)
# 	postID = models.IntegerField()

class FrateFollower(models.Model):
	follower = models.CharField(max_length = 50)
	following = models.CharField(max_length = 50)

class FrateComment(models.Model):
	username = models.CharField(max_length = 50)
	comment = models.CharField(max_length = 100)
	postID = models.IntegerField()