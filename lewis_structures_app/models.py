from django.db import models

class Molecule(models.Model):
    molecule_id = models.BigAutoField(primary_key=True)
    molecular_formula = models.CharField(max_length=50)

class Atom(models.Model):
    atom_id = models.BigAutoField(primary_key=True)
    element_symbol = models.CharField(max_length=2)
    molecule = models.ForeignKey(Molecule, on_delete=models.CASCADE)

class Electron(models.Model):
    electron_id = models.BigAutoField(primary_key=True)
    is_paired = models.BooleanField(default=False)
    atom = models.ForeignKey(Atom, on_delete=models.CASCADE)
    # front end may be able to handle this:
    # bonded_to = models.IntegerField("Electron id bonded to")
