import pyttsx3
import datetime
import speech_recognition as sd
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Moring")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello  Saurabh Sir I am Jarvis,Please tell me how I can Help you")

def takeCommand():
    s = sd.Recognizer()
    with sd.Microphone(device_index=0) as source :
        print("Listening...")
        s.pause_threshold = 1
        audio = s.listen(source)
    
    try:
        print("Recognizing...")
        query = s.recognize_google(audio)
        print("User said: " , query)
    
    except Exception as e :
        #print(e)
        print("Say that again please..")
        return "None"
    return query

def sendEmail(do,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Saurabh@gmail.com','Password')
    server.sendEmail('S@gmail.com', to,content)
    server.close()

if __name__ =="__main__" :
       wishMe()
       if 2:
       #while True :
           query = takeCommand().lower()

           if 'wikipedia' in query:
               speak('Searching Wikipedia..')
               query = query.replace("wikipedia", "")
               results = wikipedia.summary(query,sentences =1)
               speak("According to wikipedia ")
              # print(results)
               speak(results)

           elif 'Hello Jarvis' in query:
                speak("Hello Saurabh sir I am Jarvis, Your assistant")
            
           elif 'open youtube'in query:
               webbrowser.open("youtube.com")

           elif 'open google' in query:
               webbrowser.open("google.com ")
            
           elif 'the time' in query:
               strtime = datetime.datetime.now().strftime("%H:%M:%S")
               speak(f"Sir the is {strtime}")

           elif 'open code' in query:
               codePath = "D:\\Programming Code\\Jarvas_speck\\main.py"
               os.startfile(codePath)

            

           elif 'email to Saurabh' in query:
               try:
                   speak("What should I say?")
                   content = takeCommand()
                   to = "Saurabh.com"
                   sendEmail(to,content)
                   speak("Email has been sent!") 
               except Exception as e:
                    print(e)
                    speak("Sorry my friend Saurabh, I am not able to send Email")

           elif  "exit" in query:
                  quit()
            

                
            
         