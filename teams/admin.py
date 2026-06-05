from django.contrib import admin
from .models import Team, TeamReport


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "fifa_code", "confederation", "coach", "fifa_ranking", "group", "is_active")
    list_filter = ("confederation", "group", "is_active")
    search_fields = ("name", "fifa_code", "coach")
    ordering = ("name",)

@admin.register(TeamReport)
class TeamReportAdmin(admin.ModelAdmin):
    list_display = ("title", "team", "generated_at", "is_auto_generated")
    list_filter = ("is_auto_generated", "generated_at", "team__confederation")
    search_fields = ("title", "team__name", "team__confederation")
    prepopulated_fields = {"slug": ("title",)}