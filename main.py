 import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from openai import OpenAI
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, IMAP_SERVER, SMTP_SERVER, OPENAI_API_KEY

# إعداد OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "أنت مساعد بريد إلكتروني تلقائي."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def check_inbox():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mail.select('inbox')

    status, messages = mail.search(None, '(UNSEEN)')
    email_ids = messages[0].split()

    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, '(RFC822)')
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        sender = msg['From']
        subject = msg['Subject']
        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True).decode('utf-8')
        else:
            body = msg.get_payload(decode=True).decode('utf-8')

        print(f"رسالة جديدة من: {sender}\nالموضوع: {subject}\nالمحتوى: {body}\n")

        response = generate_response(body)
        send_reply(sender, subject, response)

def send_reply(to_email, subject, body):
    server = smtplib.SMTP_SSL(SMTP_SERVER, 465)
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    msg = MIMEText(body, 'plain', 'utf-8')
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg['Subject'] = f"Re: {subject}"

    server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
    server.quit()
    print(f"تم إرسال الرد إلى: {to_email}")

if __name__ == '__main__':
    print("يعمل بوت الرد التلقائي...")
    check_inbox()

