from django.shortcuts import render, redirect

from learnformapp.models import UserInfo
from learnformapp.myform import UserForm
# Create your views here.
def users(request):
    user_list = UserInfo.objects.all()
    return render(request,'users/users.html', {'user_list':user_list})

def add_user(request):
    if request.method == 'GET':
        obj = UserForm()
        return render(request, 'users/add_user.html', {'obj':obj})
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            print('cleaned_data:',obj.cleaned_data)
            UserInfo.objects.create(**obj.cleaned_data)
            return redirect('/learnformapp/users/')  # 注意：这里就体现了redirect的绝妙之处，相当于调用指定路由的view函数
            # return render(request, 'users/users.html')  # 如果用render的话还要再把传入模板的数据再传一遍
        else:
            return render(request, "users/add_user.html", {'obj':obj})   # 如果验证不通过，此时的obj里面包含了错误信息


def edit_user(request, nid):
    # nid = request.GET.get('nid')
    if request.method == 'GET':
        data = UserInfo.objects.filter(id=nid).first()
        obj = UserForm({'username':data.username, 'email':data.email, 'id':data.id})
        return render(request,"users/edit_user.html", {'obj':obj, 'nid':nid})
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            UserInfo.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/learnformapp/users/')
        else:
            return render(request,"users/edit_user.html", {'obj':obj,'nid':nid})


