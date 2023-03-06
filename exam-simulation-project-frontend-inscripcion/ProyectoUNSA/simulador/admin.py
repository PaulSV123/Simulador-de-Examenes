from django.contrib import admin
from .models import Postulante, Examen, Escuela, Area, Examen_Postulante

@admin.register(Postulante)
class PostulanteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio', 'web', 'Numero_Examenes', 'Telefono', 'DNI')

admin.site.register(Escuela)
admin.site.register(Area)
admin.site.register(Examen_Postulante)
admin.site.register(Examen)