import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(5 <= hour and hour < 12):
        speak('good morning Minho')
    elif(12 <= hour and hour < 17):
        speak('good after noon Minho')
    elif(17 <= hour and hour <= 21):
        speak('good evening Minho')
    elif(21 < hour and hour < 5):
        speak('good night Minho')
    speak("Hi I'm your desk support. How may i help you today?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('recognizing')
        query = r.recognize_google(audio, language='en-in')
        print('user said ' + query)
        return query
    except:
        print("I didn't understand. Tell me a new time")
        return 'None'


if(__name__ == '__main__'):
    wishMe()
    query=takeCommand().lower()
    if 'wikipedia' in query:
        speak('searching wikipedia')
        query=query.replace('wikipedia','')
        results=wikipedia.summary(query,sentences=3)
        print('')
        print(results)
        speak(results)
    elif 'youtube' in query:
        query=query.replace('youtube','')
        query=query.replace('in','')
        query=query.replace('open','')
        query=query.replace('search','')
        query=query.replace(' ','+')
        webbrowser.open('https://www.youtube.com/results?search_query='+query)
    elif 'google' in query:
        query=query.replace('google','')
        query=query.replace('in','')
        query=query.replace('search','')
        query=query.replace('open','')
        query=query.replace(' ','+')
        webbrowser.open('https://www.google.com/search?q='+query)
    elif 'visual' in query or 'studio'in query or 'code' in query:
        path="C:/Users/Minho/AppData/Local/Programs/Microsoft VS Code/Code.exe"
        os.startfile(path)