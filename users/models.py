from django.db import models

# Create your models here.

class FrateUser(models.Model):
	Username = models.EmailField(blank = True)
	Password = models.CharField(max_length = 20, blank = True)