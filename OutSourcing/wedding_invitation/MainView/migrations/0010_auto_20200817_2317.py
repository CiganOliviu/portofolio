# Generated by Django 3.0.8 on 2020-08-17 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainView', '0009_auto_20200817_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmanswer',
            name='answer_sent',
            field=models.BooleanField(default=False),
        ),
    ]
