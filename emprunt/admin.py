from django.contrib import admin

# Register your models here.
from .models import Enseignant, Budget, Salle, Materiel,Accessoire

admin.site.register(Enseignant)
admin.site.register(Budget)
admin.site.register(Salle)
admin.site.register(Materiel)
admin.site.register(Accessoire)

