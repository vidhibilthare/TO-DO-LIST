from django.urls import path
from .api import EmployeeCreateAPI,EmployeeAPI,UpdateemployeeAPI,DeleteemployeeAPI,EmployeeRetriveAPIview

urlpatterns = [

    path('api/create',EmployeeCreateAPI.as_view()),
    path('',EmployeeAPI.as_view()),
    path('api/<int:pk>',UpdateemployeeAPI.as_view()),
    path('api/delete/<int:pk>',DeleteemployeeAPI.as_view()),
    path('api/get/<int:pk>',EmployeeRetriveAPIview.as_view()),


]
