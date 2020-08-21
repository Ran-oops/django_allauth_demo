from django.conf.urls import url, include
from django.views.generic import TemplateView
from tutorial_channelapp2 import views


urlpatterns = [
    url('^$', views.index, name='index'),
    # url('<str:room_name>/', views.room, name='room'),
    url('^(?P<room_name>[^/]+)/$', views.room, name='room'),

]
