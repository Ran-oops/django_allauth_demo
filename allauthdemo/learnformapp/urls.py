from django.conf.urls import url, include
from django.views.generic import TemplateView
from learnformapp import views


urlpatterns = [
    url('users/', views.users),
    url('add_user/', views.add_user),
    url('edit_user/(\d+)', views.edit_user),
]
