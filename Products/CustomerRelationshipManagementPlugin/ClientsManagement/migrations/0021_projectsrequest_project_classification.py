# Generated by Django 3.0.8 on 2020-11-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClientsManagement', '0020_auto_20201109_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsrequest',
            name='project_classification',
            field=models.CharField(default='Requested', max_length=100),
        ),
    ]