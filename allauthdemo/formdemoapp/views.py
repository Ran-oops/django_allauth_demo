from django.shortcuts import render, HttpResponse
from formdemoapp.myform import EmpForm
from formdemoapp import models
from django.core.exceptions import ValidationError

# Create your views here.
def add_emp(request):
    if request.method == 'GET':
        form = EmpForm()
        return render(request, 'formdemo/add_emp.html', {'form':form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data  # 校验成功的值，会放在cleaned_data里
            data.pop('r_salary')
            print('data', data)

            models.Emp.objects.create(*data)
            return HttpResponse(
                'OK, SUCCESS'
            )
        else:
            print(form.errors) # 打印错误信息
            clean_errors = form.errors.get("__all__")
            print('3333333', clean_errors)
        return render(request, "formdemo/add_emp.html", {"form":form, "clean_errors":form.errors})