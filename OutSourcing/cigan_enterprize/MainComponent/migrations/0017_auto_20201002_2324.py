# Generated by Django 3.0.8 on 2020-10-02 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainComponent', '0016_studio_studio_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableInternship',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post', models.CharField(default='', max_length=150)),
                ('description', models.TextField(default='')),
                ('requirements', models.TextField(default='')),
                ('one_day', models.TextField(default='')),
                ('job_type', models.CharField(choices=[('Remote', 'Remote'), ('Non-Remote', 'Non-Remote')], default='Non-Remote', max_length=100)),
                ('perks', models.CharField(default='', max_length=200)),
                ('released_day', models.DateTimeField(auto_now_add=True)),
                ('internship_slug', models.SlugField(default='', max_length=200, unique=True)),
                ('location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MainComponent.Studio')),
            ],
        ),
        migrations.CreateModel(
            name='AvailableJob',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post', models.CharField(default='', max_length=150)),
                ('description', models.TextField(default='')),
                ('requirements', models.TextField(default='')),
                ('one_day', models.TextField(default='')),
                ('job_type', models.CharField(choices=[('Remote', 'Remote'), ('Non-Remote', 'Non-Remote')], default='Non-Remote', max_length=100)),
                ('perks', models.CharField(default='', max_length=200)),
                ('released_day', models.DateTimeField(auto_now_add=True)),
                ('job_slug', models.SlugField(default='', max_length=200, unique=True)),
                ('location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MainComponent.Studio')),
            ],
        ),
        migrations.RemoveField(
            model_name='avaiblejob',
            name='location',
        ),
        migrations.RemoveField(
            model_name='internshipsappliance',
            name='carrer',
        ),
        migrations.RemoveField(
            model_name='jobsappliance',
            name='carrer',
        ),
        migrations.DeleteModel(
            name='AvaibleInternship',
        ),
        migrations.DeleteModel(
            name='AvaibleJob',
        ),
        migrations.AddField(
            model_name='internshipsappliance',
            name='career',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MainComponent.AvailableJob'),
        ),
        migrations.AddField(
            model_name='jobsappliance',
            name='career',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MainComponent.AvailableJob'),
        ),
    ]