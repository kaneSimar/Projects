import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import datetime
import wikipedia
import webbrowser
import pyjokes
import os
import smtplib

print("initializing Jarvis")

MASTER = "SIMAR..."

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    speak("How may I help you")
def takeCommand():

    r = sr.Recognizer() 
    r.energy_threshold = 400
    r.dynamic_energy_threshold = True
    dur = 10000
  
    with sr.Microphone() as source: 
        print("Listening...") 
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, dur)