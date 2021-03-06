import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


# PermissionsMixin - Traz a segurança e grupos

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Nome do Usuário', max_length=30, unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
        'Nome de usuário só pode conter letras, digitos ou os seguintes caracteres'
        ': @/./+/-/_', 'invalid')]
    )
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    is_active = models.BooleanField('Está ativo ?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe ? ', blank=True, default=False)
    date_joined = models.DateTimeField('Data de cadastro', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        """Retorna a descrição curta"""
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'