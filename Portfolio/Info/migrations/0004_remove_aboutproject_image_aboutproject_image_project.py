# Generated by Django 4.2.2 on 2023-06-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info', '0003_aboutproject_image_aboutproject_technology'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutproject',
            name='image',
        ),
        migrations.AddField(
            model_name='aboutproject',
            name='image_project',
            field=models.ImageField(default='img/default.png', upload_to='img'),
        ),
    ]
