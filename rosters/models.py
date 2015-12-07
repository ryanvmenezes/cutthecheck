from django.db import models
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
        ('Vineeth','Vineeth Pillai',),
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
        return self.manager

    @property
    def cap_room(self):
        return 70000000 - self.total_cap_hit
    

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

    salary_1516 = models.IntegerField(
        null=True,
        help_text="Cap hit for this player",
    )

    manager = models.ForeignKey(
        Squad,
        null=True
    )

    class Meta:
        ordering = ["-salary_1516"]

    def __unicode__(self):
        return self.full_name

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