from django.db import models
from datetime import date


class Room(models.Model):
    name = models.CharField(max_length=30, verbose_name="Room name")
    capacity = models.PositiveSmallIntegerField(verbose_name="Room Capacity")
    projector_available = models.BooleanField(
        verbose_name="Projector available")

    def __str__(self):
        return f"{self.name}({self.capacity})"


class Reservation(models.Model):

    todays_date = date.today()

    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    reservation_date = models.DateField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.room.name} - {self.reservation_date}"

    class Meta:
        unique_together = ('reservation_date', 'room')
