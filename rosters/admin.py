from django.contrib import admin
from rosters.models import Squad, Player

class PlayerInline(admin.TabularInline):
    model = Player
    max_num = 11
    extra = 1
    fields = (
        'full_name',
        'nba_team',
        'salary',
    )
    # can_delete = False
    # def has_add_permission(self, request):
    #     return False

@admin.register(Squad)
class SquadAdmin(admin.ModelAdmin):
    readonly_fields = (
        # "manager",
        "total_cap_hit",
        "cap_room",
        "slug",
        # "player_set.full_name",
    )
    list_display = ("manager", "total_cap_hit", "cap_room",)
    inlines = [PlayerInline]
    ordering = ["-total_cap_hit"]

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = (
        # "manager",
        "full_name",
        "nba_team",
        "salary",
    )
    list_per_page = 5000
    list_display = ("full_name", "nba_team", "manager", "salary")#, "draft_round", "draft_pick")
    list_editable = ("manager",)#, "draft_round", "draft_pick")
    ordering = ["-manager","-salary"]
