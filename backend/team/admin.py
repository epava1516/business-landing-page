from django.contrib import admin
from backend.team.models import Team, TeamUser

@admin.register(TeamUser)
class TeamUserAdmin(admin.ModelAdmin):
    list_display = ['img_url', 'title', 'subtitle', 'description', 'twitter', 'facebook', 'instagram', 'linkedin', 'type',]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['description','display_team_list',]

    def display_team_list(self, obj):
        return ", ".join([team_list.title for team_list in obj.list_description.all()])
    display_team_list.short_description = 'Team List Items'
