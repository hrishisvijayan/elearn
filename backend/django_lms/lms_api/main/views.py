from ast import IsNot
from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse       # added as new after making react and to do login
from django.views.decorators.csrf import csrf_exempt    # added as new after making react and to do login
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework import permissions
from .serializers import TeacherSerializer,CategorySerializer,CourseSerializer,ChapterSerializer 
from . import models


#refer tutorial class based views Using mixins session read in django rest framework
#this is the power of rest api that we can do CRUD operations easily 
#all the below things are availabel in browsable api mode




class TeachersList(generics.ListCreateAPIView):       #through this class method we can view all the contents of the teacher allows to create data through post method
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
    # permission_classes=[permissions.IsAuthenticated]


class TeachersDetail(generics.RetrieveUpdateAPIView):   #through this class method we can view all the contents of the teacher allows to update data through put method
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
    # permission_classes=[permissions.IsAuthenticated]


class TeachersDetail(generics.RetrieveUpdateDestroyAPIView):   #through this class method we can delete the data 
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
    # permission_classes=[permissions.IsAuthenticated] 


@csrf_exempt
def teacher_login(request):
    email       = request.POST.get('email')
    password    = request.POST.get('password')
    teacherData = models.Teacher.objects.get(email=email,password=password)
    if teacherData:
        return JsonResponse({'bool' : True,'teacher_id':teacherData.id})       # this thing is used to get the user id of the current logged in teacher and to fetch all the courses under him --- inorder to have this id on the fronend we have to save in the local storage in the front end
    else:
        return JsonResponse({'bool' : False})


class CategoryList(generics.ListCreateAPIView):      
    queryset=models.CourseCategory.objects.all()
    serializer_class=CategorySerializer
    # permission_classes=[permissions.IsAuthenticated]

#course    
class CourseList(generics.ListCreateAPIView):       
    queryset=models.Course.objects.all()
    serializer_class=CourseSerializer
    # permission_classes=[permissions.IsAuthenticated]

        
#specific teacher course
class TeacherCourseList(generics.ListAPIView):       
    serializer_class=CourseSerializer
    # permission_classes=[permissions.IsAuthenticated]


    def get_queryset(self):                                   #here I am not creating any function but overwriting the query set inside apiview
        teacher_id=self.kwargs['teacher_id']                  # we are getting the id from self.keyword arguments -- this will be all in apiview class
        teacher=models.Teacher.objects.get(pk=teacher_id)     #after getting the id we have to take the teacher's id from the teachers table
        return models.Course.objects.filter(teacher=teacher)  #after that we can take the specific course according to the teachers id that we have taken in the above line     


#chapter                              #added as new
class ChapterList(generics.ListCreateAPIView): 
    queryset=models.Chapter.objects.all()      
    serializer_class=ChapterSerializer



