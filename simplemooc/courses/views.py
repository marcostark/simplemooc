from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import ContactCourse

# Create your views here.

#View para APP COURSES

#Resposavel por randerizar o template para a listagem de cursos
def index(request):
    courses = Course.objects.all() #Pegando todos os objetos cadastrados no BD
    template_name = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)

# def details(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#     context = {
#         'course':course
#     }
#     template_name = 'courses/details.html'
#     return render(request, template_name, context)

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            print(form.cleaned_data)  # Retorna um dicionario com os campos já validados
            #sempre o cleaned_data para acessar os campos do formulario depois de validados
            #print(form.cleaned_data['nome']) #Acessar o campo nome já validado
            form.send_mail(course)
            form = ContactCourse()

    else:
        form = ContactCourse()
    context['form'] = form
    context['course'] = course
    template_name = 'courses/details.html'
    return render(request, template_name, context)
