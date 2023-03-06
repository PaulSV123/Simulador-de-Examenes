from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .models import Postulante, Examen, Escuela, Examen_Postulante, Esta_en_Examen, Pregunta
from .forms import SignUpForm, PostulanteForm, UserForm, ExamenForm, Examen_PostulanteForm, PreguntaForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.views.generic.list import ListView 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

exa_id = [0]


class SignUpView(CreateView):
    model = Postulante
    form_class = SignUpForm
    success_url = reverse_lazy('tablero')

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')


class BienvenidaView(TemplateView):
    template_name = 'simulador/bienvenida.html'


class SignInView(LoginView):
    template_name = 'simulador/iniciar_sesion.html'

    def get_success_url(self):
        return reverse_lazy('tablero')


class SignOutView(LogoutView):
    pass


# funciones para cargar vistas
def tableroView(request):
    return render(request, 'simulador/redireccion.html')


def inicioView(request):
    return render(request, 'simulador/inicio.html')

def actualizar():
    d=0

def perfilView(request):
    return render(request, 'simulador/perfil.html')


def examenView(request):
    actualizar()
    Exa = Examen.objects.filter(Estado=str(True))
    Post = Examen_Postulante.objects.filter(Examen_id__Estado=str(True))
    return render(request, 'simulador/examen.html', {'Exa': Exa, 'Post': Post})


def examen2View(request):
    actualizar()
    Post = Examen_Postulante.objects.filter(Esta_inscrito=str(True), DioExamen=str(True), Examen_id__Estado=str(False))
    return render(request, 'simulador/examen2.html', {'Post': Post})


def envio(pk):
    # context = {'mail':mail}
    template = get_template('correo.html')
    content = template.render()
    temp = User.objects.filter(id=pk)
    form = []
    for i in temp:
        form.append(i)
    email = form[0].email

    contenido = EmailMultiAlternatives(
        'SEIVI',
        'Pre-Inscripcion',
        settings.EMAIL_HOST_USER,
        [email]
    )
    contenido.attach_alternative(content, 'text/html')
    contenido.send()


'''
    subjet= 'Mensaje de parte de SEIVI'
    message= 'ada'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subjet,message,email_from,recipient_list)
'''


def preinscribir(request, pk):
    if request.method == 'GET':
        exa_id[0] = pk
        form = Escuela.objects.all()
        return render(request, 'simulador/preinscripcion.html', {'Escuelas': form})
    if request.method == 'POST':
        myDict = Examen_Postulante()
        myDict.Examen_id = Examen.objects.get(id=exa_id[0])
        myDict.Escuela_id = Escuela.objects.get(id=request.POST['Escuela_id'])
        usuario = User.objects.get(id = pk)
        myDict.Postulante_id = Postulante.objects.get(usuario = usuario)
        myDict.save()
        envio(pk)
        return HttpResponseRedirect('/examen/')


def eliminarp(request, pk1, pk2):
    # print(pk1, pk2)
    myDict = Examen_Postulante.objects.filter(Examen_id=pk1, Postulante_id=pk2)
    for i in myDict:
        i.delete()
    return HttpResponseRedirect('/examen/')


def IngExamen(request, pk):
    myDict1 = Examen_Postulante.objects.filter(id=str(pk))
    id_exam=myDict1[0].Examen_id_id
    next = request.POST.get(request, '/Siguiente/')
    form = []
    for i in myDict1:
        form.append(i)
    if request.method == 'GET':
        return render(request, 'simulador/PaginaEspera.html', {'form': form[0], 'id_exa': id_exam})
    if request.method == 'POST':
        return HttpResponseRedirect(next)


def Siguiente(request, pk):
    preguntas = Esta_en_Examen.objects.filter(id_Examen_id=pk)
    return render(request, 'simulador/prueba.html', {'preguntas': preguntas})

def PFinal(request, pk):
    Exa = Examen_Postulante.objects.get(id=pk)
    print(Exa.Nota)
    return render(request, 'simulador/PaginaFinExamen.html', {'Examen' : Exa})

class PostulanteUpdate(LoginRequiredMixin, SuccessMessageMixin, View):
    model = Postulante
    template_name = 'simulador/postulante_update_form.html'
    def get(self, request, pk):
        Us = User.objects.get(id=pk)
        Post = Postulante.objects.get(usuario = Us)
        self.form1 = PostulanteForm(instance = Post)
        self.form2 = UserForm(instance = Us)
        return render(request, self.template_name, {'form2':self.form2, 'form1':self.form1})
    def post(self, request, pk):
        Us = User.objects.get(id=pk)
        Post = Postulante.objects.get(usuario = Us)
        Post.usuario.email = request.POST['email']
        Post.usuario.first_name = request.POST['first_name']
        Post.usuario.last_name = request.POST['last_name']
        Post.Telefono = request.POST['Telefono']
        Post.DNI = request.POST['DNI']
        Post.usuario.save()
        Post.save()
        return HttpResponseRedirect('/perfil/')

#usuario,examen,puntaje
def Final(request, pk1, pk2, pk3):
    EP = Examen_Postulante.objects.get(Postulante_id=pk1,Examen_id=pk2)
    EP.Nota = pk3
    EP.DioExamen = True
    EP.save()
    preguntas = Esta_en_Examen.objects.filter(id_Examen_id=pk1)
    return HttpResponseRedirect('/PFinal/'+str(EP.id)+'/')
#Administrador
class AdminView(LoginRequiredMixin, SuccessMessageMixin, View):
    def get(self,request):
        return render(request, 'simulador/admin/admin_bienvenida.html')
#Postulante
class PostuanteList(ListView):
    model = Postulante
    template_name = 'simulador/Admin/postulante_list.html'
