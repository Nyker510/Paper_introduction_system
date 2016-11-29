# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20161017_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='num_of_pages',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='reporter',
        ),
        migrations.AddField(
            model_name='paper',
            name='reading',
            field=models.CharField(verbose_name='Reading', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='paper',
            name='recommended',
            field=models.BooleanField(verbose_name='Recommended', default=False),
        ),
        migrations.AlterField(
            model_name='paper',
            name='pages',
            field=models.CharField(verbose_name='Pages', blank=True, max_length=255),
        ),
    ]
