from django.db import models

# Create your models here.

class Squad(models.Model):
    MANAGER_CHOICES = (
        ('Austin','Austin Manapsal',),
        ('Sam','Sam Tesconi',),
        ('Eli','Eli Smukler',),
        ('Pedro','Pedro Moura',),
        ('Zach','Zach Helfand',),
        ('Everett','Everett Cook',),
        ('Kartje','Ryan Kartje',),
        ('Menezes','Ryan Menezes',),
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

    def __unicode__(self):
        return self.manager

    @property
    def total_cap_hit(self):
        total = 0
        for p in self.player_set.all():
            total += p.salary_1516
        return total

    @property
    def cap_room(self):
        return 70000000 - self.total_cap_hit
    

class Player(models.Model):
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
        help_text="Cap hit for this player",
    )

    manager = models.ForeignKey(Squad)

    def __unicode__(self):
        return self.full_name    