from django.conf.urls import url, include
from django.views.generic import TemplateView
from articles import views


urlpatterns = [
    url('^index', views.index, name='index'),
    url('^new', views.NewArticleListView.as_view()),
    url('^forimg', views.GetImage.as_view(), name='GetImage_f'),
    #在一个网站中，有一些页面不需要我们从数据库中提取数据到前端页面中，例如网址中的“关于我们” 这个页面一般都是在html中写死的数据，不需要进行改动，这个时候我们就可以直接在urls中直接渲染html文件，而不用视图函数或者视图类来进行渲染。
    # url('^about/', TemplateView.as_view(template_name='socialaccount/book/about.html')),
    # url('^about/', views.AboutView.as_view()),
    # url('^add/', views.addInfo, name='add'),
    # url('^articlelist/', views.ArticleListView.as_view()),
]
