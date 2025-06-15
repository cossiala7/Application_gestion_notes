from django.shortcuts import render

def accueil_admin(request):
    return render(request, 'admin-login.html')

def admin_dashboard(request):
    return render(request, 'admin-dashboard.html')