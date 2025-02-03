# Day 30 - Password Manager with JSON Storage

## What I Learned:

- **Working with JSON Files:** Learned how to store and retrieve data using JSON files instead of plain text.
  
- **File Handling in Python:** Implemented reading, writing, and updating JSON files while handling exceptions like `FileNotFoundError`.

- **Error Handling & Exception Management:** Used `try-except` blocks to manage missing files and invalid key lookups in the JSON file.

- **Password Security:** Improved password management by allowing users to store, retrieve, and search for saved credentials.

- **Tkinter UI Improvements:** Enhanced user experience by adding a search functionality, clear input button, and a better-organized interface.

## Additional Features Added

### 🔍 Search for Saved Passwords:
- Users can enter a website name and click the **Search Website** button to retrieve saved login credentials.
- Displays an error message if the website is not found in the JSON file.

### 🔄 Improved Data Storage (JSON):
- Passwords are now saved in `data.json` instead of a text file.
- Each website entry is stored as a dictionary with its corresponding email and password.

### ✍️ Overwriting & Updating Data:
- If the file doesn’t exist, the program creates a new `data.json` file automatically.
- If the website already exists in the JSON file, new login details are added instead of overwriting everything.

### 📋 Copy Password to Clipboard:
- When generating a password, it is automatically copied to the clipboard for easy pasting.

### 🧹 Clear Input Fields:
- Added a **Clear Info** button to reset the website and password fields instantly.

## How It Works:

1. **Save a New Password:**
   - Enter a website name, email, and password.
   - Click **Save Info** to store the credentials in `data.json`.

2. **Generate a Secure Password:**
   - Click **Generate Password** to create a strong password with letters, numbers, and symbols.
   - The password is automatically copied to the clipboard.

3. **Search for a Password:**
   - Enter a website name and click **Search Website** to retrieve saved credentials.
   - If the website exists, a pop-up will display the email and password.

4. **Clear Input Fields:**
   - Click **Clear Info** to erase the website and password input fields.
