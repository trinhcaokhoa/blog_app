from django.db import models
class User(models.Model):
	user_name = models.CharField(max_length=200)
	user_password = models.CharField(max_length=200)
	fields = '__all__'
# Create your models here.
