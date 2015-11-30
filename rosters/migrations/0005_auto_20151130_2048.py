# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0004_auto_20151130_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='manager',
            field=models.ForeignKey(to='rosters.Squad', null=True),
        ),
    ]
