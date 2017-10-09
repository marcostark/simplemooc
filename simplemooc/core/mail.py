from django.template.loader import render_to_string
from django.template.defaultfilters import striptags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def send_mail_template(subject, template_name, context, recipient_list,
                       from_email=settings.DEFAULT_FROM_EMAIL,fail_silently=False):
    '''
        Centralizando o envio de emails de forma mais organizada

    '''

    #Faz a renderização do template e gera um string
    message_html = render_to_string(template_name, context)

    #Removendo as tags do html
    message_txt = striptags(message_html)

    #Email com varias alternativas, onde ele adicionará conteudo alternativo
    email = EmailMultiAlternatives(
        subject=subject, body=message_txt, from_email=from_email,
        to=recipient_list
    )
    #Adicionando conteudo alternativo para carregar o html
    email.attach_alternative(message_html, "text/html")

    #Caso o envio de email falhe, gerará uma exeção
    email.send(fail_silently=fail_silently)