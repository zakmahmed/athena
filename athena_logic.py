import speech_recognition as sr 
from datetime import date
import time
import os
from gtts import gTTS
import playsound
import random
import sys
import pyjokes 



class Athena:
    def __init__(self):
        self.speak("Initializing...")
        self.run()

    def run(self):
        self.speak("Hey Zak what can I do for you?")
        while 1:
            self.data = self.recordAudio()
            self.make_decision(self.data)
            
    def speak(self, audioString):         
        tts = gTTS(text = audioString, lang = 'en-gb', tld='co.uk')
        r1 = random.randint(1,1000)
        self.audiofile = str(r1)+"audio.mp3"
        tts.save(self.audiofile)
        print(audioString)
        playsound.playsound(self.audiofile)
        os.remove(self.audiofile)
        

    def recordAudio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            audio = r.listen(source)

            self.data = ""
            try:
                self.data = r.recognize_google(audio)
            except Exception:
                print("Unfortunately, I could not understand what you just said, please try again")
        
            return self.data

    def make_decision(self,data):
        print(data)
        if "how are you" in data:
            self.speak("I am fine")

        if "date" in data:
            d = date.today()
            Current_date = d.strftime("%d %B %Y")
            self.speak(Current_date)

        if "time" in data:
            t = time.localtime()
            self.current_time = time.strftime("%I:%M %p",t)
            self.speak(self.current_time)

        if "joke" in data:
            self.speak(pyjokes.get_joke(category='neutral'))



    #Websearch
               
    
    #Calendar API

        if "that is all" in self.data:
            self.speak("Very Well")
            # os.remove(self.audiofile)
            sys.exit(0)
        