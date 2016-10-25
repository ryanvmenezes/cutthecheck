# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0010_auto_20161024_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='draft_pick',
            field=models.IntegerField(help_text=b'Pick within round this player was drafted', null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='draft_round',
            field=models.IntegerField(help_text=b'Round this player was drafted', null=True),
        ),
    ]
