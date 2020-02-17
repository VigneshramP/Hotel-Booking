# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booked',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('smoking', models.BooleanField()),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('requirement', models.TextField()),
                ('payment', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('star', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=60)),
                ('province', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
                ('total', models.FloatField()),
                ('date', models.DateTimeField(verbose_name=b'Order Date')),
                ('code', models.CharField(max_length=45)),
                ('client', models.ForeignKey(to='hotels.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('adult', models.IntegerField()),
                ('children', models.IntegerField()),
                ('price', models.FloatField()),
                ('roomNumber', models.IntegerField()),
                ('belongto', models.ForeignKey(to='hotels.Hotel')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='located',
            field=models.ForeignKey(to='hotels.Location'),
        ),
        migrations.AddField(
            model_name='booked',
            name='order',
            field=models.ForeignKey(to='hotels.Order'),
        ),
        migrations.AddField(
            model_name='booked',
            name='room',
            field=models.ForeignKey(to='hotels.Room'),
        ),
    ]
