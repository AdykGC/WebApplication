# Generated by Django 5.0.4 on 2024-05-11 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_pm_project_pm_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='pm_activity',
            name='task_info',
            field=models.CharField(default='Change all letter to upper case in the beginning of the sentences if needed', max_length=255),
        ),
    ]
