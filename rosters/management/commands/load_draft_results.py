import csv
from django.core.management.base import BaseCommand
from rosters.models import Player, Squad, LastUpdated, DraftPick
from datetime import datetime


class Command(BaseCommand):
    '''
    docstring
    '''
    def handle(self, *args, **options):

        draft = []
        with open('rosters/management/commands/league_draft.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                squad_obj = Squad.objects.get(manager=row['manager'])
                player_obj = Player.objects.get(full_name=row['player'])
                print "trying {} {} {} {}".format(
                    row['draft_round'],row['draft_pick'],row['manager'],row['player']
                )
                pick_obj = DraftPick.objects.get(
                    draft_round=row['draft_round'],
                    draft_pick=row['draft_pick'],
                    squad=squad_obj,
                )
                pick_obj.player = player_obj
                pick_obj.save()

        for d in DraftPick.objects.all():
            print "loaded {} {} {} {}".format(
                d.draft_round,
                d.draft_pick,
                d.squad,
                d.player
            )
