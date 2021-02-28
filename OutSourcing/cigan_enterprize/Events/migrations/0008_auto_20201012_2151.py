# Generated by Django 3.0.8 on 2020-10-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0007_auto_20201012_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostevent',
            name='cover_image',
            field=models.ImageField(default='default.jpg', upload_to='events/cover/'),
        ),
        migrations.AddField(
            model_name='sponsorevent',
            name='cover_image',
            field=models.ImageField(default='default.jpg', upload_to='events/cover/'),
        ),
        migrations.AlterField(
            model_name='hostevent',
            name='location_image',
            field=models.ImageField(default='default.jpg', upload_to='events/location/'),
        ),
        migrations.AlterField(
            model_name='sponsorevent',
            name='location_image',
            field=models.ImageField(default='default.jpg', upload_to='events/location/'),
        ),
    ]
