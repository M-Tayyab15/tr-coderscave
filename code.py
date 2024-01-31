import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_personalized_email(sender_email, sender_password, recipients, subject, body_template):
    # Set up the SMTP server (for Gmail in this example)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create an SMTP session
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Start TLS for security
        server.starttls()

        # Login to the email account
        server.login(sender_email, sender_password)

        # Iterate through recipients and send personalized emails
        for recipient in recipients:
            # Create message container
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient['email']
            msg['Subject'] = subject

            # Customize the body of the email based on the template
            personalized_body = body_template.format(**recipient)

            # Attach the personalized body to the email
            msg.attach(MIMEText(personalized_body, 'plain'))

            # Send the email
            server.sendmail(sender_email, recipient['email'], msg.as_string())

if __name__ == "__main__":
    # Sender's email and password (make sure to use an app password if using Gmail)
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_password'

    # Recipients list with personalized details
    recipients = [
        {'email': 'recipient1@example.com', 'name': 'John Doe'},
        {'email': 'recipient2@example.com', 'name': 'Jane Doe'}
        # Add more recipients as needed
    ]

    # Email subject
    subject = 'Personalized Email Example'

    # Email body template (you can customize this template)
    body_template = 'Hello {name},\n\nThis is a personalized email just for you!'

    # Send personalized emails
    send_personalized_email(sender_email, sender_password, recipients, subject, body_template)

    print("Personalized emails sent successfully.")