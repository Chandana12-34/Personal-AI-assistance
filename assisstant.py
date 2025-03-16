import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import pywhatkit as kit
import pyjokes
import threading
import pyautogui
import psutil
import smtplib
import random
import pyowm
import pyperclip
import requests
import ctypes
import sys
import win32api
import win32con

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")

def takeCommand():
    r = sr.Recognizer()
    r.energy_threshold = 1000000
    r.dynamic_energy_threshold = True
    r.pause_threshold = 0.5

    with sr.Microphone() as source:
        print("Listening... Please speak clearly.")
        r.adjust_for_ambient_noise(source, duration=3)

        try:
            audio = r.listen(source, timeout=10)
            print("Recognizing...")
            statement = r.recognize_google(audio, language='en-US')
            print(f"user said: {statement}")

        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that. Please say again.")
            return "None"
        except sr.RequestError:
            speak("Sorry, there was an issue with the speech recognition service.")
            return "None"
        except Exception as e:
            speak("An error occurred.")
            return "None"

    return statement.lower()

def open_ms_word():
    try:
        subprocess.Popen(["C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"])
        speak("Opening Microsoft Word.")
    except FileNotFoundError:
        speak("Microsoft Word is not installed in the expected location.")

def open_folder(folder_path):
    if os.path.exists(folder_path):
        os.startfile(folder_path)
        speak(f"Opening folder {folder_path}.")
    else:
        speak("The specified folder does not exist.")

def open_file(file_path):
    if os.path.exists(file_path):
        os.startfile(file_path)
        speak(f"Opening file {file_path}.")
    else:
        speak("The specified file does not exist.")

def capture_photo_thread():
    try:
        ec.capture(0, "Assistant Camera", "photo.jpg")
        speak("Photo taken!")
    except Exception as e:
        speak("An error occurred while trying to take the photo.")
        print(str(e))

def send_email(to, subject, body):
    try:
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')
        msg = MIMEMultipart()
        msg['From'] = 'your_email@gmail.com'
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail('your_email@gmail.com', to, text)
        server.quit()
        speak("Email sent successfully!")
    except Exception as e:
        speak(f"Failed to send email. Error: {str(e)}")

def play_music():
    kit.playonyt("music")
    speak("Playing music on YouTube.")

def open_website(url):
    webbrowser.open(url)
    speak(f"Opening {url}.")

def shutdown_system():
    speak("Your system is shutting down in 10 seconds.")
    subprocess.call(["shutdown", "/s", "/f", "/t", "10"])

def restart_system():
    speak("Your system is restarting in 10 seconds.")
    subprocess.call(["shutdown", "/r", "/f", "/t", "10"])

def logoff_system():
    speak("Logging off your system in 10 seconds.")
    subprocess.call(["shutdown", "/l"])

def get_weather():
    try:
        owm = pyowm.OWM('your_owm_api_key')  # Replace with your OWM API Key
        observation = owm.weather_at_place("New York,US")
        w = observation.get_weather()
        temp = w.get_temperature('celsius')['temp']
        speak(f"The current temperature is {temp} degrees Celsius.")
    except Exception as e:
        speak("Unable to fetch weather details.")
        print(str(e))

def get_joke():
    joke = pyjokes.get_joke()
    speak(joke)
    print(joke)

def play_video(video_name):
    kit.playonyt(video_name)
    speak(f"Playing {video_name} on YouTube.")

def open_calculator():
    subprocess.Popen('calc.exe')
    speak("Opening Calculator.")

def open_notepad():
    subprocess.Popen('notepad.exe')
    speak("Opening Notepad.")

def open_command_prompt():
    subprocess.Popen('cmd.exe')
    speak("Opening Command Prompt.")

def get_cpu_info():
    cpu = psutil.cpu_percent()
    speak(f"Current CPU usage is {cpu}.")

def get_memory_info():
    memory = psutil.virtual_memory()
    speak(f"Total memory is {memory.total} bytes and free memory is {memory.available} bytes.")

def get_battery_info():
    battery = psutil.sensors_battery()
    speak(f"Battery is at {battery.percent}%")

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    speak("Screenshot taken and saved!")

