# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0012_auto_20161024_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='DraftPick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('draft_round', models.IntegerField(help_text=b'Round this player was drafted', null=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)])),
                ('draft_pick', models.IntegerField(help_text=b'Pick within round this player was drafted', null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='player',
            name='draft_pick',
        ),
        migrations.RemoveField(
            model_name='player',
            name='draft_round',
        ),
        migrations.AddField(
            model_name='draftpick',
            name='player',
            field=models.ForeignKey(to='rosters.Player', null=True),
        ),
        migrations.AddField(
            model_name='draftpick',
            name='squad',
            field=models.ForeignKey(to='rosters.Squad', null=True),
        ),
    ]
