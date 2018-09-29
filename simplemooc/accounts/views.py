from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from .forms import RegisterForm

# Form usado como base
def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() #Retorna um usuário
            
            # Ao se cadastrar será efetuado o login do usuário
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            #Fazendo autenticação
            login(request, user)
            return redirect('core:home')
    else:
        form = RegisterForm()
    context = {
        'form': form
        }
    return render(request, template_name, context)
