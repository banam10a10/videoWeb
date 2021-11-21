from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
# Create your views here.
from django.views import View

from User.models import CustomerUser
from Video.forms import CreateVideoForm
from Video.models import Video, Category
from django.db.models import Q

class show(View):
    def get(self,req,id):
        data = Video.objects.filter(id__exact=id)[0]
        liked = data.Likes.filter(id=req.user.id).exists()
        disliked = data.Dislikes.filter(id=req.user.id).exists()
        user = CustomerUser.objects.filter(id__exact=data.User_id)[0]
        randomVideo = Video.objects.filter(~Q(id=id)).order_by('?').select_related('User')[:5]
        context = {
            'id':id,
            'data':data,
            'liked':liked,
            'disliked':disliked,
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
            user = req.user
            video = Video.objects.filter(id = id)[0]
            if video.Likes.filter(id = user.id).exists():
                video.Likes.remove(user)
                message = 1
            else:
                video.Likes.add(user)
                if video.Dislikes.filter(id=user.id).exists():
                    video.Dislikes.remove(user)
                    message = 3
                else:
                    message = 2
            return HttpResponse(message)

class Dislike(View):
    def post(self,req,id):
        if not req.user.is_authenticated:
            message = 0
            return HttpResponse(message)
        else:
            user = req.user
            video = Video.objects.filter(id = id)[0]
            if video.Dislikes.filter(id = user.id).exists():
                video.Dislikes.remove(user)
                message = 1
            else:
                video.Dislikes.add(user)
                if video.Likes.filter(id=user.id).exists():
                    video.Likes.remove(user)
                    message = 3
                else:
                    message = 2
            return HttpResponse(message)

class CreateVideo(View):
    def get(self,req):
        form = CreateVideoForm(initial={'User':req.user})
        form.fields['User'].initial = req.user
        return render(req,'Video/CreateVideo.html',{'form':form})

    def post(self,req):
        form = CreateVideoForm(req.POST,req.FILES)
        if form.is_valid():
            new = form.save()
            return redirect('show',id=new.pk)
        return render(req,'Video/CreateVideo.html',{'form':form})

class UpdateVideo(View):
    def get(self,req,id):
        video = Video.objects.filter(id=id)[0]
        form = CreateVideoForm(instance=video)
        context = {
            'form':form
        }
        return render(req,'video/CreateVideo.html',context)

    def post(self,req,id):
        video = Video.objects.filter(id=id)[0]
        form = CreateVideoForm(req.POST, req.FILES,instance= video )
        if form.is_valid():
            form.save()
            return redirect('show',id=id)
        return render(req, 'Video/CreateVideo.html', {'form': form})

class DeleteVideo(View):
    def get(self,req,id):
        video = Video.objects.filter(id=id)[0]
        context ={
            'video':video,
        }
        return render(req,'Video/DeleteVideo.html',context)

    def post(self,req,id):
        video = Video.objects.filter(id=id)[0]
        video.delete()
        return redirect('userPage',user=req.user)

class CategoryVideo(View):
    def get(self,req,id):
        # videos = Video.objects.filter(Category=id).order_by("?").all()
        videos = Video.objects.filter(Category=id).all()[::-1]
        p = Paginator(videos,12)
        page = req.GET.get('page')
        pagination = p.get_page(page)
        nums = '1'* pagination.paginator.num_pages
        category_name = Category.objects.filter(id=id)[0].Name
        context = {
            'videos':videos,
            'CategoryName' : "Nhạc "+ category_name,
            'pagination' : pagination,
            'nums':nums,
        }
        return render(req,'Video/CategoryVideo.html',context)

class search(View):
    def get(self,req):
        v= req.GET.get('v')
        video = Video.objects.select_related('User').filter(Title__contains=v)[::-1]
        context = {
            'CategoryName' : 'Search : '+v,
            'videos':video,
            'v':v
        }
        return render(req,'Video/Search.html',context)

