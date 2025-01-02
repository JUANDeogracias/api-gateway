# Generated by Django 5.1.4 on 2025-01-02 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('primer_apellido', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Horas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('horas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horas', to='usuarios.usuario')),
            ],
        ),
    ]
