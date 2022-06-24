from django.urls import path
from . import views


urlpatterns = [
    path('teacher/', views.TeachersList.as_view()),
    path('teacher/<int:pk>/', views.TeachersDetail.as_view()),
    path('teacher-login',views.teacher_login)
]