from django.contrib import admin

# Register your models here.

from .models import Molecule

admin.site.register(Molecule)
