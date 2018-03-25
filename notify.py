import os
import sys
import smtplib

# Required for basic mails
from email.message import EmailMessage

# Required for HTML mails
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mail(subject, message, sender='aniceto.scripts@gmail.com', receiver='havok_2004@hotmail.com'):

    if sender == 'aniceto.scripts@gmail.com':
        pwd = os.getenv('MAIL_PASS')
    else:
        print('Sender e-mail and password don\'t match')
        sys.exit()

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender, pwd)
    server.sendmail(sender, receiver, msg.as_string())
    server.close()

    print('\nMail sent!')


def html_mail(subject, message, message_html, sender='aniceto.scripts@gmail.com', receiver='havok_2004@hotmail.com'):

    if sender == 'aniceto.scripts@gmail.com':
        pwd = 'anicetopython'
    else:
        print('Sender e-mail and password don\'t match')
        sys.exit()

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(message, 'plain')
    part2 = MIMEText(message_html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender, pwd)
    server.sendmail(sender, receiver, msg.as_string())
    server.close()

    print('\nMail sent to {}!'.format(receiver))
