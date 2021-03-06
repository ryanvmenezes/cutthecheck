from django.core.management.base import BaseCommand
from rosters.models import Squad, LastUpdated, Player
from yahooapi import YahooAPI
from django.template.defaultfilters import slugify
from django.utils import timezone
import datetime

class Command(BaseCommand):

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--blank',
            action='store_true',
            dest='blank',
            default=False,
            help='Create squads with no players',
        )

    def handle(self, *args, **options):
        logfile = open('rosters/management/commands/errors_load_squads.txt', 'wb')

        now = datetime.datetime.today()
        logfile.write('Starting update {}\n\n'.format(now.strftime("%d %B %Y %H:%M")))

        logfile.write("flushing squad database\n\n")
        Squad.objects.all().delete()

        if options['blank']:
            for manager_nickname, manager_fullname in Squad.MANAGER_CHOICES:
                logfile.write("initalizing blank team for {}\n".format(manager_nickname))
                squad_obj = Squad(
                    manager=manager_nickname,
                )
                squad_obj.slug = slugify(squad_obj.get_manager_display())
                squad_obj.save()
        else:
            ## Get managers from Yahoo league

            # calling Yahoo API with keys and tokens
            api = YahooAPI('keyfile.txt', 'tokenfile.txt')

            # base format for any call
            BASE_API_CALL = 'http://fantasysports.yahooapis.com/fantasy/v2/{}'

            # just getting the rosters for each team
            roster_call = BASE_API_CALL.format('team/nba.l.129466.t.{}/roster/')

            for i in range(1,11):
                request = api.request(roster_call.format(i), params={'format': 'json'}).json()
                output = request['fantasy_content']['team']

                # initialize all Squads
                manager_nickname = output[0][19]['managers'][0]['manager']['nickname']

                logfile.write("initalizing team for {}\n".format(manager_nickname))
                squad_obj = Squad(
                    manager=manager_nickname,
                )
                squad_obj.slug = slugify(squad_obj.get_manager_display())
                squad_obj.save()

                # Yahoo names --> spotrac names
                translation = {
                    'Matthew Dellavedova': 'Matt Dellavedova',
                    'Otto Porter': 'Otto Porter Jr.',
                    'Ish Smith': 'Ishmael Smith',
                    'Kentavious Caldwell-Pope': 'Kentavious Caldwell-Pope ',
                    'Enes Kanter': 'Enes  Kanter',
                    'J.J. Barea': 'Jose Barea',
                    'Patty Mills': 'Patrick Mills',
                    'Lou Williams': 'Louis Williams',
                }

                # loading players to each roster
                number_players = int(output[1]['roster']['0']['players']['count'])

                total_cap_hit = 0

                for j in range(0, number_players):
                    player_name = output[1]['roster']['0']['players'][str(j)]['player'][0][2]['name']['full']
                    if player_name in translation.keys():
                        player_name = translation[player_name]
                    try:
                        new_player_obj = Player.objects.get(full_name=player_name)
                        new_player_obj.manager = squad_obj
                        squad_obj.total_cap_hit += new_player_obj.salary
                        new_player_obj.save()
                        squad_obj.save()
                    except Player.DoesNotExist:
                        logfile.write("***NO RECORD OF {}***".format(player_name))

            # mark last update
            LastUpdated.objects.all().delete()
            last_update_obj = LastUpdated(
              last_update=timezone.now()
            )
            last_update_obj.save()
