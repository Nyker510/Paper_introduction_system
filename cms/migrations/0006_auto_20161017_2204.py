# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20161017_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='reporter',
            field=models.CharField(verbose_name='Reporter', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='num_of_pages',
            field=models.IntegerField(verbose_name='num_of_pages', default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='year',
            field=models.IntegerField(verbose_name='Year', default=0, blank=True),
        ),
    ]
