# Generated by Django 4.1.2 on 2023-02-02 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20221126_0518'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='minuman',
            new_name='pakaian',
        ),
        migrations.RenameField(
            model_name='pakaian',
            old_name='kodemnm',
            new_name='kodepkn',
        ),
    ]
