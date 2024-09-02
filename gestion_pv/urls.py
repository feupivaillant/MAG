from django.urls import path
from . import views
#from .views import MaketerListCreateView, MaketerDetailView, MaketerDeleteView, MaketerUpdateView, AllMaketerListView

urlpatterns = [
    path('index/', views.index, name='index'),
    path('maketer/', views.maketer, name='maketer'),
    path('add_mak/', views.add_mak, name='add_mak'),
    path('appel_offre/', views.appel_offre, name='appel_offre'),
    path('sign_in/', views.sign_in_view, name='sign_in'),
    path("addrec/", views.addrec, name="addrec"),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update_mak/<int:id>/',views.update,name='update'),
    path('update_mak/uprec/<int:id>/',views.uprec,name='uprec'),
    path('enregistrer-appel-offre/', views.enregistrer_appel_offre, name='enregistrer_appel_offre'),

    #path('update_mak/', views.update_mak, name='update_mak'),
    #path('maketer/', MaketerListCreateView.as_view,  name='maketer_list_create'),
    #path('Maketer/<int:pk>', MaketerDetailView.as_view(), name='maketer_detail'),
    #path('Maketer/all/', AllMaketerListView.as_view(), name='all_maketer_list'),
    #path('Maketer/delete/<int:pk>', MaketerDeleteView.as_view(), name='maketer_delete'),
    #path('Maketer/update/<int:pk>', MaketerUpdateView.as_view(), name='maketer_update'),
]
