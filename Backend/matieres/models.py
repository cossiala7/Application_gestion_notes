from django.db import models

# Create your models here.
from django.db import models

class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    coefficient = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nom} ({self.code})"
