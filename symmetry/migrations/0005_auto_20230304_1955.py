# Generated by Django 3.1.6 on 2023-03-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symmetry', '0004_auto_20230304_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symmop',
            name='rot',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='symmop',
            name='trans',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
