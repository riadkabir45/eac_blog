# Generated by Django 5.1 on 2024-09-04 12:15

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eac_api', '0007_alter_student_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='student',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]