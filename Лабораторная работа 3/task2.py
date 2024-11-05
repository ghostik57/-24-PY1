def find_common_participants(group1, group2, delimiter=","):
    participants1 = group1.split(delimiter)
    participants2 = group2.split(delimiter)

    common_participants = []
    for participant in participants1:
        if participant in participants2 and participant not in common_participants:
            common_participants.append(participant)

    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print(result)
