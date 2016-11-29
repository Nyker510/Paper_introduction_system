# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20161014_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='num_of_pages',
        ),
        migrations.AddField(
            model_name='paper',
            name='pages',
            field=models.CharField(verbose_name='pages', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.TextField(verbose_name='Abstract', blank=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='contributions',
            field=models.TextField(verbose_name='Contributions', blank=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.CharField(verbose_name='Date', max_length=255),
        ),
        migrations.AlterField(
            model_name='report',
            name='motivations',
            field=models.TextField(verbose_name='Motivations', blank=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='questions',
            field=models.TextField(verbose_name='Questions and Future works', blank=True),
        ),
    ]
