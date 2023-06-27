from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Reservas.models import UserExtraInfo, Habitacion, TipoHabitacion, EstadoHabitacion
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from Reservas.forms import UserRegisterForm, UserLoginForm, UserRegisterExtraForm, CrearHabitacion, ReservaForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def UserRegister(request):
    form = UserRegisterForm()
    extra = UserRegisterExtraForm()
    data = {'form':form, 'extra':extra}
    if request.method == 'POST':
        username = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        pais = request.POST['pais']
        rut = request.POST['rut']
        nacimiento = request.POST['nacimiento']
        telefono = request.POST['telefono']
        if password1 == password2:
            try:
                user = User.objects.get(email=email)
                error = "El correo ya esta en uso..."
                data = {'error': error, 'form':form, 'extra':extra}
                return render(request, 'register.html', data)
            except:
                try:
                    user = User.objects.create_user(username=username,first_name=first_name, last_name=last_name, email=email, password=password1)
                    user.save()
                    user_extra = UserExtraInfo(user=user, pais=pais, rut=rut, nacimiento=nacimiento, telefono=telefono)
                    user_extra.save()
                    login(request, user)
                    return redirect('/user')
                except:
                    error = "El usuario ya existe..."
                    data = {'error': error, 'form':form, 'extra':extra}
                    return render(request, 'register.html', data)
        else:
            error = "Las claves no coinciden..."
            data = {'error': error, 'form':form}
    return render(request, 'register.html', data)

def UserLogin(request):
    if request.user.is_authenticated:
        return redirect('/user')
    form = UserLoginForm()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            finduser = User.objects.get(email=email)
        except:
            error = "El usuario no existe..."
            data = {'form': form, 'error': error}
            return render(request, 'login.html', data)
        # return HttpResponse(finduser.username+"<br>"+finduser.email)
        username = finduser.username
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # usuario encontrado!
            login(request, user)
            return redirect('/user')
        else:
            #  no se encuentra el usuario.
            error = "Clave incorrecta..."
            data = {'form': form, 'error': error}
            return render(request, 'login.html', data)
    data = {'form': form}
    return render(request, 'login.html', data)

def user(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            # return HttpResponse("<p style='font-size: 30px; text-align: center; margin-top: 25%;'>Panel admin, en construccion...</h1>")
            return redirect('/admin')
        else:
            user_extra = UserExtraInfo.objects.get(user=request.user)
            data = {'user_extra':user_extra}
            return render(request, 'user.html', data)
    else:
        return redirect('/login')

def signout(request):
    logout(request)
    return redirect('/')

def adminpanel(request, subpage=None):
    if request.user.is_authenticated:
        if request.user.is_staff:
            user_extra = UserExtraInfo.objects.get(user=request.user)
            data = {'user_extra':user_extra}
            if subpage is None:
                return render(request, 'admin.html', data)
            if subpage == "users":
                return render(request, 'admin_users.html', data)
            if subpage == "crear_habitacion":
                tipos = ['Clasica', 'Superior', "Suite Junior", "Suite Presidencial"]
                for tipo in tipos:
                    try:
                        TipoHabitacion.objects.get(tipo=tipo)
                    except:
                        TipoHabitacion.objects.create(tipo=tipo)
                estados = ['Desocupada', 'Ocupada']
                for estado in estados:
                    try:
                        EstadoHabitacion.objects.get(estado=estado)
                    except:
                        EstadoHabitacion.objects.create(estado=estado)
                form = CrearHabitacion()
                estados = ['Desocupada', 'Ocupada']
                if request.method == 'POST':
                    personas = request.POST['personas']
                    tipo = request.POST['tipo']
                    valor = request.POST['valor']
                    caracteristicas = request.POST['caracteristicas']
                    estado = EstadoHabitacion.objects.get(estado='Desocupada')
                    habitacion = Habitacion.objects.create(estado=estado, personas=personas, tipo=TipoHabitacion.objects.get(id=tipo), valor=valor, caracteristicas=caracteristicas)
                    # habitacion
                    return redirect('/admin/habitaciones')
                data = {'form': form}
                return render(request, 'admin_crear_habitacion.html', data)
            if subpage == "habitaciones":
                habitaciones = Habitacion.objects.all()
                data = {'habitaciones':habitaciones}
                return render(request, 'admin_habitaciones.html', data)
            else:
                return redirect('/admin')
        else:
            return redirect('/user')
    else:
        return redirect('/login')

def reservar(request):
    form = ReservaForm()
    if request.method == 'POST':
        adultos = request.POST['adultos']
        ninos = request.POST['ninos']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_termino = request.POST['fecha_termino']
        # cotizacion = Cotizacion.objects.create()
        personas = int(adultos) + int(ninos)
        noches = str(datetime.strptime(fecha_inicio, "%Y-%m-%d").date() - datetime.strptime(fecha_termino, "%Y-%m-%d").date())[1:-14]
        if len(noches) == 0:
            noches = "1"

        # # Buscar la posición de la palabra "Days"
        # indice = dias.find("Days")

        # # Si se encuentra la palabra "Days", eliminar desde ese punto hasta el final del string
        # if indice != -1:
        #     dias = dias[:indice]

        # habitaciones = Habitacion.objects.filter(personas>=personas, estado="Desocupada")
        data = {'habitaciones':habitaciones, 'adultos':adultos, 'ninos':ninos, 'fecha_inicio':fecha_inicio, 'fecha_termino':fecha_termino, 'personas':personas, 'noches':noches}
        return render(request, 'habitaciones.html', data)
    data = {'form':form}
    return render(request, 'reservar.html', data)

def habitaciones(request):
    try:
        adultos = adultos
        ninos = ninos
        fecha_inicio = fecha_inicio
        fecha_termino = fecha_termino
        personas = personas
        noches = noches
        habitaciones = Habitacion.objects.filter(personas=personas, estado="Desocupada")
        nh = habitaciones.count()
        data = {'habitaciones':habitaciones,'adultos':adultos, 'ninos':ninos, 'fecha_inicio':fecha_inicio, 'fecha_termino':fecha_termino}
        return render(request, 'habitaciones.html', data)
    except:
        return redirect('/reservar')