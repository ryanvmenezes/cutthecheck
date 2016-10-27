import requests
import time
import re
from django.core.management.base import BaseCommand
from BeautifulSoup import BeautifulSoup
from rosters.models import Player, LastUpdated
from django.utils import timezone

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

        print "flushing player database"
        Player.objects.all().delete()

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
                    salary=cap_hit,
                    nba_team=nba_team,
                )
                player_obj.save()
            time.sleep(2)

        # mark last update
        LastUpdated.objects.all().delete()
        last_update_obj = LastUpdated(
          last_update=timezone.now()
        )
        last_update_obj.save()
