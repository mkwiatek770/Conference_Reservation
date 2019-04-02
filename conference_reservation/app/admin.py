from django.contrib import admin
from .models import Room, Reservation


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass
