import pymysql
from pymysql.cursors import Cursor
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


def test_report(request):
    api_list = Apis.objects.all()
    api_count = Apis.objects.count()
    db = pymysql.connect(user='root', db='autotest', passwd='gdc5sha1002,.', host='127.0.0.1')
    cur = db.cursor()
    sql1 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.api_status=1'
    apis_pass_count = [row[0] for row in cur.fetchmany(cur.execute(sql1))][0]
    sql2 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.api_status=0'
    apis_failed_count = [row[0] for row in cur.fetchmany(cur.execute(sql2))][0]
    cur.close()
    db.close()
    return render(request, 'apitest/report.html',
                  {
                      'apiss': api_list,
                      'apiscounts': api_count,
                      'apis_pass_counts': apis_pass_count,
                      'apis_fail_counts': apis_failed_count,
                  })
