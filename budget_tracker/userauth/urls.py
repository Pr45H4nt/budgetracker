from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("logout", views.logoutview, name= "logout"),
    path("login", views.loginview , name = "login"),
    path("edituser", views.edituser , name= 'edituser')
]