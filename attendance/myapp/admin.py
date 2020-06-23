from django.contrib import admin

# Register your models here.
from .models import Myuser,Student,Professor,Course,Attendance

admin.site.register(Myuser)
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Attendance)
