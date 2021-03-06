# Generated by Django 3.1.4 on 2020-12-09 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations_overview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_sort_description', models.CharField(default='', max_length=200)),
                ('tour_description', models.TextField(default='', max_length=1000)),
                ('tour_facility', models.TextField(default='', max_length=1000)),
                ('tour_price', models.IntegerField(default=0)),
                ('tour_pakage', models.CharField(default='', max_length=100)),
                ('tour_date', models.CharField(default='', max_length=100)),
                ('tour_image', models.ImageField(upload_to='upload/location_image/')),
                ('tourist_place_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tourist_place.locations')),
            ],
        ),
    ]
