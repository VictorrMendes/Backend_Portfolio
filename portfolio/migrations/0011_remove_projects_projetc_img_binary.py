# Generated by Django 4.2 on 2025-03-15 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_projects_projetc_img_binary_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='projetc_img_binary',
        ),
    ]
