from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('my_login', views.my_login, name="my_login")



]
