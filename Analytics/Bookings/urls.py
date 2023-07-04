from django.urls import path
from . import views

urlpatterns = [

    path('',views.Bookings_data, name='Bookings_data'),
]