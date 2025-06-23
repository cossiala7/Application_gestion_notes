from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from etudiants.models import Etudiant
from matieres.models import Matiere
from notes.models import Note
from django.db.models import Avg, Q

def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('admin_username')
        password = request.POST.get('admin_password')
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None and user.is_superuser:
            auth.login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Identifiants incorrects ou vous n'avez pas les droits administrateur.")
    
    return render(request, 'admin-login.html')


def admin_logout(request):
    auth.logout(request)
    messages.success(request, "Déconnexion réussie.")
    return redirect('accueil')

def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('accueil')
    
    stats = {
        'total_etudiants': Etudiant.objects.count(),
        'total_matieres': Matiere.objects.count(),
        'total_notes': Note.objects.count(),
        'taux_reussite': Note.objects.filter(note__gte=10).count() / Note.objects.count() * 100 if Note.objects.count() > 0 else 0,
    }
    return render(request, 'admin-dashboard.html', stats)


def admin_students(request):
    if not request.user.is_superuser:
        return redirect('accueil')
    
    etudiants = Etudiant.objects.all().order_by('nom')
    
    # Filtrage
    if classe := request.GET.get('classe'):
        etudiants = etudiants.filter(classe=classe)
    
    # Recherche
    if search := request.GET.get('search'):
        etudiants = etudiants.filter(
            Q(nom__icontains=search) | 
            Q(prenom__icontains=search) |
            Q(code_etudiant__icontains=search)
        )
    
    return render(request, 'gestion_admin/admin-students.html', {
        'etudiants': etudiants,
        'classe_filter': request.GET.get('classe', ''),
        'search_term': request.GET.get('search', ''),
    })


def student_crud(request, student_id=None):
    if not request.user.is_superuser:
        return redirect('accueil')
    
    if student_id:
        etudiant = get_object_or_404(Etudiant, id=student_id)
    else:
        etudiant = None
    
    if request.method == 'POST':
        data = {
            'code_etudiant': request.POST.get('code_etudiant'),
            'nom': request.POST.get('nom'),
            'prenom': request.POST.get('prenom'),
            'email': request.POST.get('email'),
            'date_naissance': request.POST.get('date_naissance'),
            'classe': request.POST.get('classe'),
        }
        
        try:
            if etudiant:  # Modification
                for key, value in data.items():
                    setattr(etudiant, key, value)
                etudiant.save()
                msg = "Étudiant modifié avec succès!"
            else:  # Création
                Etudiant.objects.create(**data)
                msg = "Étudiant créé avec succès!"
            
            messages.success(request, msg)
            return redirect('admin_students')
        
        except Exception as e:
            messages.error(request, f"Erreur: {str(e)}")
    
    return render(request, 'gestion_admin/student-form.html', {
        'etudiant': etudiant,
        'classes': Etudiant.CLASS_CHOICES if hasattr(Etudiant, 'CLASS_CHOICES') else [],
    })


def delete_student(request, student_id):
    if not request.user.is_superuser:
        return redirect('accueil')
    
    etudiant = get_object_or_404(Etudiant, id=student_id)
    etudiant.delete()
    messages.success(request, "Étudiant supprimé avec succès!")
    return redirect('admin_students')
