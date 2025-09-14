# Voice Assistant - Clara

## Objective

The objective of this project is to design and implement a Python-based Voice Assistant capable of performing basic system operations, retrieving information from the web, and interacting with users through speech. The assistant, named Clara, provides hands-free interaction with the computer by recognizing voice commands and responding using text-to-speech.

## Tools & Technologies Used

- Programming Language: Python 3

- Libraries & Modules:

 - speech_recognition → for speech-to-text conversion

 - pyttsx3 → for text-to-speech conversion

 - webbrowser → to open websites and perform online searches

 - os → for executing system applications

 - datetime → to fetch date and time

 - time → for handling delays in execution

### Platform: Windows (works with system apps like Notepad, Paint, etc.)

## Features Implemented

- Speech Recognition – Takes user input via microphone and converts it to text

- Text-to-Speech – Responds to the user

- System Application Control – Opens applications like Calculator, Notepad, Paint, Command Prompt, File Explorer

- Web Applications & Websites – Opens Gmail, Google Drive, YouTube, Wikipedia, Facebook, Twitter (X), Instagram, LinkedIn, W3Schools, Geeks for Geeks, etc.

- Information Retrieval – Provides current time and date

- Search & News Updates – Performs Google searches, plays YouTube videos, fetches news updates

- Exit Command – Gracefully ends execution on "exit" or "quit" command

## Steps Performed

- Environment Setup: Installed Python and required libraries (speechrecognition, pyttsx3).

- Voice Engine Initialization: Configured pyttsx3 and set speech rate.

- Speech Input Processing: Used speech_recognition to listen via microphone and convert speech into text.

- Command Execution:

 - If the command matched system apps → opened Calculator, Notepad, Paint, CMD, Explorer.

 - If the command matched web apps/websites → opened Gmail, YouTube, Wikipedia, social media, or performed Google search.

 - If the command requested date/time/news → fetched details and responded via speech.

### Output: The assistant Clara responded with both printed text and spoken response.

## Outcome

- Successfully created a working voice assistant that interacts with users naturally.

- Demonstrated integration of speech recognition, system automation, and web-based search.

- Provides an engaging and interactive way to control system and internet resources via voice commands.

## How to Run the Project

- Install Python (>=3.8) on your system.

- Install required libraries:

   pip install speechrecognition pyttsx3 pyaudio


- Save the code file as voice_assistant.py.

- Run the program:

   python voice_assistant.py

## Keywords for Commands

- Keyword for System apps (Notepad, Calculator, Paint, CMD, Explorer) → "Open ___" particular app

- Keyword for Google search → "Search ___"

- Keyword for YouTube → "Play ___"

- Keyword for Wikipedia → "Look up ___ on Wikipedia"

- Keyword for coding help → "Coding help on W3Schools ___" or "Coding help on Geeks for Geeks ___"

- Keyword for News → "___ news" or simply "News"

- Keyword for Date → "What is the date"

- Keyword for Time → "What is the time"

- Keyword for Exit → "Exit" or "Quit"
