from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from django.views import View

from User.models import CustomerUser
from Video.models import Video
from django.db.models import Q

class show(View):
    def get(self,req,id):
        data = Video.objects.filter(id__exact=id)[0]
        user = CustomerUser.objects.filter(id__exact=data.User_id)[0]
        randomVideo = Video.objects.filter(~Q(id=id)).order_by('?').select_related('User')[:5]
        context = {
            'id':id,
            'data':data,
            'user':user,
            'randomVideo':randomVideo,
        }
        return render(req,'video/show.html',context)

class addView(View):
    def get(self,req,id):
        video = Video.objects.filter(id__exact = id)[0]
        video.view += 1
        video.save()
        return HttpResponse('1')

class Like(View):
    def post(self,req,id):
        if not req.user.is_authenticated:
            message = 0
            return HttpResponse(message)
        else:
            flag = 1
            user = req.user
            video = Video.objects.filter(id = id)[0]
            if video.Likes.filter(id = user.id).exists():
                video.Likes.remove(user)
                message = 1
            else:
                video.Likes.add(user)
                message = 2
            return HttpResponse(message)
