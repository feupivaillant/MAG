from rest_framework import serializers
from .models import Mag_Emetteur, Mag_Marche, Mag_Marketer, Mag_Operation, Mag_Opposition, Mag_Prelevement, Mag_Produit_petrolier, Mag_PV,Mag_Volume_attribue,Mag_Volume_opposition

class Mag_MarketerSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Mag_Marketer
        fields = '__all__'