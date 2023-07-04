# Generated by Django 4.1.7 on 2023-06-28 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gadwords", "0002_adworddata"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AdData",
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="campaign1_conversions",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="campaign1_cost",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="campaign1_cost_per_conv",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="campaign_clicks",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="campaign_cost",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="campaign_interactions",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="clicks",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="conversions",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="cost",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="cost_per_conv",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="date",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="demographics_impressions",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="demographics_total_percent",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="device_clicks",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="device_cost",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="device_impressions",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="network_avg_cpc",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="network_clicks",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="network_cost",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="optimisation_score",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="per_day_impression",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="per_day_per_hour_impression",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="per_hour_impression",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="search_clicks",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="search_conversion",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="search_cost",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="search_impressions",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="search_keyword_clicks",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="search_keyword_cost",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="search_keyword_ctr",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="search_word_clicks",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="search_word_conversions",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="search_word_cost",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adworddata",
            name="search_word_impressions",
            field=models.CharField(max_length=100),
        ),
    ]
