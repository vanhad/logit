from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=15, default="")
    last_name = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.username