from django.db import models

# Create your models here.
from django.db import models
from etudiants.models import Etudiant
from matieres.models import Matiere

class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='notes')
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.etudiant} - {self.matiere} : {self.note}"
