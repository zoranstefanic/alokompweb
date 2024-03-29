# Generated by Django 3.1.6 on 2022-11-02 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workplan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='end',
        ),
        migrations.RemoveField(
            model_name='item',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='item',
            name='start',
        ),
        migrations.RemoveField(
            model_name='item',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='item',
            name='who',
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('O', 'Objective'), ('A', 'Activity'), ('M', 'Milestone'), ('D', 'Deliverable')], max_length=10),
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.IntegerField(choices=[('1', 'General'), ('2', 'Equipment'), ('3', 'Disemination'), ('4', 'Doctoral')], default=1)),
                ('start', models.DateField(null=True)),
                ('end', models.DateField(null=True)),
                ('users', models.ManyToManyField(related_name='workplan_items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='workplan.period'),
        ),
    ]
