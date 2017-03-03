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

to_no = {
	'first': 1, 'I': 1, 'i': 1,
	'second': 2, 'II': 2, 'ii': 2,
	'third': 3, 'III': 3, 'iii': 3,
	'fourth': 4, 'IV': 4, 'iv': 4,
	'fifth': 5, 'V': 5, 'v': 5, 
	'sixth': 6, 'VI': 6, 'vi': 6, 
	'seventh': 7, 'VII': 7, 'vii': 7, 
	'eighth': 8, 'VIII': 8, 'viii': 8, 
	'ninth': 9, 'IX': 9, 'ix': 9, 
	'tenth': 10, 'X': 10, 'x': 10, 
}

def dir(name):
	if not os.path.exists('Media'):
		os.mkdir('Media')
		os.chdir('Media')
	if not os.path.exists(name):
		os.mkdir(name)
		os.chdir(name)
	else:
		os.chdir(name)


def callback(recognizer, audio):
	try:
		cmd = r.recognize_google(audio)
		print("You said " + cmd)

		if re.search(r'news|notification', cmd):
			b.get('http://localhost/news')

		if re.search(r'help|what can i say', cmd):
			b.get('http://localhost/help')

		if re.search(r'sleep', cmd):
			b.get('http://localhost/sleep')

		if re.search(r'go home|gohome|wake up', cmd):
			b.get('http://localhost/')

		if re.search(r'yesterday|previous day', cmd):
			b.get('http://localhost/yesterday')

		if re.search(r'screenshot|screen shot', cmd):
			sc = pyautogui.screenshot()
			dir(screen_shots)
			sc.save('screenshot_' + str(datetime.now()) + '.png')
			os.chdir('..')

		# show me the map of `city`; this `city` is passed as GET param
		if re.search(r'map of \w+', cmd):
			city = cmd.split(' ')[-1]
			b.get('http://localhost/map/?city=' + city)

		if re.search(r'trending|trendings', cmd):
			b.get('http://localhost/youtube/trending')

		# play the `number` video; this `number` is passed as url
		if re.search(r'\w+ video', cmd):
			try:
				no = to_no[cmd.split(' ')[-2]]
			except:
				pass

			if no > 0:
				b.get('http://localhost/youtube/' + str(no))

		# play the music or play the songs; play the `number` song
		if re.search(r'\w+ song', cmd):
			action = cmd.split(' ')[0]
			tmp = cmd.split(' ')[2]
			try:
				if tmp == 'next' or tmp == 'previous':
					action = tmp
				else:
					no = to_no[tmp]
			except:
				if no == 'next' or no == 'previous':
					action = no
			print(action, no)
			# b.get('http://localhost/music/?action=' + action + '&no=' + str(no))

	except sr.UnknownValueError:
		print("Couldn't catch that")

	except sr.RequestError as e:
		print(e)


with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)

print("Say something!!! ")
audio = r.listen_in_background(source, callback)

while True:
	try:
		time.sleep(0.5)
	except KeyboardInterrupt:
		exit(0)
