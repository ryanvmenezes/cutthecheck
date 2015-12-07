# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0007_lastupdated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['-salary_1516']},
        ),
        migrations.AddField(
            model_name='squad',
            name='slug',
            field=models.SlugField(default='null'),
            preserve_default=False,
        ),
    ]
