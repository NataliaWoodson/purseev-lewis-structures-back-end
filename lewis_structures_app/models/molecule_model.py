from django.db import models

class Molecule(models.Model):
    molecule_id = models.BigAutoField(primary_key=True)
    molecular_formula = models.CharField(max_length=50)