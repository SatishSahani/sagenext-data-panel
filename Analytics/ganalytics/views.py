from django.shortcuts import redirect, render
from .forms import UploadFileForm
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
import plotly.graph_objects as go
# Create your views here.
import csv
from django.contrib import messages
from .models import AnalyticData
from io import TextIOWrapper
import plotly.graph_objects as go
from django.shortcuts import render
from plotly.offline import plot
from plotly.subplots import make_subplots
import numpy as np


def analytics_data(request):
    if request.method == 'POST':
        if 'myfile' not in request.FILES:
            messages.error(request, 'No file selected')
            return redirect('ad_page')

        csv_file = request.FILES['myfile']

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Wrong format. Only CSV files are allowed.')
            return redirect('analytics_data')

        csv_data = csv.reader(TextIOWrapper(csv_file, encoding='utf-8'), delimiter=',')

        next(csv_data)  # Skip the header row

        for row in csv_data:
            country = row[0]
            country_new_users = row[1]
            country_benchmark_new_users = row[2]
            #country_page_session = row[3]
            country_avg_session_duration = row[4]
            country_bounce_rate = row[5]
            country_benchmark_bounce_rate = row[6]
            device_category = row[7]
            device_users = row[8]
            device_new_users = row[9]
            device_sessions = row[10]
            device_bounce_rate = row[11]
            device_page_session = row[12]
            search_query = row[13]
            search_clicks = row[14]
            search_impressions = row[15]
            search_ctr = row[16]
            search_avg_position = row[17]
            site_search_new_users = row[18]
            site_search_bounce_rate = row[19]
            site_search_page_session = row[20]
            site_search_avg_session_duration = row[21]
            site_search_transaction = row[22]
            site_search_revenue = row[23]
            site_search_e_commerce_conversion_rate = row[24]
            goal_completion_location = row[25]
            goal_completions = row[26]
            page = row[27]
            #avg_page_load_time = row[28]
            page_per_views = row[29]
            page_bounce_rate = row[30]
            page_exit = row[31]
            event_category = row[32]
            event_total_events = row[33]
            event_unique_events = row[34]
            page_event = row[35]
            page_total_events = row[36]
            page_unique_events = row[37]
            campaign_campaign_id = row[38]
            campaign_clicks = row[39]
            campaign_cost = row[40]
            campaign_cpc = row[41]
            campaign_users = row[42]
            campaign_sessions = row[43]
            campaign_bounce_rate = row[44]
            campaign_pages_session = row[45]
            final_url = row[46]
            url_clicks = row[47]
            url_cost = row[48]
            url_cpc = row[49]
            url_users = row[50]
            url_sessions = row[51]
            url_bounce_rate = row[52]
            url_page_session = row[53]
            per_hour = row[54]
            per_hour_users = row[55]
            per_hour_new_users = row[56]
            per_hour_sessions = row[57]
            per_hour_bounce_rate = row[58]
            per_hour_pages_session = row[59]
            per_hour_avg_session_duration = row[60]
            affinity_category_reach = row[61]
            users_reach = row[62]
            new_users_reach = row[63]
            sessions_reach = row[64]
            bounce_rate_reach = row[65]
            pages_session_reach = row[66]
            avg_session_duration_reach = row[67]
            market_segment = row[68]
            market_users = row[69]
            market_new_users = row[70]
            market_sessions = row[71]
            market_bounce_rate = row[72]
            market_pages_session = row[73]
            market_avg_session_duration = row[74]
            other_category = row[75]
            other_category_users = row[76]
            other_category_new_users = row[77]
            other_category_sessions = row[78]
            other_category_bounce_rate = row[79]
            other_category_pages_session = row[80]
            other_category_avg_session_duration = row[81]
            landing_page = row[82]
            landing_sessions = row[83]
            #landing_new_session = row[84]
            landing_new_users = row[85]
            landing_bounce_rate = row[86]
            landing_page_session = row[87]
            landing_avg_session_duration = row[88]
            language = row[89]
            language_users = row[90]
            language_new_users = row[91]
            language_sessions = row[92]
            language_bounce_rate = row[93]
            language_pages_session = row[94]
            language_avg_session_duration = row[95]
            audience = row[96]
            audience_users = row[97]
            audience_new_users = row[98]
            audience_sessions = row[99]
            audience_bounce_rate = row[100]
            audience_pages_session = row[101]
            audience_avg_session_duration = row[102]
            browser_bounce_rate = row[103]
            browser_pages_session = row[104]
            browser_pages_session = row[105]
            default_channel_grouping = row[106]
            default_channel_users = row[107]
            default_channel_new_users = row[108]
            default_channel_sessions = row[109]
            default_channel_bounce_rate = row[110]
            default_channel_pages_session = row[111]
            default_channel_avg_session_duration = row[112]
            page_path_level1 = row[113]
            page_view = row[114]
            unique_page_view = row[115]
            avg_time_on_page = row[116]
            bounce_rate = row[117]
            exit_percent = row[118]
            country_impressions = row[119]
            country_clicks = row[120]
            country_ctr = row[121]
            country_average_position = row[122]
            country_sessions = row[123]
            country_bounce_rate = row[124]
            country_pages_session = row[125]
            all_website_device_category = row[126]
            all_website_impressions = row[127]
            all_website_clicks = row[128]
            all_website_ctr = row[129]
            all_website_average_position = row[130]
            all_website_sessions = row[131]
            all_website_bounce_rate = row[132]
            all_website_pages_session = row[133]
            mobile_device_info = row[134]
            mobile_device_users = row[135]
            mobile_device_new_users = row[136]
            mobile_device_sessions = row[137]
            mobile_device_bounce_rate = row[138]
            mobile_device_avg_session_duration = row[139]
            session_duration_bucket = row[140]
            bucket_session = row[141]
            bucket_page_views = row[142]
            source_medium = row[143]
            medium_users = row[144]
            medium_new_users = row[145]
            medium_sessions = row[146]
            medium_bounce_rate = row[147]
            medium_pages_session = row[148]
            medium_avg_session_duration = row[149]
            
            AnalyticData.objects.create(
                country=country,
            country_new_users=country_new_users,
            country_benchmark_new_users=country_benchmark_new_users,
            #country_page_session=country_page_session,
            country_avg_session_duration=country_avg_session_duration,
            country_bounce_rate=country_bounce_rate,
            country_benchmark_bounce_rate=country_benchmark_bounce_rate,
            device_category=device_category,
            device_users=device_users,
            device_new_users=device_new_users,
            device_sessions=device_sessions,
            device_bounce_rate=device_bounce_rate,
            device_page_session=device_page_session,
            search_query=search_query,
            search_clicks=search_clicks,
            search_impressions=search_impressions,
            search_ctr=search_ctr,
            search_avg_position=search_avg_position,
            site_search_new_users=site_search_new_users,
            site_search_bounce_rate=site_search_bounce_rate,
            site_search_page_session=site_search_page_session,
            site_search_avg_session_duration=site_search_avg_session_duration,
            site_search_transaction=site_search_transaction,
            site_search_revenue=site_search_revenue,
            site_search_e_commerce_conversion_rate=site_search_e_commerce_conversion_rate,
            goal_completion_location=goal_completion_location,
            goal_completions=goal_completions,
            page=page,
            #avg_page_load_time=avg_page_load_time,
            page_per_views=page_per_views,
            page_bounce_rate=page_bounce_rate,
            page_exit=page_exit,
            event_category=event_category,
            event_total_events=event_total_events,
            event_unique_events=event_unique_events,
            page_event=page_event,
            page_total_events=page_total_events,
            page_unique_events=page_unique_events,
            campaign_campaign_id=campaign_campaign_id,
            campaign_clicks=campaign_clicks,
            campaign_cost=campaign_cost,
            campaign_cpc=campaign_cpc,
            campaign_users=campaign_users,
            campaign_sessions=campaign_sessions,
            campaign_bounce_rate=campaign_bounce_rate,
            campaign_pages_session=campaign_pages_session,
            final_url=final_url,
            url_clicks=url_clicks,
            url_cost=url_cost,
            url_cpc=url_cpc,
            url_users=url_users,
            url_sessions=url_sessions,
            url_bounce_rate=url_bounce_rate,
            url_page_session=url_page_session,
            per_hour=per_hour,
            per_hour_users=per_hour_users,
            per_hour_new_users=per_hour_new_users,
            per_hour_sessions=per_hour_sessions,
            per_hour_bounce_rate=per_hour_bounce_rate,
            per_hour_pages_session=per_hour_pages_session,
            per_hour_avg_session_duration=per_hour_avg_session_duration,
            affinity_category_reach=affinity_category_reach,
            users_reach=users_reach,
            new_users_reach=new_users_reach,
            sessions_reach=sessions_reach,
            bounce_rate_reach=bounce_rate_reach,
            pages_session_reach=pages_session_reach,
            avg_session_duration_reach=avg_session_duration_reach,
            market_segment=market_segment,
            market_users=market_users,
            market_new_users=market_new_users,
            market_sessions=market_sessions,
            market_bounce_rate=market_bounce_rate,
            market_pages_session=market_pages_session,
            market_avg_session_duration=market_avg_session_duration,
            other_category=other_category,
            other_category_users=other_category_users,
            other_category_new_users=other_category_new_users,
            other_category_sessions=other_category_sessions,
            other_category_bounce_rate=other_category_bounce_rate,
            other_category_pages_session=other_category_pages_session,
            other_category_avg_session_duration=other_category_avg_session_duration,
            landing_page=landing_page,
            landing_sessions=landing_sessions,
            #landing_new_session=landing_new_session,
            landing_new_users=landing_new_users,
            landing_bounce_rate=landing_bounce_rate,
            landing_page_session=landing_page_session,
            landing_avg_session_duration=landing_avg_session_duration,
            language=language,
            language_users=language_users,
            language_new_users=language_new_users,
            language_sessions=language_sessions,
            language_bounce_rate=language_bounce_rate,
            language_pages_session=language_pages_session,
            language_avg_session_duration=language_avg_session_duration,
            audience=audience,
            audience_users=audience_users,
            audience_new_users=audience_new_users,
            audience_sessions=audience_sessions,
            audience_bounce_rate=audience_bounce_rate,
            audience_pages_session=audience_pages_session,
            audience_avg_session_duration=audience_avg_session_duration,
            browser_bounce_rate=browser_bounce_rate,
            browser_pages_session=browser_pages_session,
            #browser_pages_session=browser_pages_session,
            default_channel_grouping=default_channel_grouping,
            default_channel_users=default_channel_users,
            default_channel_new_users=default_channel_new_users,
            default_channel_sessions=default_channel_sessions,
            default_channel_bounce_rate=default_channel_bounce_rate,
            default_channel_pages_session=default_channel_pages_session,
            default_channel_avg_session_duration=default_channel_avg_session_duration,
            page_path_level1=page_path_level1,
            page_view=page_view,
            unique_page_view=unique_page_view,
            avg_time_on_page=avg_time_on_page,
            bounce_rate=bounce_rate,
            exit_percent=exit_percent,
            country_impressions=country_impressions,
            country_clicks=country_clicks,
            country_ctr=country_ctr,
            country_average_position=country_average_position,
            country_sessions=country_sessions,
            #country_bounce_rate1=country_bounce_rate1,
            country_pages_session=country_pages_session,
            all_website_device_category=all_website_device_category,
            all_website_impressions=all_website_impressions,
            all_website_clicks=all_website_clicks,
            all_website_ctr=all_website_ctr,
            all_website_average_position=all_website_average_position,
            all_website_sessions=all_website_sessions,
            all_website_bounce_rate=all_website_bounce_rate,
            all_website_pages_session=all_website_pages_session,
            mobile_device_info=mobile_device_info,
            mobile_device_users=mobile_device_users,
            mobile_device_new_users=mobile_device_new_users,
            mobile_device_sessions=mobile_device_sessions,
            mobile_device_bounce_rate=mobile_device_bounce_rate,
            mobile_device_avg_session_duration=mobile_device_avg_session_duration,
            session_duration_bucket=session_duration_bucket,
            bucket_session=bucket_session,
            bucket_page_views=bucket_page_views,
            source_medium=source_medium,
            medium_users=medium_users,
            medium_new_users=medium_new_users,
            medium_sessions=medium_sessions,
            medium_bounce_rate=medium_bounce_rate,
            medium_pages_session=medium_pages_session,
            medium_avg_session_duration=medium_avg_session_duration
            )

        messages.success(request, 'Data uploaded successfully')
        return redirect('analytics_data')

    else:
        ad_data = AnalyticData.objects.all()
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
        return render(request, 'Analytics.html', {'page_obj': page_obj,  'rows_per_page': rows_per_page})
        # return render(request, 'Analytics.html', {'ad_data': ad_data})

