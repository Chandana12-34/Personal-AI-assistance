AI Personal Voice Assistant - Luna
Project Description
Luna is an AI-powered personal voice assistant built using Python. It can interact with users through voice commands to perform a variety of tasks such as fetching information from the web, sending emails, playing music, taking photos, and managing system operations. Luna is designed to be highly customizable, with the ability to handle a wide range of user commands.

Features
Luna voice assistant can perform the following tasks:

Open Applications/Programs:

Open MS Word, Notepad, Command Prompt, Calculator, File Explorer, etc.
Web Operations:

Open websites (e.g., YouTube, Gmail, Google).
Play videos or music on YouTube.
Search for content on the web (e.g., images or information).
System Operations:

Shutdown, restart, or log off the system.
Take screenshots.
Open and control specific browsers (Google Chrome, Firefox, Microsoft Edge).
Mute and unmute system audio.
Information Fetching:

Get the current weather forecast for a specified city.
Fetch the latest news headlines.
Fetch information from Wikipedia.
Answer general knowledge and geographical questions.
Email Functionality:

Send emails via Gmail.
Miscellaneous Tasks:

Tell the current time and date.
Get jokes and random facts.
Generate a random number.
Fetch system info like CPU, memory, and battery status.
Copy text from clipboard.
Capture photos via webcam.
Requirements
Python: Version 3.7 or higher.
Libraries:
speech_recognition
pyttsx3
datetime
wikipedia
pywhatkit
pyjokes
pyautogui
psutil
pyperclip
requests
pyowm
smtplib
ecapture
random
ctypes
win32api
win32con
You can install the required libraries using pip:

bash
Copy
pip install speechrecognition pyttsx3 wikipedia pywhatkit pyjokes pyautogui psutil pyperclip requests pyowm smtplib ecapture random ctypes pywin32
Setup Instructions
1. Clone the repository:
bash
Copy
git clone https://github.com/yourusername/luna-assistant.git
cd luna-assistant
2. Install the required libraries:
bash
Copy
pip install -r requirements.txt
3. Set up the Weather API:
Go to OpenWeatherMap and create an account.
Generate an API key.
Replace the placeholder in the code with your API key:
python
Copy
owm = pyowm.OWM('your_owm_api_key')
4. Set up Gmail for email functionality:
Enable "Less Secure Apps" on your Gmail account or use OAuth2 authentication.
Replace the email and password in the send_email function with your own Gmail credentials.
Important: It's recommended to use environment variables or a configuration file to securely store your credentials.
5. Run the assistant:
bash
Copy
python luna_assistant.py
Usage
To activate Luna, simply speak any of the following commands:

"Hey Luna, open YouTube."
"Hey Luna, what is the time?"
"Hey Luna, take a photo."
"Hey Luna, send an email."
"Hey Luna, what's the weather in New York?"
The assistant will respond to your commands and perform the requested task.

Example Commands
Opening applications:

"Open MS Word"
"Open Notepad"
"Open Chrome"
Web-based tasks:

"Search for butterfly images."
"Play music on YouTube."
"Open Gmail."
General knowledge queries:

"What is the capital of California?"
"Tell me a joke."
"What is Sin 90?"
System tasks:

"Shutdown the system."
"Take a screenshot."
"Tell me the time."
Information fetching:

"What's the weather in Paris?"
"What's the latest news?"
Contributing
Fork the repository.
Clone your forked repository.
Create a new branch (git checkout -b feature-name).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to your branch (git push origin feature-name).
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Special thanks to the following libraries and services:
Pyttsx3
Speech Recognition
PyOWM
Wikipedia
PyWhatKit
Note
Be sure to replace any sensitive information (like API keys and credentials) before sharing or deploying your code. Always keep security in mind when working with external APIs and services.
