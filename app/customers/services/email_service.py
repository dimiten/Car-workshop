from fastapi_mail import ConnectionConfig, MessageSchema, MessageType, FastMail
from pydantic import EmailStr
import asyncio

from app.config import settings


class EmailServices:

    conf = ConnectionConfig(
        MAIL_USERNAME=settings.MAIL_USERNAME,
        MAIL_PASSWORD=settings.MAIL_PASSWORD,
        MAIL_PORT=settings.MAIL_PORT,
        MAIL_SERVER=settings.MAIL_SERVER,
        MAIL_FROM=settings.MAIL_FROM,
        MAIL_STARTTLS=False,
        MAIL_SSL_TLS=False,
    )

    @staticmethod
    def send_email(email: EmailStr):
        html = """<p>3 Auto send test body</p> """

        message = MessageSchema(
            subject="3 Auto send testing subject",
            recipients=[email],
            body=html,
            subtype=MessageType.html,
        )

        fm = FastMail(EmailServices.conf)
        asyncio.run(fm.send_message(message))

        return
