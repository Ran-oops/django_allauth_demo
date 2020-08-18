from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from testmarkdownxapp.views import TestFormView, showList
from testmarkdownxapp import views

app_name = "testmarkdownxapp"
urlpatterns = [
    url(r'^$', TestFormView.as_view(), name='form_view'),
    url(r'^lists$', showList.as_view(), name='showList'),
    url(r'^byme$', views.byme, name='byme'),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
