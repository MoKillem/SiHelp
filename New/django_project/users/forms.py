from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.fields.TextInput(attrs={'placeholder': 'e.g man@gmail.com'}))
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phonenum =forms.CharField(widget=forms.fields.TextInput(attrs={'class': 'form-control bfh-phone' , 'placeholder': 'e.g 0422676960'}), label = "Phone Number", max_length=10)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','phonenum','password1','password2']


class TutorRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.fields.TextInput(attrs={'placeholder': 'e.g man@gmail.com'}))
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phonenum =forms.CharField(widget=forms.fields.TextInput(attrs={'class': 'form-control bfh-phone' , 'placeholder': 'e.g 0422676960'}), label = "Phone Number", max_length=10)
    major = forms.CharField(max_length=30)
    profpic= forms.ImageField()
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','phonenum','password1','password2','major','profpic']




    