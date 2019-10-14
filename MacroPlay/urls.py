
from django.contrib import admin
from django.urls import path
from sistema import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('cerrar_sesion',views.cerrar_sesion,name="cerrar_sesion"),
    path('login/',views.login,name="login"),
    path('añadir_juego/',views.añadir_juego,name="añadir_juego"),
    path('editar_juego/<int:id>/videojuego/',views.editar_juego,name="editar_juego"),
    path('eliminar_juego/<int:id>/videojuego/',views.eliminar_juego,name="eliminar_juego"),
    path('macroplayers',views.macroplayers,name="macroplayers"),
    path('macroplayers/perfil/',views.perfil,name="perfil"),
    path('macroplayers/cambiar_contrasenia',views.cambiar_contrasenia,name="cambiar_contrasenia"),
    path('macroplayers/crear/',views.crear_macroplayers,name="crear_macroplayers"),
    path('juegos',views.juegos,name="juegos"),
    path('detalle/<int:id>/juego/',views.detalle,name="detalle"),
    path('borrar_comentario/<int:id>/',views.borrar_comentario,name="borrar_comentario"),
    path('eliminar_usuario/<int:id>/usuario/',views.eliminar_usuario,name="eliminar_usuario"),
]   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)