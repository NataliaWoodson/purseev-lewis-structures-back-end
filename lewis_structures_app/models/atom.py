from django.db import models 
from .molecule import Molecule

class Atom(models.Model):
    atom_id = models.BigAutoField(primary_key=True)
    element_symbol = models.CharField(max_length=2)
    molecule = models.ForeignKey(Molecule, on_delete=models.CASCADE)

    def self_to_dict(self):
        instance_dict = dict(
            atom_id=self.atom_id,
            element_symbol=self.element_symbol,
            molecule=self.molecule
        )

        return instance_dict

    def update_self(self, data_dict):
        dict_key_errors = []
        for key in data_dict.keys():
            if hasattr(self, key):
                setattr(self, key, data_dict[key])
            else:
                dict_key_errors.append(key)
        if dict_key_errors:
            raise ValueError(dict_key_errors)