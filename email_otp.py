import imaplib
import email
import re
import os
import time

def get_otp():

    mail = imaplib.IMAP4_SSL("imap.gmail.com")

    mail.login("samikshyakarki478@gmail.com", "ynqg nueu xryr cris")

    mail.select("INBOX")

    # Search for emails from the signup website
    status, messages = mail.search(
        None,
        '(FROM "no-reply@theauthorizedpartner.com")'
    )

    email_ids = messages[0].split()

    if not email_ids:
        mail.logout()
        raise Exception("OTP email not found")

    # Check latest email first
    for email_id in reversed(email_ids):

        status, data = mail.fetch(email_id, "(RFC822)")

        msg = email.message_from_bytes(data[0][1])

        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    payload = part.get_payload(decode=True)
                    if payload:
                        body += payload.decode(errors="ignore")
        else:
            payload = msg.get_payload(decode=True)
            if payload:
                body = payload.decode(errors="ignore")

        match = re.search(
            r'\b\d{6}\b',
            body
        )

        if match:
            otp = match.group()
            mail.logout()

            print("OTP extracted successfully:", otp)

            return otp

    mail.logout()
    raise Exception("OTP not found in email")