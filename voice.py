import pyttsx3
import speech_recognition as sr
import datetime
from datetime import date
import wikipedia
import webbrowser
import os
import requests
import json
import smtplib

# initializing the engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    '''introduction of the assistant and welcom note'''
    hour = int(datetime.datetime.now().hour)
    today = date.today()
    d = today.strftime("%B %d, %y")
    if hour >= 0 and hour < 12:
        speak(f"Good Morning sir, today is {d}")

    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon sir, today is {d}")

    elif hour >=18 and hour <22:
        speak(f"Good Evening sir, today is {d}")

    else:
        speak(f"Good night sir, you should sleep by now")

    speak("Hello i am MENDES, assistant of DIPESH, how can I help you.. ")


def takeCommand():
    '''it takes microphone input and returns a string variable'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # it will be printing while we input voice
        print("Listening....")
        # input process finish is 1 sec(if we stop speaking)
        r.pause_threshold = 1
        # it will store the voice input and process it
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"Human: {query}\n")

        except Exception as e:
            print("Say something bitch...")
            return "None"
        return query

def sendEmail(to, content):
    server = smtplib.server('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pauldipesh29@gmail.com', 'galahad@12345')
    server.sendmail('pauldipesh29@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    # speak("Dipesh is a pro coder")
    wishme()  

    while (True):

        # storing the command and converting it into lower case
        x = takeCommand().lower()

        if 'meaning' in x:
            speak('searching wikipedia...')
            x = x.replace("wikipedia", "")
            result = wikipedia.summary(x, sentences=1)
            print(result)
            speak(result)

        # for browsing google
        if 'browse' in x:
            x = x.replace('open', "")
            webbrowser.open(f"{x}.com")
            speak(f"Opening {x}")

        # if 'open stack overflow' in x:
        #     webbrowser.open('stackoverflow.com')

        if 'the time' in x:
            str_time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"Sir, it's {str_time}")

        if 'open code' in x:
            loc = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(loc)
            speak("Opening Code sir")

        if 'open android studio' in x:
            loc = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(loc)
            speak("Opening Android Studio sir")

        if 'weather' in x:
            api_key = "8fbfa2d67084e6d48139133219c4dadb"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"

            speak("Which state's weather do you want to know sir")
            city_name = takeCommand()
            
            # complete_url variable to store
            # complete url address
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            # get method of requests module
            # return response object
            response = requests.get(complete_url)
            y = response.json

            if y["cod"] != "404":
                z = y["main"]
                current_temperature = z["temp"]
                current_pressure = z["pressure"]

                current_humidiy = z["humidity"]

                a = y["weather"]
                weather_description = a[0]["description"]

                print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description))
            elif  'send email' in x:
                try:
                    speak('what should i say?')
                    content = takeCommand()
                    to = "pauldipesh29@gmail.com"
                    sendEmail(to, content)
                    speak('Email has been sent!')

                except Exception as e:
                    print(e)
                    speak("Sorry sir, i am not able to send the email")

                pass 

            else:
                print(" City Not Found ")

        if 'exit' or 'quit' in x:
            break