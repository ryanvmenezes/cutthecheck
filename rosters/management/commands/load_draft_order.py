import csv
from django.core.management.base import BaseCommand
from rosters.models import Player, Squad, LastUpdated, DraftPick
from datetime import datetime


class Command(BaseCommand):
    '''
    docstring
    '''
    def handle(self, *args, **options):

        DraftPick.objects.all().delete()
        with open('rosters/management/commands/draft_order.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print 'trying round {} pick {} manager {} with note {}'\
                .format(row['round'],row['pick'],row['manager'],row['note'])

                squad_obj = Squad.objects.get(manager=row['manager'])
                new_pick_obj = DraftPick(
                    draft_round=row['round'],
                    draft_pick=row['pick'],
                    note=row['note'],
                    squad=squad_obj
                )
                new_pick_obj.save()
