from django.db import models


class Player(models.Model):
    class Position(models.TextChoices):
        GOALKEEPER = "GK", "Goalkeeper"
        DEFENDER = "DF", "Defender"
        MIDFIELDER = "MF", "Midfielder"
        FORWARD = "FW", "Forward"

    class PreferredFoot(models.TextChoices):
        RIGHT = "right", "Right"
        LEFT = "left", "Left"
        BOTH = "both", "Both"

    team = models.ForeignKey(
        "teams.Team",
        on_delete=models.CASCADE,
        related_name="players",
    )
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    shirt_number = models.PositiveIntegerField(null=True, blank=True)
    position = models.CharField(max_length=2, choices=Position.choices)
    date_of_birth = models.DateField(null=True, blank=True)
    club = models.CharField(max_length=100, blank=True)
    market_value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    caps = models.PositiveIntegerField(default=0)
    international_goals = models.PositiveIntegerField(default=0)
    preferred_foot = models.CharField(
        max_length=10,
        choices=PreferredFoot.choices,
        blank=True
    )
    height_cm = models.PositiveIntegerField(null=True, blank=True)
    is_called_up = models.BooleanField(default=True)
    external_id = models.CharField(max_length=100, blank=True, null=True, unique=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        unique_together = ("team", "shirt_number")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"