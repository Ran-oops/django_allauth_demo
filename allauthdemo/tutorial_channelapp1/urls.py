from django.conf.urls import url, include
from django.views.generic import TemplateView
from tutorial_channelapp1 import views


urlpatterns = [
    url('^$', views.index, name='index'),

]
