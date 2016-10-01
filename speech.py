#!/usr/bin/env python3
import speech_recognition as sr
import re
import selenium.webdriver as webdriver
import time

r = sr.Recognizer()
b = webdriver.Firefox()


def callback(recognizer, audio):
    try:
        cmd = r.recognize(audio)
        print("You said " + cmd)

        if re.findall(r'notification', cmd):
            b.maximize_window()
            b.get('http://localhost/notification')

        if re.findall(r'sleep', cmd):
            b.maximize_window()
            b.get('http://localhost/notification/sleep')

        if re.findall(r'wake up', cmd):
            b.maximize_window()
            b.get('http://localhost/notification')

        if re.findall(r'yesterday|previous day', cmd):
            print('news..')
            b.get('http://localhost/notification/yesterday')

    except sr.UnknownValueError:
        print("Couldn't catch that")
    except sr.RequestError as e:
        print("Can not request recognition at the moment")
    except:
        print('Browser Error')


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

print("Say something!")
audio = r.listen_in_background(source, callback)

while True:
    time.sleep(0.05)
