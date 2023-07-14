
from django.contrib import admin
from django.urls import path,include
from ganalytics.views import Analytics_Dashboard
from gadwords.views import ad_page
from Meta.views import meta_data
from ganalytics.views import analytics_data
from Bookings.views import Bookings_data




from Dashboard.views import login_view,dashboard_view,logout_view,ad_data_list



urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('gadwords.urls')),
    # path("upload/",include('gadwords.urls')),
    path("meta/",include('Meta.urls')),
    path("analytics/",include('ganalytics.urls')),
    path("Bookings/",include('Bookings.urls')),
    path('Artist',include('Artist.urls')),
    path('list/',ad_data_list,name='list'),
    path('', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('Analytics_Dashboard/', Analytics_Dashboard, name='Analytics_Dashboard')
    
]
