from django.contrib.auth import views
from django.urls import path
from statistic import views

urlpatterns = [
    # Thống kê tình trạng nghề nghiệp
    path('jobStatus/', views.jobStatus, name="jobStatus"),
    path('jobStatus_k/', views.jobStatus_k, name="jobStatus_k"),

    # Thống kê mức lương ra trường
    path('income/', views.income, name="income"),
    path('income_k/', views.income_k, name="income_k"),

    # Thống kê nơi làm việc
    path('otherStatistics/', views.otherStatistics, name="otherStatistics"),
    path('otherStatistics_k/', views.otherStatistics_k, name="otherStatistics_k")
]
