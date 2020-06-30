from django.shortcuts import render
from django.http import HttpResponseRedirect
from apptest.models import AppCase, AppCaseStep


# Create your views here.


def appcase(request):
    message = ''
    if not request.session.get('is_login', None):
        message = 'Please login before browse app case Manage Page.'
        return HttpResponseRedirect('/login/')
    else:
        appcase_list = AppCase.objects.all()
        return render(request, "apptest/appcase.html",
                      {
                          "appcases": appcase_list
                      })


def appCaseStep(request):
    message = ''
    if not request.session.get('is_login', None):
        message = 'PLease login before browse app case step page.'
        return HttpResponseRedirect('/login/')
    else:
        app_case_step_list = AppCaseStep.objects.all()
        return render(request, "apptest/appcasestep.html",
                      {
                          "appcasesteps": app_case_step_list
                      })
