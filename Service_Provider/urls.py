from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.serviceproviderlogin, name="serviceproviderlogin"),
    path("dashboard/", views.View_Remote_Users, name="View_Remote_Users"),
    path("train-test/", views.Train_Test_Datasets, name="Train_Test_Datasets"),
    path("charts/<str:chart_type>/", views.charts, name="charts"),
    path("predicted/", views.View_Air_Pollution_Predicted_Details, name="View_Air_Pollution_Predicted_Details"),
    path("ratio/", views.Find_Air_Pollution_Predicted_Ratio, name="Find_Air_Pollution_Predicted_Ratio"),
    path("likeschart/<str:chart_type>/", views.likeschart, name="likeschart"),
    path("download/", views.Download_Trained_DataSets, name="Download_Trained_DataSets"),
]
