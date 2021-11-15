
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Video.views import show, addView, Like, Dislike, CreateVideo, CategoryVideo, search, UpdateVideo, DeleteVideo

urlpatterns = [
    path('show/<int:id>', show.as_view(), name='show'),
    path('addview/<int:id>', addView.as_view(), name='addview'),
    path('like/<int:id>', Like.as_view(), name='like'),
    path('dislike/<int:id>', Dislike.as_view(), name='dislike'),
    path('create',CreateVideo.as_view(), name='create_video'),
    path('updatevideo/<int:id>',UpdateVideo.as_view(), name='update_video'),
    path('deletevideo/<int:id>',DeleteVideo.as_view(), name='delete_video'),
    path('category/<int:id>',CategoryVideo.as_view(), name='CategoryVideo'),
    path('search/', search.as_view(),name ='search'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)