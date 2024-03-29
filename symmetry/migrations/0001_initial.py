# Generated by Django 3.1.6 on 2023-03-03 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pdbase', '0005_auto_20230303_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='SymmOp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rot', models.CharField(max_length=20)),
                ('trans', models.CharField(max_length=20)),
                ('geom', models.CharField(help_text='Geometric interpretation', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnitCell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('params', models.JSONField(null=True)),
                ('sg', models.CharField(max_length=10)),
                ('num', models.IntegerField()),
                ('pdb', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='unit_cell', to='pdbase.pdb')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d', models.FloatField()),
                ('prob', models.CharField(max_length=3)),
                ('from_atom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts_from', to='pdbase.atom')),
                ('symop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='symmetry.symmop')),
                ('to_atom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts_to', to='pdbase.atom')),
            ],
        ),
    ]
