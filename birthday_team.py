from random import randint
from datetime import datetime


MEMBERS = [['Zé Pedro', 'joseaniceto@ua.pt', '22-7'],
           ['Simão', 'simaocardoso@ua.pt', '21-4'],
           ['Marcelo', 'marcelomelo@ua.pt', '3-5'],
           ['Ivo', 'ivoazenha@ua.pt', '3-13'],
           ['Martinique', '@ua.pt', '3-13'],
           ['Bruno', '@ua.pt', '3-13'],
           ['Vitor', '@ua.pt', '3-13']]


def draw_team(team_size=2):
    team = []
    members_pool = MEMBERS

    for i in range(team_size):
        draw = randint(0, len(members_pool)-1)

        while birthday_overlap(members_pool[draw][2]):
            draw = randint(0, len(members_pool)-1)
        else:
            team.append(members_pool[draw])
            members_pool.pop(draw)

    return team


def birthday_overlap(date):
    team_month = datetime.now().month+1
    month = int(date.split('-')[-1])

    if month == team_month:
        return True
    else:
        return False


def birthdays_next_month():
    team_month = datetime.now().month+1
    bday_list = []

    for member in MEMBERS:
        if int(member[2].split('-')[-1]) == team_month:
            bday_list.append(member)

    return bday_list


if __name__ == '__main__':
    print(draw_team())
    print(birthdays_next_month())
