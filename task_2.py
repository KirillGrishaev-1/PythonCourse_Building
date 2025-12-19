def find_common_participants(team1, team2, sep = ","):
    team1 = team1.split(sep)
    team2 = team2.split(sep)
    intersection = set(team1).intersection(set(team2))
    intersection = list(intersection)
    intersection.sort()
    return intersection


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
