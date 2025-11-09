from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    login_id = models.CharField(max_length=50, unique=True)
    nickname = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    profile_img_url = models.URLField(null=True, blank=True)
    point = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nickname