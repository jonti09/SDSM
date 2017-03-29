#!/usr/bin/env python3
import speech_recognition as sr
import re
import time
import selenium.webdriver as webdriver
import pyautogui
from datetime import datetime
import os


class Speech:
	r = sr.Recognizer()
	b = webdriver.Firefox()
	PREV = ''
	FLAG = True
	IS_PLAYING = False
	NO = 0
	TO_NO = {
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

	def __init__(self):
		self.b.maximize_window()
		self.b.get('http://localhost:8000/')
		pyautogui.press('enter')
		pyautogui.press('f11')

	def dir(self, name):
		if not os.path.exists('Media'):
			os.mkdir('Media')
			os.chdir('Media')
		if not os.path.exists(name):
			os.mkdir(name)
			os.chdir(name)
		else:
			os.chdir(name)

	def callback(self, recognizer, audio):
		try:
			cmd = self.r.recognize_google(audio)
			print("You said " + cmd)

			if re.search(r'news|notification', cmd):
				self.PREV = 'news'
				self.b.get('http://localhost:8000/news')

			if re.search(r'help|what can i say', cmd):
				self.PREV = 'help'
				self.b.get('http://localhost:8000/help')

			if re.search(r'sleep', cmd):
				if self.PREV is 'music':
					self.b.get('http://localhost:8000/music/?action=stop&no=1')
				self.PREV = 'sleep'
				self.b.get('http://localhost:8000/sleep')

			if re.search(r'wake up|wakeup', cmd):
				if self.PREV is 'sleep':
					self.b.get('http://localhost:8000/')

			if re.search(r'go home|gohome', cmd):
				self.PREV = 'home'
				self.b.get('http://localhost:8000/')

			if re.search(r'yesterday|previous day', cmd):
				self.PREV = 'yesterday_news'
				self.b.get('http://localhost:8000/yesterday')

			if re.search(r'screenshot|screen shot', cmd):
				self.PREV = 'screenshot'
				sc = pyautogui.screenshot()
				self.dir('screen_shots')
				sc.save('screenshot_' + str(datetime.now()) + '.png')
				os.chdir('..')

			# show me the map of `city`; this `city` is passed as GET param
			if re.search(r'map of \w+', cmd):
				self.PREV = 'map'
				city = cmd.split(' ')[-1]
				self.b.get('http://localhost:8000/map/?city=' + city)

			if re.search(r'trending|trendings', cmd):
				self.PREV = 'trending'
				self.b.get('http://localhost:8000/youtube/trending')

			# play the `number` video; this `number` is passed as url
			if re.search(r'\w+ video', cmd):
				if self.PREV == 'trending':
					if self.IS_PLAYING:
						self.b.get('http://localhost:8000/music/?action=stop&no=')
					try:
						no = self.TO_NO[cmd.split(' ')[-2]]
						if no > 0:
							self.b.get('http://localhost:8000/youtube/' + str(no))
					except IndexError:
						pass
					self.PREV = 'trending'

			# play the music or play the songs; play the `number` song
			if re.search(r'\w+ song|\w+ music', cmd):
				if self.PREV == 'music':
					self.b.get('http://localhost:8000/music/?action=stop&num=' + str(self.NO))
				action = cmd.split(' ')[0]
				tmp = cmd.split(' ')[2]
				try:
					self.NO = self.TO_NO[tmp] - 1
				except:
					self.NO = 0 
				if action == 'play':
					self.b.get('http://localhost:8000/music/?action=play&num=' + str(self.NO))
				self.PREV = 'music'
				self.IS_PLAYING = True
				self.FLAG = False

			if (self.PREV == 'music' or self.IS_PLAYING) and self.FLAG:
				self.b.get('http://localhost:8000/music/?action=stop&num=' + str(self.NO))
				if re.search(r'next|next song', cmd) and self.PREV == 'music':    
					self.b.get('http://localhost:8000/music/?action=next &num=' + str(self.NO))
					self.NO += 1    
				if re.search(r'previous|previous song', cmd) and self.PREV == 'music':
					self.b.get('http://localhost:8000/music/?action=prev&num=' + str(self.NO))
					self.NO += 1
				if re.search(r'pause|pause song|pause the song', cmd) and self.PREV == 'music':
					self.b.get('http://localhost:8000/music/?action=pause&num=' + str(self.NO))
					self.NO -= 1
				if re.search(r'resume|resume song|resume the song', cmd) and self.PREV == 'music':
					self.b.get('http://localhost:8000/music/?action=resume&num=' + str(self.NO))
				if re.search(r'stop|stop song|stop the song', cmd) and self.PREV == 'music':
					self.b.get('http://localhost:8000/music/?action=resume&num=' + str(self.NO))
				self.PREV = 'music'
			self.FLAG = True

		except sr.UnknownValueError:
			print("Couldn't catch that")

		except sr.RequestError as e:
			print(e)

	def main(self):
		with sr.Microphone() as source:
			self.r.adjust_for_ambient_noise(source)

		print("Say something!!! ")
		self.r.listen_in_background(source, self.callback)

		while True:
			try:
				time.sleep(1)
			except KeyboardInterrupt:
				exit(0)


obj = Speech()
obj.main()
