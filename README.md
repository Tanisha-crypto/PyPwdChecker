PyPwd Checker is a simple yet powerful Python-based tool to analyze and validate password strength.
It helps users create secure passwords by checking various strength parameters like length, complexity, and the presence of uppercase, lowercase, numbers, and special characters.

🚀 Features

✅ Checks password strength (Weak, Moderate, Strong)

🔢 Validates length and character variety

🔒 Detects commonly used or leaked passwords (optional list-based check)

⚡ Lightweight and easy to integrate into other projects

💻 Works on any platform (Windows / Linux / macOS)

🧩 Requirements

Before running the project, ensure you have the following:

Python 3.7 or above

colorama (for colored terminal output, optional)

Install dependencies using:

pip install -r requirements.txt

🛠️ Installation

Clone the repository:

git clone https://github.com/<your-username>/pypwd-checker.git


Navigate into the project folder:

cd pypwd-checker


Run the script:

python main.py

🧠 How It Works

The program takes a password input from the user.

It analyzes multiple factors:

Length of password

Presence of uppercase & lowercase letters

Inclusion of digits & special characters

Optionally checks against a list of weak or common passwords

It gives feedback on the strength and suggestions for improvement.

🧾 Example Output
Enter your password: Tanisha@123

✅ Length check: Passed
✅ Uppercase check: Passed
✅ Lowercase check: Passed
✅ Digit check: Passed
✅ Special character check: Passed

🔹 Password Strength: STRONG 💪

📂 Project Structure
pypwd-checker/
│
├── main.py               # Entry point for password checking
├── checker.py            # Contains the logic for password strength analysis
├── requirements.txt      # Dependencies
├── common_passwords.txt  # (Optional) List of weak passwords
└── README.md             # Project documentation

💡 Future Enhancements

Add GUI using Tkinter or PyQt

Integrate with web forms (Flask/Django plugin)

Password breach check using HaveIBeenPwned API

Export reports in JSON or CSV format

