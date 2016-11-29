# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20161021_0123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='recommended',
        ),
    ]
