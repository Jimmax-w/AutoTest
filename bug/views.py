from django.shortcuts import render
from django.http import HttpResponseRedirect
from bug.models import Bug


# Create your views here.


def bug_manage(request):
    message = ''
    if not request.session.get('is_login', None):
        message = 'Please login before browse API Step Manage Page.'
        return HttpResponseRedirect('/login/')
    else:
        list_display = Bug.objects.all()
        return render(request, 'bug/bug_manage.html', {
            'bugs': list_display
        })
