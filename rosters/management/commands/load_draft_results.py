import csv
from django.core.management.base import BaseCommand
from rosters.models import Player, Squad, LastUpdated, DraftPick
from django.db.models import Sum
from django.utils import timezone


class Command(BaseCommand):
    '''
    docstring
    '''
    def handle(self, *args, **options):

        with open('rosters/management/commands/draft_results.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                squad_obj = Squad.objects.get(manager=row['manager'])

                player_obj = Player.objects.get(full_name=row['player'])
                player_obj.manager = squad_obj
                player_obj.save()

                squad_obj.total_cap_hit += player_obj.salary

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

        for s in Squad.objects.all():
            print 'summing {}'.format(s)

            players = Player.objects.filter(manager__manager=s.manager)

            if len(players) != 0:
                total = 0
                total += players.aggregate(Sum('salary'))['salary__sum']
                s.total_cap_hit = total
                s.save()
