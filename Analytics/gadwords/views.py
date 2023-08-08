from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import UploadFileForm
import io
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
# Create your views here.
import csv
from django.contrib import messages
from django.shortcuts import render
from .models import AdwordData
from io import TextIOWrapper
from datetime import datetime
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from plotly.subplots import make_subplots
from django.shortcuts import render
from plotly.offline import plot
import numpy as np
from datetime import datetime


def ad_page(request):
    if request.method == 'POST':
        if 'myfile' not in request.FILES:
            messages.error(request, 'No file selected')
            return redirect('ad_page')
        
        csv_file = request.FILES['myfile']
        
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Wrong format. Only CSV files are allowed.')
            return redirect('ad_page')
        
        csv_data = csv.reader(TextIOWrapper(csv_file, encoding='utf-8'), delimiter=',')
        
        next(csv_data)  # Skip the header row
        
        for row in csv_data:
            date_str = row[0]
            if date_str == '0000-00-00':
                date = None  # Set the date value to None or any default value you prefer
            else:
                try:
                    date = datetime.strptime(date_str, '%d %b %Y').date()  # Adjust the date format based on your CSV data format
                except ValueError:
                    date = None  # Handle invalid date format if needed
        
           
            date = row[0]
            network = row[1]
            network_clicks = row[2]
            network_cost = row[3]
            network_avg_cpc = row[4]
            campaign_name = row[5]
            campaign_adgroup_name = row[6]
            campaign_cost = row[7]
            campaign_cost_comparison = row[8]
            campaign_clicks = row[9]
            campaign_clicks_comparison = row[10]
            campaign_interactions = row[11]
            interaction_comparison = row[12]
            campaign1_name = row[13]
            campaign1_campaign_group_name = row[14]
            campaign1_campaign_status = row[15]
            campaign1_cost = row[16]
            campaign1_conversions = row[17]
            campaign1_cost_per_conv = row[18]
            search = row[19]
            search_cost = row[20]
            search_clicks = row[21]
            search_impressions = row[22]
            search_conversion = row[23]
            search_word = row[24]
            search_word_clicks = row[25]
            search_word_impressions = row[26]
            search_word_conversions = row[27]
            search_word_cost = row[28]
            search_word_top_containing_queries = row[29]
            search_keyword = row[30]
            search_keyword_match_type = row[31]
            search_keyword_criterion_status = row[32]
            search_keyword_campaign_status = row[33]
            search_keyword_adgroup_status = row[34]
            search_keyword_cost = row[35]
            search_keyword_clicks = row[36]
            search_keyword_ctr = row[37]
            demographics_gender = row[38]
            demographics_age_range = row[39]
            demographics_impressions = row[40]
            demographics_total_percent = row[41]
            device = row[42]
            device_cost = row[43]
            device_clicks = row[44]
            device_impressions = row[45]
            clicks = row[46]
            conversions = row[47]
            cost_per_conv = row[48]
            cost = row[49]
            per_hour = row[50]
            per_hour_impression = row[51]
            per_day = row[52]
            per_day_impression = row[53]
            per_day_per_hour = row[54]
            per_day_per_hour_impression = row[55]
            optimisation_score = row[56]
            optimisation_score_campaign_name = row[57]

            AdwordData.objects.create(
                    date=date,
                    network=network,
                    network_clicks=network_clicks,
                    network_cost=network_cost,
                    network_avg_cpc=network_avg_cpc,
                    campaign_name=campaign_name,
                    campaign_adgroup_name=campaign_adgroup_name,
                    campaign_cost=campaign_cost,
                    campaign_cost_comparison=campaign_cost_comparison,
                    campaign_clicks=campaign_clicks,
                    campaign_clicks_comparison=campaign_clicks_comparison,
                    campaign_interactions=campaign_interactions,
                    interaction_comparison=interaction_comparison,
                    campaign1_name=campaign1_name,
                    campaign1_campaign_group_name=campaign1_campaign_group_name,
                    campaign1_campaign_status=campaign1_campaign_status,
                    campaign1_cost=campaign1_cost,
                    campaign1_conversions=campaign1_conversions,
                    campaign1_cost_per_conv=campaign1_cost_per_conv,
                    search=search,
                    search_cost=search_cost,
                    search_clicks=search_clicks,
                    search_impressions=search_impressions,
                    search_conversion=search_conversion,
                    search_word=search_word,
                    search_word_clicks=search_word_clicks,
                    search_word_impressions=search_word_impressions,
                    search_word_conversions=search_word_conversions,
                    search_word_cost=search_word_cost,
                    search_word_top_containing_queries=search_word_top_containing_queries,
                    search_keyword=search_keyword,
                    search_keyword_match_type=search_keyword_match_type,
                    search_keyword_criterion_status=search_keyword_criterion_status,
                    search_keyword_campaign_status=search_keyword_campaign_status,
                    search_keyword_adgroup_status=search_keyword_adgroup_status,
                    search_keyword_cost=search_keyword_cost,
                    search_keyword_clicks=search_keyword_clicks,
                    search_keyword_ctr=search_keyword_ctr,
                    demographics_gender=demographics_gender,
                    demographics_age_range=demographics_age_range,
                    demographics_impressions=demographics_impressions,
                    demographics_total_percent=demographics_total_percent,
                    device=device,
                    device_cost=device_cost,
                    device_clicks=device_clicks,
                    device_impressions=device_impressions,
                    clicks=clicks,
                    conversions=conversions,
                    cost_per_conv=cost_per_conv,
                    cost=cost,
                    per_hour=per_hour,
                    per_hour_impression=per_hour_impression,
                    per_day=per_day,
                    per_day_impression=per_day_impression,
                    per_day_per_hour=per_day_per_hour,
                    per_day_per_hour_impression=per_day_per_hour_impression,
                    optimisation_score=optimisation_score,
                    optimisation_score_campaign_name=optimisation_score_campaign_name
)
  
        
        messages.success(request, 'Data uploaded successfully')
        return redirect('ad_page')
    
    else:
        ad_data = AdwordData.objects.all()
        rows_per_page = request.GET.get('rows', 10)  # Get the number of rows per page from the query parameter 'rows'
        # rows_per_page = None
        if rows_per_page == "All":
            paginator = None  # No pagination if 'all' is selected
            page_obj = ad_data
        else:
            rows_per_page = int(rows_per_page)
            paginator = Paginator(ad_data, rows_per_page)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        return render(request, 'ad_page.html', {'page_obj': page_obj, 'rows_per_page': rows_per_page})

