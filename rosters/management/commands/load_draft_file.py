import csv
import os
from django.core.management.base import BaseCommand
from rosters.models import Player, Squad, LastUpdated
from django.utils import timezone

class Command(BaseCommand):
    '''
    docstring
    '''
    def handle(self, *args, **options):

        with open('rosters/management/commands/league_draft.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print "Saving {} to {}".format(row['player'],row['manager'])
                squad_obj = Squad.objects.get(manager=row['manager'])
                player_obj = Player.objects.get(full_name=row['player'])
                player_obj.manager = squad_obj
                player_obj.draft_round = row['draft_round']
                player_obj.draft_pick = row['draft_pick']
                player_obj.save()
                squad_obj.save()

        LastUpdated.objects.all().delete()

        # mark last update
        last_update_obj = LastUpdated(
          last_update=timezone.now()
        )
        last_update_obj.save()
