from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.fields.TextInput(attrs={'placeholder': 'e.g man@gmail.com'}))
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    
    def clean_email(self):
        data = self.cleaned_data['email']
        username = self.cleaned_data['username']
        if "@student.uwa.edu.au" not in data:   # any check you need
            raise forms.ValidationError("Must be a UWA address")
        if data and User.objects.filter(email=data).exclude(username=username).exists():
            raise forms.ValidationError(u'There is already an account using this email address')
        return data
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
    tutor = forms.BooleanField(required = False, initial=False)
    phone = forms.CharField(max_length=30)
    class Meta:
        model = Profile
        fields = ['tutor','pic','phone']

    