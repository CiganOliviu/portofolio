# Generated by Django 3.0.8 on 2020-10-08 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainComponent', '0020_auto_20201008_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internshipsappliance',
            name='years_of_experience',
        ),
    ]