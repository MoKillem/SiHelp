from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author':'Juliet',
        'title':'The best',
        'content':'She is the best',
        'date':'Aug 27, 2018'
    },
    {
        'author':'Moe',
        'title':'The muahaha',
        'content':'He is the Muahaha',
        'date':'Aug 28, 2018',
    }
]
def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
  
    return render(request, 'blog/about.html', {'title':'About'})

def marketplace(request):
  
    return render(request, 'blog/TutorialPage.html',{'range': range(10)})

def layout(request):
    context = {
        'loggedin': False
    }
    return render(request, 'blog/layout.html', context)

def SignUpTutor(request):
   
    return render(request, 'blog/SignUpPageLogin.html')

def SignUpNt(request):
    
    return render(request, 'blog/Nontutorsignup.html')


   
def Account(request):
   
    return render(request, 'blog/Account.html',{'range': range(10)})
def Entry(request):
   
    return render(request, 'blog/EntryPage.html')
def ProfilePage(request):
   
    return render(request, 'blog/ProfilePage.html',{'range': range(10)})
  