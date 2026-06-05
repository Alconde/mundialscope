from django.contrib import admin
from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "fifa_code", "confederation", "coach", "fifa_ranking", "group", "is_active")
    list_filter = ("confederation", "group", "is_active")
    search_fields = ("name", "fifa_code", "coach")
    ordering = ("name",)