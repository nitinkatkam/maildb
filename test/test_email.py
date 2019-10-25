from smtplib import SMTP
from email.message import EmailMessage

def main():
    client = SMTP(host='::1', port=8025)
    msg = EmailMessage()
    msg.set_content("Test email body")
    msg['From'] = 'nospam@nospam.org'
    msg['To'] = 'nitin@nospam.org'
    msg['Subject'] = 'This is not spam'
    client.send_message(msg)
    client.quit()

if __name__=='__main__':
    main()
