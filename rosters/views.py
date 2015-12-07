from __future__ import division
import calculate
from rosters.models import Squad, Player, LastUpdated
from django.db.models import Count, Sum
from django.views.generic import TemplateView


last_updated = LastUpdated.objects.all()[0]

class AuditView(TemplateView):
    template_name = 'audit.html'
    def get_context_data(self):
        squad_list = Squad.objects.all().order_by('-total_cap_hit')
        context = {
            'squad_list': squad_list,
            'last_updated': last_updated,
        }
        return context

class DetailView(TemplateView):
    template_name = 'detail.html'
    def get_context_data(self, manager):
        squad = Squad.objects.get(slug=manager)
        context = {
            'squad': squad,
            'last_updated': last_updated,
        }
        return context

class BibleView(TemplateView):
    template_name = 'bible.html'
    def get_context_data(self):
        players = Player.objects.order_by('nba_team', '-salary_1516')
        context = {
            'players': players,
            'last_updated': last_updated,
        }
        return context
