# Generated by Django 5.0.6 on 2024-08-07 00:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaapp', '0005_remove_house_image_url_house_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='house',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gaapp.house'),
        ),
    ]