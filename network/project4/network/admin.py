from django.contrib import admin
from . models import  follower, post, User

# Register your models here.
admin.site.register(User)
admin.site.register(post)
admin.site.register(follower)
