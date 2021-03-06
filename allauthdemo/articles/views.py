from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import View,TemplateView
from . import views
from . import models
from django.views.generic import ListView
import markdown
from django.core.files.base import ContentFile

from django.core.files.images import ImageFile
from articles.forms import TestImageForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, template_name='articles/upload_img.html')

# @method_decorator(login_required, name='dispatch')
class GetImage(View):
    def get(self,request,*args,**kwargs):
        print('request', request, type(request), request.user, request.method)
        print('args', args, type(args))
        print('kwargs', kwargs, type(kwargs))
        return HttpResponse('getImage')

    def post(self, request, *args, **kwargs):
        print('request', request)
        print('args', args, type(args))
        print('kwargs', kwargs, type(kwargs))
        # img_f = ContentFile(request.FILES['im_f'].read())
        name = request.POST['name']
        im_f = request.FILES.get('im_f')
        img_f = request.FILES['im_f']
        print('im_f((((', im_f, type(im_f))
        print('img_f[[[', img_f, type(img_f))
        image_data = {
            'im_f.read()':im_f.read(),
            'im_f.name':im_f.name,
            'im_f.size':im_f.size,
            'im_f.file':im_f.file,
            'im_f.field_name':im_f.field_name,
            'im_f.content_type':im_f.content_type,
            'im_f.size':im_f.size,
            'im_f.charset':im_f.charset,
            'im_f.content_type_extra':im_f.content_type_extra,

        }
        print('=====type(read())======', type(im_f.read()))
        print('image_data',image_data)
        # file_content = ContentFile(im_f.read())
        image_content = ImageFile(im_f.read())
        print('file_content', image_content, type(image_content))
        # print('file_content.width', image_content.width, type(image_content.width))
        # print('file_content.height', image_content.height, type(image_content.height))
        im_f = models.TestImage(name=request.FILES['im_f'].name, img=request.FILES['im_f'])
        print('request here:', request, type(request))
        print('request.FILES here:', request.FILES, type(request.FILES))
        print('im_f', im_f)
        im_f.save()
        tt = models.TestImage.objects.all()
        print('tt',tt)
        print('yes you made it!')
        return HttpResponse('success')

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持POST以外的其他请求！'%request.method)

class NewArticleListView(ListView):
    model = models.NewArticle
    template_name = '/articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = 'create_time'
    page_kwarg = 'p'


    # 过滤数据,并不是把所有的数据都返回,那么就可以重写这个get_queryset方法,将一些不需要展示的数据给过滤掉
    # def get_queryset(self):
    #     return models.Article.objects.filter(id__gt=20)
    #
    #
    # # 重写父类的get_context_data方法,添加自己的参数
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     # 需要先继承自父模板的get_context_data方法,否则很多方法将不能使用
    #     context = super(ArticleListView, self).get_context_data(**kwargs)
    #     # 然后添加自定义的参数
    #     context['username'] = 'May'
    #     paginator = context.get('paginator')
    #     # 获取数据的个数
    #     print('count', paginator.count)
    #     # 获取页面数
    #     print('num_pages', paginator.num_pages)
    #     print('num_range', paginator.page_range)
    #
    #     page_obj = context.get('page_obj')
    #     print('page_obj.number',page_obj.number)
    #     print('page_obj.start_index',page_obj.start_index())
    #     print('page_obj.end_index',page_obj.end_index())
    #     print('page_obj.has_next',page_obj.has_next())
    #     print('page_obj.has_previous',page_obj.has_previous())
    #     print('page_obj.next_page_number',page_obj.next_page_number())
    #     # print('page_obj.previous_page_number',page_obj.previous_page_number())
    #
    #     return context

# 使用markdown包
def showmarkdown(request):
    text = '''
#this is title
##this is subtitle
**TALK IS CHEAP, SHOW ME YOUR CODE**
```python
content = cursor.fetchall()
conn.close()
return content
```'''
    html = markdown.markdown(text,
                             extensions = [
                                 # 包含 缩写、表格等常用扩展
                                'markdown.extensions.extra',
                                # 语法高亮扩展
                                'markdown.extensions.codehilite',
                                #toc是目录
                                'markdown.extensions.toc',
                             ])

    print('html',html, type(html))
    return render(request, 'articles/showmarkdown.html', {'html': html})

# 使用django-markdown-deux实现  语法没有高亮
def showmarkdown2(request):
    text = '''
[TOC] 目录：
#markdown2
##second list
###markdown is ok?
**关关雎鸠，在河之洲。窈窕淑女，君子好逑。**

参差荇菜，左右流之。窈窕淑女，寤寐求之。

---
+ 列表一
+ 列表二
    + 列表二-1
    + 列表二-2

```python
content=cursor.fetchall()
conn.close()
return content
```'''

    return render(request,"articles/showmarkdown2.html",{"content":text})

def send_message(request):
    return render(request, 'articles/in_markdownx.html')

def createmarkdownpa(request):
    form = TestImageForm()
    # return render(request,"articles/createmarkdownpa.html", {'form':form})
    return render(request,"markdownx/widget2.html", {'form':form})











