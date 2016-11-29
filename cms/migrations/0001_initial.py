# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=1023, verbose_name='Title')),
                ('authors', models.CharField(max_length=1023, blank=True, verbose_name='Authors')),
                ('references', models.CharField(max_length=1023, blank=True, verbose_name='References')),
                ('num_of_pages', models.IntegerField(blank=True, default=0, verbose_name='Number of pages')),
                ('year', models.IntegerField(blank=True, default=0, verbose_name='Year')),
                ('URL', models.CharField(max_length=1023, blank=True, verbose_name='URL')),
                ('abstract', models.CharField(max_length=4095, blank=True, verbose_name='Abstract')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('reporter', models.CharField(max_length=255, verbose_name='Reporter')),
                ('date', models.DateField(verbose_name='Date')),
                ('motivations', models.CharField(max_length=4095, blank=True, verbose_name='Motivations')),
                ('contributions', models.CharField(max_length=4095, blank=True, verbose_name='Contributions')),
                ('questions', models.CharField(max_length=4095, blank=True, verbose_name='Questions and Future works')),
                ('paper', models.ForeignKey(related_name='reports', verbose_name='Paper', to='cms.Paper')),
            ],
        ),
    ]
