# Generated by Django 5.0.6 on 2024-07-24 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaapp', '0004_house_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='image_url',
        ),
        migrations.AddField(
            model_name='house',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='house_images/'),
        ),
    ]
