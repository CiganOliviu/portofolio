# Generated by Django 3.0.8 on 2020-09-22 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClientsManagement', '0007_askproject_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientinfo',
            name='number_of_projects_in_progress',
            field=models.IntegerField(default=0),
        ),
    ]
