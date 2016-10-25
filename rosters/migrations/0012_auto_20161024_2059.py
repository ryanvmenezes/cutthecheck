# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0011_auto_20161024_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='draft_pick',
            field=models.IntegerField(help_text=b'Pick within round this player was drafted', null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)]),
        ),
        migrations.AlterField(
            model_name='player',
            name='draft_round',
            field=models.IntegerField(help_text=b'Round this player was drafted', null=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)]),
        ),
    ]
