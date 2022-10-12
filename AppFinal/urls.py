from re import template
from Dm.views import *
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path



UUID_CANAL_REGEX = r'canal/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'
urlpatterns = [
    # ..............Pagina de inicio......................
    path("", inicio, name= "inicio"),
    # ...............Vehiculos......................
    path("motos/", motos, name= "motos"),
    path("aviones/", aviones, name= "aviones"),
    path("camiones/", camiones, name= "camiones"),
    path("autos/", autos, name= "autos"),
    path("buscarautos/", buscarautos , name="buscarautos"),
    # ................Autos......................
    path("leerautos/", leerautos, name="leerautos"),
    path("eliminarAuto/<id>", eliminarAuto, name="eliminarAuto"),
    path("editarAuto/<id>", editarAutos, name="editarAuto"),
    # ......................Motos......................
    path("leermotos/", leermotos, name="leermotos"),
    path("eliminarMoto/<id>", eliminarMoto, name="eliminarMoto"),
    path("editarMoto/<id>", editarMotos, name="editarMoto"),
     path("buscarmotos/", buscarmotos , name="buscarmotos"),
   
    # ......................Camiones......................
    path("leercamiones/", leercamiones, name="leercamiones"),
    path("eliminarCamion/<id>", eliminarCamion, name="eliminarCamion"),
    path("editarCamion/<id>", editarCamiones, name="editarCamion"),
     path("buscarcamiones/", buscarcamiones , name="buscarcamiones"),
     # ......................Aviones......................
    path("leeraviones/", leeraviones, name="leeraviones"),
    path("eliminarAvion/<id>", eliminarAvion, name="eliminarAvion"),
    path("editarAvion/<id>", editarAviones, name="editarAvion"),
     path("buscaraviones/", buscaraviones , name="buscaraviones"),
    # ..............Login, logout, register......................
    path("login/", login_request, name='login'),
    path('register/', register, name= 'register'),
    path('logout/', LogoutView.as_view (template_name= "AppFinal/logout.html"), name= 'logout'),
    # ..................Editar Perfil.......................
    path('editarPerfil/', editarPerfil, name= 'editarPerfil'),
    # ......................Otro......................
    path('blog/', blog, name='blog'),
    
    path('agregarAvatar/', agregarAvatar, name= 'agregarAvatar'),
    path('Error/', not_found, name= 'not-found'),
    path('elements/', elem, name='elements'),
    path('generic/', gen, name='generic'),
    path('inbox/', Inbox.as_view , name= 'inbox'),
    # ......................Otro......................
    
    re_path(UUID_CANAL_REGEX, CanalDetailView.as_view()),
	path("dm/<str:username>", mensajes_privados),
	path("ms/<str:username>", DetailMs.as_view(), name="detailms"),

	path("mensajes/", Inbox.as_view(), name="inbox"),
]

