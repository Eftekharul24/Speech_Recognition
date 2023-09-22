# pip install pyaudio
# pip install SpeechRecognition
# pip install SpeechRecognition pyaudio

import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Open microphone for recording
with sr.Microphone() as source:
    print("Say something...")
    audio = r.listen(source)

# Recognize speech
try:
    text = r.recognize_google(audio, language='bn-BD')  # Specify Bengali language
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print("Could not request results. Check your network connection.")
