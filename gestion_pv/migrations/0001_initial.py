# Generated by Django 5.0.7 on 2024-08-08 02:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mag_Emetteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('raison_social', models.CharField(max_length=50)),
                ('type_opposition', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mag_Marche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('marketer', models.CharField(max_length=50)),
                ('reference', models.CharField(max_length=50)),
                ('volume', models.FloatField()),
                ('date_signature', models.DateField()),
                ('signataire', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mag_Marketer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('raison_social', models.CharField(max_length=50)),
                ('bp', models.CharField(max_length=50)),
                ('telephone', models.IntegerField()),
                ('rccm', models.CharField(max_length=50)),
                ('localistion', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Mag_Prelevement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_prel', models.DateField()),
                ('montant_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mag_PV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emission', models.DateField()),
                ('type', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Mag_Opposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('emetteur', models.CharField(max_length=50)),
                ('reference', models.CharField(max_length=50)),
                ('montant', models.IntegerField()),
                ('type_opposition', models.CharField(max_length=50)),
                ('date_emission', models.DateField()),
                ('marketer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_pv.mag_marketer')),
            ],
        ),
        migrations.CreateModel(
            name='Mag_Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_opposition', models.CharField(max_length=50)),
                ('marche', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_pv.mag_marche')),
                ('volume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_pv.mag_opposition')),
            ],
        ),
        migrations.CreateModel(
            name='Mag_Produit_petrolier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150)),
                ('nom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_pv.mag_marche')),
                ('volume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_pv.mag_opposition')),
            ],
        ),
        migrations.CreateModel(
            name='Mag_Volume_attribue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_opposition', models.CharField(max_length=50)),
                ('marche', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_pv.mag_marche')),
                ('volume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_pv.mag_opposition')),
            ],
        ),
        migrations.CreateModel(
            name='Mag_Volume_opposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_credit', models.IntegerField()),
                ('montant_debit', models.IntegerField()),
                ('solde', models.IntegerField()),
                ('emetteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_pv.mag_emetteur')),
                ('marketer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_pv.mag_marketer')),
            ],
        ),
    ]
