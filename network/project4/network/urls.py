
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addpost", views.addpost, name="addpost"),
    path("updatepost", views.updatepost, name="updatepost"),
    path("upload", views.upload, name="upload"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
