from django.test import TestCase
from .models import Esta_en_Examen
from .models import Pregunta
from .models import Examen
# Create your tests here.

class pruebas_generales(TestCase):
    def test(self):
        guar = Esta_en_Examen.objects.create(id_Examen=8,id_Pregunta=1,numero_pregunta=1)
        guar.save()
        sol = Examen.objects.filter(pk=guar.id_Examen).soluciones
        print("->->->->-->",sol)
        self.assertEqual(guar.id_Pregunta,1)
