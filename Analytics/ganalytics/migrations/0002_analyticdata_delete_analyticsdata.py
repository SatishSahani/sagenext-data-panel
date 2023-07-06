# Generated by Django 4.1.7 on 2023-06-28 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ganalytics", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AnalyticData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("country", models.CharField(max_length=100)),
                ("country_new_users", models.CharField(max_length=100)),
                ("country_benchmark_new_users", models.CharField(max_length=100)),
                ("country_page_sessions", models.CharField(max_length=100)),
                ("country_avg_session_duration", models.CharField(max_length=100)),
                ("country_benchmark_bounce_rate", models.CharField(max_length=100)),
                ("device_category", models.CharField(max_length=100)),
                ("device_users", models.CharField(max_length=100)),
                ("device_new_users", models.CharField(max_length=100)),
                ("device_sessions", models.CharField(max_length=100)),
                ("device_bounce_rate", models.CharField(max_length=100)),
                ("device_page_session", models.CharField(max_length=100)),
                ("search_query", models.CharField(max_length=100)),
                ("search_clicks", models.CharField(max_length=100)),
                ("search_impressions", models.CharField(max_length=100)),
                ("search_ctr", models.CharField(max_length=100)),
                ("search_avg_position", models.CharField(max_length=100)),
                ("site_search_new_users", models.CharField(max_length=100)),
                ("site_search_bounce_rate", models.CharField(max_length=100)),
                ("site_search_page_session", models.CharField(max_length=100)),
                ("site_search_avg_session_duration", models.CharField(max_length=100)),
                ("site_search_transaction", models.CharField(max_length=100)),
                ("site_search_revenue", models.CharField(max_length=100)),
                (
                    "site_search_e_commerce_conversion_rate",
                    models.CharField(max_length=100),
                ),
                ("goal_completion_location", models.CharField(max_length=100)),
                ("goal_completions", models.CharField(max_length=100)),
                ("page", models.CharField(max_length=100)),
                ("avg_page_load_time_sec", models.CharField(max_length=100)),
                ("page_per_views", models.CharField(max_length=100)),
                ("page_bounce_rate", models.CharField(max_length=100)),
                ("page_exit", models.CharField(max_length=100)),
                ("event_category", models.CharField(max_length=100)),
                ("event_total_events", models.CharField(max_length=100)),
                ("event_unique_events", models.CharField(max_length=100)),
                ("page_event", models.CharField(max_length=100)),
                ("page_total_events", models.CharField(max_length=100)),
                ("page_unique_events", models.CharField(max_length=100)),
                ("campaign_campaign_id", models.CharField(max_length=100)),
                ("campaign_clicks", models.CharField(max_length=100)),
                ("campaign_cost", models.CharField(max_length=100)),
                ("campaign_cpc", models.CharField(max_length=100)),
                ("campaign_users", models.CharField(max_length=100)),
                ("campaign_sessions", models.CharField(max_length=100)),
                ("campaign_bounce_rate", models.CharField(max_length=100)),
                ("campaign_pages_session", models.CharField(max_length=100)),
                ("final_url", models.CharField(max_length=100)),
                ("url_clicks", models.CharField(max_length=100)),
                ("url_cost", models.CharField(max_length=100)),
                ("url_cpc", models.CharField(max_length=100)),
                ("url_users", models.CharField(max_length=100)),
                ("url_sessions", models.CharField(max_length=100)),
                ("url_bounce_rate", models.CharField(max_length=100)),
                ("url_page_session", models.CharField(max_length=100)),
                ("per_hour", models.CharField(max_length=100)),
                ("per_hour_users", models.CharField(max_length=100)),
                ("per_hour_new_users", models.CharField(max_length=100)),
                ("per_hour_sessions", models.CharField(max_length=100)),
                ("per_hour_bounce_rate", models.CharField(max_length=100)),
                ("per_hour_pages_session", models.CharField(max_length=100)),
                ("per_hour_avg_session_duration", models.CharField(max_length=100)),
                ("affinity_category_reach", models.CharField(max_length=100)),
                ("users_reach", models.CharField(max_length=100)),
                ("new_users_reach", models.CharField(max_length=100)),
                ("sessions_reach", models.CharField(max_length=100)),
                ("bounce_rate_reach", models.CharField(max_length=100)),
                ("pages_session_reach", models.CharField(max_length=100)),
                ("avg_session_duration_reach", models.CharField(max_length=100)),
                ("market_segment", models.CharField(max_length=100)),
                ("market_users", models.CharField(max_length=100)),
                ("market_new_users", models.CharField(max_length=100)),
                ("market_sessions", models.CharField(max_length=100)),
                ("market_bounce_rate", models.CharField(max_length=100)),
                ("market_pages_session", models.CharField(max_length=100)),
                ("market_avg_session_duration", models.CharField(max_length=100)),
                ("other_category", models.CharField(max_length=100)),
                ("other_category_users", models.CharField(max_length=100)),
                ("other_category_new_users", models.CharField(max_length=100)),
                ("other_category_sessions", models.CharField(max_length=100)),
                ("other_category_bounce_rate", models.CharField(max_length=100)),
                ("other_category_pages_session", models.CharField(max_length=100)),
                (
                    "other_category_avg_session_duration",
                    models.CharField(max_length=100),
                ),
                ("landing_page", models.CharField(max_length=100)),
                ("landing_sessions", models.CharField(max_length=100)),
                ("landing_new_sessions", models.CharField(max_length=100)),
                ("landing_new_users", models.CharField(max_length=100)),
                ("landing_bounce_rate", models.CharField(max_length=100)),
                ("landing_page_session", models.CharField(max_length=100)),
                ("landing_avg_session_duration", models.CharField(max_length=100)),
                ("language", models.CharField(max_length=100)),
                ("language_users", models.CharField(max_length=100)),
                ("language_new_users", models.CharField(max_length=100)),
                ("language_sessions", models.CharField(max_length=100)),
                ("language_bounce_rate", models.CharField(max_length=100)),
                ("language_pages_session", models.CharField(max_length=100)),
                ("language_avg_session_duration", models.CharField(max_length=100)),
                ("audience", models.CharField(max_length=100)),
                ("audience_users", models.CharField(max_length=100)),
                ("audience_new_users", models.CharField(max_length=100)),
                ("audience_sessions", models.CharField(max_length=100)),
                ("audience_bounce_rate", models.CharField(max_length=100)),
                ("audience_pages_session", models.CharField(max_length=100)),
                ("audience_avg_session_duration", models.CharField(max_length=100)),
                ("browser_bounce_rate", models.CharField(max_length=100)),
                ("browser_pages_session", models.CharField(max_length=100)),
                ("default_channel_grouping", models.CharField(max_length=100)),
                ("default_channel_users", models.CharField(max_length=100)),
                ("default_channel_new_users", models.CharField(max_length=100)),
                ("default_channel_sessions", models.CharField(max_length=100)),
                ("default_channel_bounce_rate", models.CharField(max_length=100)),
                ("default_channel_pages_session", models.CharField(max_length=100)),
                (
                    "default_channel_avg_session_duration",
                    models.CharField(max_length=100),
                ),
                ("page_path_level1", models.CharField(max_length=100)),
                ("page_view", models.CharField(max_length=100)),
                ("unique_page_view", models.CharField(max_length=100)),
                ("avg_time_on_page", models.CharField(max_length=100)),
                ("bounce_rate", models.CharField(max_length=100)),
                ("exit_percent", models.CharField(max_length=100)),
                ("country_impressions", models.CharField(max_length=100)),
                ("country_clicks", models.CharField(max_length=100)),
                ("country_ctr", models.CharField(max_length=100)),
                ("country_average_position", models.CharField(max_length=100)),
                ("country_sessions", models.CharField(max_length=100)),
                ("country_bounce_rate", models.CharField(max_length=100)),
                ("country_pages_session", models.CharField(max_length=100)),
                ("all_website_device_category", models.CharField(max_length=100)),
                ("all_website_impressions", models.CharField(max_length=100)),
                ("all_website_clicks", models.CharField(max_length=100)),
                ("all_website_ctr", models.CharField(max_length=100)),
                ("all_website_average_position", models.CharField(max_length=100)),
                ("all_website_sessions", models.CharField(max_length=100)),
                ("all_website_bounce_rate", models.CharField(max_length=100)),
                ("all_website_pages_session", models.CharField(max_length=100)),
                ("mobile_device_info", models.CharField(max_length=100)),
                ("mobile_device_users", models.CharField(max_length=100)),
                ("mobile_device_new_users", models.CharField(max_length=100)),
                ("mobile_device_sessions", models.CharField(max_length=100)),
                ("mobile_device_bounce_rate", models.CharField(max_length=100)),
                (
                    "mobile_device_avg_session_duration",
                    models.CharField(max_length=100),
                ),
                ("session_duration_bucket", models.CharField(max_length=100)),
                ("bucket_session", models.CharField(max_length=100)),
                ("bucket_page_views", models.CharField(max_length=100)),
                ("source_medium", models.CharField(max_length=100)),
                ("medium_users", models.CharField(max_length=100)),
                ("medium_new_users", models.CharField(max_length=100)),
                ("medium_sessions", models.CharField(max_length=100)),
                ("medium_bounce_rate", models.CharField(max_length=100)),
                ("medium_pages_session", models.CharField(max_length=100)),
                ("medium_avg_session_duration", models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name="AnalyticsData",
        ),
    ]