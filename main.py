import speech_recognition as sr
from gtts import gTTS
import os
import requests

def joke():
    x = requests.get('https://icanhazdadjoke.com/slack')
    response = x.json()

    return response["attachments"][0]["text"]

def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
        print("Recognising....") 
        text = r.recognize_google(audio,language='en-in')
        print(text)
        if text == "yes":
            print(text)
            x = requests.get('https://icanhazdadjoke.com/slack')
            response = x.json()

            joke = response["attachments"][0]["text"]
            joke = gTTS(joke, lang='en', tld="com.au")
            joke.save('audio/joke.mp3')
            os.system("mpg123 " + "audio/joke.mp3")
        else:
            print('Sorry i didnt hear that')

def ask():
    welcome = gTTS('hello dear user, do you want to listen to a joke?', lang='en', tld="com.au")
    welcome.save('audio/welcome.mp3')
    os.system("mpg123 " + "audio/welcome.mp3")
    takecom()

ask()