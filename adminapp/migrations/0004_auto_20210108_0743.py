# Generated by Django 3.1.2 on 2021-01-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_auto_20210108_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataguru',
            name='kategori',
            field=models.CharField(choices=[('silat', 'silat'), ('renang', 'renang'), ('basket', 'basket'), ('tenis meja', 'tenis meja'), ('voli', 'voli'), ('tenis lapangan', 'tenis lapangan'), ('desain grafis', 'desain grafis'), ('memasak', 'memasak')], max_length=100, null=True),
        ),
    ]