from django import forms
from django.core.mail import send_mail
from django.conf import settings

from simplemooc.core.mail import send_mail_template

#Classe para formulario
class ContactCourse(forms.Form):

    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(
        label='Mensagem/Dúvida', widget= forms.Textarea
    )


    def send_mail(self,course):
        '''
            Resposansavél pelo envio de email
        '''
        subject = '[%s] Contato' % course
        context = {
            'nome': self.cleaned_data['nome'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message']
        }
        template_name = 'courses/contact_email.html'
        #message = message % context
        send_mail_template(subject, template_name, context,
                  [settings.CONTACT_EMAIL]
                  )
