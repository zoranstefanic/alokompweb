# Generated by Django 3.1.6 on 2023-03-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symmetry', '0003_symmop_pdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symmop',
            name='rot',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='symmop',
            name='trans',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
