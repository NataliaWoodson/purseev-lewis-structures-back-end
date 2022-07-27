from django.db import models
from lewis_structures_app.models import Atom
# from chempy.util.parsing import formula_to_composition

# needs argument passed into it
# provide chem formula to the user for display
    # eg: H2O
    # give user a visual
# creates necessary instances of atoms
class Molecule(models.Model):
    molecule_id = models.BigAutoField(primary_key=True)
    molecular_formula = models.CharField(max_length=50)

# is this being given to or by the user
    # if by then must have unfinished
# create : who is creating it and when

# if can call a few at a time and have them saved
# database for info that is frequently modified or added to
# or needs to be searched
    def to_freq_map(self):
        # return formula_to_composition(self.molecular_formula)
        pass
    
    @classmethod
    def create(cls, req_body):
        molecule = cls(
            molecule_formula=req_body["molecular_formula"]
        )
        return molecule
        