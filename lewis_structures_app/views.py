from lewis_structures_app.models import Molecule
from rest_framework import viewsets, permissions
from lewis_structures_app.serializers import MoleculeSerializer

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class MoleculeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows electrons to be viewed or edited
    """

    queryset = Molecule.objects.all().order_by("molecule_id")
    serializer_class = MoleculeSerializer
    permission_classes = [permissions.IsAuthenticated]
