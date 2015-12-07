from __future__ import division
import calculate
from rosters.models import Squad, Player, LastUpdated
from django.db.models import Count, Sum
from bakery.views import BuildableListView, BuildableDetailView
# from django.views.generic import TemplateView


last_updated = LastUpdated.objects.all()[0]

class AuditView(BuildableListView):
    '''
    An audit of the salry figures for 10 fantasy teams
    '''
    build_path = 'cutthecheck/audit.html'
    template_name = 'rosters/audit.html'
    queryset = Squad.objects.all().order_by('-total_cap_hit')
    def get_context_data(self, **kwargs):
        context = super(AuditView, self).get_context_data(**kwargs)
        context.update({
            'last_updated': last_updated,
        })
        return context

class ProfileView(BuildableDetailView):
    '''
    Profile pages for each team
    '''
    model = Squad
    # template_name = 'detail.html'
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update({
            'last_updated': last_updated,
        })
        return context
    def build_queryset(self):
        for o in Squad.objects.order_by('?'):
            print 'building {}'.format(o)
            self.build_object(o)

class BibleView(BuildableListView):
    build_path = 'cutthecheck/bible.html'
    template_name = 'rosters/bible.html'
    queryset = Player.objects.order_by('nba_team', '-salary_1516')
    def get_context_data(self, **kwargs):
        context = super(BibleView, self).get_context_data(**kwargs)
        context.update({
            'last_updated': last_updated,
        })
        return context
