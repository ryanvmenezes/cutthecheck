from __future__ import division
import calculate
from rosters.models import Squad
from django.db.models import Count, Sum
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'audit.html'
    def get_context_data(self):
        squad_list = Squad.objects.all().order_by('-total_cap_hit')
        context = {
            'squad_list': squad_list,
        }
        return context

class DetailView(TemplateView):
    template_name = 'detail.html'
    def get_context_data(self, manager):
        squad = Squad.objects.get(id=manager)
        players = Squad.objects.prefetch_related('player_set').all() #.order_by('-salary_1516')
        context = {
            'squad': squad,
            'players': players,
        }
        return context
