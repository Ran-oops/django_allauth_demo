from django.conf.urls import url, include
from . import views


app_name='app01'
urlpatterns = [
    # url('^profile', views.profile, name='profile'),
    # url('^login', views.login, name='login'),
    url('^ProfileView', views.ProfileView.as_view(), name='ProfileView'),
]
