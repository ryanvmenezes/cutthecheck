from django.core.management.base import BaseCommand
from yahooapi import YahooAPI
from rosters.models import Squad, Player

class Command(BaseCommand):

    def handle(self, *args, **options):
    	"""
    	Loading the database
    	"""
    	# purge all records
    	Squad.objects.all().delete()
    	Player.objects.all().delete()

    	# calling Yahoo API with keys and tokens
        api = YahooAPI('keyfile.txt', 'tokenfile.txt')

        # base format for any call
        BASE_API_CALL = 'http://fantasysports.yahooapis.com/fantasy/v2/{}'

        # just getting the rosters for each team
        roster_call = BASE_API_CALL.format('team/nba.l.103876.t.{}/roster/')

        for i in range(1,11):
        	request = api.request(roster_call.format(i), params={'format': 'json'}).json()
        	output = request['fantasy_content']['team']

        	# initialize all Squads
        	manager_nickname = output[0][14]['managers'][0]['manager']['nickname']
        	print "initalizing team for {}".format(manager_nickname)
        	squad_obj = Squad(
        		manager=manager_nickname,
    		)
    		squad_obj.save()

    		# loading players to each roster
        	number_players = int(output[1]['roster']['0']['players']['count'])
        	for j in range(0, number_players):
        		player_name = output[1]['roster']['0']['players'][str(j)]['player'][0][2]['name']['full']
        		print "adding player {} to team {}".format(player_name, manager_nickname)
        		nba_team = output[1]['roster']['0']['players'][str(j)]['player'][0][6]['editorial_team_abbr']
        		print len(nba_team)
        		# player_obj = Player(
        		# 	full_name=str(player_name),
        		# 	nba_team=nba_team,
        		# 	manager=squad_obj,
        		# 	# salary_1516=0,
        		# )
        		# player_obj.save()

