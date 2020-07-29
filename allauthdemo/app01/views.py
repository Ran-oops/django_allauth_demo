from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    # AUTH_USER_MODEL 类型的对象，表示当前登录的用户。
    # user = request.user
    return HttpResponse('ok')
