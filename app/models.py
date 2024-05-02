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