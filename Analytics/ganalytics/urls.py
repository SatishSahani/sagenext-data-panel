from django.urls import path
from . import views

urlpatterns = [

    path('',views.analytics_data, name='analytics_data'),
    path('delete_selected_rows/', views.delete_selected_rows, name='delete_selected_rows'),
    path('Analytics_Dashboard/',views.Analytics_Dashboard,name='Analytics_Dashboard'),
#     path('Analytics_Dashboard/', views.Analytics_Dashboard, name='Analytics_Dashboard'),
#     path('Analytic_Dasboard/', views.Analytic_Dasboard, name='Analytic_Dasboard'),
]