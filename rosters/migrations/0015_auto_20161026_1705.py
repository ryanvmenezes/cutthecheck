# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0014_draftpick_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draftpick',
            name='note',
            field=models.CharField(help_text=b'Note about this pick', max_length=500, null=True),
        ),
    ]
