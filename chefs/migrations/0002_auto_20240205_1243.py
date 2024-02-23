# Generated by Django 3.2.23 on 2024-02-05 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chefs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chef',
            name='cuisine_speciality',
        ),
        migrations.AddField(
            model_name='chef',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]