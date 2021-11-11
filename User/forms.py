from .models import CustomerUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class Register(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = (
        'username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'birthday', 'sex', 'address',
        'phone_number')


class Login(AuthenticationForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'password',)