import requests
from datetime import datetime
import smtplib
import time
import os

# Configuration
MY_EMAIL = "dimpuAmit143@outlook.com"
MY_PASSWORD = "your_secure_password"
SMTP_SERVER = "smtp.outlook.com"
TO_EMAIL = "dimpuAmit143@gmail.com"
MY_LAT = 51.507351
MY_LONG = -0.127758

# Check if ISS is within ±5 degrees of user's location
def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)

# Check if it's nighttime at the user's location
def is_night():
    params = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.utcnow().hour
    return time_now >= sunset or time_now <= sunrise

# Main loop to check conditions and send email
while True:
    if is_iss_overhead() and is_night():
        try:
            with smtplib.SMTP(SMTP_SERVER) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=TO_EMAIL,
                    msg="Subject: Look Up! 👆\n\nThe ISS is passing above your location right now!"
                )
            print("Email sent successfully!")
        except Exception as e:
            print(f"Email sending failed: {e}")

    print("Checked at:", datetime.utcnow())
    time.sleep(60)
