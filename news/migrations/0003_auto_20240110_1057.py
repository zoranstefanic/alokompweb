# Generated by Django 3.1.6 on 2024-01-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20240108_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
