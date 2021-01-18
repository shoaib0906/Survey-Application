"""DjangoVue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views

from apps.core.views import frontpage,signup,accountred
from apps.survey.views import survey_detail,add_survey
from apps.usrprofile.views import dashboard
from apps.survey.views import SurveyApiView
from rest_framework import routers
from django.urls import include
from django.conf.urls import url

router = routers.DefaultRouter()


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup', signup, name='signup'),
    path('logout',views.LogoutView.as_view(),name='logout'),
    path('login',views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('admin/', admin.site.urls),
    path('accounts/profile/',accountred,name='redirectacc'),
    path('logout',accountred,name="redirectacc"),
    path('question/',include('apps.question.urls')),
    path('dashboard/',include('apps.usrprofile.urls')),
    path('surveys/',include('apps.survey.urls')),
    url("surveyapi/",SurveyApiView.as_view()),

]
