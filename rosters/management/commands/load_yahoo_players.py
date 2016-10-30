from django.core.management.base import BaseCommand
from rosters.models import Squad, LastUpdated
from yahooapi import YahooAPI

class Command(BaseCommand):
    '''
    docstring
    '''

    def handle(self, *args, **options):

        # calling Yahoo API with keys and tokens
        api = YahooAPI('keyfile.txt', 'tokenfile.txt')

        # base format for any call
        BASE_API_CALL = 'http://fantasysports.yahooapis.com/fantasy/v2/{}'

        # just getting the rosters for each team
        player_call = BASE_API_CALL.format('league/nba.l.129466/players')

        print "CALL {}".format(player_call)

        request = api.request(player_call, params={'format': 'json'}).json()

        print request['fantasy_content']['league'][1]['players']['2']
