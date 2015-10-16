from django import forms
from .models import Customer


class Signup(forms.ModelForm):
    class Meta:
        model = Customer
        exclude=['created_date',]
        widgets={
        'password':forms.PasswordInput(),
        }
    '''full_name=forms.CharField()
    address=forms.CharField()
    mobile=forms.DecimalField(max_length=10)
    email=forms.EmailField()
    password=forms.PasswordField()
    '''

