from django.db import models

# Create your models here.
from django.urls import reverse
from django.conf import settings


class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(nome__icontains=query) | \
            models.Q(description__icontains=query)
        )


class Course(models.Model):

    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição Simples', blank=True)
    about = models.TextField('Sobre o Curso', blank=True)
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    )
    image = models.ImageField(
        upload_to='courses/images', verbose_name='Imagem',
        null=True, blank=True
    )

    create_at = models.DateTimeField('Criado em', auto_now_add=True)

    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CourseManager()


    #Metodo para retornar o nome do curso.
    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('courses:details', args=[self.slug])


    #Customizando o admin
    class Meta:
        verbose_name = 'Curso' #Vai associar ao nome da classe
        verbose_name_plural = 'Cursos'
        ordering = ['nome'] #Ordenando resultados pelo nome


class Enrollment(models.Model):
    ''' Inscrição em um curso '''

    STATUS_CHOICES = (
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Usuário',
        related_name='enrollments', on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course, verbose_name='Curso',related_name='enrollments',on_delete=models.CASCADE
    )
    status = models.IntegerField(
        'Sitação', choices=STATUS_CHOICES, default=1,
        blank=True
    )

    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    def active(self):
        self.status = 1
        self.save()


    class Meta:

        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('user','course'))
        # Indicando que para esse model, deve criar um indice de unicidade para cada usuário e curso

    def __str__(self):
        return "Inscrição"