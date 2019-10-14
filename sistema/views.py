from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# redireccionar por nombre de url
from django.urls import reverse

#cosas que se deben importar para el login
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login

#decorador para hacer que la vista sea obligatoria
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Juego,Comentario
from django.shortcuts import render

#cargar juegos para index
def index(request):
    juegos = Juego.objects.all()
    dict = {'juegos':juegos}
    return render(request,'index.html',dict)

#listoko
@staff_member_required(login_url = 'index')
@login_required(login_url = "login")
def añadir_juego(request):
    if request.POST:
        titulo = request.POST.get('titulo',False)
        genero = request.POST.get('genero',False)
        anio = request.POST.get('anio',False)
        precio = request.POST.get('precio',False)
        clasificacion = request.POST.get('clasificacion',False)
        stock = request.POST.get('stock',False)
        video = request.POST.get('video',False)
        resenia = request.POST.get('resenia',False)
        foto = request.FILES.get('foto',False)
        p = request.POST.getlist('j[]')
        #confirma ps3
        if 'PS3' in p:
            PS3 = True
        else:
            PS3 = False
        #confirma ps4
        if 'PS4' in p:
            PS4 = True
        else:
            PS4 = False
        #XBOX360
        if 'XBOX360' in p:
            XBOX360 = True
        else:
            XBOX360 = False
        #XBOXONE
        if 'XBOXONE' in p:
            XBOXONE = True
        else:
            XBOXONE = False
        #NSWITCH
        if 'NSWITCH' in p:
            NSWITCH = True
        else:
            NSWITCH = False
        #N3DS
        if 'N3DS' in p:
            N3DS = True
        else:
            N3DS = False
        #PC
        if 'PC' in p:
            PC = True
        else:
            PC = False
        #online
        if 'Online' in p:
            online = True
        else:
            online = False
        j = Juego(titulo=titulo,genero=genero,anio=anio,precio=precio,clasificacion=clasificacion,stock=stock,video=video, resenia=resenia,
        foto=foto, p=p, PS3=PS3, PS4=PS4, XBOX360=XBOX360, XBOXONE=XBOXONE, NSWITCH=NSWITCH, N3DS=N3DS, PC=PC, online= online) 
        j.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request,'añadir_juego.html')

#para deslogear al usuario
def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

#listoko
#para logear al usuario
def login(request):
    if request.POST:
        usuario = request.POST.get('usuario','')
        contrasenia = request.POST.get('contrasenia','')
        user = authenticate(request,username=usuario, password = contrasenia)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('index'))
    return render(request,'login.html')

#listo
@staff_member_required(login_url = 'index')
@login_required(login_url = "login")
def editar_juego(request,id):
    juego = Juego.objects.get(id=id)
    if request.POST:
        titulo = request.POST.get('titulo',False)
        genero = request.POST.get('genero',False)
        anio = request.POST.get('anio',False)
        precio = request.POST.get('precio',False)
        clasificacion = request.POST.get('clasificacion',False)
        stock = request.POST.get('stock',False)
        video = request.POST.get('video',False)
        resenia = request.POST.get('resenia',False)
        p = request.POST.getlist('j[]')
        #confirma ps3
        if 'PS3' in p:
            PS3 = True
        else:
            PS3 = False
        #confirma ps4
        if 'PS4' in p:
            PS4 = True
        else:
            PS4 = False
        #XBOX360
        if 'XBOX360' in p:
            XBOX360 = True
        else:
            XBOX360 = False
        #XBOXONE
        if 'XBOXONE' in p:
            XBOXONE = True
        else:
            XBOXONE = False
        #NSWITCH
        if 'NSWITCH' in p:
            NSWITCH = True
        else:
            NSWITCH = False
        #N3DS
        if 'N3DS' in p:
            N3DS = True
        else:
            N3DS = False
        #PC
        if 'PC' in p:
            PC = True
        else:
            PC = False
        #online
        if 'Online' in p:
            online = True
        else:
            online = False
        juego.titulo = titulo
        juego.genero = genero
        juego.anio = anio
        juego.precio = precio
        juego.clasificacion = clasificacion
        juego.stock = stock
        juego.video = video
        juego.resenia = resenia
        juego.PS3 = PS3
        juego.PS4 = PS4
        juego.XBOX360 = XBOX360
        juego.XBOXONE = XBOXONE
        juego.NSWITCH = NSWITCH
        juego.N3DS = N3DS
        juego.PC = PC
        juego.online = online
        juego.save()
        return HttpResponseRedirect(reverse('index'))
    dict = {'juego':juego}
    return render(request,'editar_juego.html',dict)

#listo
@staff_member_required(login_url = 'index')
@login_required(login_url = "login")
def eliminar_juego(request,id):
    juego = Juego.objects.get(id=id)
    juego.delete()
    return HttpResponseRedirect(reverse('juegos'))

@staff_member_required(login_url = 'index')
@login_required(login_url = 'login')
def macroplayers(request):
    busqueda = request.GET.get('buscar',False)
    if busqueda is False or busqueda == "":
        usuarios = User.objects.all()
    else:
        usuarios = User.objects.filter(username = busqueda)
    dict = {'usuarios':usuarios}
    return render(request,'macroplayers.html',dict)

#listo
@login_required(login_url = 'login')
def perfil(request):
    if request.POST:
        first_name= request.POST.get('first_name',False)
        last_name= request.POST.get('last_name',False)
        username= request.POST.get('username',False)
        if first_name and last_name and email:
            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.email = email
            request.user.save()
        else:
            pass
    usuario = request.user
    contexto = {'usuario':usuario}
    return render(request,'perfil.html',contexto)

@login_required(login_url = 'login')
def cambiar_contrasenia(request):
    if request.POST:
        password = request.POST.get('password','')
        re_password = request.POST.get('re_password',False)
        if password == re_password:
            request.user.set_password(password)
            request.user.save()
            logout(request)
    return HttpResponseRedirect(reverse('index'))

#listo
@staff_member_required(login_url = 'index')
@login_required(login_url = 'login')
def crear_macroplayers(request):
    if request.POST:
        first_name= request.POST.get('first_name',False)
        last_name= request.POST.get('last_name',False)
        email= request.POST.get('email',False)
        username= request.POST.get('username',False)
        password= request.POST.get('password',False)
        user = User.objects.create_user(username,email,password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return HttpResponseRedirect(reverse('macroplayers'))
    return render(request,'crear_macroplayers.html')

#listo
@staff_member_required(login_url = 'index')
@login_required(login_url = 'login')
def juegos(request):
    juegos = Juego.objects.all()
    dict = {'juegos':juegos}
    return render(request,'juegos.html',dict)


def detalle(request,id):
    if request.POST and request.user.is_authenticated:
        comentario = request.POST.get('comentario',False)
        usuario = request.user.username
        juego = id
        c = Comentario(comentario = comentario, usuario = usuario,juego = juego)
        c.save()
    comentarios = Comentario.objects.filter(juego=id)
    juego = Juego.objects.get(id=id)
    contexto = {'juego':juego,'comentarios':comentarios}
    return render(request,'detalle.html',contexto)

@login_required(login_url = 'login')
@staff_member_required(login_url = 'index')
def borrar_comentario(request,id):
    comentario = Comentario.objects.get(id=id)
    comentario.delete()
    return HttpResponseRedirect(reverse('index'))

@staff_member_required(login_url = 'index')
@login_required(login_url = "login")
def eliminar_usuario(request,id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return HttpResponseRedirect(reverse('macroplayers'))