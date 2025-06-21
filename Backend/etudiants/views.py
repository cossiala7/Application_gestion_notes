<<<<<<< HEAD
from django.shortcuts import render

=======
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Etudiant
from notes.models import Note
from matieres.models import Matiere  # Importez votre modèle Etudiant
from django.utils import timezone
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
>>>>>>> 7cc894827e96518a722427114b6f7e10ca1a40bc

def accueil(request):
    return render(request, 'index.html')

<<<<<<< HEAD
def accueil_etudiant(request):
    return render(request,'student-login.html')
=======
def etudiant_login(request):
    # Si l'utilisateur est déjà connecté, redirigez-le vers le dashboard
    #if 'student_id' in request.session:
    #    return redirect('etudiant_dashboard')
    
    if request.method == 'POST':
        code_etudiant = request.POST.get('etudiant_code_etudiant', '').strip()
        
        # Validation de base
        if not code_etudiant:
            messages.error(request, "Le code étudiant est requis.")
            return render(request, 'student-login.html')
        
        try:
            etudiant = Etudiant.objects.get(code_etudiant=code_etudiant)
            
            # Stockage minimal dans la session
            request.session['student_id'] = etudiant.id
            request.session['student_name'] = f"{etudiant.prenom} {etudiant.nom}"
            
            # Message de bienvenue personnalisé
            messages.success(request, f"Bienvenue {etudiant.prenom} !")
            
            # Redirection sécurisée
            next_url = request.POST.get('next', 'etudiant_dashboard')
            return redirect(next_url)
            
        except Etudiant.DoesNotExist:
            messages.error(request, "Code étudiant incorrect. Veuillez réessayer.")
            # Ne pas révéler que le code n'existe pas pour des raisons de sécurité
            return render(request, 'student-login.html')
        
        except Exception as e:
            # Loguer l'erreur en production (vous pouvez utiliser logging)
            messages.error(request, "Une erreur s'est produite lors de la connexion.")
            return render(request, 'student-login.html')
    
    # Gestion du paramètre 'next' pour la redirection après login
    context = {}
    if 'next' in request.GET:
        context['next'] = request.GET['next']
    
    return render(request, 'student-login.html', context)

def etudiant_register(request):
    if request.method == 'POST':
        # Récupération des données du formulaire
        code_etudiant = request.POST.get('code_etudiant')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        date_naissance = request.POST.get('date_naissance')

        # Validation des données
        if not all([code_etudiant, nom, prenom, email, date_naissance]):
            messages.error(request, 'Tous les champs sont obligatoires.')
            return redirect('etudiant_register')

        # Vérification si l'étudiant existe déjà
        if Etudiant.objects.filter(code_etudiant=code_etudiant).exists():
            messages.error(request, 'Un étudiant avec ce code existe déjà.')
            return redirect('etudiant_register')

        try:
            # Création du nouvel étudiant
            nouvel_etudiant = Etudiant(
                code_etudiant=code_etudiant,
                nom=nom,
                prenom=prenom,
                email=email,
                date_naissance=date_naissance,
                date_inscription=timezone.now()
            )
            nouvel_etudiant.save()

            messages.success(request, 'Inscription réussie! Vous pouvez maintenant vous connecter.')
            return redirect('etudiant_login')
            
        except Exception as e:
            messages.error(request, f"Une erreur s'est produite lors de l'inscription: {str(e)}")
            return redirect('etudiant_register')

    return render(request, 'register.html')

def etudiant_logout(request):    
    if 'student_id' in request.session:
        del request.session['student_id']
        del request.session['student_name']
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('accueil')

@login_required
def etudiant_dashboard(request):
    return render(request, 'student-dashboard.html')



"""def student_dashboard(request):
    # Récupérer l'étudiant connecté
    student = request.user.student
    
    # Récupérer les données nécessaires
    subjects = Matiere.objects.filter(student=student)
    
    
    # Calculer les statistiques
    validated_subjects = subjects.filter(status='validated').count()
    failed_subjects = subjects.filter(status='failed').count()
    total_subjects = subjects.count()
    
    # Calculer la moyenne générale (exemple simplifié)
    general_average = sum(grade.score * grade.subject.coefficient for grade in grades) / sum(grade.subject.coefficient for grade in grades) if grades else 0
    
    # Préparer les données pour le graphique
    semesters = ['Semestre 1', 'Semestre 2', 'Semestre 3', 'Semestre 4']
    semester_averages = [12.5, 13.2, 14.1, general_average]  # Ici vous devriez calculer les moyennes par semestre
    
    context = {
        'student': student,
        'subjects': subjects,
        'validated_subjects': validated_subjects,
        'failed_subjects': failed_subjects,
        'total_subjects': total_subjects,
        'general_average': round(general_average, 2),
        'semesters': semesters,
        'semester_averages': semester_averages,
    }
    
    return render(request, 'student-dashboard.html', context)"""
>>>>>>> 7cc894827e96518a722427114b6f7e10ca1a40bc
