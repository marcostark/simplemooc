from django.db import models

# Create your models here.
from django.urls import reverse


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
