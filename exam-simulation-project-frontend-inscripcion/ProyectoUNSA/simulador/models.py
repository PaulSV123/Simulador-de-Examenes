from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
#SPRINT 1
class Postulante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    web = models.URLField(blank=True)
    Numero_Examenes = models.IntegerField(default=0)
    Telefono = models.IntegerField(validators=[MaxValueValidator(999999999)], default=954347604)
    DNI = models.IntegerField(validators=[MaxValueValidator(99999999)], default=77777777)

    # Python 3
    def __str__(self):
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_postulante(sender, instance, created, **kwargs):
    if created:
        Postulante.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_postulante(sender, instance, **kwargs):
    instance.postulante.save()

#SPRINT 1
GEEKS_CHOICES =[
    ("O", "Ordinario"),
    ("C", "CEPRUNSA"),
    ("E", "Extraordinario"),
]
class Examen(models.Model):
    Tipo = models.CharField(max_length=100, choices=GEEKS_CHOICES, default='O')
    Fecha_Examen = models.DateTimeField(blank=False,null=False)
    Fecha_Resultados = models.DateTimeField(default=None,blank=True,null=True)
    Duracion = models.TimeField(default=0,blank=True,null=False)
    Estado = models.BooleanField(default=True)
    Nmro_Preguntas = models.IntegerField(default=80)
    soluciones = models.TextField(default="000000000000000000000000000000000000000000000000000000000000000000000000000000000")
    def __str__(self):
        return str(self.id)

class Area(models.Model):
    Nombre = models.CharField(max_length = 100, blank=True)
    def __str__(self):
        return self.Nombre

class Escuela(models.Model):
    Nombre = models.CharField(max_length = 100, blank=True)
    Vacantes = models.IntegerField()
    Area_id = models.ForeignKey(Area, on_delete=models.CASCADE, blank=False, null=False)
    def __str__(self):
        return self.Nombre

class Solucionario(models.Model):
    respuestas = models.TextField(default="000000000000000000000000000000000000000000000000000000000000000000000000000000000",blank=True,null=False)
    def save(self,*args,**kwargs):
        if Solucionario.objects.filter(pk=1).exists():
            #max_id = Solucionario.objects.all().order_by("-id")[0]
            conta = 1
            while Solucionario.objects.filter(pk=conta).exists():
                conta = conta +1
            self.id = conta
            #self.id=max_id.pk+1
        return super(Solucionario, self).save( *args, **kwargs)
    def act(self,sol,pos,*args,**kwargs):
        print("######################")
        solucion = self.respuestas
        print("######################")
        print(solucion)
        txt = ""
        for c in range(len(solucion)):
            if c == int(pos):
                txt = txt + str(sol)
                print(str(sol))
            else:
                txt = txt + solucion[c]
        print("######################")
        solucion = txt
        print("######################")
        print(solucion)
        EX = Solucionario.objects.filter(pk = self.pk).update(respuestas = solucion)
        self.respuestas = solucion
        #EX = Examen.objects.filter(pk=self.id_Examen.id).update(soluciones = solucion)
        return super(Solucionario, self).save( *args, **kwargs)


class Examen_Postulante(models.Model):
    Examen_id = models.ForeignKey(Examen, on_delete=models.CASCADE, blank=False, null=False)
    Postulante_id = models.ForeignKey(Postulante, on_delete=models.CASCADE, blank=False, null=False)
    Solucionario_id = models.ForeignKey(Solucionario, on_delete=models.CASCADE, blank=True, null=True, default=None)
    Nota = models.IntegerField(default=0)
    Escuela_id = models.ForeignKey(Escuela, on_delete=models.CASCADE, blank=False, null=False)
    Esta_inscrito = models.BooleanField(default=False)
    DioExamen = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)
    def save(self,*args,**kwargs):
        sol = Solucionario()
        sol.save()
        self.Solucionario_id = sol
        return super(Examen_Postulante, self).save( *args, **kwargs)
    def actualiza(self,sol,pos,*args,**kwargs):
        postulante_solucionario = Solucionario.objects.filter(pk = int(self.Solucionario_id.pk))
        print("========================")
        postulante_solucionario.first().act(sol,pos)
        print("========================")
        return super(Examen_Postulante, self).save( *args, **kwargs)
#SPRINT 2
class Pregunta(models.Model):
    Tema = models.CharField(max_length = 100,default="General")
    Enunciado = models.TextField(blank=False,null=False)
    E_imagen = models.ImageField(upload_to='photos',null=True,blank=True,default=None)
    sovle = models.IntegerField(default=1,blank=False, null=False)
    Resolucion = models.TextField(blank=True)
    Opcion1 = models.TextField(blank=False,null=False,default="No encontrado")
    Opcion2 = models.TextField(blank=False,null=False,default="No encontrado")
    Opcion3 = models.TextField(blank=False,null=False,default="No encontrado")
    Opcion4 = models.TextField(blank=False,null=False,default="No encontrado")
    Opcion5 = models.TextField(blank=False,null=False,default="No encontrado")
    O1_imagen = models.ImageField(upload_to='photos',null=True,blank=True,default=None)
    O2_imagen = models.ImageField(upload_to='photos',null=True,blank=True,default=None)
    O3_imagen = models.ImageField(upload_to='photos',null=True,blank=True,default=None)
    O4_imagen = models.ImageField(upload_to='photos',null=True,blank=True,default=None)
    O5_imagen = models.ImageField(upload_to='photos',null=True,blank=True,default=None)

class Esta_en_Examen(models.Model):
    id_Examen = models.ForeignKey(Examen, on_delete=models.CASCADE,blank=False,null=False)
    id_Pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE,blank=False,null=False)
    numero_pregunta = models.IntegerField(blank=True,null=False,default=1)
    def act(self,*args,**kwargs):
        EX = Examen.objects.filter(pk=self.id_Examen.id)
        solucion = EX.first().soluciones
        print(solucion)
        txt = ""
        for c in range(len(solucion)):
            if c == int(self.numero_pregunta):
                txt = txt + str(self.id_Pregunta.sovle)
                print(str(self.id_Pregunta.sovle))
            else:
                txt = txt + solucion[c]
        solucion = txt
        print(solucion)
        #EX.first().soluciones = solucion
        EX = Examen.objects.filter(pk=self.id_Examen.id).update(soluciones = solucion)
        #EX.save()
        return super(Esta_en_Examen, self).save( *args, **kwargs)
