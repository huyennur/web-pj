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
    path('export_donation/', views.export_donation, name="export_donation"),
    path('export_introduce/', views.export_introduce, name="export_introduce"),
    path('export_teachingReg/', views.export_teachingReg,
         name="export_teachingReg"),
]
