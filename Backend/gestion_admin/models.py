from django.db import models
from django.contrib.auth.models import User

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
    def moyenne_generale(self):
        moyenne = Note.objects.filter(etudiant=self).aggregate(models.Avg('note'))['note__avg']
        return moyenne if moyenne is not None else None


class Matiere(models.Model):
    code_matiere = models.CharField(max_length=20, unique=True)
    nom = models.CharField(max_length=100)
    coefficient = models.IntegerField(default=1)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom


class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=4, decimal_places=2)
    date_evaluation = models.DateField(auto_now_add=True)
    commentaire = models.TextField(blank=True)

    def __str__(self):
        return f"{self.etudiant} - {self.matiere} : {self.note}"

    class Meta:
        unique_together = ('etudiant', 'matiere')