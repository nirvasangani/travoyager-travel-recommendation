# Generated by Django 3.0.6 on 2021-03-28 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0009_user_input_status'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='itinerary',
            unique_together={('place_id', 'trip_id', 'arrival_DnT')},
        ),
    ]