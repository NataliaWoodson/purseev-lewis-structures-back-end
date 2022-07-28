# from django.contrib.auth.models import Electron, Atom, Molecule
from lewis_structures_app.models import Electron, Atom, Molecule
from rest_framework import viewsets, permissions
from lewis_structures_app.serializers import (
    ElectronSerializer,
    AtomSerializer,
    MoleculeSerializer,
)

# from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework.response import Response


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


# def bond(request):
#     return HttpResponse("inside bond view")
    # if request.method == 'PATCH':
    #     # return HttpResponse('<h1>inside bond view</h1>') 
    #     data = JSONParser().parse(request)
    #     for electron_id in data.electrons:
    #         electron = Electron.objects.get(electron_id=electron_id)
    #         electron.is_paired = True
    #     return HttpResponse("Successfully bonded electrons")


class ElectronViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows electrons to be viewed or edited
    """

    queryset = Electron.objects.all().order_by("electron_id")
    serializer_class = ElectronSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['patch'])
    def bond(self, request, pk=None):
        data = JSONParser().parse(request)
        electron = self.get_object()
        serializer = ElectronSerializer(data=data)
        
        if serializer.is_valid():
            if data["is_paired"] == True:
                electron.is_paired = False
                electron.save()
            else:
                electron.is_paired = True
                electron.save()
        # else:
        #     return Response(serializer.errors,
        #                     status=status.HTTP_400_BAD_REQUEST)
        new_data = {
            "electron_id":electron.electron_id,
            "is_paired":electron.is_paired
        }
        return Response(new_data)

        

        # data = JSONParser().parse(request)
        # for electron_id in data["electrons"]:
        #     electron = Electron.objects.get(electron_id=electron_id)
        #     electron.is_paired = True
        #     Electron.save(electron)
        
        # return HttpResponse("Successfully bonded electrons")
        # return Response("in bond function")


    # def partial_update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)

    # @csrf_exempt
    # def patch(self, request, *args, **kwargs):
    #     kwargs["partial"] = True
    #     # if request.method == 'PATCH':
    #     data = JSONParser().parse(request)
    #     serializer = ElectronSerializer(data=data)

    #     if data.action == "bond":
    #         electrons = Electron.objects.all()
    #         serializer = ElectronSerializer(electrons, many=True)
    #         for electron_id in data.electrons:
    #             electron = electrons.objects.get(electron_id=electron_id)
    #             electron.is_paired = True
    #         serializer.save()

    #         return JsonResponse(serializer.data, status=200)

    #     if data.action == "unpair":
    #         electrons = Electron.objects.all()
    #         serializer = ElectronSerializer(electrons, many=True)
    #         for electron_id in data.electrons:
    #             electron = electrons.objects.get(electron_id=electron_id)
    #             electron.is_paired = electron.starting_is_paired
    #         serializer.save()

    #         return JsonResponse(serializer.data, status=200)


class AtomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows electrons to be viewed or edited
    """

    queryset = Atom.objects.all().order_by("atom_id")
    serializer_class = AtomSerializer
    permission_classes = [permissions.IsAuthenticated]


class MoleculeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows electrons to be viewed or edited
    """

    queryset = Molecule.objects.all().order_by("molecule_id")
    serializer_class = MoleculeSerializer
    permission_classes = [permissions.IsAuthenticated]
