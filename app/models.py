from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('translator', 'translator'),
        ('project_manager', 'project_manager'),
        ('chief_editor', 'chief_editor'),
    ]

    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)

    # Define custom related_name for groups and user_permissions fields
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')



# Модель для проекта
class Project(models.Model):
    # Поле для названия проекта
    project_name = models.CharField(max_length=255)

    # Метод для отображения объекта проекта в админке Django
    def __str__(self):
        return self.project_name
# Модель для активности


# Модель для активности
class Activity(models.Model):
    # Поле для названия активности
    name = models.CharField(max_length=100, default="Active")
    task_info = models.CharField(max_length=100, default="Change all letter to upper case in the beginning of the sentences if needed")
    deadline = models.DateField(default='2024-05-07')
    status = models.CharField(max_length=50, default="Not completed")
    # Поле для связи с проектом, ForeignKey указывает на связь "много к одному" (много активностей к одному проекту)
    project = models.ForeignKey('Project', related_name='activities', on_delete=models.CASCADE)

    # Метод для отображения объекта активности в админке Django
    def __str__(self):
        return self.name





class PM_Project(models.Model):
    project_name = models.CharField(max_length=255)
    deadline = models.DateField()
    status = models.CharField(max_length=20, default='Not completed', editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    activity = models.ForeignKey('PM_Activity', on_delete=models.CASCADE, related_name="activities")
    def __str__(self):
        return self.project_name


class PM_Activity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    activity_name = models.CharField(max_length=255)
    task_info = models.CharField(max_length=255, default="Change all letter to upper case in the beginning of the sentences if needed")
    translator = models.CharField(max_length=255)
    deadline = models.DateField()
    remaining_text_volume = models.CharField(max_length=100, default="0%")
    status = models.CharField(max_length=100, default="Not Completed")
    project = models.ForeignKey('PM_Project', on_delete=models.CASCADE, related_name="activities")

    def __str__(self):
        return self.activity_name