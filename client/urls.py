
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('client-dashboard', views.client_dashboard, name="client-dashboard"),
    path('browse-articles', views.browse_articles, name="browse-articles"),
    path("Subscription_locked", views.Subscription_locked,
         name="Subscription-locked"),

]
