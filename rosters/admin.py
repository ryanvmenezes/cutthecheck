from django.contrib import admin
from rosters.models import Squad, Player

class SquadAdmin(admin.ModelAdmin):
	readonly_fields = (
        "total_cap_hit", "cap_room",
    )

# Register your models here.
admin.site.register(Squad, SquadAdmin)
admin.site.register(Player)