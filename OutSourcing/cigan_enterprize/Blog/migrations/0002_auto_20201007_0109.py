# Generated by Django 3.0.8 on 2020-10-06 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='manager_image',
            field=models.ImageField(default='default.jpg', upload_to='managers_image/'),
        ),
        migrations.AddField(
            model_name='post',
            name='manager_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
