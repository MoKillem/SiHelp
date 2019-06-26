from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.fields.TextInput(attrs={'placeholder': 'e.g man@gmail.com'}))
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','phone','password1','password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','phone']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['tutor','pic']

    