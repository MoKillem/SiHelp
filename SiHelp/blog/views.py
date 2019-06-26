from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Ad
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
        'ads': Ad.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Ad
    template_name = 'blog/home.html'
    context_object_name = 'ads'
    ordering = ['-date']

class PostDetailView(DetailView):
    model = Ad
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    fields = ['title','subject', 'unit', 'description']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ad
    fields = ['subject', 'unit', 'description']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        ad = self.get_object()
        if self.request.user == ad.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ad
    success_url = '/'

    def test_func(self):
        ad = self.get_object()
        if self.request.user == ad.author:
            return True
        return False

def about(request):
  
    return render(request, 'blog/about.html', {'title':'About'})

def marketplace(request):
    context = {
        'ads': Ad.objects.all()
    }
    return render(request, 'blog/TutorialPage.html', context)

def layout(request):
    context = {
        'loggedin': False
    }
    return render(request, 'blog/layout.html', context)

def SignUpTutor(request):
   
    return render(request, 'blog/SignUpPageLogin.html')

def SignUpNt(request):
    
    return render(request, 'blog/Nontutorsignup.html')


@login_required
def Account(request):
    return render(request, 'blog/Account.html',{'range': range(10)})
    
def Entry(request):
   
    return render(request, 'blog/EntryPage.html')

def ProfilePage(request):
   
    return render(request, 'blog/ProfilePage.html',{'range': range(10)})
  