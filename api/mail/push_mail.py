from os import path
from jinja2 import Environment, FileSystemLoader, PackageLoader
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os import environ as env
from django.conf import settings

EMAIL = env.get("EMAIL_ADDRESS")
PASSWORD = env.get("EMAIL_PASSWORD")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


def render_template(file, data):

    fileenv = Environment(loader=FileSystemLoader(str(path.join(settings.BASE_DIR,
                                                            r"api\mail\templates"))))
    template = fileenv.get_template(file)
    rendered_template = template.render(**data)

    return rendered_template


def push_mail(subject, recepient, html_path=None, html_data=dict(), attachment_path=None):
    print(f"sending to {recepient} ...")
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = recepient
    msg['Subject'] = subject

    if html_path:
        html = render_template(html_path, html_data)
        msg.attach(MIMEText(html, 'html'))

    # if attachment_path:
    #     # Attach files
    #     attachment = open(f"./attachments/{attachment_path}", 'rb')
    #     part = MIMEBase('application', 'octet-stream')
    #     part.set_payload(attachment.read())
    #     encoders.encode_base64(part)
    #     part.add_header('Content-Disposition', f"attachment; filename= {attachment_path}")
    #     msg.attach(part)

    # Send the email
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, recepient, msg.as_string())
    server.quit()

    print(f"sent to {recepient} ...")
