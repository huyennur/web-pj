from django.contrib.auth import views
from django.urls import path
from report import views

urlpatterns = [
    path('report/', views.report, name="report"),
]
