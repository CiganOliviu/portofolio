# Generated by Django 3.0.8 on 2020-09-28 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainComponent', '0012_studio_moment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studio',
            name='moment',
        ),
    ]