def delete_selected_rows(request):
    if request.method == 'POST':
        ids = request.POST.getlist('ids[]')
        try:
            # Delete the selected rows from the database
            AdwordData.objects.filter(id__in=ids).delete()
            return JsonResponse({'success': True})
        except:
            return JsonResponse({'success': False})

def dashboard(request):
    id = request.GET.get('id')  # Get the 'id' parameter from the request's query parameters

    if id:
        try:
            data = AdwordData.objects.get(id=id)  # Retrieve the data from the database based on the 'id' parameter
            # Process the retrieved data or pass it to the template
            return render(request, 'graph.html', {'data': data})
        except AdwordData.DoesNotExist:
            # Handle the case when the data with the provided 'id' doesn't exist
            return render(request, 'error.html', {'message': 'Data not found'})
    else:
        # Handle the case when the 'id' parameter is not provided
        return render(request, 'error.html', {'message': 'ID parameter is missing'})


# Graph1 code by satish 6July23
# Code For date range selection

def Adwords_Dashboard(request):
    # print("yes")
    # Retrieve the start_date and end_date from the form submission (if any)
    try:
        start_g_date = request.GET.get('start_date')
        print("yes1",start_g_date)
        end_g_date = request.GET.get('end_date')       
        print("yes2",end_g_date)
        start_g_date = datetime.fromisoformat(start_g_date)
        # start_date_new = start_date.strftime("%a, %d %b %Y")  # Example: "Thu, 20 Mar 2023"
        # print("yes3",start_date)
        # end_date = datetime.fromisoformat(end_date)
        # end_date_new = end_date.strftime("%a, %d %b %Y")
        # print("yes4",end_date)
        # Filter the data based on the selected date range
        if start_g_date and end_g_date:
            data = AdwordData.objects.filter(date__gte=start_g_date, date__lte=end_g_date)
            # data = AdwordData.objects.filter(date__range=(start_date_new, end_date_new))
            # [print(entry.date) for entry in data]
            # [print(start_date == entry.date) for entry in data] 
            # print(start_date) cd
            #[print(type(entry.date)) for entry in data]  
        else:
            # If no date range is selected, retrieve all data
            data = AdwordData.objects.all()
            [print(entry.date) for entry in data] 
            print("satish")      
           
    except Exception as e:
        print(e)
        data = AdwordData.objects.all()
    context = {
        'data': data
    }

    return render(request, 'Adwords_Dashboard(copy).html', context)


