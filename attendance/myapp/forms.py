from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import *
from django.forms import ModelChoiceField


class Signup_user_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email id already exists')
        return email


class Signup_profile_form(forms.ModelForm):
    class Meta:
        model = Myuser
        fields = ['firstname','lastname', 'phone_num','category']


class TrainingDataUploadform(forms.Form):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    course = forms.CharField()
    rollnum = forms.IntegerField()

class Courseform(forms.ModelForm):
    course_id = forms.CharField(widget=forms.TextInput())
    name=forms.CharField(widget=forms.TextInput())
    startdate=forms.DateField()
    enddate=forms.DateField()
    taught_by=forms.ModelChoiceField(queryset=Professor.objects.all())
    student=forms.ModelMultipleChoiceField(queryset=Student.objects.all(),widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Course
        fields = ['name','course_id','startdate','enddate','taught_by','student']
        widgets = {
    'startdate': forms.DateTimeInput(attrs={'class': 'datetime-input'})
}

class DateForm(forms.Form):
	date = forms.CharField(required=True)
class ClassImagesForm(forms.Form):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    date = forms.CharField()
