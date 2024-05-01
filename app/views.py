from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, CustomAuthenticationForm, ProjectForm, ActivityForm
from .models import CustomUser, Project, Activity
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db import connection
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def handlelogin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 'translator':
                    return redirect('translator_home')
                elif user.user_type == 'project_manager':
                    return redirect('project_manager_home')
                elif user.user_type == 'chief_editor':
                    return redirect('chief_editor_home')
                # Add more user type conditions as needed
            else:
                # Handle invalid login
                # Redirect back to login page or display an error message
                pass
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

    
def handleregistration(request):
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user_type = form.cleaned_data['user_type']

            # Create a new CustomUser object and save it to the database
                new_user = CustomUser.objects.create_user(username=username, password=password, user_type=user_type)

                return redirect('successful_register')  # Redirect to the login page after successful registration
        else:
            form = UserRegistrationForm()
        return render(request, 'registration.html', {'form': form})



def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    projects = Project.objects.all()  # Получаем список всех проектов
    return render(request, 'project_detail.html', {'project': project, 'projects': projects})
def project_detail_2(request, project_id):
    project = Project.objects.get(id=project_id)
    projects = Project.objects.all()  # Получаем список всех проектов
    return render(request, 'project_detail_2.html', {'project': project, 'projects': projects})


def translator_home(request):
    all_projects = Project.objects.all()
    context = {
        'translator_projects': all_projects,
    }
    return render(request, 'translator_home.html', context)
def chief_editor_home(request):
    all_projects = Project.objects.all()
    context = {
        'chief_editor_projects': all_projects,
    }
    return render(request, 'chief_editor_home.html', context)



def translator_detail(request):
    all_projects = Project.objects.all()
    context = {
        'projects_detail': all_projects,
    }
    return render(request, 'project_detail.html', context)
def chief_editor_detail(request):
    all_projects = Project.objects.all()
    context = {
        'projects_detail_2': all_projects,
    }
    return render(request, 'project_detail_2.html', context)


def update_activity(request, activity_id):
    # Получаем объект из базы данных по его идентификатору
    activity = Activity.objects.get(id=activity_id)
    project = activity.project

    # Проверяем, был ли отправлен POST-запрос с обновленными данными
    if request.method == 'POST':
        # Получаем новый статус из POST-запроса
        new_status = request.POST.get('status')
        # Обновляем поле статуса объекта
        activity.status = new_status
        # Сохраняем изменения в базе данных
        activity.save()
        # Перенаправляем пользователя обратно на страницу деталей проекта
        return redirect(reverse('project_detail', kwargs={'project_id': project.id}))
    
    # Если запрос не метода POST, возвращаем HttpResponse с информацией о том, что метод не поддерживается
    return HttpResponse("Метод не поддерживается")

# def edit_activity(request):
    # if request.method == "POST":
    #     form = EditActivityForm(request.POST)
    #     if form.is_valid():

# ТУТ КОД

# def activity_edit(request):
#     if request.method == 'POST':
#         # Получение данных из POST-запроса
#         data = json.loads(request.body)
        
#         # Извлечение данных
#         completed = data.get('completed', False)
#         name = data.get('name', '')

#         # Поиск существующей активности по имени
#         activity = get_object_or_404(Activity, name=name)

#         # Обновление или создание активности
#         activity.completed = completed
#         activity.save()

#         # Возвращение успешного ответа в формате JSON
#         return JsonResponse({'status': 'success'})
#     else:
#         # Если метод запроса не POST, возвращаем ошибку
#         return JsonResponse({'error': 'Only POST method is allowed'})




def successful_register(request):
    # Your logic for translator home page
    return render(request, 'successful_register.html', )

def project_manager(request):
    projects = Project.objects.all()
    user = request.user
    translators = CustomUser.objects.filter(user_type='translator')

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.selected_translator = user
            project.save()
            return redirect('project_manager_home')  
    else:
        form = ProjectForm()

    context = {
        'projects': projects,
        'user': user,
        'form': form,
        'translators': translators
    }
    return render(request, 'project_manager_home.html', context)

def update_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_manager_home')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form})

def project_manager_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    activities = Activity.objects.filter(project=project)

    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.project = project
            activity.save()
            return redirect('project_manager_detail', project_id=project_id)
    else:
        form = ActivityForm()

    context = {
        'project': project,
        'activities': activities,
        'form': form,
    }
    return render(request, 'project_manager_detail.html', context)


