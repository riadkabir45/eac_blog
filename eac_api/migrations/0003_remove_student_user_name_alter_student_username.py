# Generated by Django 5.1 on 2024-09-04 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eac_api', '0002_alter_student_options_alter_student_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user_name',
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
