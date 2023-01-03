def  speak(text):
	import pyttsx3
	speaker = pyttsx3.init()
	speaker.say(text)
	speaker.runAndWait()