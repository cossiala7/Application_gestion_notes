from django.shortcuts import render, get_object_or_404, redirect
from .models import Matiere
from .forms import MatiereForm

# Vue pour lister les matières
def liste_matieres(request):
    matieres = Matiere.objects.all()
    return render(request, 'matieres/liste_matieres.html', {'matieres': matieres})

# Vue pour ajouter une matière
def ajouter_matiere(request):
    if request.method == 'POST':
        form = MatiereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_matieres')
    else:
        form = MatiereForm()
    return render(request, 'matieres/ajouter_matiere.html', {'form': form})

# Vue pour modifier une matière
def modifier_matiere(request, pk):
    matiere = get_object_or_404(Matiere, pk=pk)
    if request.method == 'POST':
        form = MatiereForm(request.POST, instance=matiere)
        if form.is_valid():
            form.save()
            return redirect('liste_matieres')
    else:
        form = MatiereForm(instance=matiere)
    return render(request, 'matieres/modifier_matiere.html', {'form': form, 'matiere': matiere})

# Vue pour supprimer une matière
def supprimer_matiere(request, pk):
    matiere = get_object_or_404(Matiere, pk=pk)
    if request.method == 'POST':
        matiere.delete()
        return redirect('liste_matieres')
    return render(request, 'matieres/supprimer_matiere.html', {'matiere': matiere})
