from django.contrib.auth import views
from django.urls import path
from report import views

urlpatterns = [
    path('report/', views.report, name="report"),
    path('export_report/', views.export_report, name="export_report"),
]
