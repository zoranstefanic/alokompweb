# Generated by Django 3.1.6 on 2022-07-10 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pdbase', '0003_pdb_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qscore', models.FloatField()),
                ('rmsd', models.FloatField()),
                ('aligned_num', models.IntegerField()),
                ('seq_identity', models.FloatField()),
                ('chain_fixed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alignments_fixed', to='pdbase.chain')),
                ('chain_moving', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alignments_moving', to='pdbase.chain')),
            ],
        ),
        migrations.CreateModel(
            name='ResidueMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('text', models.CharField(max_length=50)),
                ('distance', models.FloatField(null=True)),
                ('similarity', models.IntegerField(null=True)),
                ('ss_fixed', models.CharField(choices=[('H', 'helix'), ('S', 'sheet')], max_length=1, null=True)),
                ('ss_moving', models.CharField(choices=[('H', 'helix'), ('S', 'sheet')], max_length=1, null=True)),
                ('h_fixed', models.CharField(choices=[('-', 'hydrophobic'), ('+', 'hydrophylic'), ('.', 'neutral')], max_length=1, null=True)),
                ('h_moving', models.CharField(choices=[('-', 'hydrophobic'), ('+', 'hydrophylic'), ('.', 'neutral')], max_length=1, null=True)),
                ('alignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='alignments.alignment')),
                ('fixed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches_fixed', to='pdbase.residue')),
                ('moving', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches_moving', to='pdbase.residue')),
            ],
        ),
    ]