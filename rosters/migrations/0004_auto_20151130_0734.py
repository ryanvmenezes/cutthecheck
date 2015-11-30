# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0003_auto_20151123_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='salary_1516',
            field=models.IntegerField(help_text=b'Cap hit for this player', null=True),
        ),
        migrations.AlterField(
            model_name='squad',
            name='manager',
            field=models.CharField(help_text=b'Who helms this ship', max_length=150, null=True, choices=[(b'Austin', b'Austin Manapsal'), (b'sam', b'Sam Tesconi'), (b'eli', b'Eli Smukler'), (b'Pedro Moura', b'Pedro Moura'), (b'Zach', b'Zach Helfand'), (b'Everett', b'Everett Cook'), (b'Ryan Kartje', b'Ryan Kartje'), (b'Ryan', b'Ryan Menezes'), (b'Justin', b'Justin Cerri'), (b'Vineeth', b'Vineeth Pillai')]),
        ),
    ]
