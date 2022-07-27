from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models.molecule import Molecule
from .models.atom import Atom
from .models.electron import Electron


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def bond(request):
    '''
    Request body:
    {
    "electrons": [<electron1>,<electron2>]
    }       
    '''
    print(HttpRequest.POST)