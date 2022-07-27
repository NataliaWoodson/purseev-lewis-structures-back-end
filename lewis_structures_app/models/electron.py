from operator import mod
from django.db import models


class Electron(models.Model):
    electron_id = models.BigAutoField(primary_key=True)
    is_paired = models.BooleanField(default=False)
    atom = models.ForeignKey("lewis_structures_app.Atom", on_delete=models.CASCADE)
    # front end may be able to handle this:
    # bonded_to = models.IntegerField("Electron id bonded to")

    def self_to_dict(self):
        instance_dict = dict(
            electron_id=self.electron_id,
            is_paired=self.is_paired,
            atom=self.atom,
        )

        return instance_dict

    def __str__(self):
        return str(self.electron_id)
