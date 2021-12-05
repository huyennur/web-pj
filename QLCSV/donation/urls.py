from django.contrib.auth import views
from django.urls import path
from donation import views

urlpatterns = [
    path('donation/', views.donation, name="donation"),
    path('registration/', views.registration_teaching, name="regis"),
    path('introduce/', views.introduce, name="introduce"),
    path('search-donation/', views.searchDonation, name="search-donation"),
    path('search-introduce/', views.searchIntroduce, name="search-introduce"),
    path('search-regs/', views.searchRegs, name="search-regs"),
]
