"""TheResources URL Configuration

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
from FirstApp import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$',views.index,name='index'),
    path('admin/', admin.site.urls),
    url(r'^FirstApp/',include('FirstApp.url')),
    url(r'^detail12345/$',views.detail12345,name='detail12345'),
    url(r'^DetailPersonalDevelopment/$',views.DetailPersonalDevelopmentView,name='DetailPersonalDevelopment'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^detailAdvice/$',views.detailAdvice,name='detailAdvice'),
    url(r'^ApplyJob/$',views.ApplyJob,name='ApplyJob'),
    url(r'^AddJobPortal/$',views.AddJobPortal,name='AddJobPortal'),
    url(r'^CompanyAndStartup/$',views.CompanyAndStartup,name='CompanyAndStartup'),
    url(r'^AddCompanyAndStartup/$',views.AddCompanyAndStartup,name='AddCompanyAndStartup'),
    url(r'^ListOfCompanyOrStartup/$',views.ListOfCompanyOrStartup,name='ListOfCompanyOrStartup'),


]
