from django.core.management.base import BaseCommand
from rosters.models import Squad
import csv


class Command(BaseCommand):

    def handle(self, *args, **options):
        print "Dumping CSV"
        csv_file = open('rosters/management/commands/league_rosters.csv', 'wb')
        csv_writer = csv.writer(csv_file)
        header = ["manager", "player", "salary", "team"]
        csv_writer.writerow(header)
        for squad in Squad.objects.all():
        	# print squad.manager
        	for player in squad.player_set.all():
        		row = [squad.get_manager_display(), player.full_name, player.salary_1516, player.nba_team]
        		csv_writer.writerow(row)