from django.shortcuts import render
from apitest.models import ApiTest, ApiStep, Apis
from django.http import HttpResponseRedirect


# Create your views here.

def api_test_manage(request):
    message = ''
    if not request.session.get('is_login', None):
        message = 'Please login before browse APT Test Manage Page.'
        # TODO：显示提示登录信息后自动跳转登录界面
        return HttpResponseRedirect('/login/')
    else:
        test_list = ApiTest.objects.all()
        return render(request, 'apitest/apitest_manage.html',
                      {
                          'apitests': test_list
                      })


def api_step_manage(request):
    message = ''
    if not request.session.get('is_login', None):
        message = 'Please login before browse API Step Manage Page.'
        return HttpResponseRedirect('/login/')
    else:
        step_list = ApiStep.objects.all()
        return render(request, 'apitest/apistep_manage.html',
                      {
                          'apisteps': step_list
                      })


def apis_manage(request):
    message = ''
    if not request.session.get('is_login', None):
        message = 'Please login before browse API Step Manage Page.'
        return HttpResponseRedirect('/login/')
    else:
        apis_list = Apis.objects.all()
        return render(request, 'apitest/apis_manage.html',
                      {
                          'apiss': apis_list
                      })
