import speech_recognition as sr
r=sr.Recognizer()

import datetime
import webbrowser
import pyttsx3
import numpy as np
import subprocess
import pywhatkit

a1=pyttsx3.init()
a2=pyttsx3.init()
a4=pyttsx3.init()

i=0
p=0

a1.say("Please enter the password below.")
a1.runAndWait()

print("OPEN GOOGLE,OPEN YOUTUBE, PLAY "" ON YOUTUBE, WHATS THE TIME, OPEN INSTAGRAM, EXIT")
pwd=input("PASSWORD:")

hour=int(datetime.datetime.now().hour)
def play_on_youtube(command):
    pywhatkit.playonyt(command)
if pwd=='kartick14':
    if hour>=0 and hour<12:
        a2.say("Hello Sir, Good Morning. JARVIS at your service. Importing all prefrences from home interface, system is now fully operational.")
        a2.runAndWait()
    elif hour>=12 and hour<18:
        a2.say("Hello Sir, Good Afternoon. JARVIS at your service. Importing all prefrences from home interface, system is now fully operational.")
        a2.runAndWait()
    else:
        a2.say("Hello Sir, Good Evening. JARVIS at your service. Importing all prefrences from home interface, system is now fully operational.")
        a2.runAndWait()
    while i==0:
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(mic)
            print("Please say something....")
            audio=r.listen(mic)
            try:
                cmd = r.recognize_google(audio)
                cmd2=cmd.lower()
                length=len(cmd)
                txt=11
                var=length-txt
                task=cmd[5:var]
                if cmd.lower()=="sing a song":
                    a1.say("I don't think i sing well, sorry Sir.")
                    a1.runAndWait()
                    cmd=""
                elif cmd.lower()=="open google":
                    a1.say("Sure Sir, opening GOOGLE")
                    a1.runAndWait()
                    webbrowser.open("https://www.google.com")
                    cmd=""
                elif cmd.lower()=="open youtube":
                    a1.say("Sure Sir, opening youtube")
                    a1.runAndWait()
                    webbrowser.open("https://www.youtube.com")
                    cmd=""
                elif cmd.lower()=="open instagram":
                    a1.say("Sure Sir, opening insta")
                    a1.runAndWait()
                    webbrowser.open("https://www.instagram.com")
                    cmd=""
                elif cmd.lower()=="open whatsapp":
                    a1.say("Sure sir opening WhatsApp")
                    a1.runAndWait()
                    subprocess.run(["start", "whatsapp.exe"], shell=True)
                    cmd=""
                elif cmd.lower()=="what's the time":
                    a1.say(str(datetime.datetime.now().strftime("%H:%M:%S")))
                    a1.runAndWait()
                    cmd=""
                elif cmd2.endswith('on youtube'):
                    task = cmd[5:-10].strip()  # Extract the task from the command
                    play_on_youtube(task)
                    a1.say("Sure Sir, playing"+task+"on youtube")
                    a1.runAndWait()
                    cmd=""
                elif cmd.lower()=="exit":
                    a1.say("Sure Sir, Shutting down servers and databases. Enjoy your time Sir. JARVIS SIGNING OFF.")
                    a1.runAndWait()
                    exit()
                else:
                    a1.say("Sorry boss I am currently not capable of doing that, please upgrade me.")
                    a1.runAndWait()
                    cmd=""
            except Exception as e:
                print("Error: " + str(e))
        
else:
    a4.say("Hello Guest, I am JARVIS, a virtual artificial assistant and i here to assist you with a variety of tasks as best as i can. Importing all preferences from home interface, system is now operational")
    a4.runAndWait()
    while p==0:
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(mic)
            print("Please say something....")
            audio2=r.listen(mic)
            try:
                cmd2 = r.recognize_google(audio2)
                if cmd2.lower()=="sing a song":
                    a1.say("I don't think i sing well, sorry Sir.")
                    a1.runAndWait()
                    cmd=""
                elif cmd2.lower()=="open google":
                    a4.say("Sure, opening GOOGLE")
                    a4.runAndWait()
                    webbrowser.open("https://www.google.com")
                    cmd=""
                elif cmd2.lower()=="open youtube":
                    a4.say("Sure, opening youtube")
                    a4.runAndWait()
                    webbrowser.open("https://www.youtube.com")
                    cmd=""
                elif cmd2.lower()=="open insta":
                    a4.say("Sure, opening insta")
                    a4.runAndWait()
                    webbrowser.open("https://www.instagram.com")
                    cmd=""
                elif cmd2.lower()=="exit":
                    a4.say("JARVIS HERE, SIGNING OFF. SEE YA LATER")
                    a4.runAndWait()
                    exit()
                else:
                    a4.say("Sorry I am currently not capable of doing so, my boss needs to upgrade me.")
                    a4.runAndWait()
                    cmd=""
            except Exception as e:
                print("Error: " + str(e))
