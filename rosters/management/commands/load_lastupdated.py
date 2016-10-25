import csv
from django.core.management.base import BaseCommand
from rosters.models import LastUpdated
from datetime import datetime


class Command(BaseCommand):
    '''
    docstring
    '''
    def handle(self, *args, **options):
        
        print "flushing lastupdated database"
        LastUpdated.objects.all().delete()

        # mark last update
        last_update_obj = LastUpdated(
          last_update=datetime.now()
        )
        last_update_obj.save()
