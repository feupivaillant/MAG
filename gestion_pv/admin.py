from django.contrib import admin
from .models import Mag_Marketer, AppelOffre

class MaketerAdmin(admin.ModelAdmin):
    list_display=('nom','raison_social','bp','telephone','rccm','localistion','email')

admin.site.register(Mag_Marketer,MaketerAdmin)

"""class AppelOffreAdmin(admin.ModelAdmin):
    list_display=('titre','date_lancement','nombre_total_lot','volume_total','numero_lot','quantite_lot','lieu_livraison','taux_surestaries','devise_surestaries','navire_initial_surestaries','navire_final_surestaries','heures_planches','lieu_planches','navire_initial_planches','navire_final_planches','montant_penalite','unité_penalite')

admin.site.register(AppelOffre,AppelOffreAdmin)"""