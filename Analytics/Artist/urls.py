from django.urls import path
from . import views

urlpatterns = [

    path('',views.Artist_data, name='Artist_data'),
]