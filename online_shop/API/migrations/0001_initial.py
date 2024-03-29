# Generated by Django 5.0.3 on 2024-03-08 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qty', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.material')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.product')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveBigIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.material')),
            ],
        ),
    ]
