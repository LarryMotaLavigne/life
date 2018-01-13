from django import forms
from django.contrib.auth.models import User

from core.models import Profile, Application


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    application = forms.ModelMultipleChoiceField(queryset=Application.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Profile
        fields = ('application','picture')
