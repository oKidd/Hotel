"""Hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Reservas.views import UserLogin, UserRegister, user, home, signout, adminpanel, reservar, habitaciones, editar_habitacion, crear_cama, crear_tipo_cama

urlpatterns = [
    path('djangoadmin/', admin.site.urls),
    path('', home),
    path('register/', UserRegister),
    path('user/', user),
    path('login/', UserLogin),
    path('logout/', signout),
    path('admin/', adminpanel),
    path('admin/<slug:subpage>/', adminpanel),
    path('editar_habitacion/', editar_habitacion),
    path('editar_habitacion/<int:numero>/', editar_habitacion),
    path('crear_cama/<int:numero>/', crear_cama),
    path('crear_tipo_cama/', crear_tipo_cama),
    path('crear_tipo_cama/<int:id>/', crear_tipo_cama),
    path('reservar/', reservar),
    path('reservar/<int:numero>/', reservar),
    path('habitaciones/', habitaciones)
]
