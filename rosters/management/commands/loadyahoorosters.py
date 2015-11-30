from yahooapi import YahooAPI
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        api = YahooAPI('keyfile.txt', 'tokenfile.txt')
        BASE_API_CALL = 'http://fantasysports.yahooapis.com/fantasy/v2/{}'
        roster_call = BASE_API_CALL.format('team/nba.l.103876.t.{}/roster/')
        for i in range(1,11):
        	request = api.request(roster_call.format(i), params={'format': 'json'}).json()
        	output = request['fantasy_content']['team'] #[0][0]['managers'][0]['manager']['nickname']
        	# print output[0][14]['managers'][0]['manager']['nickname']
        	print output[1]['roster']['0']
