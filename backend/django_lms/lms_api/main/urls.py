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
    path('course/',views.CourseList.as_view()),
    #chapter
    path('chapter/',views.ChapterList.as_view()),

    # specific chapter
    path('course-chapter/<int:course_id>',views.CourseChapterList.as_view()),

    #teacher Courses
    path('teacher-courses/<int:teacher_id>',views.TeacherCourseList.as_view()),

]