from django.db import models


class Molecule(models.Model):
    molecule_id = models.BigAutoField(primary_key=True)
    molecular_formula = models.CharField(max_length=50)

    def __str__(self):
        return self.molecular_formula
