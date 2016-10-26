from django.db import models
from django.db.models import Sum
from bakery.models import BuildableModel

# Create your models here.

class Squad(BuildableModel):
    '''
    A fantasy team in this league
    '''

    detail_views = (
        'rosters.views.AuditView',
        'rosters.views.ProfileView',
        'rosters.views.BibleView',
    )

    # nicknames from each Yahoo account
    MANAGER_CHOICES = (
        ('Austin','Austin Manapsal',),
        ('sam','Sam Tesconi',),
        ('eli','Eli Smukler',),
        ('Pedro Moura','Pedro Moura',),
        ('Zach','Zach Helfand',),
        ('Everett','Everett Cook',),
        ('Ryan Kartje','Ryan Kartje',),
        ('Ryan','Ryan Menezes',),
        ('Justin','Justin Cerri',),
        ('Christian M','Christian Mikkelson',),
        # (None, "FA")
    )

    manager = models.CharField(
        max_length=150,
        null=True,
        help_text="Who helms this ship",
        choices=MANAGER_CHOICES,
    )

    total_cap_hit = models.IntegerField(
        null=True,
        default=0
    )

    slug = models.SlugField(unique=False, db_index=True)

    def __unicode__(self):
        return self.get_manager_display()

    @models.permalink
    def get_absolute_url(self):
        return ('profile-page', [], dict(slug=self.slug))

    @property
    def cap_room(self):
        return 94143000 - self.total_cap_hit


class Player(BuildableModel):
    '''
    A real player from the NBA
    '''

    detail_views = (
        'rosters.views.AuditView',
        'rosters.views.ProfileView',
        'rosters.views.BibleView',
    )

    full_name = models.CharField(
        max_length=150,
        null=True,
        help_text="NBA player's name",
    )

    nba_team = models.CharField(
        max_length=150,
        null=True,
        help_text="NBA player's team",
    )

    salary = models.IntegerField(
        null=True,
        help_text="Cap hit for this player",
    )

    manager = models.ForeignKey(
        Squad,
        null=True
    )

    class Meta:
        ordering = ["-salary"]

    def __unicode__(self):
        return self.full_name

class DraftPick(BuildableModel):
    draft_round = models.IntegerField(
        null=True,
        help_text='Round this player was drafted',
        choices=[(i,i) for i in range(12)],
    )

    draft_pick = models.IntegerField(
        null=True,
        help_text='Pick within round this player was drafted',
        choices=[(i,i) for i in range(1,11)],
    )

    player = models.ForeignKey(
        Player,
        null=True
    )

    squad = models.ForeignKey(
        Squad,
        null=True
    )


class LastUpdated(BuildableModel):
    '''
    When these data were updated last
    '''

    detail_views = (
        'rosters.views.AuditView',
        'rosters.views.ProfileView',
        'rosters.views.BibleView',
    )

    last_update = models.DateTimeField(
        null=True,
        blank=False,
    )
