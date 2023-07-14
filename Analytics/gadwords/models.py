from django.db import models
from datetime import datetime


# # Create your models here.
# class AdData(models.Model):
#     month = models.CharField(max_length=20)
#     impression = models.PositiveIntegerField()
#     cost = models.DecimalField(max_digits=10, decimal_places=2)
#     conversions = models.DecimalField(max_digits=10, decimal_places=2)
#     bookings = models.PositiveIntegerField()

# Create your models here.
from django.db import models

class AdwordData(models.Model):
    date = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    network_clicks = models.CharField(max_length=100)
    network_cost = models.CharField(max_length=100)
    network_avg_cpc = models.CharField(max_length=100)
    campaign_name = models.CharField(max_length=100)
    campaign_adgroup_name = models.CharField(max_length=100)
    campaign_cost = models.CharField(max_length=100)
    campaign_cost_comparison = models.CharField(max_length=100)
    campaign_clicks = models.CharField(max_length=100)
    campaign_clicks_comparison = models.CharField(max_length=100)
    campaign_interactions = models.CharField(max_length=100)
    interaction_comparison = models.CharField(max_length=100)
    campaign1_name = models.CharField(max_length=100)
    campaign1_campaign_group_name = models.CharField(max_length=100)
    campaign1_campaign_status = models.CharField(max_length=100)
    campaign1_cost = models.CharField(max_length=100)
    campaign1_conversions = models.CharField(max_length=100)
    campaign1_cost_per_conv = models.CharField(max_length=100)
    search = models.CharField(max_length=100)
    search_cost = models.CharField(max_length=100)
    search_clicks = models.CharField(max_length=100)
    search_impressions = models.CharField(max_length=100)
    search_conversion = models.CharField(max_length=100)
    search_word = models.CharField(max_length=100)
    search_word_clicks = models.CharField(max_length=100)
    search_word_impressions = models.CharField(max_length=100)
    search_word_conversions = models.CharField(max_length=100)
    search_word_cost = models.CharField(max_length=100)
    search_word_top_containing_queries = models.CharField(max_length=100)
    search_keyword = models.CharField(max_length=100)
    search_keyword_match_type = models.CharField(max_length=100)
    search_keyword_criterion_status = models.CharField(max_length=100)
    search_keyword_campaign_status = models.CharField(max_length=100)
    search_keyword_adgroup_status = models.CharField(max_length=100)
    search_keyword_cost = models.CharField(max_length=100)
    search_keyword_clicks = models.CharField(max_length=100)
    search_keyword_ctr = models.CharField(max_length=100)
    demographics_gender = models.CharField(max_length=100)
    demographics_age_range = models.CharField(max_length=100)
    demographics_impressions = models.CharField(max_length=100)
    demographics_total_percent = models.CharField(max_length=100)
    device = models.CharField(max_length=100)
    device_cost = models.CharField(max_length=100)
    device_clicks = models.CharField(max_length=100)
    device_impressions = models.CharField(max_length=100)
    clicks = models.CharField(max_length=100)
    conversions = models.CharField(max_length=100)
    cost_per_conv = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    per_hour = models.CharField(max_length=100)
    per_hour_impression = models.CharField(max_length=100)
    per_day = models.CharField(max_length=100)
    per_day_impression = models.CharField(max_length=100)
    per_day_per_hour = models.CharField(max_length=100)
    per_day_per_hour_impression = models.CharField(max_length=100)
    optimisation_score = models.CharField(max_length=100)
    optimisation_score_campaign_name = models.CharField(max_length=100)



    def __str__(self):
        return self.date


    # def __str__(self):
    #     return self.month
    

