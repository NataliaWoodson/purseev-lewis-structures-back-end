from django.contrib import admin

# Register your models here.

from .models import Molecule, Atom, Electron

admin.site.register(Molecule)
admin.site.register(Atom)
admin.site.register(Electron)
