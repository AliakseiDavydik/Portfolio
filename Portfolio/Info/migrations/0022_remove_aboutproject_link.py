# Generated by Django 4.2.2 on 2023-06-28 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Info', '0021_alter_aboutproject_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutproject',
            name='link',
        ),
    ]
