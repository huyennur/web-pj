from django.contrib.auth import views
from django.urls import path
from donation import views

urlpatterns = [
    path('donation/', views.donation, name="donation"),
    path('registration/', views.registration_teaching, name="regis"),
    path('introduce/', views.introduce, name="introduce"),
]
