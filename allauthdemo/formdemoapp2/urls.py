from django.conf.urls import url, include
from django.views.generic import TemplateView
from formdemoapp2 import views


urlpatterns = [
    url('add_emp/', views.add_emp),
]
