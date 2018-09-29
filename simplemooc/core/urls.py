from django.conf.urls import url
from django.urls import path
from simplemooc.core.views import home
from simplemooc.core.views import contact

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contact, name='contact'),
]