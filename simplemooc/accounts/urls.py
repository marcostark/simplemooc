from django.conf.urls import url
#from simplemooc.accounts.views import index
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path
from simplemooc.accounts.views import register, dashboard, edit

from simplemooc.accounts.views import edit_password

urlpatterns = [
    path('entrar/',LoginView.as_view(template_name = 'accounts/login.html'), name='login'),
    path('sair/', LogoutView.as_view(next_page = 'core:home'), name='logout'),
    path('cadastre-se/', register, name='register'),
    path('', dashboard, name='dashboard'),
    path('editar/', edit, name='edit'),
    path('editar-password/', edit_password, name='edit_password'),
]

