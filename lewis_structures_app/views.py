# from django.contrib.auth.models import Electron, Atom, Molecule
from lewis_structures_app.models import Electron, Atom, Molecule
from rest_framework import viewsets, permissions
from lewis_structures_app.serializers import ElectronSerializer, AtomSerializer, MoleculeSerializer
# from django.shortcuts import render
# from django.http import HttpResponse, HttpRequest
# from .models.molecule import Molecule
# from .models.atom import Atom
# from .models.electron import Electron


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def bond(request):
#     '''
#     Request body:
#     {
#     "electrons": [<electron1>,<electron2>]
#     }       
#     '''
#     print(HttpRequest.POST)

class ElectronViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows electrons to be viewed or edited
    """
    queryset = Electron.objects.all().order_by('electron_id')
    serializer_class = ElectronSerializer
    permission_classes = [permissions.IsAuthenticated]

class AtomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows electrons to be viewed or edited
    """
    queryset = Atom.objects.all().order_by('atom_id')
    serializer_class = AtomSerializer
    permission_classes = [permissions.IsAuthenticated]

class MoleculeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows electrons to be viewed or edited
    """
    queryset = Molecule.objects.all().order_by('molecule_id')
    serializer_class = MoleculeSerializer
    permission_classes = [permissions.IsAuthenticated]