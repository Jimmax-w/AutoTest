from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import hashlib
from login.models import UserForm
from login.models import RegisterForm
from login import models


# Create your views here.

def hello_django(request):
    return render(request, 'login/helloDjango.html', {
        'data': "Hello Django, I am ready to explore!",
    })


def home1(request):
    return render(request, 'login/home.html')


def hash_password(s, salt='NJBZWn7vwYXMw'):
    h = hashlib.sha512()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def register1(request):
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        message = 'Please check your information'
        if registerForm.is_valid():
            username = registerForm.cleaned_data['username']
            password1 = registerForm.cleaned_data['password1']
            password2 = registerForm.cleaned_data['password2']
            email = registerForm.cleaned_data['email']
            gen = registerForm.cleaned_data['sex']
            if password1 != password2:
                message = 'Confirm password is different from password.'
                return render(request, 'login/register.html', locals())
            else:
                userNameConfirm = models.User.objects.filter(username=username)
                if userNameConfirm:
                    message = 'The username has existed, please replace another one.'
                    return render(request, 'login/register.html', locals())
                emailConfirm = models.User.objects.filter(email=email)
                if emailConfirm:
                    message = 'The email address has been registered, please use another one.'
                    return render(request, 'login/register.html', locals())
            new_user = models.User.objects.create()
            new_user.username = username
            new_user.password = hash_password(password1)
            new_user.email = email
            new_user.sex = gen
            new_user.save()
            return HttpResponseRedirect('/login/')
    else:
        register_form = RegisterForm()
        return render(request, 'login/register.html', locals())


def logout1(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    # request.session.flush()
    del request.session['is_login']
    del request.session['user_name']
    del request.session['user_id']
    return redirect('/login/')


def login1(request):
    if request.method == 'POST':
        message = ''
        login_form = UserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(username=username)
                if user.password == hash_password(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/home/')
                else:
                    return render(request, 'login/login.html', locals())
            except ValueError:
                message = 'Username not exists'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())
    else:
        login_form = UserForm()
        return render(request, 'login/login.html', locals())
