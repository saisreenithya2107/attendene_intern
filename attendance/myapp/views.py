from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User, auth
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, login as auth_login, logout as out, update_session_auth_hash
from django.conf import settings
from .models import Myuser,Student,Professor,Course,Attendance
from django.contrib.auth import authenticate
import random
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import csv, io
import os
from glob import glob
from datetime import date
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import subprocess




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# def cmail(request):
#     send_mail('sub', 'body', 'oclinic2020@gmail.com', ['sandeshjatla@gmail.com'], fail_silently= False)
#     return render(request, 'doctor/home.html')

def register(request):
    print("hi  dfg")
    print(request)
    registered = False
    if request.method == 'POST':
        user_form = Signup_user_form(request.POST)
        profile_form = Signup_profile_form(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            UserForm = user_form.save()
            UserForm.set_password(UserForm.password)
            UserForm.save()

            ProfileForm = profile_form.save(commit=False)
            ProfileForm.user = UserForm
            ProfileForm.save()
            registered = True
        else:
            return HttpResponse("Invalid details!")
    else:
        user_form = Signup_user_form()
        profile_form = Signup_profile_form()

    if registered:
        request.session['username'] = user_form.cleaned_data.get('username')
        return render(request,'doctor/login2.html')
    else:
        return render(request, 'doctor/signup.html', {'user_form': user_form, 'profile_form': profile_form})




def login1(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print("1")
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            print("3")
            temp = 1
            print("4")
            #doc = get_object_or_404(User, user=request.user)

            print("5")
            print(request.user)
            user=request.user

            #return HttpResponse("Loginsuccssefful")
            if user.is_superuser:

                return render(request,'doctor/afterlogin.html')
            elif user.is_staff:
                print("hi prof")
                return redirect('/prof_home')
            else:
                return redirect('/stud_home/')






            #return HttpResponse("login successful")
        else:
            return redirect('http://127.0.0.1:8000/l2')
            return HttpResponse("invalid details!")
    else:
        form = AuthenticationForm()
    return render(request, 'doctor/login2.html', {'form': form})
def logout(request):
    out(request)
    print("hi people")
    messages.info(request, "Logged out successfully!")
    return render(request,'doctor/logout.html')


def dhome(request):
    # user=request.user
    # doc=Doctor.objects.get(user=user)
    # app=Appointment.objects.filter(doctor_id=doc)
    # print(app)
    return render(request,'doctor/dhome.html')

def home_view(request):
    return render(request, 'doctor/base.html')
def profile_upload(request):
    # declaring template
    template = "doctor/profile_upload.html"
    data = Student.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'students': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
      print(column[2])
      user = User.objects.get_or_create(username=column[1],email=column[9]),
      user[0][0].set_password(column[4])
      print(user[0][0])
      user[0][0].save(),
      _, created = Student.objects.update_or_create(

     username=column[1],
     firstname=column[2],
     lastname=column[3],
     phone_num=column[4],
     year=column[5],
     roll_num=column[6],
     branch=column[7],
     category=Student,
     email=column[9],


     #password=column[4],



    )


    context = {}
    messages.success(request, 'Files uploaded successfully!')
    return render(request, template, context)
def profile_upload_prof(request):
    # declaring template
    template = "doctor/profile_upload_prof.html"
    data = Professor.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'professors': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
      print(column[2])
      user = User.objects.get_or_create(username=column[2],email=column[4],is_staff=True),
      user[0][0].set_password(column[5])
      print(user[0][0])
      user[0][0].save(),
      _, created = Professor.objects.update_or_create(

     username=column[1],
     firstname=column[2],
     lastname=column[3],
     email=column[4],
     phone_num=column[5],
     branch=column[6],
     category=Professor
     #password=column[4],



    )


    context = {}
    messages.success(request, 'Files uploaded successfully!')
    return render(request, template, context)
def profile_upload_cor(request):
    # declaring template
    template = "doctor/profile_upload_stu.html"
    data = Professor.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'professors': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
      print(column[2])
      user = User.objects.get_or_create(username=column[1],email=column[4],is_staff=True),
      user[0][0].set_password(column[5])
      print(user[0][0])
      user[0][0].save(),
      _, created = Professor.objects.update_or_create(

     username=column[1],
     firstname=column[2],
     lastname=column[3],
     email=column[4],
     phone_num=column[5],

     #password=column[4],



    )


    context = {}
    messages.success(request, 'Files uploaded successfully!')
    return render(request, template, context)
def profile_view(request):

       info_object,created = Myuser.objects.get_or_create(user=request.user)
       user_name=request.user.username
       email=request.user.email
       print(user_name)
       my_dict = {'user': user_name, 'firstname': info_object.firstname,'lastname':info_object.lastname, 'email':email,'phone_num': info_object.phone_num,'category': info_object.category}
       return render(request,'doctor/user_profile.html', my_dict)
def edit_profile(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        phone_num=request.POST.get('phone_num')
        email=request.POST.get('email')
        user=request.user
        info_object,created=Myuser.objects.get_or_create(user=user)
        info_object.firstname=firstname
        info_object.phone_num=phone_num
        info_object.lastname=lastname
        info_object.email=email

        info_object.save()

        user_name = request.user.username

        print(email)
        print(user_name)

        my_dict = {'user': user_name, 'firstname': info_object.firstname,'lastname':info_object.lastname, 'email':email,'phone_num': info_object.phone_num}
        return render(request, 'doctor/user_profile.html', my_dict)
    return render(request,'doctor/edit_profile.html')
def display_students(request):
    data = Student.objects.all()
    stu = {
         "student_number": data
     }
    return render(request,"doctor/studentprofile.html",stu)
def display_professors(request):
    data = Professor.objects.all()
    prof = {
         "prof_number": data
     }
    return render(request,"doctor/profprofile.html",prof)
def upload_class_photoss(request):
    return render(request, 'doctor/upload-training-data.html')
def upload_trainingData(request):
    if request.method == 'POST':
        form=TrainingDataUploadform(request.POST,request.FILES)
        if form.is_valid:
            course = request.POST.get('course')
            rollnum = request.POST.get('rollnum')
            images = request.FILES.getlist('myfiles')
            paths = []
            for i in images:
                path = default_storage.save(course+'/'+rollnum+'/'+i.name, ContentFile(i.read()))
                p= os.path.join(BASE_DIR, 'media',course,rollnum,i.name)
                paths.append(p)
            messages.success(request, 'Files uploaded successfully!')
            return render(request,'doctor/afterlogin.html')
def upload_class_course(request):
    return render(request, 'doctor/upload-course.html')
def display_courses(request):
    today = date.today()
    data =  Course.objects.filter(enddate__lt=today)
    cou = {
         "course_number": data
     }
    return render(request,"doctor/display_courses.html",cou)
def display_current_courses(request):
    today = date.today()
    data =  Course.objects.filter(enddate__gt=today)
    cou = {
         "course_number": data
     }
    return render(request,"doctor/display_courses.html",cou)

def add_course(request):
    print("test1")


        # if request is not post, initialize an empty form
    #print(studentlist)
    print("test2")
    form=Courseform()
    if request.method == 'POST':
        form = Courseform(request.POST)
        if form.is_valid:

            form1= form.save(commit=False)


            print("hi")
            form1.save()
            form.save_m2m()
            return render(request,'doctor/afterlogin.html')

    return render(request, 'doctor/upload-course.html', {'form':form})
  
def fill_images(request):
    return render(request,'doctor/viewfolders.html')

def view_images_folders(request):
    if request.method =='POST':
        course=request.POST.get('course')
        rollnum=request.POST.get('rollnum')
        images = [os.path.basename(x) for x in glob(os.path.join(BASE_DIR, 'media/'+ course +'/'+rollnum+'/*'))]
        for i in range(len(images)):
                images[i] = course+'/'+rollnum+'/' + images[i]

        return render(request, 'doctor/view_images.html', {'list':images})
