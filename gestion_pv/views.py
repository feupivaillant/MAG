from django.shortcuts import redirect, render
from .models import Mag_Marketer, AppelOffre, Produit
from .forms import AppelOffreForm, ProduitForm
from .serializers import Mag_MarketerSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'ges_pv/index.html')

def maketer(request):
    maketer = Mag_Marketer.objects.all()
    return render(request, 'ges_pv/maketer.html', {'maketer' : maketer})

def add_mak(request):
    return render(request, 'ges_pv/add_mak.html')

def appel_offre(request):
    return render(request, 'ges_pv/Appel_offre.html')

def sign_in(request):
    return render(request, 'ges_pv/sign_in.html')

def addrec(request):
    a= request.POST['nom']
    b= request.POST['raison_social']
    c= request.POST['bp']
    d= request.POST['telephone']
    e= request.POST['rccm']
    f= request.POST['localisation']
    g= request.POST['email']

    maketer = Mag_Marketer(nom=a,raison_social=b,bp=c,telephone=d,rccm=e,localistion=f,email=g)
    maketer.save()
    return redirect("/gestion_pv/maketer")

def delete(request,id):
    maketer = Mag_Marketer.objects.get(id=id)
    maketer.delete()
    return redirect("/gestion_pv/maketer")

def update(request,id):
    maketer = Mag_Marketer.objects.get(id=id)
    return render(request, 'ges_pv/update_mak.html', {'maketer' : maketer})

def uprec(request, id):
    a=request.POST['nom']
    b=request.POST['raison_social']
    c= request.POST['bp']
    d= request.POST['telephone']
    e= request.POST['rccm']
    f= request.POST['localisation']
    g= request.POST['email']
    maketer=Mag_Marketer.objects.get(id=id)
    maketer.nom=a
    maketer.raison_social=b
    maketer.bp=c
    maketer.telephone=d
    maketer.rccm=e
    maketer.localistion=f
    maketer.email=g
    maketer.save()
    return redirect("/gestion_pv/maketer")

@csrf_exempt
def enregistrer_appel_offre(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Création de l'objet AppelOffre
            appel_offre = AppelOffre(
                titre=data['lancement']['titre'],
                date_lancement=data['lancement']['date'],
                lots=json.dumps(data['lots']),  # Convertir la liste des lots en JSON
                taux_surestaries=data['surestaries']['taux'],
                devise_surestaries=data['surestaries']['devise'],
                navire_initial_surestaries=data['surestaries']['navireInitial'],
                navire_final_surestaries=data['surestaries']['navireFinal'],
                heures_planches=data['tempsDesPlanches']['heure'],
                shinc=data['tempsDesPlanches']['shinc'],
                lieu_planches=data['tempsDesPlanches']['lieu'],
                navire_initial_planches=data['tempsDesPlanches']['navireInitial'],
                navire_final_planches=data['tempsDesPlanches']['navireFinal'],
                penalite=data['penalite'],
                finalisation=data['finalisation']
            )
            appel_offre.save()
            
            return JsonResponse({'success': True, 'message': 'Appel d\'offre enregistré avec succès'})
        except KeyError as e:
            return JsonResponse({'success': False, 'error': f'Champ manquant: {str(e)}'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Données JSON invalides'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Méthode non autorisée'})

"""class MaketerListCreateView(generics.ListCreateAPIView):
    queryset = Mag_Marketer.objects.all()
    serializer_class = Mag_MarketerSerializer

class MaketerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mag_Marketer.objects.all()
    serializer_class = Mag_MarketerSerializer

class AllMaketerListView(generics.ListAPIView):
    queryset = Mag_Marketer.objects.all()
    serializer_class = Mag_MarketerSerializer

class MaketerUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Mag_Marketer.objects.all()
    serializer_class = Mag_MarketerSerializer
    partial = True

class MaketerDeleteView(generics.DestroyAPIView):
    queryset = Mag_Marketer.objects.all()
    serializer_class = Mag_MarketerSerializer 

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("Maketer supprimer"))"""

