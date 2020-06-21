from django.db import models

# Create your models here.

class FrateUser(models.Model):
	Email = models.EmailField()
	Username = models.CharField(max_length = 50)
	Password = models.CharField(max_length = 20)

class FratePost(models.Model):
	Username = models.CharField(max_length = 50)
	Date = models.CharField(max_length = 20)
	Filename = models.CharField(max_length = 50)
	Category = models.IntegerField()
	Ratings = models.CharField(max_length = 20)
	Caption = models.CharField(max_length = 100, blank = True)
