from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from testmarkdownxapp.forms import MyForm
from django.views.generic import ListView
from .models import MyModel

class showList(ListView):
    model = MyModel
    paginate_by = 20
    context_object_name = "articles"
    template_name = "markdownx/lists.html"

    # def get_queryset(self):
    #     return MyModel.objects.get_one()

class TestFormView(FormView):
    template_name = "index.html"
    # template_name = "markdownx/widget.html"
    form_class = MyForm
    model = MyModel

    # def form_valid(self, form):
    #     # form.instance.user = self.request.user
    #     return super(TestFormView, self).form_valid(form)
    def post(self, request, *args, **kwargs):
        print('hhhh, I am here')
        # super(TestFormView, self).post(request, *args, **kwargs)
        form = MyForm(request.POST)
        if form.is_valid():
            print('hhhhh')
            print('cleanded_data',form.cleaned_data)
            MyModel.objects.create(**form.cleaned_data)
        return redirect('/testmarkdownxapp/lists')

    def get_success_url(self):
        return reverse("testmarkdownxapp:showList")
        # return reverse("lists/")

def byme(request):
    form = MyForm()
    return render(request,"index2.html",{'form':form})


