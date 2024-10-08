# Generated by Django 5.0.7 on 2024-08-30 04:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_pv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppelOffre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('date_lancement', models.DateField()),
                ('nombre_total_lot', models.IntegerField()),
                ('volume_total', models.IntegerField()),
                ('numero_lot', models.JSONField()),
                ('quantite_lot', models.FloatField()),
                ('lieu_livraison', models.CharField(max_length=100)),
                ('taux_surestaries', models.FloatField()),
                ('devise_surestaries', models.CharField(max_length=3)),
                ('navire_initial_surestaries', models.CharField(max_length=100)),
                ('navire_final_surestaries', models.CharField(max_length=100)),
                ('heures_planches', models.IntegerField()),
                ('lieu_planches', models.CharField(max_length=100)),
                ('navire_initial_planches', models.CharField(max_length=100)),
                ('navire_final_planches', models.CharField(max_length=100)),
                ('montant_penalite', models.IntegerField()),
                ('unité_penalite', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_produit', models.CharField(max_length=255)),
                ('quantite', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lieu', models.CharField(max_length=255)),
                ('appel_offre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='gestion_pv.appeloffre')),
            ],
        ),
    ]
