from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    #NAME of the USER
    first_name = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=15, default="")
    #address of the USER
    last_name = models.CharField(max_length=50, default="")

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email