"""GameofThrones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from GameofThronesApp import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^house/(?P<pk>\d+)/$',views.house,name='house'),
    url(r'^character/(?P<pk>\d+)/$', views.character, name='character'),
    url(r'^character/(?P<pk>\d+)new/$',views.new_character,name='new_character'),
    url(r'^house/(?P<pk>\d+)new/$',views.new_house,name='new_house'),
    url(r'^battle/(?P<pk>\d+)new/$',views.new_battle,name='new_battle'),
]