class UsuarioDelete(DeleteView):
    model = User
    success_url = '/PList'
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
class PostulanteEdit(LoginRequiredMixin, SuccessMessageMixin, View):
    template_name = 'simulador/Admin/postulante_update_form.html'
    id_post = []
    def get(self, request, pk):
        Post = Postulante.objects.get(id=pk)
        self.form1 = PostulanteForm(instance = Post)
        self.form2 = UserForm(instance = Post.usuario)
        self.id_post.append(pk)
        print(self.id_post)
        return render(request, self.template_name, {'form2':self.form2, 'form1':self.form1})
    def post(self, request, pk):
        print(self.id_post[0])
        Post = Postulante.objects.get(id=self.id_post[len(self.id_post)-1])
        Post.usuario.email = request.POST['email']
        Post.usuario.first_name = request.POST['first_name']
        Post.usuario.last_name = request.POST['last_name']
        Post.Telefono = request.POST['Telefono']
        Post.DNI = request.POST['DNI']
        Post.usuario.save()
        Post.save()
        return HttpResponseRedirect('/PList/')

#Resultados
class Solucionario(View):
    def get(self, request, pk):
        ExPost = Examen_Postulante.objects.get(id=pk)
        object_list = Esta_en_Examen.objects.filter(id_Examen=ExPost.Examen_id)
        return render(request, 'simulador/solucionario.html', {'object_list':object_list})

#AdminExamen
class ExamenList(ListView):
    model = Examen
    template_name = 'simulador/Admin/examen_list.html'
class ExamenDelete(DeleteView):
    model = Examen
    success_url = '/ExList'
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
class ExamenCreate(LoginRequiredMixin, SuccessMessageMixin, View):
    form = ExamenForm
    template_name = 'simulador/Admin/examen_form.html'
    success_url = '/ExList'
    def get(self, request):
        return render(request, self.template_name, {'form':self.form})
    def post(self, request):
        model = Examen.objects.create(Duracion = request.POST['Duracion'], Tipo = request.POST['Tipo'], Fecha_Examen = request.POST['Fecha_Examen'], Fecha_Resultados = request.POST['Fecha_Resultados'], Nmro_Preguntas = request.POST['Nmro_Preguntas'])
        return HttpResponseRedirect(self.success_url)
class ExamenUpdate(UpdateView):
    model = Examen
    fields = ("__all__")
    template_name = 'simulador/Admin/examen_update_form.html'
    success_url = '/ExList'
#PostulanteAdmin
class Examen_PostulanteList(View):
    template_name = 'simulador/Admin/Examen_postulante_list.html'
    def get(self, request, pk):
        Exa = Examen.objects.get(id=pk)
        object_list = Examen_Postulante.objects.filter(Examen_id=Exa)
        return render(request, self.template_name, {'object_list':object_list, 'pk' : pk})
class Examen_PostulanteCreate(View):
    template_name = 'simulador/Admin/Examen_postulante_form.html'
    form = Examen_PostulanteForm
    Exa = []
    def get(self, request, pk):
        self.Exa.append(Examen.objects.get(id=pk))
        return render(request,self.template_name, {'form':self.form})
    def post(self, request, pk):
        Post = Postulante.objects.get(id = request.POST['Postulante_id'])
        Esc = Escuela.objects.get(id = request.POST['Escuela_id'])
        Examen_Postulante.objects.create(Postulante_id = Post, Examen_id = self.Exa[len(self.Exa)-1], Escuela_id = Esc)
        return HttpResponseRedirect('/ExPostList/'+str(self.Exa[len(self.Exa)-1].id)+'/')
class Examen_PostulanteDelete(View):
    def get(self, request, pk):
        ExPost = Examen_Postulante.objects.get(id=pk)
        exa = ExPost.Examen_id
        ExPost.delete()
        return HttpResponseRedirect('/ExPostList/'+str(exa.id)+'/')
#Preguntas
class PreguntasList(View):
    template_name = 'simulador/Admin/Examen_pregunta_list.html'
    def get(self, request, pk):
        Exa = Examen.objects.get(id = pk)
        object_list = Esta_en_Examen.objects.filter(id_Examen=Exa)
        return render(request, self.template_name, {'object_list':object_list, 'pk':pk})
class PreguntasCreate(View):
    form = PreguntaForm
    Exa = []
    template_name = 'simulador/Admin/Examen_pregunta_form.html'
    def get(self, request, pk):
        self.Exa.append(Examen.objects.get(id=pk))
        return render(request, self.template_name, {'form':self.form, 'pk':pk})
    def post(self, request, pk):
        print(pk)
        preg = Pregunta.objects.create(Tema= request.POST['Tema'], Enunciado = request.POST['Enunciado'],
                                         sovle = request.POST['sovle'],
                                        Resolucion = request.POST['Resolucion'], Opcion1 = request.POST['Opcion1'],
                                        Opcion2 = request.POST['Opcion2'], Opcion3 = request.POST['Opcion3'],
                                        Opcion4 = request.POST['Opcion4'],
                                        Opcion5 = request.POST['Opcion5'])
        Esta_en_Examen.objects.create(id_Examen=self.Exa[len(self.Exa)-1], id_Pregunta = preg, numero_pregunta =request.POST['numero_pregunta'])
        return HttpResponseRedirect('/ExPregList/'+str(self.Exa[len(self.Exa)-1].id)+'/')
class PreguntaDelete(View):
    def get(self, request, pk):
        preg = Esta_en_Examen.objects.get(id=pk)
        exa = preg.id_Examen
        preg.delete()
        return HttpResponseRedirect('/ExPregList/'+str(exa.id)+'/')