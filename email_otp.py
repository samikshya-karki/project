import imaplib
import email
import re
import os
import time

from dotenv import load_dotenv



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

if not EMAIL_USER or not EMAIL_APP_PASSWORD:
    raise ValueError("Gmail credentials missing in .env")



def get_latest_uid():

    mail = imaplib.IMAP4_SSL("imap.gmail.com")

    try:
        mail.login(EMAIL_USER, EMAIL_APP_PASSWORD)
        mail.select("INBOX")

        status, data = mail.uid("search", None, "ALL")

        if status != "OK":
            raise Exception("Unable to search Gmail inbox")

        email_ids = data[0].split()

        latest_uid = max(
            (int(uid) for uid in email_ids),
            default=0
        )

        print("Latest existing UID:", latest_uid)

        return latest_uid

    finally:
        mail.logout()



def get_otp(old_uid, timeout=120):

    start_time = time.time()

    while time.time() - start_time < timeout:

        mail = imaplib.IMAP4_SSL("imap.gmail.com")

        try:
            mail.login(EMAIL_USER, EMAIL_APP_PASSWORD)
            mail.select("INBOX")

            
            status, messages = mail.uid(
                "search", None, "ALL"
            )

            if status != "OK":
                print("Unable to search emails")
                time.sleep(5)
                continue

            email_ids = messages[0].split()

            
            new_email_ids = [
                uid for uid in email_ids
                if int(uid) > old_uid
            ]

            print("Old UID:", old_uid)
            print("Genuinely new email UIDs:", new_email_ids)

            
            for email_id in reversed(new_email_ids):

                status, data = mail.uid(
                    "fetch", email_id, "(RFC822)"
                )

                if status != "OK":
                    continue

                raw_email = next(
                    (
                        item[1]
                        for item in data
                        if isinstance(item, tuple)
                    ),
                    None
                )

                if not raw_email:
                    continue

                msg = email.message_from_bytes(raw_email)

                
                sender = email.utils.parseaddr(
                    msg.get("From", "")
                )[1].lower()

                if sender != "no-reply@theauthorizedpartner.com":
                    continue

                
                body = ""

                if msg.is_multipart():

                    for part in msg.walk():

                        if part.get_content_type() == "text/plain":

                            payload = part.get_payload(decode=True)

                            if payload:
                                charset = part.get_content_charset() or "utf-8"
                                body += payload.decode(
                                    charset,
                                    errors="ignore"
                                )

                else:

                    payload = msg.get_payload(decode=True)

                    if payload:
                        charset = msg.get_content_charset() or "utf-8"
                        body = payload.decode(
                            charset,
                            errors="ignore"
                        )

                
                match = re.search(r"\b\d{6}\b", body)

                if match:

                    otp = match.group()

                    print("New OTP extracted successfully")

                    return otp

            print("Waiting for a genuinely new OTP email...")

        finally:
            mail.logout()

        time.sleep(5)

    raise TimeoutError(
        "No new OTP email received within 120 seconds"
    )