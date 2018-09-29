from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    
    email = forms.EmailField(label='E-mail')

    # Validar se já existe um email na base de dados com o campo informado
    def clean_email(self): # Tanto verifica quanto faz uma mudanças
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe um usuário com este E-mail')
        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False) # Retornar apenas o usuario com os valores dos campos
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

