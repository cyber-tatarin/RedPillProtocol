import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import markdown
from dotenv import load_dotenv, find_dotenv
from weasyprint import HTML

load_dotenv(find_dotenv())

gmail_user = os.getenv('GMAIL_USER')
gmail_password = os.getenv('GMAIL_PASSWORD')


def send_email(header, body, recipient_email, attachment_path=None):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Port 587 is used for TLS encryption
        server.starttls()  # Enable TLS (Transport Layer Security)
        server.login(gmail_user, gmail_password)
    except Exception as e:
        print("Error: Unable to connect to Gmail's SMTP server.")
        print(e)
        exit()

    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = recipient_email
    msg['Subject'] = header
    msg.attach(MIMEText(body, 'plain'))

    if attachment_path:
        try:
            # Open the file to be sent
            with open(attachment_path, "rb") as attachment:
                part = MIMEText(attachment.read().decode("utf-8"), "pdf")
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {attachment_path}",
                )
                msg.attach(part)
        except Exception as e:
            print("Error: Unable to attach file.")
            print(e)
            exit()

    try:
        server.sendmail(gmail_user, recipient_email, msg.as_string())
        print("Email sent successfully!")
        if attachment_path:
            os.remove(attachment_path)
            print(f"File {attachment_path} deleted.")
    except Exception as e:
        print("Error: Unable to send email.")
        print(e)

    server.quit()


def create_pdf_file(folder_path, file_name, content, participant):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Create dir for BP. Existence: {os.path.exists(folder_path)}")
    file_name = os.path.join(folder_path, participant + "-" + file_name)
    print(file_name)

    # Write the content to the file
    html_content = markdown.markdown(content)

    # Convert HTML content to a PDF
    HTML(string=html_content).write_pdf(file_name)

    return file_name  # Return the full path of the created file
