# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(help_text=b"NBA player's name", max_length=150, null=True)),
                ('nba_team', models.CharField(help_text=b"NBA player's team", max_length=150, null=True)),
                ('salary_1516', models.IntegerField(help_text=b'Cap hit for this player')),
            ],
        ),
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manager', models.CharField(help_text=b'Who helms this ship', max_length=150, null=True, choices=[(b'Austin', b'Austin'), (b'Sam', b'Sam'), (b'Eli', b'Eli'), (b'Pedro', b'Pedro'), (b'Zach', b'Zach'), (b'Everett', b'Everett'), (b'Kartje', b'Kartje'), (b'Menezes', b'Menezes'), (b'Justin', b'Justin'), (b'Vineeth', b'Vineeth')])),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='manager',
            field=models.OneToOneField(to='rosters.Squad'),
        ),
    ]
