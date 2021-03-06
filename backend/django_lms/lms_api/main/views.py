from ast import IsNot
from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse       # added as new after making react and to do login
from django.views.decorators.csrf import csrf_exempt    # added as new after making react and to do login
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework import permissions
from .serializers import StudentSerializer, TeacherSerializer,CategorySerializer,CourseSerializer,ChapterSerializer 
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
    print('this is email',email)
    print('this is password',password)
    try:
        teacherData = models.Teacher.objects.get(email=email,password=password)
    # except:                  this commented code was my own code
    #     teacherData = None
    #     print(teacherData)
    except models.Teacher.DoesNotExist:   #this is the standard code
        teacherData = None

    if teacherData:
        print('inside if')
        return JsonResponse({'bool' : True,'teacher_id':teacherData.id})       # this thing is used to get the user id of the current logged in teacher and to fetch all the courses under him --- inorder to have this id on the fronend we have to save in the local storage in the front end
    else:
        print('outside if')
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

#specific chapter under courses         added as new also 
class CourseChapterList(generics.ListAPIView): 
    # queryset=models.Chapter.objects.all()      
    serializer_class=ChapterSerializer
    
    def get_queryset(self):
        course_id = self.kwargs['course_id']       #here the id that we pass along with url is taken 
        course=models.Course.objects.get(pk=course_id)
        return models.Chapter.objects.filter(course=course)


class ChapterSingle(generics.RetrieveUpdateAPIView): 
    queryset=models.Chapter.objects.all()      
    serializer_class=ChapterSerializer



#student
class StudentList(generics.ListCreateAPIView):       #through this class method we can view all the contents of the teacher allows to create data through post method
    queryset=models.Student.objects.all()
    serializer_class=StudentSerializer


class StudentDetail(generics.RetrieveUpdateAPIView):   #through this class method we can delete the data 
    queryset=models.Student.objects.all()
    serializer_class=StudentSerializer
    # permission_classes=[permissions.IsAuthenticated] 



@csrf_exempt
def student_login(request):
    email       = request.POST.get('email')
    password    = request.POST.get('password')
    print('this is email',email)
    print('this is password',password)
    try:
        studentData = models.Student.objects.get(email=email,password=password)
    # except:                  this commented code was my own code
    #     teacherData = None
    #     print(teacherData)
    except models.Student.DoesNotExist:   #this is the standard code
        studentData = None

    if studentData:
        print('inside if')
        return JsonResponse({'bool' : True,'student_id':studentData.id})       # this thing is used to get the user id of the current logged in teacher and to fetch all the courses under him --- inorder to have this id on the fronend we have to save in the local storage in the front end
    else:
        print('outside if')
        return JsonResponse({'bool' : False})