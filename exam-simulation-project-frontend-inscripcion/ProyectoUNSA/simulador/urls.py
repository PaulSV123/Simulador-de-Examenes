from django.urls import path, include, reverse
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.BienvenidaView.as_view(), name='bienvenida'),
    path('tablero/', views.tableroView, name='tablero'),
    path('inicio/', views.inicioView, name='inicio'),
    path('perfil/', views.perfilView, name='perfil'),
    path('perfilU/<int:pk>/', views.PostulanteUpdate.as_view(), name='perfilU'),
    path('examen/', views.examenView, name='examen'),
    path('examen2/', views.examen2View, name='examen2'),
    path('registrate/', views.SignUpView.as_view(), name='sign_up'),
    path('incia-sesion/', views.SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion/', views.SignOutView.as_view(), name='sign_out'),
    path('preinscribir/<int:pk>/', views.preinscribir, name='preinscribir'),
    path('eliminarp/<int:pk1>/<int:pk2>/', views.eliminarp, name='eliminarp'),
    path('IngExamen/<int:pk>/', views.IngExamen, name='IngExamen'),
    path('prueba/<int:pk>/', views.Siguiente, name='examenentrada'),
    path('PFinal/<int:pk>/', views.PFinal, name = 'PFinal'),
    path('Final/<int:pk1>/<int:pk2>/<int:pk3>/', views.Final, name = 'Final'),
    #admin
    path('Administrador/', views.AdminView.as_view(), name = 'Administrador'),
    path('PList/', views.PostuanteList.as_view(), name = 'Plist'),
    path('PEdit/<int:pk>/', views.PostulanteEdit.as_view(), name = 'Pedit'),
    #User
    path('UDelete/<int:pk>/', views.UsuarioDelete.as_view(), name = 'Udelete'),
    path('Soluc/<int:pk>/', views.Solucionario.as_view(), name = 'Soluc'),
    # Cambiar contraseña
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/change_done.html'), name='password_change_done'),
    # Olvide mi contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/reset_complete.html'), name='password_reset_complete'),
    #ExamenAdmin
    path('ExList', views.ExamenList.as_view(), name='Exlist'),
    path('ExDelete/<int:pk>/', views.ExamenDelete.as_view(), name='Exdelete'),
    path('ExCreate', views.ExamenCreate.as_view(), name= 'Excreate'),
    path('ExEdit/<int:pk>/', views.ExamenUpdate.as_view(), name= 'Exedit'),
    #Examen_Postulante
    path('ExPostList/<int:pk>/', views.Examen_PostulanteList.as_view(), name= 'ExPostlist'),
    path('ExPostCreate/<int:pk>/', views.Examen_PostulanteCreate.as_view(), name = 'ExPostcreate'),
    path('ExPostDelete/<int:pk>/', views.Examen_PostulanteDelete.as_view(), name = 'ExPostdelete'),
    #Examen_pregunta
    path('ExPregList/<int:pk>/', views.PreguntasList.as_view(), name = 'ExPreglist'),
    path('ExPregCreate/<int:pk>/', views.PreguntasCreate.as_view(), name = 'ExPregcreate'),
    path('ExPregDelete/<int:pk>/', views.PreguntaDelete.as_view(), name = 'ExPregdelete'),
]
