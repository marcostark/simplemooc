from django.conf.urls import url
from simplemooc.core.views import home
from simplemooc.core.views import contact

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contato/$', contact, name='contact'),
]