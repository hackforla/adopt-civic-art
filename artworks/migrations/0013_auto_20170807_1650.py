# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0012_auto_20170804_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtworkMedium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medium', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ArtworkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='artwork',
            name='artwork_type',
        ),
        migrations.AlterField(
            model_name='artwork',
            name='creation_date',
            field=models.IntegerField(help_text='Enter a year in YYYY format, like 1978 or 2017'),
        ),
        migrations.RemoveField(
            model_name='artwork',
            name='medium',
        ),
        migrations.AlterField(
            model_name='artwork',
            name='show_date_description',
            field=models.BooleanField(default=False, help_text='Checking this will show the date description         instead of creation date on the artwork page'),
        ),
        migrations.AddField(
            model_name='artwork',
            name='artwork_type',
            field=models.ManyToManyField(to='artworks.ArtworkType'),
        ),
        migrations.AddField(
            model_name='artwork',
            name='medium',
            field=models.ManyToManyField(to='artworks.ArtworkMedium'),
        ),
    ]