from django.db import models

class Etudiant(models.Model):
    code_etudiant = models.CharField(max_length=20, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_naissance = models.DateField(null=True, blank=True)
    niveau = models.CharField(max_length=50)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom.upper()} {self.prenom.capitalize()} ({self.code_etudiant})"
