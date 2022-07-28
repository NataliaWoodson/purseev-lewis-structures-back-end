# from django.contrib.auth.models import Electron, Atom, Molecule
from lewis_structures_app.models import Electron, Atom, Molecule
from rest_framework import viewsets, permissions
from lewis_structures_app.serializers import ElectronSerializer, AtomSerializer, MoleculeSerializer
# from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


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

    @csrf_exempt
    def electron_list(request):
        if request.method == 'PATCH':
            data = JSONParser().parse(request)
            serializer = ElectronSerializer(data=data)

            if "bond" in data.keys():
                electrons = Electron.objects.all()
                serializer = ElectronSerializer(electrons, many=True)
                for electron_id in data.electrons:
                    electron = electrons.objects.get(electron_id=electron_id)
                    electron.is_paired = True
                serializer.save()

                return JsonResponse(serializer.data, status=200)
            
            if "unpair" in data.keys():
                electrons = Electron.objects.all()
                serializer = ElectronSerializer(electrons, many=True)
                for electron_id in data.electrons:
                    electron = electrons.objects.get(electron_id=electron_id)
                    electron.is_paired = electron.starting_is_paired
                serializer.save()

                return JsonResponse(serializer.data, status=200)
                


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