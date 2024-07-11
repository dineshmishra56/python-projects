# python-projects
Project From code with Dinesh Mishra

Email Validation and Sending Script
This project contains a Python script for validating email addresses, categorizing them into valid and invalid lists, and then sending personalized emails to the valid addresses using an SMTP server.

Project Structure
Email Validation:

Uses the email_validator package to validate email addresses.
Checks the domain of the email address for a valid MX (Mail Exchange) record using dns.resolver.

Reading Email List:

Reads email addresses from a file named email_list.txt.

Categorizing Emails:

Validates each email address and categorizes them into valid_emails and invalid_emails.
Writes the categorized emails to separate files: valid_emails.txt and invalid_emails.txt.

Email Sending:

Reads an email template from email_template.html.
Uses the SMTP protocol to send emails through a Gmail account.
Records the sent and failed emails into sent_emails.txt and failed_emails.txt.

Usage Instructions

Email Validation:

Ensure you have the necessary packages installed: smtplib, email-validator, and dnspython.
Place your list of email addresses in a file named email_list.txt in the same directory as the script.
Sending Emails:

Update the from_email and password variables with your Gmail account credentials.
Customize the email_template.html file to fit your email content. Use [name] as a placeholder for the recipient's name.
Run the script to send emails to the validated email addresses.


Notes:

Ensure you handle your email credentials securely and avoid hardcoding sensitive information in your script.
Update the SMTP server details if using a different email provider.
This script is intended for educational purposes and should be used responsibly.
