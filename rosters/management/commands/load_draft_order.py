import csv
from django.core.management.base import BaseCommand
from rosters.models import Player, Squad, LastUpdated, DraftPick
from django.db.models import Sum
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
                print 'trying round {} pick {} manager {} player {}'\
                .format(row['round'],row['pick'],row['manager'],row['player'])

                squad_obj = Squad.objects.get(manager=row['manager'])

                if row['player']:
                    player_obj = Player.objects.get(full_name=row['player'])
                    player_obj.manager = squad_obj

                    new_pick_obj = DraftPick(
                        draft_round=row['round'],
                        draft_pick=row['pick'],
                        note=row['note'],
                        squad=squad_obj,
                        player=player_obj,
                    )
                else:
                    new_pick_obj = DraftPick(
                        draft_round=row['round'],
                        draft_pick=row['pick'],
                        note=row['note'],
                        squad=squad_obj,
                    )

                squad_obj.save()
                player_obj.save()
                new_pick_obj.save()

            for s in Squad.objects.all():
                print 'summing {}'.format(s)

                players = Player.objects.filter(manager__manager=s.manager)

                if len(players) != 0:
                    total = 0
                    total += players.aggregate(Sum('salary'))['salary__sum']
                    s.total_cap_hit = total
                    s.save()

            for p in DraftPick.objects.order_by('draft_round','draft_pick','squad'):
                print p.draft_round, p.draft_pick, p.player, p.squad, p.player.salary
