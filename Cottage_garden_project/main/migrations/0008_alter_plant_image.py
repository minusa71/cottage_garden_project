# Generated by Django 4.0.3 on 2022-04-08 20:45

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_plant_plant_protections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]