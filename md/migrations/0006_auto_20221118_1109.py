# Generated by Django 3.1.6 on 2022-11-18 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('md', '0005_torsionangle'),
    ]

    operations = [
        migrations.AddField(
            model_name='mdtrajectory',
            name='replica',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='torsionangle',
            name='chain',
            field=models.CharField(max_length=2, null=True),
        ),
    ]