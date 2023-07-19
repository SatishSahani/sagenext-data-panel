from django.urls import path
from . import views

urlpatterns = [
    
    # path('upload',views.upload, name='upload'),
    path('ad_page/',views.ad_page, name='ad_page'),
    path('ad_page/delete_selected_rows/', views.delete_selected_rows, name='delete_selected_rows   '),
    path('graph/', views.dashboard, name='dashboard'),
    path('generate-graph/', views.generate_graph, name='generate_graph'),
    path('Adwords_Dashboard/', views.Adwords_Dashboard, name='Adwords_Dashboard'),
     
]
