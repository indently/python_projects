import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any

import credentials


def create_image_attachment(path: Any) -> MIMEImage:
    """Create an image type for our email and add a header to it."""

    try:
        with open(path, 'rb') as image:
            mime_image = MIMEImage(image.read())
            mime_image.add_header('Content-Disposition', f'attachment; filename={path}')
            return mime_image
    except Exception as e:
        print('Error:', e)


def send_email(to_email: str, subject: str, body: str, image: Any = None):
    # Specify the host and the port
    host: str = 'smtp-mail.outlook.com'
    port: int = 587

    # Validates the host name and its certificates and optimizes the security of the connection.
    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        # Login
        print('Logging in...')
        server.ehlo()
        server.starttls(context=context)
        server.login(credentials.EMAIL, credentials.PASSWORD)  # NEVER INCLUDE SENSITIVE VALUES IN YOUR SCRIPTS!!!

        # Prepare the email
        print('Attempting to send the message...')
        message = MIMEMultipart()
        message['From'] = credentials.EMAIL
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # If there is an attachment, attach it to the e-mail
        if image:
            file: MIMEImage = create_image_attachment(image)
            message.attach(file)

        # Send the email
        server.sendmail(from_addr=credentials.EMAIL, to_addrs=to_email, msg=message.as_string())

        # Success!
        print('Sent!')


if __name__ == '__main__':
    send_email(to_email='indently@fastmail.com', subject='hello', body='this is a message', image='cat.png')
