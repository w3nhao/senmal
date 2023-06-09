from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import smtplib

def send_notification(sender_email, sender_auth, receiver_email, msg, subject="Training Update", server="smtp.qq.com", port=465, retries=3):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = formataddr(["ML Training", sender_email])
    message["To"] = formataddr(["User", receiver_email])

    part = MIMEText(msg, 'plain')
    message.attach(part)

    for i in range(retries):
        try:
            with smtplib.SMTP_SSL(server, port) as server:
                server.login(sender_email, sender_auth)
                server.sendmail(sender_email, receiver_email, message.as_string())
                print("Email sent successfully")
                break
        except Exception as e:
            print(f"Failed to send notification. Error: {e}")
            if i < retries - 1:  # If not the last retry
                print("Retrying...")
            else:  # On last retry, raise error
                raise

if __name__ == "__main__":
    # Test cases
    sender_email = "sender@email.com" 
    sender_auth = "sender_auth"
    receiver_email = "receiver@email.com"
    msg = "This is a test message."
    subject = "Test Email"

    send_notification(sender_email, sender_auth, receiver_email, msg, subject)
