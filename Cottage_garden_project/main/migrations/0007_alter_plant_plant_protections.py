# Generated by Django 4.0.3 on 2022-04-07 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_garden_image_alter_plant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='plant_protections',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]