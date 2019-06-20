from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,TutorRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "You can now login as " + username)
            return redirect('loginAcc')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})

def Tutoregister(request):
    if(request.method) == 'POST':
        form1 = TutorRegisterForm(request.POST)
        if form1.is_valid():
            form1.save()
            username = form1.cleaned_data.get('username')
            messages.success(request, "You can now login as " + username)
            return redirect('loginAcc')
    else:
        form1 = TutorRegisterForm()
    return render(request, 'users/register.html', {'form':form1})




        