from django import forms

from User.models import CustomerUser
from Video.models import Video

class CreateVideoForm(forms.ModelForm):
    User = forms.ModelChoiceField(widget=forms.HiddenInput(),queryset= CustomerUser.objects.all())
    class Meta:
        model = Video
        fields = ['Title','Thumbnail','Location','Description','Category','User']

