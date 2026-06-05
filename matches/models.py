from django.db import models


class Tournament(models.Model):
    class TournamentType(models.TextChoices):
        WORLD_CUP = "world_cup", "World Cup"
        QUALIFIERS = "qualifiers", "Qualifiers"
        FRIENDLY = "friendly", "Friendly"

    name = models.CharField(max_length=150)
    year = models.PositiveIntegerField()
    host_country = models.CharField(max_length=100, blank=True)
    tournament_type = models.CharField(
        max_length=20,
        choices=TournamentType.choices,
        default=TournamentType.WORLD_CUP,
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ["-year", "name"]
        unique_together = ("name", "year")

    def __str__(self):
        return f"{self.name} {self.year}"
    
class Match(models.Model):
    class Stage(models.TextChoices):
        GROUP = "group", "Group Stage"
        ROUND_OF_32 = "round_32", "Round of 32"
        ROUND_OF_16 = "round_16", "Round of 16"
        QUARTERFINAL = "quarterfinal", "Quarterfinal"
        SEMIFINAL = "semifinal", "Semifinal"
        THIRD_PLACE = "third_place", "Third Place"
        FINAL = "final", "Final"

    class Status(models.TextChoices):
        SCHEDULED = "scheduled", "Scheduled"
        LIVE = "live", "Live"
        FINISHED = "finished", "Finished"
        POSTPONED = "postponed", "Postponed"
        CANCELLED = "cancelled", "Cancelled"

    tournament = models.ForeignKey(
        "matches.Tournament",
        on_delete=models.CASCADE,
        related_name="matches",
    )
    home_team = models.ForeignKey(
        "teams.Team",
        on_delete=models.CASCADE,
        related_name="home_matches",
    )
    away_team = models.ForeignKey(
        "teams.Team",
        on_delete=models.CASCADE,
        related_name="away_matches",
    )
    stage = models.CharField(max_length=20, choices=Stage.choices)
    group = models.CharField(max_length=1, blank=True)
    match_date = models.DateTimeField()
    stadium = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=100, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.SCHEDULED,
    )
    home_score = models.PositiveIntegerField(default=0)
    away_score = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["match_date"]

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"
    

class MatchEvent(models.Model):
    class EventType(models.TextChoices):
        GOAL = "goal", "Goal"
        OWN_GOAL = "own_goal", "Own Goal"
        PENALTY_GOAL = "penalty_goal", "Penalty Goal"
        MISSED_PENALTY = "missed_penalty", "Missed Penalty"
        YELLOW_CARD = "yellow_card", "Yellow Card"
        RED_CARD = "red_card", "Red Card"
        SECOND_YELLOW_RED = "second_yellow_red", "Second Yellow Red"
        SUBSTITUTION = "substitution", "Substitution"
        VAR = "var", "VAR Review"
        INJURY = "injury", "Injury"
        OTHER = "other", "Other"

    match = models.ForeignKey(
        "matches.Match",
        on_delete=models.CASCADE,
        related_name="events"
    )
    team = models.ForeignKey(
        "teams.Team",
        on_delete=models.CASCADE,
        related_name="match_events"
    )
    player = models.ForeignKey(
        "players.Player",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="match_events"
    )
    related_player = models.ForeignKey(
        "players.Player",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="related_match_events"
    )
    minute = models.PositiveIntegerField()
    extra_minute = models.PositiveIntegerField(null=True, blank=True)
    event_type = models.CharField(
        max_length=30,
        choices=EventType.choices
    )
    title = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    is_key_event = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["minute", "extra_minute", "id"]

    def __str__(self):
        extra = f"+{self.extra_minute}" if self.extra_minute else ""
        return f"{self.match} - {self.minute}{extra}' - {self.get_event_type_display()}"
    

class MatchReport(models.Model):
    match = models.OneToOneField(
        "matches.Match",
        on_delete=models.CASCADE,
        related_name="report"
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.TextField(blank=True)
    key_points = models.TextField(blank=True)
    tactical_notes = models.TextField(blank=True)
    generated_at = models.DateTimeField(auto_now=True)
    is_auto_generated = models.BooleanField(default=True)

    class Meta:
        ordering = ["-generated_at"]

    def __str__(self):
        return self.title