# Generated by Django 3.1.4 on 2020-12-09 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tourist_place', '0002_destinations_overview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel_rating_in_star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_star', models.CharField(default='0', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(default='', max_length=200)),
                ('hotel_location', models.CharField(default='', max_length=100)),
                ('hotel_sort_description', models.CharField(default='', max_length=100)),
                ('hotel_description', models.TextField(default='', max_length=1000)),
                ('hotel_facility', models.TextField(default='', max_length=1000)),
                ('hotel_room_price', models.IntegerField(default=0)),
                ('hotel_image', models.ImageField(upload_to='upload/hotel_image/')),
                ('category_location', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tourist_place.locations')),
                ('hotel_star', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel_rating_in_star')),
            ],
        ),
    ]
