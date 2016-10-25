import requests
import time
import re
from BeautifulSoup import BeautifulSoup
from django.core.management.base import BaseCommand
from yahooapi import YahooAPI
from rosters.models import Squad, Player, LastUpdated
from datetime import datetime
from django.template.defaultfilters import slugify

class Command(BaseCommand):
    """
    Load the database in three steps:
    1. Input every player from spotrac with their cap hit
    2. Pull the squad managers from Yahoo
    3. For every player on each fantasy squad, find that player and update his squad field
    Then leave a record for when this was updated.
    """
    def handle(self, *args, **options):
        # purge all records

        print "flushing databases"
        Squad.objects.all().delete()
        Player.objects.all().delete()
        LastUpdated.objects.all().delete()

        ### Scrape spotrac for cap hits

        teams = ["atlanta-hawks","boston-celtics","brooklyn-nets",
        "charlotte-hornets","chicago-bulls","cleveland-cavaliers",
        "dallas-mavericks","denver-nuggets","detroit-pistons",
        "golden-state-warriors","houston-rockets","indiana-pacers",
        "los-angeles-clippers","los-angeles-lakers","memphis-grizzlies",
        "miami-heat","milwaukee-bucks","minnesota-timberwolves",
        "new-orleans-pelicans","new-york-knicks","oklahoma-city-thunder",
        "orlando-magic","philadelphia-76ers","phoenix-suns",
        "portland-trail-blazers","sacramento-kings","san-antonio-spurs",
        "toronto-raptors","utah-jazz","washington-wizards"]

        URL = 'http://www.spotrac.com/nba/{}/cap/'

        for t in teams:
            r = requests.get(URL.format(t))
            soup = BeautifulSoup(r.text)
            table = soup.find("table")
            rows = table.findAll('tr')
            for r in rows[1:]:
                full_name = r.find(attrs={'class':'player'}).a.string
                cap_hit = r.find(title=re.compile('Cap Figure')).string.replace('$','').replace(',','').replace(' ','')
                nba_team = t.replace('-',' ')
                while True:
                    try:
                        print "adding {} from {} with salary {}".format(full_name, nba_team, cap_hit)
                    except (UnicodeEncodeError, UnicodeDecodeError) as e:
                        full_name = "Dennis Schroder"
                        continue
                    break
                player_obj = Player(
                    full_name=full_name,
                    salary_1516=cap_hit,
                    nba_team=nba_team,
                )
                player_obj.save()
            time.sleep(2)

        ### Get managers from Yahoo league

        # # calling Yahoo API with keys and tokens
        # api = YahooAPI('keyfile.txt', 'tokenfile.txt')
        #
        # # base format for any call
        # BASE_API_CALL = 'http://fantasysports.yahooapis.com/fantasy/v2/{}'
        #
        # # just getting the rosters for each team
        # roster_call = BASE_API_CALL.format('team/nba.l.129466.t.{}/roster/')
        #
        # for i in range(1,11):
        #     request = api.request(roster_call.format(i), params={'format': 'json'}).json()
        #     output = request['fantasy_content']['team']
        #
        #     # initialize all Squads
        #     manager_nickname = output[0][14]['managers'][0]['manager']['nickname']
        #     print "initalizing team for {}".format(manager_nickname)
        #     squad_obj = Squad(
        #         manager=manager_nickname,
        #     )
        #     squad_obj.slug = slugify(squad_obj.get_manager_display())
        #     squad_obj.save()
        #
        #     # Yahoo names --> spotrac names
        #     translation = {
        #         'Matthew Dellavedova': 'Matt Dellavedova',
        #         'Otto Porter': 'Otto Porter Jr.',
        #         'Ish Smith': 'Ishmael Smith',
        #         'Steven Adams': 'Steve Adams',
        #         'Kentavious Caldwell-Pope': 'Kentavious Caldwell-Pope ',
        #     }
        #
        #     # loading players to each roster
        #     number_players = int(output[1]['roster']['0']['players']['count'])
        #
        #     total_cap_hit = 0
        #
        #     for j in range(0, number_players):
        #         player_name = output[1]['roster']['0']['players'][str(j)]['player'][0][2]['name']['full']
        #         if player_name in translation.keys():
        #             player_name = translation[player_name]
        #         try:
        #             new_player_obj = Player.objects.get(full_name=player_name)
        #             new_player_obj.manager = squad_obj
        #             squad_obj.total_cap_hit += new_player_obj.salary_1516
        #             new_player_obj.save()
        #             squad_obj.save()
        #         except Player.DoesNotExist:
        #             print "No record of {}".format(player_name)

        # mark last update
        last_update_obj = LastUpdated(
            last_update=datetime.now()
        )
        last_update_obj.save()
