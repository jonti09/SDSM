#!/usr/bin/env python3
import speech_recognition as sr
import re
import selenium.webdriver as webdriver
import time
from selenium.common.exceptions import WebDriverException

r = sr.Recognizer()
try:
    fp = webdriver.FirefoxProfile('/home/viper/.mozilla/firefox/mwad0hks.default')
    b = webdriver.Firefox(fp)
    b.maximize_window()
    b.get('http://localhost/')
except WebDriverException:
    pass


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

        if re.findall(r'map of \w+', cmd):
            city = cmd.split(' ')[-1]
            b.get('http://localhost/map/?city=' + city)

    except sr.UnknownValueError:
        print("Couldn't catch that")

    except sr.RequestError as e:
        print("Can not request recognition at the moment")


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

print("Say something!")
audio = r.listen_in_background(source, callback)

while True:
    time.sleep(0.05)
