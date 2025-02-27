# ISS Tracker & Email Alert System

This script checks if the International Space Station (ISS) is passing over your location at night and sends an email alert.

## 📌 Features
- Checks ISS position using Open Notify API.
- Determines nighttime using the Sunrise-Sunset API.
- Sends an email alert if ISS is overhead at night.
- Runs continuously and checks every 60 seconds.


### 2️ Configure Email & Location
Edit the script and replace placeholders with your details:  
```python
MY_EMAIL = "dimpuAmit143@outlook.com"
MY_PASSWORD = "your_password"
SMTP_SERVER = "smtp.outlook.com"

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude
```

`

## 🚀 How It Works
- The script checks the ISS position.
- It verifies if the ISS is within ±5° of your location.
- It checks if it's nighttime at your location.
- If both conditions are met, an email alert is sent.
- The script runs continuously, checking every 60 seconds.

## 🔧 Troubleshooting
- **No email received?**  
  - Ensure SMTP settings and login credentials are correct.  
  - If using Gmail, enable "Less Secure Apps" or generate an App Password.  
- **Wrong location or ISS not detected?**  
  - Verify `MY_LAT` and `MY_LONG` are correctly set.  
  - Run `print(is_iss_overhead())` to debug ISS position.


