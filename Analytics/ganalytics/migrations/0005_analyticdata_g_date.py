# Generated by Django 4.1.7 on 2023-07-26 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ganalytics", "0004_remove_analyticdata_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="analyticdata",
            name="g_date",
            field=models.CharField(default="null", max_length=100),
        ),
    ]
