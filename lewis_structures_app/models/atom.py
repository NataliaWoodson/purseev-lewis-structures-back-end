from django.db import models
from .electron import Electron

valence_electrons_by_element = {
    "H": 1,
    "B": 3,
    "C": 4,
    "N": 4,
    "N": 5,
    "O": 6,
    "F": 7,
    "Al": 3,
    "Si": 4,
    "P": 5,
    "S": 6,
    "Cl": 7,
}


class Atom(models.Model):
    atom_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10, blank=True)
    element_symbol = models.CharField(max_length=2)
    molecule = models.ForeignKey(
        "lewis_structures_app.Molecule", on_delete=models.CASCADE
    )
    electrons = None

    def self_to_dict(self):
        instance_dict = dict(
            atom_id=self.atom_id,
            element_symbol=self.element_symbol,
            molecule=self.molecule,
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

    def __str__(self):
        return self.element_symbol

    def create_electron_instances(self):
        self.electrons = []

        num_electrons = valence_electrons_by_element[self.element_symbol]

        if num_electrons < 5:
            num_paired_electrons = 0
        else:
            num_paired_electrons = num_electrons % 4 * 2
        num_unpaired_electrons = num_electrons - num_paired_electrons

        for _ in range(num_paired_electrons):
            electron = Electron(is_paired=True, atom=self)
            self.electrons.append(electron)

        for _ in range(num_unpaired_electrons):
            electron = Electron(is_paired=False, atom=self)
            self.electrons.append(electron)

    def all_electrons_bonded(self):
        for electron in self.electrons:
            if electron.is_paired == False:
                return False

        return True
