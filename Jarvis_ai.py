import os
from bs4 import BeautifulSoup
import webbrowser
import pyttsx3
import datetime
import random
import speech_recognition as sr
import wikipedia
import pywhatkit
import pyautogui
import time
import pyjokes
import smtplib
import requests
import PyPDF2
from tkinter.filedialog import *
import pyfiglet
from sketchpy import library as obj
import cv2


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Makes jarvis to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Find IP address
def ip_address():
    ip = requests.get("https://api.ipify.org").text
    speak(f"Your IP address is {ip}")

# Sketch art converter
def sketch_art():
    image = cv2.imread("jarivspic.jpeg")
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(gray_img)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    invertedBlur = cv2.bitwise_not(blur)
    sketch = cv2.divide(gray_img, invertedBlur, scale=256.0)

    cv2.imwrite("jarvisart.png", sketch)

# screenshot taking
def screen_shot():
    speak("ok buddy, what should i name that file")
    path = takeCommand()
    path1name = path + "screenshot.png"
    path1 = "C:\\Users\\Durgadevi\\Pictures\\Saved Pictures" + path1name
    dd = pyautogui.screenshot()
    dd.save(path1)
    os.startfile("C:\\Users\\Durgadevi\\Pictures\\Saved Pictures")
    speak("here is your screenshot Mam")

# Set alarm
def set_alarm():
    from playsound import playsound
    alarm_hour = int(input("Enter hour: "))
    alarm_min = int(input("Enter minutes :"))
    alarm_am = input("am / pm: ")

    if alarm_am == "pm":
        alarm_hour += 12

    while True:
        if alarm_hour == datetime.datetime.now().hour and alarm_min == datetime.datetime.now().minute:
            print("Playing.........")
            playsound("jarvisalarm.mp3.wav")
            break

# Pdf file reading
def pdf_read():
    book = askopenfilename()
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages

    for num in range(0, pages):
        page = pdfreader.getPage(num)
        text = page.extractText()
        player = pyttsx3.init()
        player.say(text)
        player.runAndWait()

# Temperature checking
def Temp():
    place = input("Enter the name of place: ")
    search = f"Weather in {place}"
    url = f"https://www.google.com/search?&q={search}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    update = soup.find("div", class_="BNeawe").text
    print(f"{search} now is {update}")

# Spiral drawing using pyautogui
def automate_draw():
    time.sleep(3)
    distance = 300
    while distance > 0:
        pyautogui.dragRel(distance, 0, 1, button="left")
        distance = distance - 20
        pyautogui.dragRel(0, distance, 1, button="left")
        pyautogui.dragRel(-distance, 0, 1, button="left")
        distance = distance - 20
        pyautogui.dragRel(0, -distance, 1, button="left")
        time.sleep(2)

# Send whatsapp message
def what_msg():
    speak("Enter the number")
    no = input("Enter the number:")
    speak("Tell me the message")
    msg = takeCommand()
    speak("Please specify the time")
    hour = int(input("Enter the hour"))
    minu = int(input("Enter the minutes"))
    pywhatkit.sendwhatmsg(no, msg, hour, minu)

# Wishing the user
def wishMe():
  hour = int(datetime.datetime.now().hour)

  if hour>=0 and hour<12:
      speak("Good morning sir")

  elif hour>=12 and hour<18:
      speak("good afternoon sir")

  else:
      speak("Good evening sir")

  b = "How may i help you sir", "Give me a command sir", "Online and ready sir"
  speak("I am jarvis"+random.choice(b))

# Send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('durgadevid2003@gmail.com', 'vgqczcoavjnydowk')
    server.sendmail('durgadevid2003@gmail.com', to, content)
    server.close()

# Speech Recognizer
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("wait for few moments ")
        query = r.recognize_google(audio, language='en-in')
        print("user said", query)
    except Exception as e:
        print(e)
        print("say that again please")
        return "None"
    return query

if __name__== "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("searching in wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'play' in query:
            playQuery = query.replace('play', '')
            speak("playing " + playQuery)
            pywhatkit.playonyt(playQuery)

        elif 'open youtube' in query:
            speak("Yes dude opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("yeah buddy sure")
            webbrowser.open("google.com")
            while True:
                chromeQuery = takeCommand().lower()
                if "search" in chromeQuery:
                    youtubeQuery = chromeQuery
                    youtubeQuery = youtubeQuery.replace("search", "")
                    pyautogui.write(youtubeQuery)
                    pyautogui.press('enter')
                    speak('Searching buddy.....')
                elif 'open new tab' in query:
                    pyautogui.hotkey('ctrl', 't')
                elif "close chrome" in chromeQuery or "exit" in chromeQuery or "stop" in chromeQuery:
                    pyautogui.hotkey('ctrl', 'w')
                    speak("closing google chrome buddy..")
                    break

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open chatgpt' in query:
            webbrowser.open("chat.openai.com")

        elif 'open code' in query:
            speak("Opening note pad")
            codePath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            speak("Opening chrome buddy")
            codePath1 = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath1)

        elif 'open android studio' in query:
            speak("Opening android app")
            codePath2 = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
            os.startfile(codePath2)

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(time)
            print(time)

        elif 'type' in query:
            speak("please tell me what should i write")
            while True:
                typeQuery = takeCommand()
                if typeQuery == "exit typing":
                    speak("done boss")
                    break
                else:
                    pyautogui.write(typeQuery)

        elif 'close' in query:
            speak('Closing mam')
            pyautogui.hotkey('ctrl', 'w')

        elif 'minimize' in query or 'minimise' in query:
            speak('Minimizing mam')
            pyautogui.hotkey('win', 'down', 'down')

        elif 'maximize' in query:
            speak('Maximizing mam')
            pyautogui.hotkey('win', 'up', 'up')

        elif 'screenshot' in query:
            screen_shot()

        elif "open paint" in query:
            speak("Opening paint application")
            os.startfile('%windir%\\system32\\mspaint.exe')

        elif 'joke' in query:
            jarvisJoke = pyjokes.get_joke()
            print(jarvisJoke)
            speak(jarvisJoke)

        elif "ip address" in query:
            ip_address()

        elif "draw spiral" in query:
            automate_draw()

        elif "chat" in query:
            what_msg()

        elif 'send email' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'harieshk561@gmail.com'
                sendEmail(to, content)
                speak('Email has been sent!')
            except Exception as e:
                speak(e)
                speak('Sorry mam, Not able to send email at the moment')

        elif 'read pdf' in query:
            pdf_read()

        elif 'set alarm' in query:
            set_alarm()

        elif 'make fun text' in query:
            text = input('Enter a word : ')
            k = pyfiglet.figlet_format(text)
            print(k)

        elif 'translate' in query:
            webbrowser.open("translate.google.com")

        elif 'dictionary' in query:
            webbrowser.open("dictionary.com")

        elif 'temperature' in query:
            Temp()

        elif 'draw iron man' in query:
            durga = obj.rdj()
            durga.draw()

        elif 'writing' in query:
            text = input("Write text : ")
            pywhatkit.text_to_handwriting(text, save_to="art23.jpg", rgb=[0, 0, 0])

        elif 'sketch art' in query:
            sketch_art()