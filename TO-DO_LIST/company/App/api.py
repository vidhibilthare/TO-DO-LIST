from rest_framework import generics
from rest_framework.response import Response
from . models import *
from . serializers import EmployeeSerializer


class EmployeeCreateAPI(generics.CreateAPIView):
    querveset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeAPI(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class UpdateemployeeAPI(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeleteemployeeAPI(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetriveAPIview(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

