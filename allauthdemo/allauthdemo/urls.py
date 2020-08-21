"""testemail URL Configuration

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
from django.conf.urls import url, include
from allauthdemo import settings
from django.views.static import serve

urlpatterns = [
    url('admin/', admin.site.urls),
    url('accounts/', include('allauth.urls')),
    url('chat/', include('tutorial_channelapp1.urls')),
    url('chat2/', include('tutorial_channelapp2.urls')),
    url(r'media/(?P<path>.*)',serve, {'document_root':settings.MEDIA_ROOT} ),
    url('^app01/', include('app01.urls')),
    url('^book/', include('bookapp.urls')),
    url('^articles/', include('articles.urls')),
    url('^formdemo/', include('formdemoapp.urls')),
    url('^formdemoapp2/', include('formdemoapp2.urls')),
    url('^learnformapp/', include('learnformapp.urls')),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^testmarkdownxapp/', include('testmarkdownxapp.urls')),
    url(r'^static/(?P<path>.*)', serve, {'document_root':settings.STATIC_ROOT}),

]
