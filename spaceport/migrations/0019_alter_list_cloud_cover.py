# Generated by Django 3.2 on 2022-01-28 06:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceport', '0018_auto_20220127_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='cloud_cover',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
