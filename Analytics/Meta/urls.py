from django.urls import path
from . import views

urlpatterns = [

    path('',views.meta_data, name='meta_data'),
]
