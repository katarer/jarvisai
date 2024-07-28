
import sys
import pywhatkit as kit
import smtplib
import os
import webbrowser
import wikipedia
from requests import get
import cv2
import pyttsx3
# import openai
import speech_recognition as sr
import datetime
import pyautogui
from plyer import notification
from pygame import mixer
import speedtest

for i in range(3):

    a = input("Enter Password to open Jarvis :- ")

    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! YOU CAN ACCESS JARVIS NOW")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

from INTRO import play_gif
play_gif
#paste this just below the password function


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)



def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print('listening....')
#         r.pause_threshold = 1
#         audio = r.listen(source,timeout=1, phrase_time_limit=5)
#
#     try:
#         print('recognizing....')
#         query = r.recognize_google(audio,language='en-in')
#         print(f"user said: {query}")
#
#     except Exception as e:
#         speak("say that agai please ")
#         return "none"
#     return query
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>=12 and hour<=18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("hello mam I am jarvis how can i help you?")
def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rkatare247@gmail.com','rmoa ruxf nzud oknl')
    server.sendmail('rkatare247@gmail.com',to,content)
    server.close()
if __name__ == '__main__':
 #speak("this is advanced jarvis")
  wish()
  #int(x)=1
while True:
  if 1:
        speak("enter the instruction")
        query=input()

        if "open notepad" in query:
          npath="C:\\Windows\\System32\\notepad.exe"
          os.startfile(npath)


        elif "open command prompt" in query:
          npath = "C:\\Windows\\System32\\cmd.exe"
          os.startfile(npath)

        elif "open vs code" in query:
            npath = "C:\\Users\\MSkoh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(npath)

        elif "open youtube" in query:
            npath = "C:\\Users\\MSkoh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\YouTube.lnk"
            os.startfile(npath)


        elif "open ms world" in query:
          npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
          os.startfile(npath)

        elif "open firefox" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Firefox.lnk"
            os.startfile(npath)

        # elif "translate" in query:
        #     from Translator import translategl
        #
        #     query = query.replace("jarvis", "")
        #     query = query.replace("translate", "")
        #     translategl(query)

        elif "schedule my day" in query:
            tasks = []  # Empty list
            speak("Do you want to clear old tasks (Plz speak YES or NO)")
            query = input("")
            if "yes" in query:
                file = open("tasks.txt", "w")
                file.write(f"")
                file.close()
                no_tasks = int(input("Enter the no. of tasks :- "))
                i = 0
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt", "a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()

            elif "play a game" in query:
                from game import game_play
                game_play()

            elif "no" in query:
                i = 0
                no_tasks = int(input("Enter the no. of tasks :- "))
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt", "a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
        elif "show my schedule" in query:
            file = open("tasks.txt", "r")
            content = file.read()
            file.close()
            mixer.init()
            mixer.music.load("notification.mp3")
            mixer.music.play()
            notification.notify(
                title="My schedule :-",
                message=content,
                timeout=15
            )

        elif "open firefox" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Firefox.lnk"
            os.startfile(npath)

        elif "internet speed" in query:
            wifi = speedtest.Speedtest()
            upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
            download_net = wifi.download() / 1048576

            speak(f"Wifi download speed is {download_net}")
            speak(f"Wifi Upload speed is {upload_net}")

        # elif "ipl score" in query:
        #     from plyer import notification  # pip install plyer
        #     import requests  # pip install requests
        #     from bs4 import BeautifulSoup  # pip install bs4
        #
        #     url = "https://www.cricbuzz.com/"
        #     page = requests.get(url)
        #     soup = BeautifulSoup(page.text, "html.parser")
        #     team1 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
        #     team2 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
        #     team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
        #     team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()
        #
        #     a = print(f"{team1} : {team1_score}")
        #     b = print(f"{team2} : {team2_score}")
        #
        #     notification.notify(
        #         title="IPL SCORE :- ",
        #         message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
        #         timeout=15
        #     )

        elif "ipl score" in query:
            import requests
            from bs4 import BeautifulSoup

            url = "https://www.cricbuzz.com/"
            page = requests.get(url)
            soup = BeautifulSoup(page.text, features="html.parser")

            team_elements = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")

            if team_elements:
                team1 = team_elements[0].get_text()
                team2 = team_elements[1].get_text()
                team1_score = team_elements[8].get_text()
                team2_score = team_elements[10].get_text()
            else:
                team1 = "Team 1 not found"
                team2 = "Team 2 not found"
                team1_score = "Score not available"
                team2_score = "Score not available"

            a = print(f"{team1} - {team1_score}")
            b = print(f"{team2} - {team2_score}")

            # You can use 'a' and 'b' to print the scores or perform any other actions



        # You can use 'a' and 'b' to print the scores or perform any other actions

        elif "open camera" in query:
            cap= cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                  break
            cap.release()
            cv2.destroyAllWindows()

        elif "set an alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done,sir")

        elif "ip address" in query:
             ip=get('https://api.ipify.org').text
             speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("what would you like to search")
            search=input("")

            speak("searching wikipedia")

            query=query.replace("wikipedia",search)
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
        elif "get weather update" in query:
            webbrowser.open("http://localhost:3001/")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        # elif "pause" in query:
        #     pyautogui.press("k")
        #     speak("video paused")
        # elif "play" in query:
        #     pyautogui.press("k")
        #     speak("video played")
        # elif "mute" in query:
        #     pyautogui.press("m")
        #     speak("video muted")
        #
        # elif "volume up" in query:
        #     from keyboard import volumeup
        #
        #     speak("Turning volume up,sir")
        #     volumeup()
        # elif "volume down" in query:
        #     from keyboard import volumedown
        #
        #     speak("Turning volume down, sir")
        #     volumedown()


        elif "search on google" in query:

            speak("sir what should I search on Google?")

            search_query = input().lower()

            search_url = "https://www.google.com/search?q=" + "+".join(search_query.split())

            webbrowser.open(search_url)
        elif "send message" in query:
            kit.sendwhatmsg("+919579950402","this is advance jarvis",12,30, 5)

        elif "play song on youtube" in query:
            speak("which song should I play")
            song=input()
            kit.playonyt(song)

        elif "remember that" in query:
            rememberMessage = query.replace("remember that", "")
            rememberMessage = query.replace("jarvis", "")
            speak("You told me to remember that" + rememberMessage)
            remember = open("Remember.txt", "a")
            remember.write(rememberMessage)
            remember.close()
        elif "what do you remember" in query:
            remember = open("Remember.txt", "r")
            speak("You told me to remember that" + remember.read())

        elif "get news" in query:
            from NewsRead import latestnews

            latestnews()
        elif "shutdown the system" in query:
            speak("Are You sure you want to shutdown")
            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")

            elif shutdown == "no":
                break
        elif "send email" in query:
           # try:
                speak("what email should i send")
                #speak()
                content=input()
                speak("enter email id of receiver")
                to=input()
               # to="nikkhilpawar@gmail.com"
                sendemail(to,content)
                speak("email has been sent")



        elif "no thanks" in query:
            sys.exit()

        speak("do you have any work")
        query=input()


