from gtts import gTTS
import os

welcome = gTTS('hello dear user, do you want to listen to a joke?', lang='en', tld="com.au")
welcome.save('audio/welcome.mp3')

os.system("mpg123 " + "audio/welcome.mp3")