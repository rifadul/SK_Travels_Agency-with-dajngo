# Generated by Django 3.1.4 on 2020-12-09 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Create_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('hotel_name', models.CharField(max_length=50)),
                ('number_of_adults', models.IntegerField(default='0', max_length=15)),
                ('number_of_childen', models.IntegerField(default='0', max_length=15)),
                ('number_of_room', models.IntegerField(default='0', max_length=15)),
                ('cheek_in_date', models.CharField(default='', max_length=15)),
                ('cheek_in_out', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('bank_card_name', models.CharField(max_length=30)),
                ('bank_card_no', models.CharField(max_length=30)),
                ('bank_card_expiration', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tour_booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('tourist_place', models.CharField(max_length=50)),
                ('pakage_price', models.IntegerField(default='0', max_length=15)),
                ('number_of_adults', models.IntegerField(default='0', max_length=15)),
                ('number_of_childen', models.IntegerField(default='0', max_length=15)),
                ('payment_method', models.CharField(default='', max_length=15)),
                ('payment_mobile_number', models.CharField(max_length=15)),
                ('payment_transaction_number', models.CharField(max_length=50)),
                ('payment_amount', models.IntegerField(max_length=15)),
            ],
        ),
    ]
