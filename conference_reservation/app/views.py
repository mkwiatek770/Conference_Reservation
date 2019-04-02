from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse
from django.views import View
from .models import Reservation, Room
from datetime import date, timedelta
from .forms import AddReservationForm, AddRoomForm


class HomePage(View):
    def get(self, request):
        today = date.today()
        reservations = Reservation.objects.filter(reservation_date=today)

        rooms = Room.objects.all()
        room_available = {}
        for room in rooms:
            try:
                Reservation.objects.get(room=room)
                room_available[room] = False
            except:
                room_available[room] = True
        print(room_available)
        return render(request, 'home.html', {
            'room_available': room_available,
        })


class AddRoom(View):

    def get(self, request, msg=''):
        form = AddRoomForm()
        return render(request, 'addroom.html', {
            'form': form,
            'msg': msg
        })

    def post(self, request):
        form = AddRoomForm(request.POST)

        if form.is_valid():
            form.save()
            msg = 'Added new room!'
        else:
            msg = 'Something is wrong!'
        return self.get(request, msg)


class ModifyRoom(View):

    def get(self, request, id, msg=''):
        instance = Room.objects.get(id=id)
        form = AddRoomForm(instance=instance)
        return render(request, 'modify_room.html', {
            'form': form,
            'msg': msg
        })

    def post(self, request, id):
        instance = Room.objects.get(id=id)
        form = AddRoomForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
        else:
            return self.get(request, id, msg='Invalid data')
        return redirect(reverse('home'))


class AddReservation(View):

    def get(self, request, msg=''):
        form = AddReservationForm()
        return render(request, 'addreservation.html', {
            'form': form,
            'msg': msg
        })

    def post(self, request):
        form = AddReservationForm(request.POST)

        if form.is_valid():
            form.save()
            msg = 'Added new reservation!'
        else:
            msg = "This day is already occupated or you didn't fill all fields properly"
        return self.get(request, msg)


class AddReservationById(View):

    def get(self, request, id, msg=''):
        room = Room.objects.get(pk=int(id))
        form = AddReservationForm(initial={'room': room})

        return render(request, 'addreservation.html', {
            'form': form,
            'msg': msg
        })


class RoomInfo(View):

    def get(self, request, id):
        room = get_object_or_404(Room, pk=id)
        reservation = get_list_or_404(Reservation, room=room)

        curr_date = date.today()
        day = timedelta(days=1)

        days = {}
        for _ in range(14):
            try:
                Reservation.objects.get(reservation_date=curr_date)
                days[curr_date] = False
            except:
                days[curr_date] = True
            curr_date += day

        return render(request, 'roominfo.html', {
            'days': days,
            'room': room
        })


def test(request):
    return render(request, 'base2.html')
