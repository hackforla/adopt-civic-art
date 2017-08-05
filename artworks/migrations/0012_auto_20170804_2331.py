# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-05 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0011_auto_20170803_2013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkindamage',
            options={'verbose_name': 'Check In Damage Description'},
        ),
        migrations.AddField(
            model_name='artwork',
            name='show_date_description',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='creation_date',
            field=models.IntegerField(help_text='Enter a year in YYYY format, like "1978" or "2017"'),
        ),
    ]