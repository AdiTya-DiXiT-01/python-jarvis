import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
from client import ai_response

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    cmd = command.lower()
    if 'open google' in cmd:
        speak('Opening Google')
        webbrowser.open('https://www.google.com')
    elif 'open youtube' in cmd:
        speak('Opening YouTube')
        webbrowser.open('https://www.youtube.com')
    elif 'open stack overflow' in cmd:
        speak('Opening Stack Overflow')
        webbrowser.open('https://stackoverflow.com')
    elif cmd.startswith('play music'):
        song = cmd.replace('play music', '')
        speak('Playing: ' + song)
        webbrowser.open('https://www.youtube.com/results?search_query=' + song.strip())
    elif 'news' in cmd:
        try:
            api_key = '3f6fbb138c91448b9e59dbc5de540c54'
            url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
            response = requests.get(url)
            news = response.json()
            for article in news['articles'][:5]:
                speak(article['title'])
        except:
            speak("Sorry, I couldn't fetch the news.")
    else:
        response = ai_response(command)
        speak(response)

if __name__ == "__main__":
    speak("Hello, I am your voice assistant. How can I help you today?")
    
    while True:
        try:
            with sr.Microphone() as source:
                print("Say 'Jarvis' to activate...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                trigger = recognizer.recognize_google(audio)
                if trigger.lower() == 'jarvis':
                    speak("Hey ya, I am listening!")
                    with sr.Microphone() as source:
                        audio = recognizer.listen(source, timeout=5)
                        command = recognizer.recognize_google(audio)
                        print("Command received:", command)
                        processCommand(command)
        except Exception as e:
            print(f"Error: {e}")
