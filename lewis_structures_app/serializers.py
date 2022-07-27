# from django.contrib.auth.models import Electron
# , Atom, Molecule
from lewis_structures_app.models import Electron, Atom, Molecule
from rest_framework import serializers

class ElectronSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Electron
        fields = ['electron_id', 'is_paired', 'paired_with', 'atom']

class AtomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Atom
        fields = ['atom_id', 'molecule', 'electrons', 'name']

class MoleculeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Molecule
        fields = ['molecule_id', 'molecular_formula']
