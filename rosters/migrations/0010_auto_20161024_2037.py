# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0009_auto_20161024_2036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['-salary']},
        ),
        migrations.RenameField(
            model_name='player',
            old_name='salary_1516',
            new_name='salary',
        ),
    ]
