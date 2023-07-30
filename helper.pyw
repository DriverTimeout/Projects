import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import time
import threading
import pyautogui
import torch
import subprocess
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')                     
engine.setProperty('rate', 160)     
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
        if 'bucky' in command:
            talk('Yes Sir')
            command = command.replace('bucky', '')
            print(command)
    except:
        pass
    return command


def run_bucky():
    event = threading.Event()
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        event.wait(3)
        talk("I'm listening again")

    elif 'write a note saying' in command:
        mar = command.replace('write a note', '')
        talk('writing '+ mar)
        file = open('note.txt', 'a')
        strTime = datetime.datetime.now().strftime('At %I:%M %p')
        file.write(strTime)
        file.write(' - ')
        file.write(mar+'\n')

    elif 'show note' in command:
        talk('showing notes')
        file = open('note.txt', 'r')
        print(file.readlines)
        talk(file.readlines(500))

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)
        event.wait(3)
        talk("I'm listening again")

    elif 'tell me' in command:
        look_for = command.replace('tell me', '')
        talk('telling you' + look_for)
        toughstuff = pywhatkit.search(look_for)
        event.wait(3)
        talk("I'm listening again")

    elif 'show me' in command:
        monster = command.replace('show me', '')
        talk('showing you' + monster)
        ghstuff = pywhatkit.search(monster)
        event.wait(3)
        talk("I'm listening again")

    elif 'explain to me' in command:
        guter = command.replace('explain to me', '')
        talk('Explaining to you' + guter)
        oughstuff = pywhatkit.search(guter)
        event.wait(3)
        talk("I'm listening again")
        
    elif 'scroll' in command:
        jsfk = command.replace('scroll', '')
        pyautogui.moveTo(230,300,2)
        pyautogui.click
        talk('scrolling')
        pyautogui.scroll(-500)

    elif 'figure out' in command:
        mercy = command.replace('figure out', '')
        talk('figuring out' + mercy)
        toustuff = pywhatkit.search(mercy)
        event.wait(3)
        talk("I'm listening again")

    elif 'connect to raspberry' in command:
        maga = command.replace('connect to raspberry', '')
        os.system("start cmd /k ssh losts@superman")
        pyautogui.moveTo(1490,820,2)
        pyautogui.click
        pyautogui.typewrite('thedog', interval=0.1)
        pyautogui.press('enter')
        event.wait(3)
        pyautogui.typewrite('clear', interval=0.1)
        pyautogui.press('enter')

    elif 'hold on' in command:
        meas = command.replace('hold on', '')
        print(meas)
        talk('Waiting four seconds')
        event.wait(4)
        talk("I'm listening again")
    
    elif 'give me a second' in command:
        talk("waiting for 3 seconds")
        event.wait(3)
        talk("I'm listening again")

    elif 'shut down' in command:
        closing = command.replace('shut down', '')
        print(closing)
        talk('Goodbye Sir')
        quit()

    else:
        talk('I did not get that, I will start to listen in 3 seconds')
        event.wait(3)
        talk("I'm listening again")

while True:
    run_bucky()
    