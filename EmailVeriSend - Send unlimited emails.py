import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_validator import validate_email, EmailNotValidError
import dns.resolver

# Email Validation
def validate_email_address(email):
    try:
        v = validate_email(email)
        try:
            dns.resolver.query(v["domain"], 'MX')
            return True
        except dns.resolver.NoAnswer:
            return False
    except EmailNotValidError as e:
        return False

# Read email list
with open('email_list.txt', 'r') as f:
    emails = f.readlines()

valid_emails = []
invalid_emails = []

for email in emails:
    if validate_email_address(email.strip()):
        valid_emails.append(email.strip())
    else:
        invalid_emails.append(email.strip())

# Write valid and invalid emails to separate files
with open('valid_emails.txt', 'w') as f:
    for email in valid_emails:
        f.write(email + '\n')

with open('invalid_emails.txt', 'w') as f:
    for email in invalid_emails:
        f.write(email + '\n')

# Email Sending
from_email = "your_email@gmail.com"  #add your own credentials here
password = "nwek xttv inks quuc"

# Read email template
with open('email_template.html', 'r', encoding='utf-8') as f:
    email_template = f.read()

# Initialize SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_email, password)

# Send emails
sent_emails = []
failed_emails = []

for email in valid_emails:
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = email
    msg['Subject'] = "Test Email"
    body = email_template.replace('[name]', email.split('@')[0])
    msg.attach(MIMEText(body, 'html'))

    try:
        server.send_message(msg)
        sent_emails.append(email)
    except Exception as e:
        failed_emails.append(email)

server.quit()

# Write sent and failed emails to separate files
with open('sent_emails.txt', 'w') as f:
    for email in sent_emails:
        f.write(email + '\n')

with open('failed_emails.txt', 'w') as f:
    for email in failed_emails:
        f.write(email + '\n')
