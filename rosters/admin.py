from django.contrib import admin
from rosters.models import Squad, Player

class PlayerInline(admin.TabularInline):
    model = Player
    can_delete = False
    def has_add_permission(self, request):
        return False

@admin.register(Squad)
class SquadAdmin(admin.ModelAdmin):
    readonly_fields = (
        "total_cap_hit", 
        "cap_room",
        #"self.Player.full_name",
    )
    list_display = ("manager", "total_cap_hit", "cap_room",)
    inlines = [PlayerInline]
    ordering = ["-total_cap_hit"]

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = (
        "manager",
        "full_name", 
        "nba_team",
        "salary_1516",
    )
    list_display = ("full_name", "nba_team", "manager", "salary_1516")
    ordering = ["-manager","-salary_1516"]
