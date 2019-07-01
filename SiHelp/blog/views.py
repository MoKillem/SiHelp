from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Ad, Rate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from .forms import CommentForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from users.models import Profile
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

searchfunction = True


def home(request):
    context = {
        'ads': Ad.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Ad
    template_name = 'blog/TutorialPage.html'
    context_object_name = 'ads'
    ordering = ['-date']

class PostDetailView(DetailView):
    model = Ad

class UserDetailView(ListView):
    model = User
    template_name = 'blog/user_detail.html'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        user = self.request.user
        data['ads'] = Ad.objects.filter(author=user).order_by('-date')
        data['user'] = user
        return data

    
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

def add_comment_to_post(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.ad_id = ad
            rate.user_id = request.user
            rate.save()
            return redirect('/')
    else:
        form = CommentForm()
    return redirect('/')

def about(request):
  
    return render(request, 'blog/about.html', {'title':'About'})

def marketplace(request):
    rateArray = []
    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)
        if search_query is not None:
            realAds = Ad.objects.filter(Q(subject__contains=search_query) | Q(unit__contains=search_query)).order_by("-date")
        else:
            realAds = Ad.objects.all()
    else:
        realAds = Ad.objects.all()
  
    context = {
        'ads': realAds,
        'rates':rateArray,
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
  