from django.contrib import admin
from backend.team.models import Team, TeamUser

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['description',]

@admin.register(TeamUser)
class TeamUserAdmin(admin.ModelAdmin):
    list_display = ['img_url', 'title', 'subtitle', 'description', 'twitter', 'facebook', 'instagram', 'linkedin', 'type',]
