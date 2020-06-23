from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
import datetime
from datetime import date


class Myuser(models.Model):
    category_choices=(
    ('Student','Student'),
    ('Teacher','Teacher'),
    ('Admin','Admin'),
    ('CourseCoordinator','CourseCoordinator')

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    phone_num = models.BigIntegerField(null=True,blank=True)
    category= models.CharField(max_length=150,default="",choices=category_choices)
def __str__(self):
        return self.firstname+' '+self.lastname
class  Student(models.Model):
    category_choices=(
    ('Student','Student'),
    ('Teacher','Teacher'),
    ('Admin','Admin'),
    ('CourseCoordinator','CourseCoordinator')

    )
    Branch_choices=(
    ('ECE','ECE'),
    ('CSE','CSE'),
    ('EEE','EEE'),
    ('mech','mech')

    )
    username = models.CharField(max_length=150,default="",)

    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email= models.EmailField(max_length=150,null=True,blank=True)

    phone_num = models.BigIntegerField(null=True,blank=True)
    year = models.BigIntegerField(null=True,blank=True)
    roll_num= models.CharField(max_length=150)
    branch=models.CharField(max_length=150,default="",choices=Branch_choices)
    category= models.CharField(max_length=150,default="",choices=category_choices)
    def __str__(self):
        return self.username
class Meta:
        permissions = (("is_student", "is_student"), )

class  Professor(models.Model):
    category_choices=(
    ('Student','Student'),
    ('Teacher','Teacher'),
    ('Admin','Admin'),
    ('CourseCoordinator','CourseCoordinator')

    )
    Branch_choices=(
    ('ECE','ECE'),
    ('CSE','CSE'),
    ('EEE','EEE'),
    ('mech','mech')

    )
    username = models.CharField(max_length=150,default="",)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email= models.EmailField(max_length=150,null=True,blank=True)
    phone_num = models.BigIntegerField(null=True,blank=True)
    branch=models.CharField(max_length=150,default="",choices=Branch_choices)
    category= models.CharField(max_length=150,default="",choices=category_choices)
    def __str__(self):
        return self.firstname
class  CourseCoordinator(models.Model):
    category_choices=(
    ('Student','Student'),
    ('Teacher','Teacher'),
    ('Admin','Admin'),
    ('CourseCoordinator','CourseCoordinator')

    )

    username = models.CharField(max_length=150,default="",)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email= models.EmailField(max_length=150,null=True,blank=True)
    phone_num = models.BigIntegerField(null=True,blank=True)

def __str__(self):
        return self.firstname+' '+self.lastname

class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True,default='')
    name = models.CharField(max_length=100)
    student=models.ManyToManyField(Student, related_name='courses')
    taught_by = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_prof",default=" ")
    startdate= models.DateField(default=datetime.date.today)
    enddate=models.DateField(default=datetime.date.today)

class Attendance(models.Model):
    IS_PRESENT = (
		('0', 'ABSENT'),
		('1', 'PRESENT'),
	)
    course_id = models.CharField(max_length=10)	# Use foreign key if possible
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_stud")
    taught_by = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_prof")
    date = models.DateField(default=datetime.date.today)	# Date is a string of the form YYYY-MM-DD
    is_present = models.CharField(max_length=1, choices = IS_PRESENT, default='0')

    class Meta:		# This is included to make the row unique w.r.t course_id, student and date taken together.
    	unique_together = ('course_id', 'student', 'date',)
class Query(models.Model):
    STATUS = (
		('0', 'IN PROGRESS'),
		('1', 'ACCEPTED'),
		('2', 'DECLINED'),
	)
    course_id = models.CharField(max_length=10)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_stud")
    date = models.DateField(default=datetime.date.today)
    query = models.CharField(max_length=500)
    status = models.CharField(max_length=1, choices = STATUS, default='0')