def copy_text():
    text = pyperclip.paste()
    speak(f"The copied text is: {text}")

def tell_time():
    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {time_now}.")

def tell_date():
    today = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {today}.")

def get_ip_address():
    ip = requests.get('https://api.ipify.org').text
    speak(f"Your IP address is {ip}.")

def make_random_number():
    number = random.randint(1, 100)
    speak(f"The generated random number is {number}.")

def play_random_fact():
    facts = ["The sun is 93 million miles away from Earth.", "Honey never spoils.", "There are more stars in the universe than grains of sand on Earth."]
    fact = random.choice(facts)
    speak(fact)

def shutdown_program():
    speak("Shutting down the program.")
    sys.exit()

def open_file_explorer():
    subprocess.Popen('explorer')
    speak("Opening File Explorer.")

def open_microsoft_edge():
    subprocess.Popen('msedge')
    speak("Opening Microsoft Edge.")

def open_firefox_browser():
    subprocess.Popen('firefox')
    speak("Opening Firefox Browser.")

def open_chrome_browser():
    subprocess.Popen('chrome')
    speak("Opening Google Chrome.")

def mute_system():
    win32api.keybd_event(0xA0, 0, 0, 0)  # Volume mute (Windows key)
    win32api.keybd_event(0xA0, 0, win32con.KEYEVENTF_KEYUP, 0)
    speak("System muted.")

def unmute_system():
    win32api.keybd_event(0xA0, 0, 0, 0)  # Volume unmute (Windows key)
    win32api.keybd_event(0xA0, 0, win32con.KEYEVENTF_KEYUP, 0)
    speak("System unmuted.")

# Main assistant loop
if __name__ == '__main__':
    speak("Loading your AI personal assistant - G-One")
    wishMe()

    while True:
        speak("How can I help you today?")
        statement = takeCommand()

        if "goodbye" in statement or "exit" in statement:
            speak('Goodbye! Shutting down.')
            break

        elif "open ms word" in statement:
            open_ms_word()

        elif "open folder" in statement:
            speak("What is the folder path?")
            folder_path = takeCommand()
            open_folder(folder_path)

        elif "open file" in statement:
            speak("What is the file path?")
            file_path = takeCommand()
            open_file(file_path)

        elif "send email" in statement:
            speak("Please provide the recipient email.")
            to = takeCommand()
            speak("Please provide the subject.")
            subject = takeCommand()
            speak("Please provide the body.")
            body = takeCommand()
            send_email(to, subject, body)

        elif "play music" in statement:
            play_music()

        elif "open website" in statement:
            speak("Please provide the website URL.")
            url = takeCommand()
            open_website(url)

        elif "shutdown" in statement:
            shutdown_system()

        elif "restart" in statement:
            restart_system()

        elif "log off" in statement:
            logoff_system()

        elif "weather" in statement:
            get_weather()

        elif "joke" in statement:
            get_joke()

        elif "play video" in statement:
            speak("What video do you want to play?")
            video_name = takeCommand()
            play_video(video_name)

        elif "calculator" in statement:
            open_calculator()

        elif "notepad" in statement:
            open_notepad()

        elif "command prompt" in statement:
            open_command_prompt()

        elif "cpu usage" in statement:
            get_cpu_info()

        elif "memory usage" in statement:
            get_memory_info()

        elif "battery" in statement:
            get_battery_info()

        elif "take screenshot" in statement:
            take_screenshot()

        elif "copy text" in statement:
            copy_text()

        elif "time" in statement:
            tell_time()

        elif "date" in statement:
            tell_date()

        elif "ip address" in statement:
            get_ip_address()

        elif "random number" in statement:
            make_random_number()

        elif "random fact" in statement:
            play_random_fact()

        elif "shutdown program" in statement:
            shutdown_program()

        elif "file explorer" in statement:
            open_file_explorer()

        elif "microsoft edge" in statement:
            open_microsoft_edge()

        elif "firefox browser" in statement:
            open_firefox_browser()

        elif "chrome browser" in statement:
            open_chrome_browser()

        elif "mute system" in statement:
            mute_system()

        elif "unmute system" in statement:
            unmute_system()

        time.sleep(3)
