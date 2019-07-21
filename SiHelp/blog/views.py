from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Ad, Rate
from django.db.models import Avg, Max, Min, Sum, Count
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from .forms import CommentForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.db.models import Func
from users.models import Profile
from django.template.defaulttags import register
import logging
from django.urls import reverse, reverse_lazy
from django.contrib import messages
import pickle
import uuid 
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
        data = super(UserDetailView, self).get_context_data(**kwargs)
        user = self.kwargs.get('pk')
        ads = Ad.objects.filter(author = user).order_by("-date").annotate(average_rating=Avg('rate__rating'))
        data['ads'] = ads
        count = 0
        summed = 0
        for ad in ads:
            if (ad.average_rating):
                summed += ad.average_rating 
            count +=1
        average=round(summed/count)
        SubtractedAverage = 10 -average
        data['range'] = range(0,average)
        data['invertedRange'] = range(0,SubtractedAverage)
        data['avg'] = average
        data['mockuser'] = User.objects.get(id=user)
        realuser = self.request.user
        if user is not None:
            data['user'] = realuser
        else:
            data['user'] = None


        return data

    
class PostCreateView(LoginRequiredMixin, CreateView):

    model = Ad
    fields = ['title','subject', 'unit', 'description','price']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        if Ad.objects.filter(author=self.request.user).count() >= 3:
            messages.error(self.request, 'You can only post 3 ads at maximum!')
            return redirect('/')
        if Profile.objects.filter(user=self.request.user).first().is_active == False:
            messages.error(self.request, 'Please activate your account by verifying your email address first')
            return redirect('/')
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ad
    fields = ['title','subject', 'unit', 'description','price']
    success_url = reverse_lazy('user-profile')
    
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
    success_url = reverse_lazy('user-profile')

    def test_func(self):
        ad = self.get_object()
        if self.request.user == ad.author:
            return True
        return False

@login_required
def add_comment_to_post(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        exist = Rate.objects.filter(user_id=request.user, ad_id=ad)
        if form.is_valid() and len(exist) == 0 and request.user.profile.tutor == False:
            rate = form.save(commit=False)
            rate.ad_id = ad
            rate.user_id = request.user
            rate.save()
            return redirect('/')
        elif form.is_valid() and len(exist) != 0 and request.user.profile.tutor == False:
            rate = exist.first()
            rate.rating = form.cleaned_data['rating']
            rate.save(update_fields=["rating"]) 
            return redirect('/') #flash some message here
        elif request.user.profile.tutor == True:
            messages.error(self.request, 'Tutors are not allowed to rate ads')
            return redirect('/')
    else:
        form = CommentForm()
    return redirect('/')

def about(request):
  
    return render(request, 'blog/about.html', {'title':'About'})

def marketplace(request):
    user = request.user
    realAds = Ad.objects.all().order_by("-date").annotate(average_rating=Avg('rate__rating')).annotate(Counted=Count('rate__rating'))
    if request.method == 'GET':
        if 'search' in request.GET:#order by search query
            search_query = request.GET.get('search_box', None)
            if search_query is not None:
                realAds = Ad.objects.filter(Q(subject__contains=search_query) | Q(unit__contains=search_query) | Q(title__contains=search_query) | Q(description__contains=search_query)).order_by("-date").annotate(average_rating=Avg('rate__rating')).annotate(Counted=Count('rate__rating'))      
                request.session['search'] = search_query
            else:
                realAds = Ad.objects.all().annotate(average_rating=Avg('rate__rating')).annotate(Counted=Count('rate__rating'))      

        if 'refresh'in request.GET:
            realAds = Ad.objects.all().annotate(average_rating=Avg('rate__rating')).annotate(Counted=Count('rate__rating'))      


        if 'highestrated' in request.GET:#order by rated
            search_request = request.session.get('search')
            if search_request is not None:
                realAds = Ad.objects.filter(Q(subject__contains=search_request) | Q(unit__contains=search_request) | Q(title__contains=search_request) | Q(description__contains=search_request)).annotate(average_rating=Avg('rate__rating')).annotate(Counted=Count('rate__rating')).order_by('-average_rating')       
            else:
                realAds = Ad.objects.annotate(average_rating=Avg('rate__rating')).order_by('-average_rating')

        if 'mostaffordable' in request.GET:#order by rated
            search_request = request.session.get('search')
            if search_request is not None:
                realAds = Ad.objects.filter(Q(subject__contains=search_request) | Q(unit__contains=search_request) | Q(title__contains=search_request) | Q(description__contains=search_request)).annotate(average_rating=Avg('rate__rating')).annotate(Counted=Count('rate__rating')).order_by('price')       
            else:
                realAds = Ad.objects.all().annotate(average_rating=Avg('rate__rating')).annotate(Counted=Count('rate__rating')).order_by('price')

        if 'controversial' in request.GET:#order by rated
            search_request = request.session.get('search')
            if search_request is not None:
                realAds = Ad.objects.filter(Q(subject__contains=search_request) | Q(unit__contains=search_request) | Q(title__contains=search_request) | Q(description__contains=search_request)).annotate(average_rating=Avg('rate__rating')).annotate(Counted=Count('rate__rating')).order_by('-Counted')       
            else:
                realAds = Ad.objects.all().annotate(average_rating=Avg('rate__rating')).annotate(Counted=Count('rate__rating')).order_by('-Counted')




    context = {
        'ads': realAds,
        'user': user
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
  