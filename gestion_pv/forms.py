from django import forms
from .models import AppelOffre, Produit

class AppelOffreForm(forms.ModelForm):
    class Meta:
        model = AppelOffre
        fields = '__all__'

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'
