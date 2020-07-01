from django.shortcuts import render
from django.http import HttpResponseRedirect
from webtest.models import WebCase, WebCaseStep


# Create your views here.


def webCase(request):
    message = ''
    if not request.session.get('is_login', None):
        message = 'Please login before browse app case Manage Page.'
        return HttpResponseRedirect('/login/')
    else:
        webcase_list = WebCase.objects.all()
        return render(request, 'webcase.html',
                      {
                          'webcases': webcase_list
                      })


def webCaseStep(request):
    message = ''
    if not request.session.get('is_login', None):
        message = 'Please login before browse app case Manage Page.'
        return HttpResponseRedirect('/login/')
    else:
        webstep_list = WebCaseStep.objects.all()
        return render(request, 'webcasestep.html',
                      {
                          'webcasesteps': webstep_list
                      })
