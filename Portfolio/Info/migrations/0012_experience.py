# Generated by Django 4.2.2 on 2023-06-22 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info', '0011_remove_about_me_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_of_work', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('period', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experience',
            },
        ),
    ]