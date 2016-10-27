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
                new_pick_obj = DraftPick(
                    draft_round=row['round'],
                    draft_pick=row['pick'],
                    note=row['note'],
                )
                new_pick_obj.save()
                print 'added round {} pick {} with note {}'.format(row['round'],row['pick'],row['note'])
