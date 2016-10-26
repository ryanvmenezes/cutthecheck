import os
from django.core.management.base import BaseCommand
from rosters.models import Squad, Player, LastUpdated
from django.db.models import Sum
from django.utils import timezone

class Command(BaseCommand):
    '''
    docstring
    '''

    def handle(self, *args, **options):
        for s in Squad.objects.all():
            print s

            players = Player.objects.filter(manager__manager=s.manager)

            if len(players) != 0:
                total = 0
                total += players.aggregate(Sum('salary'))['salary__sum']
                s.total_cap_hit = total
                s.save()

        # mark last update
        LastUpdated.objects.all().delete()
        last_update_obj = LastUpdated(
          last_update=timezone.now()
        )
        last_update_obj.save()
