# Generated by Django 3.2.23 on 2024-01-14 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='chef',
            new_name='owner',
        ),
    ]
