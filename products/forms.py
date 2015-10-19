from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Signup(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=30)
    mobile = forms.DecimalField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'mobile', 'address',
                  'username', 'password1', 'password2')

    def save(self, commit=True):
        # so that form is not saved at first
        user = super(Signup, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.address = self.cleaned_data['address']
        user.mobile = self.cleaned_data['mobile']
        if commit:
            user.save()
        return user


class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