def delete_selected_rows(request):
    if request.method == 'POST':
        ids = request.POST.getlist('ids[]')
        try:
            # Delete the selected rows from the database
            AnalyticData.objects.filter(id__in=ids).delete()
            return JsonResponse({'success': True})
        except:
            return JsonResponse({'success': False})

def Analytic_Dasboard(request):
    id = request.GET.get('id')  # Get the 'id' parameter from the request's query parameters

    if id:
        try:
            data = AnalyticData.objects.get(id=id)  # Retrieve the data from the database based on the 'id' parameter
            # Process the retrieved data or pass it to the template
            return render(request, 'Analytics_Dashboard.html', {'data': data})
        except AnalyticData.DoesNotExist:
            # Handle the case when the data with the provided 'id' doesn't exist
            return render(request, 'error.html', {'message': 'Data not found'})
    else:
        # Handle the case when the 'id' parameter is not provided
        return render(request, 'error.html', {'message': 'ID parameter is missing'})

    # Retrieve data from the database
data = AnalyticData.objects.all()  # Replace AdwordData with the actual model representing your data

import plotly.graph_objects as go
from plotly.offline import plot

def Analytic_Dasboard(request):
    id = request.GET.get('id')  # Get the 'id' parameter from the request's query parameters

    if id:
        try:
            data = AnalyticData.objects.get(id=id)  # Retrieve the data from the database based on the 'id' parameter
            # Process the retrieved data or pass it to the template
            return render(request, 'Analytics_Dashboard.html', {'data': data})
        except AnalyticData.DoesNotExist:
            # Handle the case when the data with the provided 'id' doesn't exist
            return render(request, 'error.html', {'message': 'Data not found'})
    else:
        # Handle the case when the 'id' parameter is not provided
        return render(request, 'error.html', {'message': 'ID parameter is missing'})



