
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Video.views import show,addView,Like

urlpatterns = [
    path('show/<int:id>', show.as_view(), name='show'),
    path('addview/<int:id>', addView.as_view(), name='addview'),
    path('like/<int:id>', Like.as_view(), name='like'),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)