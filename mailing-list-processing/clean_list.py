import csv
import re
from collections import OrderedDict


def get_list(filepath):
    """Loads .txt list."""
    print('Loading list...')
    with open(filepath, 'r') as f:
        mail_list = []
        for line in f:
            mail_list.append(line.strip('\n'))
    print('Original list has', len(mail_list), 'items.')
    return mail_list


def save_list(filepath, newlist):
    """Saves .txt list."""
    with open(filepath, 'w') as f:
        for item in newlist:
            f.write("{}\n".format(item))
    print('New list saved as', filepath)


def save_list_as_csv(filepath, newlist):
    """Saves .csv list."""
    CSV_HEADER = ['email']
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(CSV_HEADER)
        for row in newlist:
            writer.writerow([row])
    print('New list saved as', filepath)


def remove_invalid_mails(bad_list):
    """Removes from the list invalid mails."""
    print('Removing invalid emails...')
    EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    new_list = []
    for mail in bad_list:
        if EMAIL_REGEX.match(mail):
            new_list.append(mail)
    print('New list has', len(new_list), 'items.')
    return new_list


def clean_mails(bad_list):
    """Lowercases all emails and black spaces at the beginning or ending."""
    print('Lowercasing all emails and removing spaces...')
    new_list = [mail.lower().strip() for mail in bad_list]
    return new_list
    

def remove_role_mails(bad_list):
    """Removes from the list role-based emails. Define unwanted domains in ROLE_LIST."""
    print('Removing role emails...')
    ROLE_LIST = ['help', 'admin', 'info', 'support', 'sales', 'all', 'ftp', 'test']
    new_list = []
    for mail in bad_list:
        if any(role in mail for role in ROLE_LIST):
            pass
        else:
            new_list.append(mail)
    print('New list has', len(new_list), 'items.')
    return new_list


def remove_numbers(bad_list):
    """Removes from the list emails containing numbers."""
    print('Removing emails with numbers...')
    new_list = []
    for mail in bad_list:
        if any(char.isdigit() for char in mail):
            pass
        else:
            new_list.append(mail)
    print('New list has', len(new_list), 'items.')
    return new_list


def remove_domains(bad_list):
    """Removes from the list selected domains. Define unwanted domains in BAD_DOMAINS."""
    print('Removing bad domains...')
    BAD_DOMAINS = ['iol.pt', 'yahool.com.br', 'hotmail.com.br', 'ist.utl.pt', 'dq.ua.pt']
    new_list = []
    for mail in bad_list:
        if any(domain in mail for domain in BAD_DOMAINS):
            pass
        else:
            new_list.append(mail)
    print('New list has', len(new_list), 'items.')
    return new_list


def remove_large_emails(bad_list):
    """Removes from the list mails too large. Define character limits with MAX_LENGTH."""
    print('Removing large emails...')
    MAX_LENGTH = 30
    new_list = []
    for mail in bad_list:
        if len(mail) > MAX_LENGTH:
            pass
        else:
            new_list.append(mail)
    print('New list has', len(new_list), 'items.')
    return new_list


def remove_small_emails(bad_list):
    """Removes from the list mails too small. Define character limits with MIN_LENGTH."""
    print('Removing small emails...')
    MIN_LENGTH = 4
    new_list = []
    for mail in bad_list:
        if len(mail.split('@')[0]) < MIN_LENGTH:
            pass
        else:
            new_list.append(mail)
    print('New list has', len(new_list), 'items.')
    return new_list


def remove_duplicates(bad_list):
    """Removes duplicates."""
    print('Removing duplicates...')
    new_list = list(OrderedDict.fromkeys(bad_list))
    print('New list has', len(new_list), 'items.')
    return new_list


def main():
    # Load list
    og_list = get_list('contacts/list.txt')

    # Process list
    new_list = clean_mails(og_list)
    new_list = remove_invalid_mails(new_list)
    new_list = remove_role_mails(new_list)
    new_list = remove_numbers(new_list)
    new_list = remove_domains(new_list)
    new_list = remove_large_emails(new_list)
    new_list = remove_small_emails(new_list)
    new_list = remove_duplicates(new_list)

    # Save new list
    save_list('contacts/new_list.txt', new_list)
    save_list_as_csv('contacts/new_list.csv', new_list)


if __name__ == "__main__":
    main()
