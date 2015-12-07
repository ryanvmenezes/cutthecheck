# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0006_squad_total_cap_hit'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastUpdated',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.DateTimeField(null=True)),
            ],
        ),
    ]
