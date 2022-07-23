from django.db import models
from molecule_model import Molecule

class Atom(models.Model):
    atom_id = models.BigAutoField(primary_key=True)
    element_symbol = models.CharField(max_length=2)
    molecule = models.ForeignKey(Molecule, on_delete=models.CASCADE)