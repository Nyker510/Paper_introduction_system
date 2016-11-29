# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.CharField(max_length=255, verbose_name='Reporter'),
        ),
    ]
