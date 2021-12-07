from django.contrib.auth import views
from django.urls import path
from list import views

urlpatterns = [
    # show list
    path('list/', views.list, name="list"),
    path('listAdmin/', views.listAdmin, name="listAdmin"),

    # import and ßexport file
    path('importList/', views.importList, name="importList"),
    path('exportList/', views.exportList, name="exportList"),


    path('delete-student/', views.delete, name="delete-student"),
    path('search-student/', views.search, name="search-student"),
    path('add-student/', views.add, name="add-student"),
]
