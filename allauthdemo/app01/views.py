from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, reverse
from django.utils.decorators import method_decorator

# @login_required
# def profile(request):
#     # AUTH_USER_MODEL 类型的对象，表示当前登录的用户。
#     # user = request.user
#     return HttpResponse('个人中心页面')


# class ProfileView(View):
#     def get(self, request):
#         return HttpResponse("个人中心页面")
#     # 因为所有的请求方法在类视图中最终都会通过dispatch这个方法,所以我们需要重写dispatch方法
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(ProfileView, self).dispatch(request, *args, **kwargs)


#写一个装饰器来装饰dispatch
# def login_required(func):
#     def wrapper(request, *args, **kwargs):
#         username = request.GET.get('username')
#         if username:
#             return func(request, *args, **kwargs)
#         else:
#             return redirect(reverse('app01:login'))
#
#         return wrapper

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        return HttpResponse("个人中心页面")

# def login(request):
#     return HttpResponse('need login!')




