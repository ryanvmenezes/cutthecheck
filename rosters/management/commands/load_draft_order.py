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
        FILE_PATH = 'rosters/management/commands/draft_order.csv'

        DraftPick.objects.all().delete()
        with open(FILE_PATH, 'r') as csvfile:
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

        with open(FILE_PATH, 'w+') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['round','pick','manager','player','salary','team','note'])
            for p in DraftPick.objects.order_by('draft_round','draft_pick','squad'):
                csvwriter.writerow(
                    [
                        p.draft_round,
                        p.draft_pick,
                        p.squad,
                        p.player if p.player else '',
                        p.player.salary if p.player else '',
                        p.player.nba_team if p.player else '',
                        p.note,
                    ]
                )

        LastUpdated.objects.all().delete()

        # mark last update
        last_update_obj = LastUpdated(
          last_update=timezone.now()
        )
        last_update_obj.save()
