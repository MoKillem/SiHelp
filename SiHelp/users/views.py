from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Avg, Max, Min, Sum
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from blog.models import Ad,Rate
from blog.views import PostDeleteView
from django.template.defaulttags import register
from django.db.models import Func
import logging

logger = logging.getLogger(__name__)

@register.filter
def get_range(value):
    return range(value)
@register.filter
def subtract(value, arg):
    return value - arg

    
@register.filter
def rounding(value):
    return round(value)
    

class Round(Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 0)'
# Create your views here.
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })
    
#register view
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
            return redirect('user-profile')
    else:
        p_form = ProfileUpdateForm(instance= request.user.profile)
    context = {
             'p_form': p_form
    }
    return render(request, 'users/createprofile.html', context)


@login_required
def profile(request):
    user = request.user#acquire current user
    ads = Ad.objects.filter(author = user).order_by("-date").annotate(average_rating=Round(Avg('rate__rating')))
    count = 0
    summed = 0
    for ad in ads:
        if (ad.average_rating):
            summed += ad.average_rating 
        count +=1
    average_value = round(summed/count)

    if(request.method) == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if 'Update' in request.POST:
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account information is updated')
                return redirect('user-profile')
            else:
                print(u_form.errors)
                print(p_form.errors)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance= request.user.profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'ads':ads,
        'avg':average_value
    }

    return render(request, 'users/profile.html', context)