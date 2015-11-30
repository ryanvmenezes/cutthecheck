# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0005_auto_20151130_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='total_cap_hit',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
