# Generated by Django 5.0.3 on 2024-06-24 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0011_historicallocationmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoricalLocationModel',
        ),
    ]
