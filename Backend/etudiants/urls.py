from django.urls import path
from . import views 

urlpatterns = [
    path('', views.accueil, name = 'accueil'),
    path('etudiant/login/', views.etudiant_login, name = 'etudiant_login'),
    path('etudiant/register/', views.etudiant_register, name='etudiant_register'),
    path('etudiant/dashboard/', views.etudiant_dashboard, name='etudiant_dashboard'),
    path('etudiant/logout/', views.etudiant_logout, name='etudiant_logout'),
    

]