# Generated by Django 5.1.2 on 2024-11-03 23:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('calculadora', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libras', models.FloatField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculadora.ingrediente')),
            ],
        ),
    ]
