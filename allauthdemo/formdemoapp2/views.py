from django.shortcuts import render, HttpResponse, redirect
from formdemoapp2.myform import EmForm
from formdemoapp2 import models

# Create your views here.
def add_emp(request):
    if request.method == 'GET':
        form = EmForm()
        print('formmmmmmmmmmm', form, type(form))
        return render(request, "formdemo2/add_em.html", {"form": form})
    else:
        form = EmForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data.pop("r_salary")
            models.Emp.objects.create(**data)
            # return redirect("/index/")
            return HttpResponse("yes this is right!")
        else:
            clear_errors = form.errors.get("__all__")  # 获取全局钩子错误信息
            return render(request, "formdemo2/add_em.html", {"form":form, "clear_errors":clear_errors})