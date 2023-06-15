from django.urls import path
from .views import StudentCreateAPI,StudentAPI,UpdatestudentAPI,DeletestudentAPI,StudentRetriveAPIview,RegistrationAPIView,LoginAPIView


urlpatterns = [

    path('api/',StudentCreateAPI.as_view()),
    path('api/ragistration',RegistrationAPIView.as_view()),
    path('api/login',LoginAPIView.as_view()),


    path('',StudentAPI.as_view()),
    path('update/<int:pk>', UpdatestudentAPI.as_view()),
    path('delete/<int:pk>',DeletestudentAPI.as_view()),
    path('get/<int:pk>',StudentRetriveAPIview.as_view()),
     
]
