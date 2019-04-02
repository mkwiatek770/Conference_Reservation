
from django.contrib import admin
from django.urls import path
from app import views
# STATIC AND MEDIA
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('room/new/', views.AddRoom.as_view(), name="add_room"),
    path('room/modify/<int:id>', views.ModifyRoom.as_view(), name="modify_room"),
    path('add-reservation/', views.AddReservation.as_view(), name='add_reservation'),
    path('add-reservation/<int:id>', views.AddReservationById.as_view(),
         name='add_reservation_byid'),
    path('room-info/<int:id>', views.RoomInfo.as_view(), name="room_info"),
    path('test/', views.test),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
