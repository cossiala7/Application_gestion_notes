from django.urls import path
from . import views 

urlpatterns = [
    path('', views.accueil, name = 'accueil'),
    path('etudiants/', views.accueil_etudiant, name = 'accueil_etudiant'),

]