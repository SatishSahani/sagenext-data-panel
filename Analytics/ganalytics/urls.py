from django.urls import path
from . import views

urlpatterns = [

    path('',views.analytics_data, name='analytics_data'),
    path('delete_selected_rows/', views.delete_selected_rows, name='delete_selected_rows')
]