from django import forms
from django.contrib.auth.models import User

from core.models import Profile, Application


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    application = forms.ModelMultipleChoiceField(queryset=Application.objects.order_by('name'), to_field_name='id', widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Profile
        fields = ('application', 'picture')
