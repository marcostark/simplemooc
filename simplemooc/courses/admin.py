from django.contrib import admin
from .models import Course, Enrollment


# Registrar os modelos aqui.

#Definindo opções para customização do model no admin do Django
class CourseAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'start_date','create_at']
    search_fields = ['nome','slug']
    prepopulated_fields = {'slug': ('nome',)} #Populando o slug de acordo com o nome do curso de forma automatica

admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment)


