# Generated by Django 3.2 on 2022-01-28 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spaceport', '0019_alter_list_cloud_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='image_previous_url',
            new_name='image_preview_url',
        ),
    ]
