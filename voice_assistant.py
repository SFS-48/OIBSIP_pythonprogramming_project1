import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import os
import time

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # speech speed

# Select a female voice
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    print("Clara:", text)
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.5)  # ensure speech finishes

def take_command():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

# Open system apps
def open_system_apps(command):
    if "calculator" in command:
        os.system("calc")
        speak("Opening Calculator")
    elif "notepad" in command:
        os.system("notepad")
        speak("Opening Notepad")
    elif "paint" in command:
        os.system("mspaint")
        speak("Opening Paint")
    elif "cmd" in command or "command prompt" in command:
        os.system("start cmd")
        speak("Opening Command Prompt")
    elif "explorer" in command or "file explorer" in command:
        os.system("explorer")
        speak("Opening File Explorer")
    else:
        return False  # app not recognized
    return True

# Open web apps and websites
def open_websites(command):
    # Specific web apps
    if "gmail" in command:
        webbrowser.open("https://mail.google.com")
        speak("Opening Gmail")
    elif "google drive" in command:
        webbrowser.open("https://drive.google.com")
        speak("Opening Google Drive")
    elif "facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
    elif "twitter" in command or "x" in command:
        webbrowser.open("https://twitter.com")
        speak("Opening Twitter")
    elif "instagram" in command:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram")
    elif "linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn")
    
    # General searches
    elif "search" in command:
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching Google for {query}")
    elif "play" in command and "youtube" in command:
        query = command.replace("play", "").replace("on youtube", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        speak(f"Playing {query} on YouTube")
    elif "look up" in command and "wikipedia" in command:
        query = command.replace("look up", "").replace("on wikipedia", "").strip()
        webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")
        speak(f"Looking up {query} on Wikipedia")
    elif "coding help" in command and "w3schools" in command:
        query = command.replace("coding help", "").replace("on w3schools", "").strip()
        webbrowser.open(f"https://www.w3schools.com/howto/howto_search.asp?q={query}")
        speak(f"Opening W3Schools for {query}")
    elif "coding help" in command and "geeks for geeks" in command:
        query = command.replace("coding help", "").replace("on geeks for geeks", "").strip()
        webbrowser.open(f"https://www.geeksforgeeks.org/?s={query}")
        speak(f"Opening Geeks for Geeks for {query}")
    elif "news" in command:
        query = command.replace("news", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}+news")
            speak(f"Showing news for {query}")
        else:
            webbrowser.open("https://www.bbc.com/news")
            speak("Opening latest news")
    else:
        speak("Sorry, I can't perform that action.")

# Main function for single input per run
def main():
    speak("Hello! I am Clara, your assistant. Please say your command.")
    command = take_command()
    
    if command == "":
        speak("No valid command detected. Exiting.")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {now}")
    elif "date" in command:
        today = datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")
    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a great day.")
    else:
        # Try system apps first
        if not open_system_apps(command):
            # If not a system app, try websites/web apps
            open_websites(command)

if __name__ == "__main__":
    main()
