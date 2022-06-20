from unicodedata import category
from django.db import models

# Create your models here.


#Teacher model
class Teacher(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=200,null=True)
    mobile_no = models.CharField(max_length=20)
    address=models.TextField()

    class Meta:                #this meta is used inorder to modify the name of database during display in django admin page
        verbose_name_plural = "1. Teacher" 

#Course Category Model
class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:                #this meta is used inorder to modify the name of database during display in django admin page
        verbose_name_plural = "2. Course Categories"         




#Course Model
class Course(models.Model):
    category = models.ForeignKey(CourseCategory,on_delete=models.CASCADE)    #here cascade so that if the course category is deleted then the the course is deleted
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE) 
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:                #this meta is used inorder to modify the name of database during display in django admin page
        verbose_name_plural = "3. Course " 


#Teacher model
class Student(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=20)
    address=models.TextField() 
    interested_categories=models.TextField() 


    class Meta:                #this meta is used inorder to modify the name of database during display in django admin page
        verbose_name_plural = "4. Student" 



