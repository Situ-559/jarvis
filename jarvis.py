import pyttsx3
import speech_Recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getproperty('voices')
print(voices[0].id)
engines.setproperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
        speak("I am Jarvis sir. please tell me how may I help you")
def takeCommand():
     #it takes Microphone input from user and returns String Output 
    r=sr.Recognizer()
    with sr.Microphone() as source:     
    print("Listening...")              
          
    r.pause_threshold=1
    audio=r.listen(source)
      
     try:
         print("Recognizing...")
         query=r.Recognize_google(audio,Language='en-in')
         print(f"User said: {query}\n")
     except Exception as e:
         # print(e)
         print("Say that again please...")
         return "None"
     return "query"
     def sendEmail(to,content):
         server=smtplib.SMTP('smtp.gmail.com',587)
         server.ehlo()
         server.starttls()
         server.login('youremail@gmail.com','your-password')
         server.sendmail('youremail@gmail.com',to,content)
     if __name__ == "__main__":
         wishMe()
         if 1:
         query=takeCommand().lower()
         
         
         if 'wikipedia' in query
         # Logic for executing tasks based on query
             speak= ("searching wikipedia...")
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query,sentences*2)
             print(results)
             speak(results)
             
     elif 'open youtube' in query:
         webbrowser.open("youtube.com")
         
     elif 'open google' in query:
         webbrowser.open("google.com")
      elif 'open stackoverflow' in query:
         webbrowser.open("stackoverflow.com")
         
     elif 'playmusic' in query:
         music_dir="D:\\Non Critical\\songs\\favorite songs2"
         songs=os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir,songs[0]))
         
     elif 'the time' in query:
         strTime=dateTime.dateTime.now().strTime("%H:%M:%S")
         speak(f"sir,the time is,{strTime}")
         
     elif 'open code' in query:
         codepath="c:\\Users\\Sourav\\AppData\\Local\\Program\\Microsoft vs code\\code.exe"
         os.startfile(codepath)
         
     elif 'email to Sourav' in query:
                 
       try:
           speak("why should I say")
           content=techCommand()
           to="YourEmail@gmail.com"
           SendEmail(to,content)
           speak("Email has been Sent")
       except Exception as e:
           print(e)
       speak("I am not able to send this email")        
               
             
         
             
             
                         
         
                         
            

            




if __name__ == "__main__":
  speak("harry is a good boy")
