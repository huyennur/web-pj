from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('<str:toUser>/', views.room, name='room'),
    path('index/get-messages/', views.getMessages, name='get-messages'),
    path('index/create-msg/', views.createMsg, name='create-msg'),
    path('index/check-room/', views.checkRoom, name='check-room'),
    path('index/load-contacts/', views.loadContacts, name='load-contacts'),
]