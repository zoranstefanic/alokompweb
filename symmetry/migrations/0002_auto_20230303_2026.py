# Generated by Django 3.1.6 on 2023-03-03 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('symmetry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='symop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='symmetry.symmop'),
        ),
    ]