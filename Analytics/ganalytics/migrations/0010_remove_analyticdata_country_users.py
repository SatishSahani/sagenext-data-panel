# Generated by Django 4.1.7 on 2023-08-03 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ganalytics", "0009_analyticdata_country_users"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="analyticdata",
            name="country_users",
        ),
    ]