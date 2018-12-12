from random import randint
from datetime import datetime
import logging

import group_info
import notify


logging.basicConfig(filename='log.txt', level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s')

GROUP_INFO = group_info.birthdays()


def team_month():
    """
    Determines the relevant month (always the next month)
    """
    if datetime.now().month == 12:
        month_number = 1
    else:
        month_number = datetime.now().month+1
    return month_number


def draw_team(team_size=2):
    """
    Draw group member for the birthday team.
    """
    team = []
    members_pool = GROUP_INFO

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

    month = int(date.split('-')[-1])

    if month == team_month():
        return True
    else:
        return False


def birthdays_next_month():
    """
    Checks for upcoming birthays (following month).
    """

    bday_list = []
    for member in GROUP_INFO:
        if int(member[2].split('-')[-1]) == team_month():
            bday_list.append(member)

    return bday_list


def create_message(bday_team, bday_list):
    """
    Creates the html code for a message to be sent to the birthdays team containing team members and upcoming birthdays
    info.
    """

    month_dict = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho',
                  7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}

    month_index = team_month()

    # Subject
    subject = 'Equipa de aniversários para {}'.format(month_dict[month_index])

    # Simple message
    message = '''Olá\n\nA equipa de aniversários para o mês de {} é:
    '''.format(month_dict[month_index])

    # HTML message
    team_string = ''
    for team_member in bday_team:
        team_string += '<li>{}</li>'.format(team_member[0])

    bdays_string = ''
    for bdays in bday_list:
        bdays_string += '<li>Dia {} - {}</li>'.format(bdays[2].replace('-', '/'), bdays[0])

    html_message = '''<p>Olá.</p>
    <p>A equipa de aniversários para o mês de {} é:</p>
    <ul>{}</ul><br>
    <br>
    <p>Os aniversários em {} são:</p>
    <ul>{}</ul><br>
    <p>Este e-mail foi enviado para todos os membros do grupo, excepto os aniversariantes.</p>
    <p>Zé Pedro<br><small>Esta mensagem é automática. Em caso de erro contactar joseaniceto@ua.pt.</small></p>
        '''.format(month_dict[month_index], team_string, month_dict[month_index], bdays_string)

    return subject, message, html_message


def main():
    # Get next month birthdays
    next_bdays = birthdays_next_month()
    logging.info('Next month birthdays: {}'.format(birthdays_next_month()))

    # If there are birthdays next month...
    if next_bdays:
        # Draw a birthday team at random
        bday_team = draw_team()
        logging.info('Birthday team: {}'.format(bday_team))

        # Create and send e-mail
        members_pool = group_info.birthdays()
        mail_to = [member[1] for member in members_pool if member not in next_bdays]
        sub, msg, msg_html = create_message(bday_team, next_bdays)
        for mail_address in mail_to:
            notify.html_mail(sub, msg, msg_html, receiver=mail_address)
        logging.info('Mail sent to: {}'.format(mail_to))
        

if __name__ == '__main__':
    main()
