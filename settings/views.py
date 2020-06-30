from django.shortcuts import render
from settings.models import Settings
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.


def settings_manage(request):
    message = ''
    if not request.session.get('is_login', None):
        message = 'Please login before into settings page.'
        return HttpResponseRedirect('/login/')
    else:
        list_display = Settings.objects.all()
        return render(request, 'settings/settings.html', {
            'sets': list_display
        })


def set_user(request):
    message = ''
    if not request.session.get('is_login', None):
        message = 'Please login before into settings page.'
        return HttpResponseRedirect('/login/')
    else:
        user_list = User.objects.all()
        return render(request, 'settings/set_user.html', {
            'users': user_list
        })
