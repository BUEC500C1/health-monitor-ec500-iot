import smtplib
import os

GMAIL_EMAIL = os.environ.get("EC500_GMAIL_EMAIL")
GMAIL_PASSWORD = os.environ.get("EC500_GMAIL_PASSWORD")


def send_email(emails, patient_id, alarm_type, alarm_val, alarm_threshold: tuple):
    if GMAIL_EMAIL is None or GMAIL_PASSWORD is None:
        return
    low, high = alarm_threshold
    SUBJECT = f'EC500 HW5 - ICU monitor alarm for {patient_id} - {alarm_type}!'
    TEXT = f"""
    An alarm was triggered by the ICU monitor for patient {patient_id}:
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

    BODY = '\r\n'.join([f'To: {emails}',
                        f'From: {gmail_sender}',
                        f'Subject: {SUBJECT}',
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, emails, BODY)
        print('email sent to', emails)
    except Exception as e:
        print('error sending mail:', e)

    server.quit()


if __name__ == '__main__':
    send_email(["rjewing@bu.edu"], "test_alarm", 10, (5, 15))
