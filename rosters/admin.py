from django.contrib import admin
from rosters.models import Squad, Player, DraftPick

class PlayerInline(admin.TabularInline):
    model = Player
    max_num = 11
    extra = 1
    fields = (
        'full_name',
        'nba_team',
        'salary',
    )

class DraftPickInline(admin.TabularInline):
    model = DraftPick
    max_num = 1
    fields = (
        # 'draft_round',
        # 'draft_pick',
        # 'squad',
        # "draft_pick_display",
    )


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
    list_display = ("full_name", "nba_team", "manager", "salary")
    list_editable = ("manager",)
    inlines = [DraftPickInline]
    ordering = ["-manager","-salary"]

@admin.register(DraftPick)
class DraftPickAdmin(admin.ModelAdmin):
    list_display = ("squad","player","draft_round", "draft_pick",)
    readonly_fields = ("note",)
    list_editable = ("player",)
    ordering = ["draft_round","draft_pick","squad"]
    list_display = ("full_name", "nba_team", "manager", "salary", "draft_round", "draft_pick")
    list_editable = ("manager", "draft_round", "draft_pick")
    ordering = ["nba_team","-salary"]
