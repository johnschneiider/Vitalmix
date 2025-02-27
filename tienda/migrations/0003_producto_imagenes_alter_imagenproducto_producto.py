# Generated by Django 5.1.2 on 2024-11-11 00:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_imagenproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagenes',
            field=models.ImageField(default=1, upload_to='productos/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagenproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_del_producto', to='tienda.producto'),
        ),
    ]
