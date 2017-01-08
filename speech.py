#!/usr/bin/env python3
import speech_recognition as sr
import re
import time
import selenium.webdriver as webdriver
import pyautogui
from datetime import datetime
import os

r = sr.Recognizer()

b = webdriver.Firefox()
b.maximize_window()
b.get('http://localhost/')
pyautogui.press('enter')
pyautogui.press('f11')

video_no = {
    'first': 1,
    'second': 2,
    'third': 3,
    'fourth': 4,
    'fifth': 5,
    'sixth': 6,
    'seventh': 7,
    'eighth': 8,
    'ninth': 9,
    'tenth': 10,
}


def callback(recognizer, audio):
    try:
        cmd = r.recognize(audio)
        print("You said " + cmd)

        if re.findall(r'news|notification', cmd):
            b.get('http://localhost/news')

        if re.findall(r'help|what can i say', cmd):
            b.get('http://localhost/help')

        if re.findall(r'sleep', cmd):
            b.get('http://localhost/sleep')

        if re.findall(r'go home|gohome|wake up', cmd):
            b.get('http://localhost/')

        if re.findall(r'yesterday|previous day', cmd):
            b.get('http://localhost/yesterday')

        if re.findall(r'screenshot|screen shot', cmd):
            sc = pyautogui.screenshot()
            if not os.path.exists('Media'):
                os.mkdir('Media')
            os.chdir('Media')
            sc.save('screenshot_' + str(datetime.now()) + '.png')
            os.chdir('..')

        if re.findall(r'map of \w+', cmd):
            city = cmd.split(' ')[-1]
            b.get('http://localhost/map/?city=' + city)

        if re.findall(r'trending|trendings', cmd):
            b.get('http://localhost/youtube/trending')

        if re.search(r'\w+ video', cmd):
            no = video_no[cmd.split(' ')[-2]]
            if no > 0:
                b.get('http://localhost/youtube/' + str(no))

    except sr.UnknownValueError:
        print("Couldn't catch that")

    except sr.RequestError as e:
        print("Can not request recognition at the moment")


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

print("Say something!!! ")
audio = r.listen_in_background(source, callback)

while True:
    try:
        time.sleep(0.5)
    except KeyboardInterrupt:
        exit(0)
