from django.db import models

# Create your models here.

class FrateUser(models.Model):
	Email = models.EmailField()
	Username = models.CharField(max_length = 50, blank = True)
	Password = models.CharField(max_length = 20, blank = True)