# Generated by Django 3.1.5 on 2021-03-26 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_auto_20210323_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='type_of_Place',
            field=models.CharField(max_length=15),
        ),
    ]
