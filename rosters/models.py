from django.db import models

# Create your models here.

class Player(models.model):
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
		help_text="Cap hit for this player"
	)
	manager = models.OneToOneField(Squad)

class Squad(models.model):
    MANAGER_CHOICES = (
        ('Austin','Austin',),
        ('Sam','Sam',),
        ('Eli','Eli',),
        ('Pedro','Pedro',),
        ('Zach','Zach',),
        ('Everett','Everett',),
        ('Kartje','Kartje',),
        ('Menezes','Menezes',),
        ('Justin','Justin',),
        ('Vineeth','Vineeth',),
        # (None, "FA")
    )
	manager = models.CharField(
        max_length=150,
        null=True,
        help_text="Who helms this ship",
        choices=MANAGER_CHOICES,
    )
    player = models.ForeignKey(Player)

    @property
    def total_cap_hit(self):
        total = 0
        for p in self.player_set.all():
            total += p.salary_1516