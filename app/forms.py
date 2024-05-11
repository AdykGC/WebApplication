from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError
from .models import CustomUser
import re
from django import forms
from .models import Project, Activity
from .models import PM_Project, PM_Activity


class UserRegistrationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('translator', 'Translator'),
        ('project_manager', 'Project Manager'),
        ('chief_editor', 'Chief Editor'),
    ]

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = "Your password must contain at least 8 characters, including one capital letter, one number, and one special character."

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'user_type']

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError('Password must be at least 8 characters long.')
        if not re.search(r'[A-Z]', password1):
            raise ValidationError('Password must contain at least one capital letter.')
        if not re.search(r'\d', password1):
            raise ValidationError('Password must contain at least one number.')
        if not re.search(r'[!@#$%^&*()_+{}|:"<>?]', password1):
            raise ValidationError('Password must contain at least one special character.')
        return password1
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")

        return cleaned_data

User = get_user_model()

class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('Invalid username or password.')
        return cleaned_data

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name']

class ActivityForm(forms.ModelForm):
    PERCENT_CHOICES = [
        (0, '0%'),
        (33, '33%'),
        (67, '67%'),
        (100, '100%'),
    ]
    percent_complete = forms.ChoiceField(choices=PERCENT_CHOICES, label='Percentage Complete')

    class Meta:
        model = Activity
        fields = ['percent_complete']




#/////////////////////////////////////////////////////////////////////////////////////////////////////
# ERROR-1 Rename this fucking shit
#/////////////////////////////////////////////////////////////////////////////////////////////////////
class PM_ProjectForm(forms.ModelForm):
    class Meta:
        model = PM_Project
        fields = ['project_name', 'deadline']

class PM_ActivityForm(forms.ModelForm):
    class Meta:
        model = PM_Activity
        fields = ['activity_name','task_info','translator','project','deadline']