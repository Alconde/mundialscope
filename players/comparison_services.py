def build_player_comparison(player_a, player_b):
    metrics = [
        {
            "label": "Edad",
            "a": player_a.date_of_birth,
            "b": player_b.date_of_birth,
        },
        {
            "label": "Club",
            "a": player_a.club or "-",
            "b": player_b.club or "-",
        },
        {
            "label": "Posición",
            "a": player_a.get_position_display(),
            "b": player_b.get_position_display(),
        },
        {
            "label": "Dorsal",
            "a": player_a.shirt_number or "-",
            "b": player_b.shirt_number or "-",
        },
        {
            "label": "Valor de mercado",
            "a": player_a.market_value or "-",
            "b": player_b.market_value or "-",
        },
    ]

    if hasattr(player_a, "caps") and hasattr(player_b, "caps"):
        metrics.append({
            "label": "Internacionalidades",
            "a": player_a.caps,
            "b": player_b.caps,
        })

    if hasattr(player_a, "international_goals") and hasattr(player_b, "international_goals"):
        metrics.append({
            "label": "Goles internacionales",
            "a": player_a.international_goals,
            "b": player_b.international_goals,
        })

    if hasattr(player_a, "height_cm") and hasattr(player_b, "height_cm"):
        metrics.append({
            "label": "Altura (cm)",
            "a": player_a.height_cm or "-",
            "b": player_b.height_cm or "-",
        })

    return {
        "player_a": player_a,
        "player_b": player_b,
        "metrics": metrics,
    }