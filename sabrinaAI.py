import pyttsx3
import datetime
import speech_recognition 
import wikipedia
import webbrowser as wb
import os
import psutil
import pyjokes
import subprocess


engine = pyttsx3.init('sapi5')
#engine.say("This is rita")
#engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)



def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent )

def jokes():
    speak(pyjokes.get_joke())


def wish_me():
    speak("Welcome back sir!, This is your personal AI assistant , sabrina")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good morning sir!")
    elif hour >= 12 and hour<18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour<24:
        speak("Good Evening sir!")
    #else:
    #    speak("Good night sir!")
    cpu()
    speak("sabrina at your service. please tell me how can i help you sir!?")



def take_command():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"[Me]: {query}")

    except Exception as e:
        #print(e)
        speak("Say that again please...")
        return "None"
    return query 
def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("abzc@gmail.com","123")
    server.sendmail("abzc@gmail.com", to, content)
    server.close()

if __name__ == '__main__':
    wish_me()
    # cpu()
    while True:
        query = take_command().lower()

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "wikipedia" in query:
            speak("searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences= 2)
            print(result)
            speak(result)

        elif "weather" in query:
            speak("today's wheather is ",+weather)

        elif "send email" in query:
            try:
                speak("what should I say?")
                content =  take_command()
                to = "Xyz@gmail.com"
                #send_email(to, content)
                speak(content)
            except Exception as e:
                print (e)
                speak("unable to send the email")

        elif "search in chrome" in query:
            speak("What should i search?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = take_command().lower()
            wb.get(chromepath).open_new_tab(search+".com")

        elif "logout" in query:
            os.system("shutdown -1")
        
        elif "shutdown" in query:
            os.system("shutdown /s /t -1")

        elif "file" in query:
            speak("which file you want me to open sir?")
            file= take_command()
            speak("you want me to open file")


        elif "restart" in query:
            os.system("shutdown /r /t -1")
        
        elif 'how are you' in query:
            speak('I am doing good, sir.')

        elif query == 'stop':
            speak('Bye Sir, Have a good Day')
            quit()

        elif "open word" in query:
            os.system("Winword.exe")

        elif "open powerpoint" in query:
            os.system("POWERPNT.EXE")

        elif "open EXCEL" in query:
            os.system("EXCEL.EXE")

        elif "open notepad" in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

        elif "remember that" in query:
            speak("What should i remember sir?")
            data = take_command()
            speak("you said me to remember that "+data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "do you remember anything" in query:
            remember = open("data.txt","r")
            speak("you said me to remember that" +remember.read())
        
        elif "cpu" in query:
            cpu()
        
        elif "joke" in query:
            jokes()

        elif "offline" in query:
            quit()
            



