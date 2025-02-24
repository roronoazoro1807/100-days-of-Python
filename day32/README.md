# Birthday Email Automation Setup

## TL;DR
This script automatically sends birthday emails based on a CSV file. Set up your `.env` file, update `birthdays.csv`, create email templates, and run the script.

## Prerequisites
- Python installed
- Required libraries: `pandas`, `python-dotenv` (`pip install pandas python-dotenv`)
- `.env` file for secure credential storage

## Setup Steps

### 1. Configure Environment Variables
Create a `.env` file in the project directory and add:

```
MY_EMAIL=your_email@example.com
MY_PASSWORD=your_secure_password
SMTP_SERVER=smtp.yourprovider.com
```

If using Gmail, set `SMTP_SERVER=smtp.gmail.com`.

### 2. Update `birthdays.csv`
Ensure the file follows this format:

```
name,email,year,month,day
John Doe,johndoe@example.com,1990,2,24
Jane Smith,janesmith@example.com,1995,3,15
```

### 3. Create Letter Templates
Inside `letter_templates`, create three text files (`letter_1.txt`, `letter_2.txt`, `letter_3.txt`) with a birthday message:

```
Happy Birthday [NAME]!

Wishing you a fantastic day filled with joy and happiness!

Best,
Your Friend
```

### 4. Run the Script
Run the following command:

```
python birthday_email.py
```

## Troubleshooting
- **Missing environment variables:** Ensure `.env` is properly set and loaded.
- **SMTP connection issues:** Double-check `SMTP_SERVER` and credentials.
- **Email not sent:** Verify email addresses and ensure SMTP settings allow sending.
- **No birthdays found:** Check if today’s date matches any entry in `birthdays.csv`.

---
Now you're all set! The script will send birthday emails automatically if any match today’s date.

