from gtts import gTTS
import os

tts = gTTS('hello dear user, do you want to listen to a joke?', lang='en', tld="com.au")
tts.save('audio/welcome.mp3')

os.system("mpg123 " + "audio/welcome.mp3")