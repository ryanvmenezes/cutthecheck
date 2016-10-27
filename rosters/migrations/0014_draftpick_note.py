# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0013_auto_20161026_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='draftpick',
            name='note',
            field=models.CharField(help_text=b'Note aboute this pick', max_length=500, null=True),
        ),
    ]
