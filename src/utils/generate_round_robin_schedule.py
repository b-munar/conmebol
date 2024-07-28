
def generate_double_round_robin_schedule(teams):
    if len(teams) % 2 != 0:
        teams.append(None)  # Añadir equipo fantasma si es impar

    schedule = []
    num_days = len(teams) - 1
    num_matches_per_day = len(teams) // 2

    for day in range(num_days):
        id_match = 0
        day_matches = []
        for i in range(num_matches_per_day):
            team1 = teams[i]
            team2 = teams[-i-1]
            if team1 is not None and team2 is not None:
                id_match += 1
                day_matches.append({"idMatch": id_match,"idLocal": team1, "idVisitor": team2, "golLocal": None, "golVisitor": None})
        schedule.append(day_matches)
        teams.insert(1, teams.pop())

    double_schedule = schedule + [[{"idMatch": match["idMatch"],"idLocal": match["idVisitor"], "idVisitor": match["idLocal"], "golLocal": None, "golVisitor": None} for match in day] for day in schedule]

    return double_schedule
