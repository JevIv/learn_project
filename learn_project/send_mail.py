# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
from learn_project.config import SENDGRID_API_KEY, SRC_MAIL
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_mail(dst_mail, subj, body):
    message = Mail(
        from_email=SRC_MAIL,
        to_emails=dst_mail,
        subject=subj,
        html_content=body)
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
