from django.contrib.auth import views
from django.urls import path
from notification import views


urlpatterns = [
    path('', views.all_notifi, name="notifi"),

]
