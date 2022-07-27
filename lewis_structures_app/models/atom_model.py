from django.db import models
from molecule_model import Molecule

class Atom(models.Model):
    atom_id = models.BigAutoField(primary_key=True)
    element_symbol = models.CharField(max_length=2)
    molecule = models.ForeignKey(Molecule, on_delete=models.CASCADE)


    """
    def create_electron_instances(self):
        self.electrons = []

        num_electrons = valence_electrons_by_element[self.element_symbol]
        num_paired_electrons = num_electrons % 4 * 2
        num_unpaired_electrons = num_electrons - num_unpaired_electrons

        for _ in range(num_paired_electrons):
            electron = Electron(is_paired=True, atom=self.atom_id)
            self.electrons.append(electron)

        for _ in range(num_unpaired_electrons):
            electron = Electron(is_paired=False, atom=self.atom_id)
            self.electrons.append(electron)
    """