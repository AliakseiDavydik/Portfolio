# Generated by Django 4.2.2 on 2023-06-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info', '0016_alter_about_me_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_me',
            name='certifications',
            field=models.TextField(default='none', max_length=200),
        ),
    ]
