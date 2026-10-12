"""Helpers for football scores."""


def total_score(goals, behinds):
    """Return the score from goals and behinds."""
    return goals * 6 + behinds


def margin(home_points, away_points, absolute=False):
    """This function returns the margin of a game. If absolute is True, it returns the absolute value of the margin."""
    if absolute:
        return abs(home_points - away_points)
    return home_points - away_points


def result(home_points, away_points):
    """Return 'home', 'away' or 'draw'."""
    if home_points > away_points:
        return "home"
    elif home_points < away_points:
        return "away"
    else:
        return "draw"
