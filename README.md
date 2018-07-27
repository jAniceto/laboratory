# egichem-lab
Collection of scripts for the management of the Egichem Laboratory

## birthday-team

A script to select a team to handle birthdays. Team is selected at random for each month where bithdays exist. All members of the group, except the birthday person is email this information. Script runs monthly via crontab.

#### Requires:
* e-mail account password as environmental variable `MAIL_PASS`.
* group_info file containing member info in the format `['name', 'mail', 'bday']`. E.g.: `[['name1', 'mail1@mail.com', '26-7'], ['name2', 'mail2@mail.com', '1-10'],...]`.



## mailing-list-processing

A collection of scripts to clean up a mailing list. Removes duplicates, removes invalid emails, separates mails by country domain, removes role emails, etc.