# Python Micro Assistant : LEMON

import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

# method to recognize the commands given to LEMON
# using speech_Recognition module 
def takeCommand():

	r = sr.Recognizer()

	with sr.Microphone() as source:
		print('Listening')
		r.adjust_for_ambient_noise(source, duration = 1)

		# seconds of non-speaking audio before a phrase is considered complete
		r.pause_threshold = 0.7
		audio = r.listen(source)

		try:
			print("Recognizing")
			Query = r.recognize_google(audio, language='en-IN')
			print("Your Query = ", Query)
			
		except Exception as e:
			print(e)
			print("Pardon please")
			return "None"
		
		return Query

def speak(audio):
	
	engine = pyttsx3.init()

	# gets the current value of engine property
	voices = engine.getProperty('voices')
	
	engine.setProperty('voice', voices[11].id)
	'''  
	voices[11].id represents english :

	<Voice id = english
          name=english
          languages=[b'\x02en-gb']
          gender=male
          age=None> english

	# CODE to obtain the Voice ID in file check.py
	'''
	engine.say(audio)
	
	# blocks while processing all the currently queued commands
	engine.runAndWait()

def tellDay():
	
	day = datetime.datetime.today().weekday() + 1
	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week)


def tellTime():
	
	time = str(datetime.datetime.now())
	
	# time format "2020-06-05 17:50:14.582630" before slicing
	print(time)
	hour = time[11:13]
	min = time[14:16]
	speak("The time is sir" + hour + "Hours and" + min + "Minutes")	

def Hello():
	speak("Hello, how can I help you?")


def Take_query():

	Hello()
	
	# infinite loop to keep listening until
	# bye is said or program is terminated
	while(True):

		query = takeCommand().lower()
		if "open github" in query:
			speak("Opening GitHub ")
			webbrowser.open("github.com")
			continue
		
		elif "open google" in query:
			speak("Opening Google ")
			webbrowser.open("www.google.com")
			continue
			
		elif "which day is it" in query:
			tellDay()
			continue
		
		elif "what time is it" in query:
			tellTime()
			continue
		
		# this will exit and terminate the program
		elif "bye" in query:
			speak("Bye, have a nice day!")
			exit()
		
		elif "from wikipedia" in query:
			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			
			# results into summary of 4 lines (customizable) from wikipedia
			result = wikipedia.summary(query, sentences = 4)
			speak("According to wikipedia, ")
			print(result)
			speak(result)
		
		elif "what is your name" in query:
			speak("I am Lemon, your deskstop Assistant until you say bye")

if __name__ == '__main__':
	Take_query()
