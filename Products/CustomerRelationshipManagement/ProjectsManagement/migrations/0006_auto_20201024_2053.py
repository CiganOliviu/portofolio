# Generated by Django 3.0.8 on 2020-10-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsManagement', '0005_activeworkingproject_ready_for_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activeworkingproject',
            name='type',
            field=models.CharField(choices=[('Presentation WebSite', 'Presentation WebSite'), ('WebApp', 'Webapp'), ('Mobile App', 'Mobile App'), ('Marketing Project', 'Marketing Project')], max_length=100),
        ),
        migrations.AlterField(
            model_name='finishedproject',
            name='type',
            field=models.CharField(choices=[('Presentation WebSite', 'Presentation WebSite'), ('WebApp', 'Webapp'), ('Mobile App', 'Mobile App'), ('Marketing Project', 'Marketing Project')], max_length=100),
        ),
        migrations.AlterField(
            model_name='plannedproject',
            name='type',
            field=models.CharField(choices=[('Presentation WebSite', 'Presentation WebSite'), ('WebApp', 'Webapp'), ('Mobile App', 'Mobile App'), ('Marketing Project', 'Marketing Project')], max_length=100),
        ),
    ]
