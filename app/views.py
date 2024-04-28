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

def project1_detail(request, project_id):
    # Получаем информацию о проекте 1 из базы данных
    project = Project1.objects.get(pk=project_id)
    # Загружаем шаблон и передаем информацию о проекте
    template = loader.get_template('project1_detail_template.html')
    context = {'project': project}
    return HttpResponse(template.render(context, request))

def project2_detail(request, project_id):
    # Получаем информацию о проекте 2 из базы данных
    project = Project2.objects.get(pk=project_id)
    # Загружаем шаблон и передаем информацию о проекте
    template = loader.get_template('project2_detail_template.html')
    context = {'project': project}
    return HttpResponse(template.render(context, request))


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

def translator_home(request):
    # Your logic for translator home page
    return render(request, 'translator_home.html')



def chief_editor_home(request):
    # Your logic for chief editor home page
    return render(request, 'chief_editor_home.html')

def successful_register(request):
    # Your logic for translator home page
    return render(request, 'successful_register.html')

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



def some_view(request):
    # Получение объекта Activity из базы данных
    activity = "Ваше собственное значение для тега <p>"
    custom_text = "Ваше собственное значение для тега <p>"
    
    # Передача объекта Activity и текста в контекст шаблона
    return render(request, 'translator_home.html', {'activity': activity, 'custom_text': custom_text})