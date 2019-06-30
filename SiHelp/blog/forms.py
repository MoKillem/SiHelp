from django import forms
from django.contrib.auth.models import User
from .models import Ad, Rate

class CommentForm(forms.ModelForm):

    class Meta:
        model = Rate
        fields = ('rating',)