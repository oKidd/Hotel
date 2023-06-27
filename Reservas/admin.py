from django.contrib import admin
from Reservas.models import UserExtraInfo, TipoHabitacion, Habitacion, EstadoHabitacion, Cama, Reserva, DetalleReserva


class UserExtraInfoAdmin(admin.ModelAdmin):
    verbose_name = 'Usuarios Info Extra'
    list_display = ('user',)
    pass

class TipoHabitacionAdmin(admin.ModelAdmin):
    verbose_name = 'Tipos Habitaciones'
    list_display = ('tipo',)
    pass

class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero',)
    pass

class EstadoHabitacionAdmin(admin.ModelAdmin):
    list_display = ('estado',)
    pass

class CamaAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
    pass

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'habitacion', 'usuario',)
    pass

class DetalleReservaAdmin(admin.ModelAdmin):
    list_display = ('id',)
    pass

admin.site.register(UserExtraInfo, UserExtraInfoAdmin)
admin.site.register(TipoHabitacion, TipoHabitacionAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(EstadoHabitacion, EstadoHabitacionAdmin)
admin.site.register(Cama, CamaAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(DetalleReserva, DetalleReservaAdmin)