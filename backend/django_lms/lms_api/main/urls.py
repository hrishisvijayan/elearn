# from unicodedata import category
from django.urls import path

# from django_lms.lms_api.main.models import Course, CourseCategory
from . import views


urlpatterns = [
    #teacher
    path('teacher/', views.TeachersList.as_view()),
    path('teacher/<int:pk>/', views.TeachersDetail.as_view()),
    path('teacher-login',views.teacher_login),
    #categroy 
    path('category/',views.CategoryList.as_view()),
    #course
    path('course/',views.CourseList.as_view())
]