# With Overlapping
# def Analytics_Dashboard(request):
#     # Retrieve data from the database
#     data = AnalyticData.objects.all()

#     # Extract values for the required columns
#     countries = [entry.country for entry in data]
#     new_users = [entry.country_new_users for entry in data]

#     # Remove commas from new_users values and convert to floats
#     new_users = [float(val.replace(',', '')) if val else 0.0 for val in new_users]

#     # Sort the data based on the new_users values in ascending order
#     sorted_data = sorted(zip(new_users, countries))
#     sorted_new_users, sorted_countries = zip(*sorted_data)

#     # Create the Plotly bar graph
#     fig = go.Figure()
#     fig.add_trace(go.Bar(x=sorted_countries, y=sorted_new_users, name='Country New Users',marker=dict(color='green')))

#     # Update axis labels and layout
#     fig.update_xaxes(title_text='Country')
#     fig.update_yaxes(title_text='New Users')
#     fig.update_layout(title='Country New Users')
#     # Convert the Plotly figure to HTML
#     graph_html = plot(fig, output_type='div')

#     # return render(request, 'Analytics_Dashboard.html', {'graph_html': graph_html})

# # Graph2
# # def Analytics_Dashboard(request):
#     # Retrieve data from the database
#     # data = AnalyticData.objects.all()

