# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_paper_num_of_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='num_of_pages',
            field=models.IntegerField(verbose_name='num_of_pages', blank=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='year',
            field=models.IntegerField(verbose_name='Year', blank=True),
        ),
    ]
