# Generated by Django 3.1.6 on 2021-02-07 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app4', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task_title',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]