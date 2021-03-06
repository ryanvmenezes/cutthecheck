from __future__ import division
import os
import calculate
from rosters.models import Squad, Player, LastUpdated, DraftPick
from django.db.models import Count, Sum
from django.conf import settings
from bakery.views import BuildableListView, BuildableDetailView
# from django.views.generic import TemplateView


last_updated = LastUpdated.objects.all()[0]

universal_context = {
    'last_updated': last_updated,
}

class AuditView(BuildableListView):
    '''
    An audit of the salary figures for 10 fantasy teams
    '''
    queryset = Squad.objects.all().order_by('-total_cap_hit')
    build_path = 'cutthecheck/audit/index.html'
    template_name = 'rosters/audit.html'

    def get_context_data(self, **kwargs):
        context = super(AuditView, self).get_context_data(**kwargs)
        context.update(universal_context)
        return context

class ProfileView(BuildableDetailView):
    '''
    Profile pages for each team
    '''
    model = Squad
    def get_url(self, obj):
        # The URL at which the detail page should appear.
        return '%s' % obj.slug
    def get_build_path(self, obj):
        dir_path = "cutthecheck/detail/"
        dir_path = os.path.join(settings.BUILD_DIR, dir_path, self.get_url(obj))
        os.path.exists(dir_path) or os.makedirs(dir_path)
        return os.path.join(dir_path, 'index.html')
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update(universal_context)
        return context

class BibleView(BuildableListView):
    '''
    The salary bible
    '''
    build_path = 'cutthecheck/bible/index.html'
    template_name = 'rosters/bible.html'
    queryset = Player.objects.order_by('nba_team', '-salary')
    def get_context_data(self, **kwargs):
        context = super(BibleView, self).get_context_data(**kwargs)
        context.update(universal_context)
        return context

class DraftPickView(BuildableListView):
    '''
    The draft
    '''
    build_path = 'cutthecheck/draft/index.html'
    template_name = 'rosters/draft.html'
    queryset = DraftPick.objects.order_by("draft_round","draft_pick","squad")
    def get_context_data(self, **kwargs):
        context = super(DraftPickView, self).get_context_data(**kwargs)
        context.update(universal_context)
        return context
