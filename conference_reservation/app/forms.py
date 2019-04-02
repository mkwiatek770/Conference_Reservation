from django import forms
from .models import Room, Reservation


class AddRoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('name', 'capacity', 'projector_available')


class AddReservationForm(forms.ModelForm):

    reservation_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Reservation
        fields = '__all__'
