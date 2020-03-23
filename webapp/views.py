from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeList(APIView):
    def get(self,request):
        emp = Employee.objects.all()
        ser = EmployeeSerializer(emp,many=True)
        return Response(ser.data)

    def post(self,request):
        pass