# Generated by Django 5.0.3 on 2024-06-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sos_history', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsoshistory',
            name='phone_numbers',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='soshistory',
            name='phone_numbers',
            field=models.CharField(max_length=500),
        ),
    ]