from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import View,TemplateView
from . import views
from . import models
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
# @method_decorator(login_required, name='dispatch')
class BookListView(View):
    def get(self,request,*args,**kwargs):
        print('request', request, type(request), request.user, request.method)
        print('args', args, type(args))
        print('kwargs', kwargs, type(kwargs))
        return HttpResponse('book list view')

    def post(self, request, *args, **kwargs):
        print('request', request, type(request), request.user, request.method)
        print('args', args, type(args))
        print('kwargs', kwargs, type(kwargs))
        book_name = request.POST.get('name')
        book_author = request.POST.get('author')
        print('name:{},author:{}'.format(book_name, book_author))
        return HttpResponse('success')

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持POST以外的其他请求！'%request.method)

class AboutView(TemplateView):
    template_name = 'socialaccount/book/about.html'

    def get_context_data(self, **kwargs):
        context = {'phone': '145200000015'}
        return context


def addInfo(request):
    articles = []
    for i in range(101):
        article = models.Article(title='标题%s' % i, content='内容%s'%i)
        articles.append(article)

    models.Article.objects.bulk_create(articles)
    return HttpResponse('you succeed')


class ArticleListView(ListView):
    model = models.Article
    template_name = 'socialaccount/book/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = 'create_time'
    page_kwarg = 'p'


    # 过滤数据,并不是把所有的数据都返回,那么就可以重写这个get_queryset方法,将一些不需要展示的数据给过滤掉
    def get_queryset(self):
        return models.Article.objects.filter(id__gt=20)


    # 重写父类的get_context_data方法,添加自己的参数
    def get_context_data(self, *, object_list=None, **kwargs):
        # 需要先继承自父模板的get_context_data方法,否则很多方法将不能使用
        context = super(ArticleListView, self).get_context_data(**kwargs)
        # 然后添加自定义的参数
        context['username'] = 'May'
        paginator = context.get('paginator')
        # 获取数据的个数
        print('count', paginator.count)
        # 获取页面数
        print('num_pages', paginator.num_pages)
        print('num_range', paginator.page_range)

        page_obj = context.get('page_obj')
        print('page_obj.number',page_obj.number)
        print('page_obj.start_index',page_obj.start_index())
        print('page_obj.end_index',page_obj.end_index())
        print('page_obj.has_next',page_obj.has_next())
        print('page_obj.has_previous',page_obj.has_previous())
        print('page_obj.next_page_number',page_obj.next_page_number())
        # print('page_obj.previous_page_number',page_obj.previous_page_number())

        return context























