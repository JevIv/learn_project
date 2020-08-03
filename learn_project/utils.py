from flask import request
from learn_project.config import SENDGRID_API_KEY, SRC_MAIL
from learn_project.advert.model import Products
from learn_project.user.model import Users
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from subprocess import Popen
from urllib.parse import urlparse, urljoin


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def get_redirect_target():
    for target in request.values.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return target


def run_parser():
    Popen(['python3', 'learn_project/parser.py'])


def send_mail(dst_mail: str, subj: str, body: str):
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


def comment_notification(product_id, comment_text):
    ad_owner_id = Products.query.get(product_id).created_by  # Определяем хозяина объявления
    ad_title    = Products.query.get(product_id).name
    mail_to     = Users.query.get(ad_owner_id).email  # Определяем email хозяина объявления

    if mail_to:
        subj = 'Вам новый коммент'
        body = f'К объявлению {ad_title} <br> \
                 оставлен новый комментарий: <br> \
                 "{comment_text}" <br> \
                 Посмотреть {get_redirect_target()}'
        send_mail(mail_to, subj, body)
