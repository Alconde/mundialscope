from django.db import models


class Team(models.Model):
    class Confederation(models.TextChoices):
        UEFA = "UEFA", "UEFA"
        CONMEBOL = "CONMEBOL", "CONMEBOL"
        CONCACAF = "CONCACAF", "CONCACAF"
        CAF = "CAF", "CAF"
        AFC = "AFC", "AFC"
        OFC = "OFC", "OFC"

    name = models.CharField(max_length=100, unique=True)
    fifa_code = models.CharField(max_length=3, unique=True)
    confederation = models.CharField(max_length=10, choices=Confederation.choices)
    coach = models.CharField(max_length=100, blank=True)
    fifa_ranking = models.PositiveIntegerField(null=True, blank=True)
    group = models.CharField(max_length=1, blank=True)
    primary_color = models.CharField(max_length=7, blank=True)
    secondary_color = models.CharField(max_length=7, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.fifa_code})"
    

class TeamReport(models.Model):
    team = models.OneToOneField(
        "teams.Team",
        on_delete=models.CASCADE,
        related_name="report"
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.TextField(blank=True)
    performance_overview = models.TextField(blank=True)
    squad_notes = models.TextField(blank=True)
    discipline_notes = models.TextField(blank=True)
    generated_at = models.DateTimeField(auto_now=True)
    is_auto_generated = models.BooleanField(default=True)

    class Meta:
        ordering = ["team__name"]

    def __str__(self):
        return self.title