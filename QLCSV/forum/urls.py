from django.contrib.auth import views
from django.urls import path
from forum import views


urlpatterns = [
    path('', views.forum, name="forum"),
    path('discussion/id=<int:pk>', views.discussion, name="discussion"),
    path('topic/', views.topic, name="topic"),
    path('topic/edit/<int:pk>', views.editpost, name="editpost"),
    path('likepost/<int:pk>', views.likepost, name="like_post"),
    path('deletepost/<int:pk>', views.deletepost, name="deletepost"),
    path('deletecmt/<int:pk>', views.deletecmt, name="deletecmt"),
    path('discussion/editcmt/idcmt=<int:pk>', views.editcmt, name="editcmt"),
]
