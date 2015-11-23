# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0002_auto_20151123_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='manager',
            field=models.ForeignKey(to='rosters.Squad'),
        ),
    ]
