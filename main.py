import speech_recognition as sr
from gtts import gTTS
import os


def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising....") 
        text = r.recognize_google(audio,language='en-in')
        if text == "yes":
            print('Cool')
        else:
            print('Sorry i didnt hear that')
    except Exception:      
        print("Network connection error") 
        return "none"
    return text

def ask():
    welcome = gTTS('hello dear user, do you want to listen to a joke?', lang='en', tld="com.au")
    welcome.save('audio/welcome.mp3')
    os.system("mpg123 " + "audio/welcome.mp3")

    takecom()

ask()