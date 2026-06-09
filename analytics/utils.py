def safe_divide(numerator, denominator, default=0):
    if not denominator:
        return default
    return numerator / denominator


def build_player_full_name(player):
    full_name = f"{player.first_name} {player.last_name}".strip()
    return full_name or "Sin nombre"


def normalize_ordering(value, allowed_values, default):
    if value in allowed_values:
        return value
    return default