# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20161017_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='num_of_pages',
            field=models.IntegerField(blank=True, default=0, verbose_name='num_of_pages'),
        ),
    ]
