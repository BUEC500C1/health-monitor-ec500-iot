import smtplib
import os

GMAIL_EMAIL = os.environ["EC500_GMAIL_EMAIL"]
GMAIL_PASSWORD = os.environ["EC500_GMAIL_PASSWORD"]


def send_email(email, alarm_type, alarm_val, alarm_threshold: tuple):
    low, high = alarm_threshold
    SUBJECT = f'EC500 HW5 - ICU monitor alarm for {alarm_type}!'
    TEXT = f"""
    An alarm was triggered by the ICU monitor:
    {alarm_type} = {alarm_val}
    {alarm_val} went out of the normal range of {low} - {high}
    """

    # Gmail Sign In
    gmail_sender = GMAIL_EMAIL
    gmail_passwd = GMAIL_PASSWORD

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join([f'To: {email}',
                        f'From: {gmail_sender}',
                        f'Subject: {SUBJECT}',
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [email], BODY)
        print('email sent')
    except Exception as e:
        print('error sending mail:', e)

    server.quit()


if __name__ == '__main__':
    send_email("rjewing@bu.edu", "test_alarm", 10, (5, 15))
