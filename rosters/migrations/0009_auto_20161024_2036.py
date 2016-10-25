# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0008_auto_20151206_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squad',
            name='manager',
            field=models.CharField(help_text=b'Who helms this ship', max_length=150, null=True, choices=[(b'Austin', b'Austin Manapsal'), (b'sam', b'Sam Tesconi'), (b'eli', b'Eli Smukler'), (b'Pedro Moura', b'Pedro Moura'), (b'Zach', b'Zach Helfand'), (b'Everett', b'Everett Cook'), (b'Ryan Kartje', b'Ryan Kartje'), (b'Ryan', b'Ryan Menezes'), (b'Justin', b'Justin Cerri'), (b'Christian M', b'Christian Mikkelson')]),
        ),
    ]
