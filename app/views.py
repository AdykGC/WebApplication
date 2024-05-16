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
from .models import PM_Project, PM_Activity
from .forms import PM_ProjectForm, PM_ActivityForm



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
    all_projects = PM_Project.objects.all().order_by('-created_at')
    translator_activitys = PM_Activity.objects.all().order_by('-created_at')
    context = {
        'translator_projects': all_projects,
        'translator_activitys': translator_activitys,
    }
    return render(request, 'translator_home.html', context)
def chief_editor_home(request):
    all_projects = PM_Project.objects.all().order_by('-created_at')
    chief_editor_activitys = PM_Activity.objects.all().order_by('-created_at')
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


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////      User's Interface      ///////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def project_manager(request):
    projects = PM_Project.objects.all().order_by('-created_at')  # Retrieve all projects sorted by creation time
    user = request.user  # Get the current user
    translators = CustomUser.objects.filter(user_type='translator')
    activities = PM_Activity.objects.all().order_by('-created_at')  # Retrieve all activities sorted by creation time

    if request.method == 'POST':
        form = PM_ProjectForm(request.POST)
        if form.is_valid():
            # Save the project with the current user as the selected_translator
            project = form.save(commit=False)
            project.save()
            return redirect('project_manager_home')  # Redirect after successful form submission
    else:
        form = PM_ProjectForm()

    context = {
        'projects': projects,
        'user': user,
        'form': form,
        'translators': translators,
        'activities': activities  # Pass sorted activities to the template context
    }
    return render(request, 'project_manager_home.html', context)














def update_project(request, project_id):
    project = get_object_or_404(PM_Project, id=project_id)
    if request.method == 'POST':
        form = PM_ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_manager_home')  # Replace with your actual home view
    else:
        form = PM_ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form})


#/////////////////////////////////////////////////////////////////////////////////////////////////////
# ERROR-1 Rename this fucking shit
#/////////////////////////////////////////////////////////////////////////////////////////////////////
def PM_update_activity(request, activity_id): 
    if request.method == 'POST':
        activity = get_object_or_404(PM_Activity, pk=activity_id)
        activity.activity_name = request.POST.get('activity_name', activity.activity_name)
        activity.task_info = request.POST.get('task_info', activity.task_info)
        activity.translator = request.POST.get('translator', activity.translator)
        activity.project_id = request.POST.get('project_id', activity.project_id)
        activity.deadline = request.POST.get('deadline', activity.deadline)
        activity.save()
        messages.success(request, 'Activity updated successfully!')
        return redirect('project_manager_home')  # Redirect to a specific view after updating
    else:
        return render(request, 'edit_project.html')

def create_activity(request):
    projects = PM_Project.objects.all()  # Fetch all projects for the dropdown
    translators = CustomUser.objects.filter(user_type='translator')  # Assuming CustomUser is your user model with a 'user_type' field

    if request.method == 'POST':
        form = PM_ActivityForm(request.POST)
        print(request.POST)
        if form.is_valid():
            
            activity = form.save(commit=False)
            activity.remaining_text_volume = "0%"
            activity.status = "Not Completed"
            activity.save()
            
            return redirect('project_manager_home')  # Redirect to a home or appropriate page
        else:
            print(form.is_valid())
    else:
        form = PM_ActivityForm()

    return render(request, 'project_manager_home.html', {'form': form, 'projects': projects, 'translators': translators})