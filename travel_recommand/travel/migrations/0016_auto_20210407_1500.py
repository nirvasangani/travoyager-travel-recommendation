# Generated by Django 3.0.6 on 2021-04-07 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0015_auto_20210407_1459'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hotel_booking',
            unique_together={('hotel_id', 'trip_id')},
        ),
        migrations.RemoveField(
            model_name='hotel_booking',
            name='ending_date',
        ),
    ]
