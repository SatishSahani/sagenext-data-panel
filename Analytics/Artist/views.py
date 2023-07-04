# from django.shortcuts import render
# from requests import request
# # Create your views here.
# def Artist_data(request):
#     return render(request , 'artist.html')
from django.shortcuts import redirect, render
from requests import request
from .forms import UploadFileForm
import csv
from django.contrib import messages
from django.shortcuts import render
from .models import ArtistData
from io import TextIOWrapper

def Artist_data(request):
    if request.method == 'POST':
        if 'myfile' not in request.FILES:
            messages.error(request, 'No file selected')
            return redirect('Artist_data')
        
        csv_file = request.FILES['myfile']
        
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Wrong format. Only CSV files are allowed.')
            return redirect('Artist_data')
        
        csv_data = csv.reader(TextIOWrapper(csv_file, encoding='utf-8'), delimiter=',')
        
        next(csv_data)  # Skip the header row
        
        for row in csv_data:
            month = row[0]
            impression = float(row[1]) if row[1] else 0
            cost = float(row[2]) if row[2] else 0
            conversions = row[3] if row[3] else 0
            bookings = row[4] if row[4] else 0
            
            ArtistData.objects.create(month=month, impression=impression, cost=cost, conversions=conversions, bookings=bookings)
        
        messages.success(request, 'Data uploaded successfully')
        return redirect('Artist_data')
    
    else:
        ad_data = ArtistData.objects.all()
        return render(request, 'artist.html', {'ad_data': ad_data})

def Artist_data_list(request):
    ad_data = ArtistData.objects.all()
    return render(request, 'artist.html', {'ad_data': ad_data})