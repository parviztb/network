from time import timezone
from xmlrpc.client import DateTime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.conf import settings
import datetime




class User(AbstractUser):
    pass

class post(models.Model):
    author        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=DO_NOTHING,related_name ='author')
    title         = models.CharField(max_length=100)
    des_content   = models.TextField(max_length=300 , null=True, blank=True,)
    likes         = models.DecimalField(max_digits=6, decimal_places=0)
    status        = models.BooleanField(default=False) 
    created_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} : {self.title} - {self.des_content} "

class follower(models.Model):
    followeruser    = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=CASCADE, related_name='followeruser')
    followpost = models.ForeignKey('post', on_delete = CASCADE)
    def __str__(self):
        return f"{self.followeruser} : {self.followpost}"