# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squad',
            name='manager',
            field=models.CharField(help_text=b'Who helms this ship', max_length=150, null=True, choices=[(b'Austin', b'Austin Manapsal'), (b'Sam', b'Sam Tesconi'), (b'Eli', b'Eli Smukler'), (b'Pedro', b'Pedro Moura'), (b'Zach', b'Zach Helfand'), (b'Everett', b'Everett Cook'), (b'Kartje', b'Ryan Kartje'), (b'Menezes', b'Ryan Menezes'), (b'Justin', b'Justin Cerri'), (b'Vineeth', b'Vineeth Pillai')]),
        ),
    ]
