"""Session 4 debugging exercise.

This script runs without errors but prints the wrong ladder.
Find the bug with the VS Code debugger rather than by reading the code.
"""

MATCHES = [
    {"home": "Geelong", "away": "Sydney",
     "home_goals": 15, "home_behinds": 12, "away_goals": 9, "away_behinds": 8},
    {"home": "Brisbane", "away": "Geelong",
     "home_goals": 12, "home_behinds": 8, "away_goals": 12, "away_behinds": 8},
    {"home": "Sydney", "away": "Brisbane",
     "home_goals": 12, "home_behinds": 5, "away_goals": 11, "away_behinds": 12},
]

EXPECTED = {"Geelong": 6, "Brisbane": 6, "Sydney": 0}


def ladder_points(matches):
    """Return premiership points per team: 4 for a win, 2 each for a draw."""
    points = {}
    for m in matches:
        home, away = m["home"], m["away"]
        points.setdefault(home, 0)
        points.setdefault(away, 0)

        home_total = m["home_goals"] * 6 + m["home_behinds"]
        away_total = m["away_goals"] * 6 + m["home_behinds"]

        if home_total > away_total:
            points[home] += 4
        elif home_total < away_total:
            points[away] += 4
        else:
            points[home] += 2
            points[away] += 2
    return points


def main():
    ladder = ladder_points(MATCHES)
    print("Calculated:", ladder)
    print("Expected:  ", EXPECTED)
    print("Correct!" if ladder == EXPECTED else "Something is wrong. Time for the debugger.")


if __name__ == "__main__":
    main()
