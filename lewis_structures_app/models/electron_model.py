from django.db import models
from atom_model import Atom

class Electron(models.Model):
    electron_id = models.BigAutoField(primary_key=True)
    is_paired = models.BooleanField(default=False)
    atom = models.ForeignKey(Atom, on_delete=models.CASCADE)
    # front end may be able to handle this:
    # bonded_to = models.IntegerField("Electron id bonded to")