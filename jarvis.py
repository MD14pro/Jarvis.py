import subprocess
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def exit_program():

    sys.exit(0)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am  JARVIS created by students of Computer branch, final year Sooshganga polytechnic. How may I help you?")
    print("I am  JARVIS created by students of Computer branch, final year Sushganga polytechnic. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching in wikipedia...")
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            exit_program()

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
            exit_program()

        elif 'how are you jarvis' in query:
            speak("I am fine sir. Thank you.")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google chrome.com")
            exit_program()

        elif 'jarvis sleep' in query:
            print("exiting program...")
            speak("exiting program")
            subprocess.run(["python", "hotword detection+face recognition.py"])
            exit_program()


        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"sir, the time is {strTime}")
            speak("sir, I do anything else for you?")


        elif 'virtual mouse' in query:
            subprocess.run(["python", "virtual mouse mark 1.py"])


