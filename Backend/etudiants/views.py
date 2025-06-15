from django.shortcuts import render


def accueil(request):
    return render(request, 'index.html')

def accueil_etudiant(request):
    return render(request,'student-login.html')