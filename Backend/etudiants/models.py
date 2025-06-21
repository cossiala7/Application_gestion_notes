from django.db import models
from django.db.models import Avg


class Etudiant(models.Model):
    CLASS_CHOICES = [
        ('L1', 'Licence 1'),
        ('L2', 'Licence 2'),
        ('L3', 'Licence 3'),
        ('M1', 'Master 1'),
        ('M2', 'Master 2'),
    ]
    code_etudiant = models.CharField(max_length=20, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    classe = models.CharField(max_length=2, choices=CLASS_CHOICES, blank=True, null=True)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.code_etudiant})"

@property
def nom_complet(self):
    return f"{self.prenom} {self.nom}"

@property
def moyenne(self):
    from django.db.models import Avg
    avg = self.notes.aggregate(Avg('valeur'))['valeur__avg']
    return f"{avg:.2f}" if avg else None    
