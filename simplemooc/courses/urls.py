from django.conf.urls import url
from simplemooc.courses.views import index, details, enrollment

urlpatterns = [
    url(r'^$', index, name='index'),
    #url(r'^(?P<pk>\d+)/$', details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/$', details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/inscricao/$', enrollment, name='enrollment'),
]