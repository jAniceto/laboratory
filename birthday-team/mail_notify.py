import os
import smtplib
from email.message import EmailMessage


def plain_mail(subject, body, sender='aniceto.scripts@gmail.com', receiver='aniceto.scripts@gmail.com'):
    email_pw = os.environ.get('MAIL_PASS')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, email_pw)

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(sender, receiver, msg)

        print('\nMail sent!')


def html_mail(subject, message_plain, message_html, sender='aniceto.scripts@gmail.com', receiver='aniceto.scripts@gmail.com'):
    email_pw = os.environ.get('MAIL_PASS')

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(message_plain)
    msg.add_alternative(message_html, subtype='html')
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, email_pw)
        smtp.send_message(msg)

    print('\nMail sent!')


if __name__ == "__main__":
    # Testing

    email_address = 'aniceto.scripts@gmail.com'
    sub = 'Test subject'
    msg_plain = 'Test plain message'
    msg_html = """\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
"""
    html_email(sub, msg_plain, msg_html, sender=email_address, receiver=email_address)