#     # Extract values for the required columns
#     device_categories = [entry.device_category for entry in data]
#     device_users = [entry.device_users for entry in data]

#     # Remove commas from device_users values and convert to floats
#     device_users = [float(val.replace(',', '')) if val else 0.0 for val in device_users]

#     # Sort the data based on the device_users values in ascending order
#     sorted_data = sorted(zip(device_users, device_categories))
#     sorted_device_users, sorted_device_categories = zip(*sorted_data)

#     # Create the Plotly bar graph
#     fig1 = go.Figure()
#     fig1.add_trace(go.Bar(x=sorted_device_categories, y=sorted_device_users, name='Device Users', marker=dict(color='green')))

#     # Update axis labels and layout
#     fig1.update_xaxes(title_text='Device Category')
#     fig1.update_yaxes(title_text='Device Users')
#     fig1.update_layout(title='Device Users by Category')

#     # Convert the Plotly figure to HTML
#     graph_html1 = plot(fig1, output_type='div')
#     return render(request, 'Analytics_Dashboard.html', {'graph_html':graph_html,'graph_html1': graph_html1})
    # return render(request, 'Analytics_Dashboard.html', {'graph_html2': graph_html2})

# without overlapping
def Analytics_Dashboard(request):
    # Retrieve data from the database
    data = AnalyticData.objects.all()

    # Extract values for the required columns
    countries = [entry.country for entry in data]
    new_users = [entry.country_new_users for entry in data]
    device_categories = [entry.device_category for entry in data]
    device_users = [entry.device_users for entry in data]

    # Remove commas from new_users and device_users values and convert to floats
    new_users = [float(val.replace(',', '')) if val else 0.0 for val in new_users]
    device_users = [float(val.replace(',', '')) if val else 0.0 for val in device_users]

    # Sort the data based on the new_users values in ascending order
    sorted_countries, sorted_new_users = zip(*sorted(zip(countries, new_users)))
    # Graph 3
    # Extract values for the required columns
    search_queries = [entry.search_query for entry in data]
    search_clicks = [entry.search_clicks for entry in data]
    search_impressions = [entry.search_impressions for entry in data]

    # Create the Plotly bar graph for Country New Users
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=sorted_countries, y=sorted_new_users, name='Country New Users', marker=dict(color='lightgreen')))
    fig1.update_xaxes(title_text='Country')
    fig1.update_yaxes(title_text='New Users')
    fig1.update_layout(title='Country New Users')
    graph_html1 = plot(fig1, output_type='div')

    # Create the Plotly bar graph for Device Users
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=device_categories, y=device_users, name='Device Users', marker=dict(color='lightgreen')))
    fig2.update_xaxes(title_text='Device Category')
    fig2.update_yaxes(title_text='Device Users')
    fig2.update_layout(title='Device Users by Category')
    graph_html2 = plot(fig2, output_type='div')

     # Create the Plotly figure with subplots
    fig3 = make_subplots(specs=[[{"secondary_y": True}]])

    fig3.add_trace(go.Scatter(x=search_queries, y=search_clicks, name='Search Clicks', mode='lines+markers',
                             marker=dict(color='green', size=10, symbol='circle')))
    fig3.add_trace(go.Scatter(x=search_queries, y=search_impressions, name='Search Impressions', mode='lines+markers',
                             marker=dict(color='blue', size=10, symbol='circle')))

    fig3.update_layout(title='Search Metrics')
    fig3.update_xaxes(title_text='Search Query')
    fig3.update_yaxes(title_text='Search Clicks', secondary_y=False)
    fig3.update_yaxes(title_text='Search Impressions', secondary_y=True)

    fig3.update_traces(text=search_clicks, textposition='top center', textfont=dict(color='green'), selector=dict(name='Search Clicks'))
    fig3.update_traces(text=search_impressions, textposition='top center', textfont=dict(color='blue'), selector=dict(name='Search Impressions'))

    # Add lines to the traces
    fig3.update_traces(mode='lines+markers', selector=dict(mode='lines+markers'))

    # Convert the Plotly figure to HTML
    graph_html3 = fig3.to_html(full_html=False)
    # Convert the Plotly figure to HTML
    graph_html3 = plot(fig3, output_type='div')
    return render(request, 'Analytics_Dashboard.html', {'graph_html1': graph_html1, 'graph_html2': graph_html2,'graph_html3':graph_html3})





    