from django.shortcuts import render

from .models import Note
import datetime
from django.http import HttpResponse
# Create your views here.
def add_data(request):
    pass
#     t=datetime.datetime.now()
#     print('t', t, type(t))
#     Note.objects.create(pub_date=t, title='thisisatitle', body='mybody', user_id=8)
#     return HttpResponse('hi, update')