# Generated by Django 3.0.8 on 2020-09-22 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductsManagement', '0002_delete_pastproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='finishedproduct',
            name='ready_for_delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='plannedproduct',
            name='working_status',
            field=models.CharField(choices=[('On Queue', 'On Queue'), ('Current Working at', 'Current Working at')], default='On Queue', max_length=100),
        ),
    ]