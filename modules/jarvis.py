import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I did not understand")
        return ""

# Greeting
speak("Hello, I am Jarvis. How can I help you?")

while True:
    command = take_command()

    # TIME
    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")

    # DATE
    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {date}")

    # OPEN GITHUB
    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    # OPEN VS CODE
    elif "open visual studio code" in command or "open vscode" in command:
        speak("Opening Visual Studio Code")
        os.system("code")

    # OPEN GOOGLE
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # EXIT
    elif "exit" in command or "bye" in command:
        speak("Goodbye! Have a nice day")
        break
