# Generated by Django 3.2.7 on 2022-04-04 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fastqc',
            fields=[
                ('index', models.BigIntegerField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('patient_id', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('sequence', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('sample_type', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('path_name', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('basic_statistics', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('per_base_sequence_quality', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('per_tile_sequence_quality', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('per_sequence_quality_scores', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('Per_base_sequence_content', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('per_sequence_gc_content', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('per_base_n_content', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('sequence_length_distribution', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('sequence_duplication_levels', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('overrepresented_sequences', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('adapter_content', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('sample_name', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('true_sequence', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('flowcell', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('lane', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('row', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('total_sequences', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('sequence_length', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('GC', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('multiqc_report', models.FileField(max_length=3000, null=True, upload_to='media')),
                ('fastqc_report', models.FileField(max_length=3000, null=True, upload_to='media')),
            ],
        ),
    ]
