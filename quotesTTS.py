from pygame import mixer
from gtts import gTTS
from mutagen.mp3 import MP3
import time
import requests

def getQuote():
    response = requests.request("GET", "https://zenquotes.io/api/random")
    jsonResponse = response.json()
    quoteText = jsonResponse[0]['q'] + ' -' + jsonResponse[0]['a']
    print(quoteText)
    return(quoteText)

def main():
    tts = gTTS(getQuote())
    tts.save('speech.mp3')
    mixer.init()
    mixer.music.load('speech.mp3')
    mixer.music.play()
    time.sleep(MP3('speech.mp3').info.length)

main()