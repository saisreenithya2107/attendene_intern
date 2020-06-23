from django.urls import re_path, include, path
from .views import register,login1,logout,home_view,profile_upload,profile_view,upload_class_photoss,edit_profile,profile_upload_prof,upload_class_course,add_course, view_images_folders,fill_images,display_courses,display_current_courses,display_professors,profile_upload_cor
from . import views

app_name = 'myapp'

urlpatterns = [

    # path('', views.login, name='login'),
  #  path('pregister', views.patientregister, name='patientregister'),
    path('', views.register, name='register'),
    path('l2', views.login1, name='login1'),
    path('logout', views.logout, name='logout'),
    path('dhome/', views.dhome, name='dhome'),
    path('uploadhome', views.home_view, name="home_view"),

    path('upload-csv', profile_upload, name="student_upload"),
    path('upload-csv-prof', profile_upload_prof, name="prof_upload"),
    path('upload-csv-cor', profile_upload_cor, name="cor_upload"),
    path('profile_view/',views.profile_view,name="profile_view"),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('display_students',views.display_students,name="display_students"),
    path('display_professors',views.display_professors,name="display_professors"),
    path('upload_training_data',views.upload_trainingData,name="upload-training-data"),
    path('upload_class_photoss',views.upload_class_photoss,name="upload_class_data"),
    path('upload_class_course',views.upload_class_course,name="upload_class_course"),
    path('add_course',views.add_course,name="add_course"),
    path('view_images_folders',views.view_images_folders,name=" view_images_folders"),
    path('fill_images',views.fill_images,name=" fill_images"),
    path('display_courses',views.display_courses,name="display_courses"),
    path('display_current_courses',views.display_current_courses,name="display_current_courses"),






]
