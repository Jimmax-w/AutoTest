from django.db import models
from django import forms

gender = (
    ('M', "Male"),
    ("F", "Female"),
)


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=512)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='M')
    c_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['c_time']
        verbose_name = 'Users'
        verbose_name_plural = 'Users'


class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    password = forms.CharField(label='password', max_length=512, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))


class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", max_length=512,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm password", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='Gender', choices=gender)
