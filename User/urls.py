from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from django.urls import path
from User.views import index, RegisterPage, LoginPage, Logout, UserPage, UserUpdate, UserDetail, PasswordsChangeView,password_success

urlpatterns = [
    path('', index.as_view(), name='home'),
    path('user/<str:user>/',UserPage.as_view(),name = 'userPage'),
    path('register/',RegisterPage.as_view(), name = 'register'),
    path('login/',LoginPage.as_view(), name = 'login'),
    path('logout/',Logout.as_view(), name = 'logout'),
    path('userupdate/<int:id>',UserUpdate.as_view(),name='user_update'),
    path('userdetial/<int:id>',UserDetail.as_view(),name='user_detail'),
    path('password/',PasswordsChangeView.as_view(template_name='registration/change_password.html'),name = 'change_password'),
    path('password_success/',password_success,name ='password_success'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)