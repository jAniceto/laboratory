from random import randint
from datetime import datetime

import group_info
import notify


def draw_team(team_size=2):
    """
    Draw group member for the birthday team.
    """
    team = []
    members_pool = group_info.birthdays()

    for i in range(team_size):
        draw = randint(0, len(members_pool)-1)

        while birthday_overlap(members_pool[draw][2]):
            draw = randint(0, len(members_pool)-1)
        else:
            team.append(members_pool[draw])
            members_pool.pop(draw)

    return team


def birthday_overlap(date):
    """
    Checks for birthdays overlaps.
    """

    team_month = datetime.now().month+1
    month = int(date.split('-')[-1])

    if month == team_month:
        return True
    else:
        return False


def birthdays_next_month():
    """
    Checks for upcoming birthays (following month).
    """

    team_month = datetime.now().month+1
    bday_list = []

    for member in group_info.birthdays():
        if int(member[2].split('-')[-1]) == team_month:
            bday_list.append(member)

    return bday_list


def create_message(bday_team, bday_list):
    """
    Creates the html code for a message to be sent to the birthdays team containing team members and upcoming birthdays
    info.
    """

    month_dict = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho',
                  7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}

    team_month = datetime.now().month + 1

    # Simple message
    message = '''Olá\n\nFazes parte da equipa de aniversários para o mês de {}.
    '''.format(month_dict[team_month])

    # HTML message
    team_string = ''
    for team_member in bday_team:
        team_string += '{} '.format(team_member[0])

    bdays_string = ''
    for bdays in bday_list:
        bdays_string += '<li>Dia {} - {}</li>'.format(bdays[2].replace('-', '/'), bdays[0])

    html_message = '''<p>Olá.</p>
    <p>Fazes parte da equipa de aniversários para o mês de {}. Equipa: {}</p>
    <p>Os aniversários em {} são:</p>
    <ul>{}</ul><br>
    <p>Zé Pedro<br><small>Esta mensagem é automática. Em caso de erro contactar joseaniceto@ua.pt.</small></p>
        '''.format(month_dict[team_month], team_string, month_dict[team_month], bdays_string)

    return message, html_message


def main():
    # Get next month birthdays
    next_bdays = birthdays_next_month()
    print('Next month birthdays:', birthdays_next_month())

    # If there are birthdays next month...
    if next_bdays:
        # Draw a birthday team at random
        bday_team = draw_team()
        print('Birthday team:', bday_team)

        # Create and send e-mail
        mail_to = [member[1] for member in bday_team]
        print(mail_to)
        msg, msg_html = create_message(bday_team, next_bdays)
        subject = 'Lembrete equipa de aniversários'
        for mail in mail_to:
            notify.html_mail(subject, msg, msg_html, receiver=mail)


if __name__ == '__main__':
    main()
