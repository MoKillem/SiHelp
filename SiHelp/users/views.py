from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from blog.models import Ad
from blog.views import PostDeleteView
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "You are now logged in " + username)
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('createprofile')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def createprofile(request):
    if(request.method) == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account information is updated')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance= request.user.profile)
    context = {
             'p_form': p_form
    }
    return render(request, 'users/createprofile.html', context)


@login_required
def profile(request):
    user = request.user#acquire current user
    ads = Ad.objects.filter(author=user).order_by('-date')# Filter ads
    if(request.method) == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if 'Update' in request.post:
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account information is updated')
                return redirect('profile')
            else:
                print(u_form.errors)
                print(p_form.errors)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance= request.user.profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'ads':ads
    }
    return render(request, 'users/profile.html', context)




        