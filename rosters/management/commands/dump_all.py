from django.core.management.base import BaseCommand
from rosters.models import Squad, Player
import csv


class Command(BaseCommand):

    def handle(self, *args, **options):
        print "Dumping league CSV"
        csv_file = open('rosters/management/commands/league_draft.csv', 'wb')
        csv_writer = csv.writer(csv_file)
        header = ["manager", "player", "salary", "team", "draft_round", "draft_pick"]
        csv_writer.writerow(header)
        for squad in Squad.objects.all():
        	# print squad.manager
        	for player in squad.player_set.all():
        		row = [squad.manager, player.full_name, player.salary, player.nba_team, player.draft_round, player.draft_pick]
        		csv_writer.writerow(row)
        csv_file.close()

        print "Dumping salaries CSV"
        csv_file = open('rosters/management/commands/all_salaries.csv', 'wb')
        csv_writer = csv.writer(csv_file)
        header = ['player', 'salary', 'team']
        csv_writer.writerow(header)
        for player in Player.objects.all():
        	row = [player.full_name, player.salary, player.nba_team]
        	csv_writer.writerow(row)
        csv_file.close()
