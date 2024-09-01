from django.db import models

# Create your models here.
class Mag_Marketer(models.Model):
    nom = models.CharField(max_length = 50)
    raison_social = models.CharField(max_length = 50)
    bp = models.CharField(max_length=50)
    telephone = models.IntegerField()
    rccm = models.CharField(max_length=50)
    localistion = models.CharField(max_length=50)
    email = models.EmailField()

class Mag_Marche(models.Model):
    nom = models.CharField(max_length = 50)
    marketer = models.CharField(max_length = 50)
    reference = models.CharField(max_length=50)
    volume = models.FloatField()
    date_signature = models.DateField()
    signataire = models.CharField(max_length=50)


class Mag_Opposition(models.Model):
    nom = models.CharField(max_length = 50)
    marketer = models.ForeignKey(Mag_Marketer, on_delete = models.CASCADE)
    emetteur = models.CharField(max_length=50)
    reference = models.CharField(max_length=50)
    montant = models.IntegerField()
    type_opposition = models.CharField(max_length=50)
    date_emission = models.DateField()
    
class Mag_Emetteur(models.Model):
    nom = models.CharField(max_length = 50)
    raison_social = models.CharField(max_length = 50)
    type_opposition = models.CharField(max_length=50)
    email = models.EmailField()
    telephone = models.IntegerField()

class Mag_Volume_opposition(models.Model):
    marketer = models.ForeignKey(Mag_Marketer, on_delete = models.CASCADE)
    emetteur = models.ForeignKey(Mag_Emetteur, on_delete = models.CASCADE)
    montant_credit = models.IntegerField()
    montant_debit = models.IntegerField()
    solde = models.IntegerField()

class Mag_Operation(models.Model):
    marche = models.ForeignKey(Mag_Marche, on_delete = models.CASCADE)
    type_opposition = models.CharField(max_length=50)
    volume = models.ForeignKey(Mag_Opposition, on_delete = models.CASCADE)

class Mag_Volume_attribue(models.Model):
    marche = models.ForeignKey(Mag_Marche, on_delete = models.CASCADE)
    type_opposition = models.CharField(max_length=50)
    volume = models.ForeignKey(Mag_Opposition, on_delete = models.CASCADE)

class Mag_Produit_petrolier(models.Model):
    nom = models.ForeignKey(Mag_Marche, on_delete = models.CASCADE)
    type = models.CharField(max_length=150)
    volume = models.ForeignKey(Mag_Opposition, on_delete = models.CASCADE)

class Mag_PV(models.Model):
    date_emission = models.DateField()
    type = models.CharField(max_length=150)

class Mag_Prelevement(models.Model):
    date_prel = models.DateField()
    montant_total = models.IntegerField()

class AppelOffre(models.Model):
    # Champs pour la section Lancement
    titre = models.CharField(max_length=200)
    date_lancement = models.DateField()
    nombre_total_lot = models.IntegerField()
    volume_total = models.IntegerField()

    # Champs pour la section Lots
    lots = models.JSONField()

    # Champs pour la section Surestaries
    taux_surestaries = models.FloatField()
    devise_surestaries = models.CharField(max_length=3)
    navire_initial_surestaries = models.CharField(max_length=100)
    navire_final_surestaries = models.CharField(max_length=100)

    # Champs pour la section Temps de planches
    heures_planches = models.IntegerField()
    lieu_planches = models.CharField(max_length=100)
    navire_initial_planches = models.CharField(max_length=100)
    navire_final_planches = models.CharField(max_length=100)

    # Champs pour la section Pénalité
    montant_penalite = models.IntegerField()
    unité_penalite = models.CharField(max_length=100)

    def __str__(self):
        return self.titre


class Produit(models.Model):
    appel_offre = models.ForeignKey(AppelOffre, on_delete=models.CASCADE, related_name='produits')
    nom_produit = models.CharField(max_length=255)
    quantite = models.DecimalField(max_digits=10, decimal_places=2)
    lieu = models.CharField(max_length=255)
