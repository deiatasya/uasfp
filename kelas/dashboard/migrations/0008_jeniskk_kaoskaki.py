# Generated by Django 4.1.2 on 2023-02-02 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_rename_kodepkn_pakaian_kodepakaian'),
    ]

    operations = [
        migrations.CreateModel(
            name='jeniskk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('ket', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='kaoskaki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodekaoskaki', models.CharField(max_length=8)),
                ('nama', models.CharField(max_length=50)),
                ('stok', models.IntegerField()),
                ('harga', models.BigIntegerField()),
                ('link_gbr', models.CharField(blank=True, max_length=150)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('jeniskk_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.jeniskk')),
            ],
        ),
    ]
