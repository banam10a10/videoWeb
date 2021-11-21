from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from User.forms import Login, Register, UserUpdateForm
from User.models import CustomerUser
from Video.models import Video


class index(View):
    def get(self,req):
        videos = Video.objects.select_related('User').order_by('?').all()
        video_rap = Video.objects.select_related('User').filter(Category=1).order_by('?')[:8]
        video_ballad = Video.objects.select_related('User').filter(Category=2).order_by('?')[:8]
        context = {
            'videos':videos,
            'video_rap':video_rap,
            'video_ballad':video_ballad,
        }
        return render(req,'Home/index.html',context)

class UserPage(View):
    def get(self,req,user):
        User = CustomerUser.objects.filter(username__exact=user)[0]
        videos = Video.objects.filter(User_id__exact=User.id)[::-1]
        p = Paginator(videos, 20)
        page = req.GET.get('page')
        pagination = p.get_page(page)
        nums = '1' * pagination.paginator.num_pages
        context={
            'user':User,
            'video':videos,
            'img':User.avatar.url,
            'pagination': pagination,
            'nums': nums,
        }
        return render(req,'User/UserPage.html',context)

class RegisterPage(View):
    def get(self, req):
        form = Register()
        return render(req, 'Auth/RegisterPage.html', {'f': form})

    def post(self, req):
        form = Register(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(req, 'Account was created for ' + user)
            return redirect('login')
        return render(req, 'Auth/RegisterPage.html', {'f': form})


class LoginPage(View):
    def get(self, req):
        form = Login()
        return render(req, 'Auth/LoginPage.html', {'f': form})

    def post(self, req):
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)
        if user is None:
            messages.info(req, 'Username or Password is incorrect')
            form = Login()
            return render(req, 'Auth/LoginPage.html', {'f': form})
        login(req, user)
        return redirect('home')

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(req):
    return render(req,'registration/password_success.html',{})

class Logout(View):
    def get(self, req):
        logout(req)
        return redirect('home')

class UserUpdate(View):
    def get(self,req,id):
        user = CustomerUser.objects.filter(id=id)[0]
        form = UserUpdateForm(instance=user)
        context = {
            'form':form,
        }
        return render(req,'User/UserUpdate.html',context)
    def post(self,req,id):
        user = CustomerUser.objects.filter(id=id)[0]
        form = UserUpdateForm(req.POST,req.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('userPage',user = user)
        return render(req, 'User/UserUpdate.html', {'form':form})

class UserDetail(View):
    def get(self,req,id):
        User = CustomerUser.objects.filter(id__exact=id)[0]
        return render(req,'User/UserDetail.html',{'user':User})

