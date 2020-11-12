# Generated by Django 3.0.8 on 2020-09-27 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainComponent', '0008_internshipsappliance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avaibleinternship',
            old_name='job_slug',
            new_name='internship_slug',
        ),
        migrations.AlterField(
            model_name='avaibleinternship',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='avaiblejob',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='internshipsappliance',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jobsappliance',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studio',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]