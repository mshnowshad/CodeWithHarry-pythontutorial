print()


import pyttsx3
import speech_recognition as sr
import datetime


  
  
  
engine = pyttsx3.init('sapi5')  #> মাইক্রোসফ্ট স্পিচ API (SAPI5) হল মাইক্রোসফ্ট দ্বারা প্রদত্ত ভয়েস স্বীকৃতি এবং সংশ্লেষণের প্রযুক্তি।
voices = engine.getProperty('voices')    

# print(voices[0].id)

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    # pass

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12 :
        speak('Good Morning !')

    elif hour >= 12 and hour < 18:
        speak("Good after noon")
    else:
        speak("Good Evening!")
    
    speak("I am Yourfirst jarvis sir , Please tell me how may i  help you?")






def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    # speak("Nowshad is python beginner")
    wishme() 
    takeCommand()
    












print()






# import pyttsx3 #pip install pyttsx3##> pyttsx3: পাঠ্য থেকে বক্তৃতা (Text-to-Speech) এর জন্য।
# import speech_recognition as sr #pip install speechRecognition    #> ভয়েস শনাক্তকরণের জন্য।
# import datetime   #>  সময়ের সাথে সম্পর্কিত কার্যকলাপের জন্য।
# import wikipedia #pip install wikipedia   #>  উইকিপিডিয়া থেকে তথ্য সংগ্রহের জন্য।
# import webbrowser    #> ওয়েব ব্রাউজার খোলার জন্য।
# import os    #> : অপারেটিং সিস্টেমের সাথে মিথস্ক্রিয়ার জন্য।
# import smtplib   #> ইমেইল পাঠানোর জন্য।
  


# engine = pyttsx3.init('sapi5')  
# voices = engine.getProperty('voices')
# # print(voices[1].id)
# engine.setProperty('voice', voices[0].id)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# speak("Hello IRONMAN how are you?")
# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("Good Morning!")

#     elif hour>=12 and hour<18:
#         speak("Good Afternoon!")   

#     else:
#         speak("Good Evening!")  

#     speak("I am Jarvis Sir. Please tell me how may I help you")       

# def takeCommand():
#     #It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")

#     except Exception as e:
#         # print(e)    
#         print("Say that again please...")  
#         return "None"
#     return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()

# if __name__ == "__main__":
#     wishMe()
#     while True:
#     # if 1:
#         query = takeCommand().lower()

#         # Logic for executing tasks based on query
#         if 'wikipedia' in query:
#             speak('Searching Wikipedia...')
#             query = query.replace("wikipedia", "")
#             results = wikipedia.summary(query, sentences=2)
#             speak("According to Wikipedia")
#             print(results)
#             speak(results)

#         elif 'open youtube' in query:
#             webbrowser.open("youtube.com")

#         elif 'open google' in query:
#             webbrowser.open("google.com")

#         elif 'open stackoverflow' in query:
#             webbrowser.open("stackoverflow.com")   


#         elif 'play music' in query:
#             webbrowser.open('open.spotify.com/')
#             # music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
#             # songs = os.listdir(music_dir)
#             # print(songs)    
#             # os.startfile(os.path.join(music_dir, songs[0]))

#         elif 'the time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")    
#             speak(f"Sir, the time is {strTime}")

#         elif 'open code' in query:
#             codePath = "F:\Python Folder\CodeWithHarry\project\jarvis.py"
#             os.startfile(codePath)

#         elif 'email to harry' in query:
#             try:
#                 speak("What should I say?")
#                 content = takeCommand()
#                 to = "harryyourEmail@gmail.com"    
#                 sendEmail(to, content)
#                 speak("Email has been sent!")
#             except Exception as e:
#                 print(e)
#                 speak("Sorry my friend harry bhai. I am not able to send this email")    





































