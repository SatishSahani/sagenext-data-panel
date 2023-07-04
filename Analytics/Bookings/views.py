# from django.shortcuts import render
# from requests import request
from django.shortcuts import redirect, render
from requests import request
from .forms import UploadFileForm
import csv
from django.contrib import messages
from django.shortcuts import render
from .models import BookingsData
from io import TextIOWrapper
# Create your views here.
# def Bookings_data(request):
#     return render(request , 'Booking.html')

def Bookings_data(request):
    if request.method == 'POST':
        if 'myfile' not in request.FILES:
            messages.error(request, 'No file selected')
            return redirect('Bookings_data')
        
        csv_file = request.FILES['myfile']
        
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Wrong format. Only CSV files are allowed.')
            return redirect('Bookings_data')
        
        csv_data = csv.reader(TextIOWrapper(csv_file, encoding='utf-8'), delimiter=',')
        
        next(csv_data)  # Skip the header row
        
        for row in csv_data:
            month = row[0]
            impression = float(row[1]) if row[1] else 0
            cost = float(row[2]) if row[2] else 0
            conversions = row[3] if row[3] else 0
            bookings = row[4] if row[4] else 0
            
            BookingsData.objects.create(month=month, impression=impression, cost=cost, conversions=conversions, bookings=bookings)
        
        messages.success(request, 'Data uploaded successfully')
        return redirect('Bookings_data')
    
    else:
        ad_data = BookingsData.objects.all()
        return render(request, 'Booking.html', {'ad_data': ad_data})

def Booking_data_list(request):
    ad_data = BookingsData.objects.all()
    return render(request, 'Booking.html', {'ad_data': ad_data})