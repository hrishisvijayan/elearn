from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework import permissions
from .serializers import TeacherSerializer
from . import models


#refer tutorial class based views Using mixins session read in django rest framework
#this is the power of rest api that we can do CRUD operations easily 
#all the below things are availabel in browsable api mode




class TeachersList(generics.ListCreateAPIView):       #through this class method we can view all the contents of the teacher allows to create data through post method
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
    permission_classes=[permissions.IsAuthenticated]


class TeachersDetail(generics.RetrieveUpdateAPIView):   #through this class method we can view all the contents of the teacher allows to update data through put method
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
    permission_classes=[permissions.IsAuthenticated]


class TeachersDetail(generics.RetrieveUpdateDestroyAPIView):   #through this class method we can delete the data 
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
    permission_classes=[permissions.IsAuthenticated] 


