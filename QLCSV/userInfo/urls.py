from django.contrib.auth import views
from django.urls import path
from userInfo import views

urlpatterns = [
    path('profile/<user_mssv>', views.profile, name='profile'),
    path('editProfile/', views.editProfile, name="updateProfile"),
]
