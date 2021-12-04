from django.contrib.auth import views
from django.urls import path
from connection import views

urlpatterns = [
    path('', views.connect, name="connect"),
    path('group/<int:pk>', views.group, name="group"),
    path('discussion/<int:pk1>/<int:pk2>',
         views.g_discussion, name="g_discussion"),
    path('topic/<int:pk>', views.g_topic, name="g_topic"),
    path('topic/edit/<int:pk1>/<int:pk2>', views.g_editpost, name="g_editpost"),
    path('deletepost/<int:pk1>/<int:pk2>',
         views.g_deletepost, name="g_deletepost"),
    path('deletecmt/<int:pk1>/<int:pk2>',
         views.g_deletecmt, name="g_deletecmt"),
    path('discussion/editcmt/<int:pk1>/<int:pk2>',
         views.g_editcmt, name="g_editcmt"),
]
