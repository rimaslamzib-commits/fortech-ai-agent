def predict_match(stats):
    stats = stats.lower()

    if "strong home form" in stats:
        return "Home Win"

    if "strong away form" in stats:
        return "Away Win"

    return "Draw"
