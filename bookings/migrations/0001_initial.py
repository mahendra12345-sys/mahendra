# Generated by Django 5.1.6 on 2025-03-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('hotel_name', models.CharField(blank=True, max_length=255, null=True)),
                ('car_rental', models.BooleanField(default=False)),
            ],
        ),
    ]
