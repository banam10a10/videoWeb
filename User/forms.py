from django import forms

from .models import CustomerUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class DateInput(forms.DateInput):
    input_type = 'date'

class Register(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = (
        'username', 'password1', 'password2', 'avatar','first_name', 'last_name', 'email', 'birthday', 'sex', 'address',
        'phone_number')
        widgets = {
            'birthday': DateInput(),
            'phone_number': forms.TextInput(attrs={'pattern':"\d{9,12}",'title':"Nhập số thuê bao từ 9 - 12 số!"}),
        }


class Login(AuthenticationForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'password',)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ('avatar','first_name', 'last_name', 'email', 'birthday', 'sex', 'address',
        'phone_number')
        widgets = {
            'birthday': DateInput()
        }

