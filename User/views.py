from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from User.forms import Login, Register
from Video.models import Video


class index(View):
    def get(self,req):
        videos = Video.objects.select_related('User').all()
        context = {'videos':videos}
        return render(req,'Home/index.html',context)

class search(View):
    def get(self,req):
        v= req.GET.get('v')
        video = Video.objects.select_related('User').filter(Title__contains=v)
        context = {
            'videos':video,
            'v':v
        }
        return render(req,'Home/index.html',context)

class RegisterPage(View):
    def get(self, req):
        form = Register()
        return render(req, 'Auth/RegisterPage.html', {'f': form})

    def post(self, req):
        form = Register(req.POST)
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


class Logout(View):
    def get(self, req):
        logout(req)
        return redirect('home')
