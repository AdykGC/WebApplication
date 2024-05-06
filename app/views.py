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
    all_projects = Project.objects.all()
    translator_activitys = Activity.objects.all()
    context = {
        'translator_projects': all_projects,
        'translator_activitys': translator_activitys,
    }
    return render(request, 'translator_home.html', context)
def chief_editor_home(request):
    all_projects = Project.objects.all()
    chief_editor_activitys = Activity.objects.all()
    context = {
        'chief_editor_projects': all_projects,
        'chief_editor_activitys': chief_editor_activitys,
    }
    return render(request, 'chief_editor_home.html', context)




def update_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    project = activity.project
    if request.method == 'POST':
        new_status = request.POST.get('status')
        activity.status = new_status
        activity.save()
        return redirect(reverse('translator_home'))
    return HttpResponse("Метод не поддерживается")
def update_activity_2(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    project = activity.project
    if request.method == 'POST':
        new_status = request.POST.get('status')
        activity.status = new_status
        activity.save()
        return redirect(reverse('chief_editor_home'))
    return HttpResponse("Метод не поддерживается")



def successful_register(request):
    # Your logic for translator home page
    return render(request, 'successful_register.html', )