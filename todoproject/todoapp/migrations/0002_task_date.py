# Generated by Django 4.2 on 2023-05-18 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1998-11-11'),
            preserve_default=False,
        ),
    ]
