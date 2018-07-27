from clean_list import get_list, save_list_as_csv


def select_endings(bad_list):
    good_endings = ['ua.pt', 'fe.up.pt', 'ipl.pt']

    sublist = []
    for mail in bad_list:
        if mail.endswith(tuple(good_endings)):
            sublist.append(mail)

    return sublist


def create_sublists(main_list):
    print('Creating sublists...')
    SUBLISTS = ['.pt', '.br', '.es', '.fr', '.uk', '.com']

    sublist_others = []
    for mail in main_list:
        if not any(ending in mail for ending in SUBLISTS):
            sublist_others.append(mail)
    with open('sublists/others.txt', 'w') as f:
        for item in sublist_others:
            f.write("{}\n".format(item))
    print('Sublist OTHERS created. Size:', len(sublist_others), 'contacts.')

    for ending in SUBLISTS:
        sublist = []
        for mail in main_list:
            if mail.endswith(ending):
                sublist.append(mail)
        with open('sublists/{}.txt'.format(ending), 'w') as f:
            for item in sublist:
                f.write("{}\n".format(item))
        print('Sublist', ending, 'created. Size:', len(sublist), 'contacts.')


def main():
    # Load list
    the_list = get_list('contacts/new_list.txt')

    # Create sublists
    create_sublists(the_list)
    

if __name__ == "__main__":
    main()
