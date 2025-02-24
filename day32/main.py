from datetime import datetime
import pandas as pd
import random
import smtplib
import os
import logging

# Setup logging
logging.basicConfig(filename="birthday_mail.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Load environment variables
MY_EMAIL = os.getenv("MY_EMAIL", "dimpuAmit143@example.com")
MY_PASSWORD = os.getenv("MY_PASSWORD", "fakepassword123")  
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")  

if not MY_EMAIL or not MY_PASSWORD or not SMTP_SERVER:
    logging.error("Missing environment variables. Please set MY_EMAIL, MY_PASSWORD, and SMTP_SERVER.")
    raise ValueError("Missing environment variables.")

# Get today's date
today = datetime.now()
today_tuple = (today.month, today.day)

# Load birthdays
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row for (_, row) in data.iterrows()}

print("Script started...")
if today_tuple in birthdays_dict:
    print("Birthday found!")
    birthday_person = birthdays_dict[today_tuple]
    print(f"Sending email to: {birthday_person['name']} ({birthday_person['email']})")
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    try:
        with open(file_path) as letter_file:
            contents = letter_file.read().replace("[NAME]", birthday_person["name"])

        # Test SMTP connection
        try:
            with smtplib.SMTP(SMTP_SERVER) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                print("SMTP login successful!")
                
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=birthday_person["email"],
                    msg=f"Subject:Happy Birthday!\n\n{contents}"
                )

            logging.info(f"Email sent to {birthday_person['name']} ({birthday_person['email']})")
            print("Email sent successfully!")
        except Exception as smtp_error:
            logging.error(f"SMTP error: {smtp_error}")
            print(f"SMTP error: {smtp_error}")

    except Exception as e:
        logging.error(f"Failed to send email to {birthday_person['email']}: {e}")
        print(f"Error: {e}")
else:
    print("No birthdays today.")
