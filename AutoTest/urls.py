"""AutoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views
from product import views as product_view
from apitest import views as api_view
from bug import views as bug_view
from settings import views as settings_view
from apptest import views as apptest_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.hello_django),
    path('login/', views.login1),
    path('home/', views.home1),
    path('register/', views.register1),
    path('product_manage/', product_view.product_manage),
    path('apitest_manage/', api_view.api_test_manage),
    path('apistep_manage/', api_view.api_step_manage),
    path('apis_manage/', api_view.apis_manage),
    path('apptest/', apptest_view.appcase),
    path('apptest_step/', apptest_view.appCaseStep),
    path('bug_manage/', bug_view.bug_manage),
    path('settings/', settings_view.settings_manage),
    path('user/', settings_view.set_user),
]
