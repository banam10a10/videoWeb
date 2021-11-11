from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from User.views import index, RegisterPage, LoginPage, Logout,search

urlpatterns = [
    path('', index.as_view(), name='home'),
    path('register/',RegisterPage.as_view(), name = 'register'),
    path('login/',LoginPage.as_view(), name = 'login'),
    path('logout/',Logout.as_view(), name = 'logout'),
    path('search/',search.as_view(), name = 'search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)