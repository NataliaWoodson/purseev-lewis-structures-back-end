# from django.contrib.auth.models import Electron, Atom, Molecule
from lewis_structures_app.models import Electron, Atom, Molecule
from rest_framework import viewsets, permissions
from lewis_structures_app.serializers import MoleculeSerializer

# from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework.response import Response

from django.core import serializers


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class MoleculeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows electrons to be viewed or edited
    """

    queryset = Molecule.objects.all().order_by("molecule_id")
    serializer_class = MoleculeSerializer
    permission_classes = [permissions.IsAuthenticated]
