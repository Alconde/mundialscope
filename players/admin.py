from django.contrib import admin
from .models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "team", "position", "shirt_number", "club", "is_called_up")
    list_filter = ("position", "is_called_up", "team")
    search_fields = ("first_name", "last_name", "club", "team__name")
    ordering = ("team", "last_name", "first_name")