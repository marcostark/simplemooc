from django.conf.urls import url
#from simplemooc.accounts.views import index
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from simplemooc.accounts.views import register

urlpatterns = [
    # O Terceiro parametro indica que há substituição na view do template do django pelo personalizado
    url(r'^entrar/$', login,
        {'template_name':'accounts/login.html'}, name='login'),

    url(r'^sair/$', logout,{'next_page':'core:home'}, name='logout'),

    url(r'^cadastre-se/$', register, name='register'),
]

