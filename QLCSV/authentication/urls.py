from django.contrib.auth import views
from django.urls import path
from authentication import views

urlpatterns = [
    # authentication
    path('login/', views.login, name="login"),
    path('forgotPass/', views.forgotPass, name="forgotPass"),
    path('forgotPassEmail/', views.forgotPassEmail, name="forgotPassEmail"),
    path('changePass/', views.changePass, name="changePass"),
    path('logout/', views.logout, name="logout"),

    # student registration
    path('registration/', views.UserReg, name="registration"),
    path('regSchool/', views.studentSchoolReg, name="regSchool"),
    path('regJob/', views.studentJobReg, name="regJob"),
    path('regGPA/', views.studentGPAReg, name="regGPA"),

    # main page
    path('afterLogin/', views.afterLogin, name="afterLogin"),

    # index page
    path('index/', views.index, name="index"),

    # user info
    path('search/', views.search, name="search"),

    path('event/', views.event_forum, name="event"),
]
