# Generated by Django 2.2.12 on 2022-11-25 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_jeniss_minuman'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minuman',
            name='jenis_id',
        ),
        migrations.AddField(
            model_name='barang',
            name='link_gbr',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='minuman',
            name='jeniss_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.jeniss'),
        ),
        migrations.AddField(
            model_name='minuman',
            name='link_gbr',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='barang',
            name='jenis_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.jenis'),
        ),
    ]
