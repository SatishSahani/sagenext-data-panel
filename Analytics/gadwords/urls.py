from django.urls import path
from . import views

urlpatterns = [
    
    # path('upload',views.upload, name='upload'),
    path('ad_page/',views.ad_page, name='ad_page'),
    path('ad_data/',views.ad_data_list,name='list'),
    path('delete/',views.ad_data_delete, name='delete'),
     path('ad_page/delete_selected_rows/', views.delete_selected_rows, name='delete_selected_rows   '),
     
]
