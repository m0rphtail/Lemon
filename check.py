# code to obtain the Voice ID :

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hello World! How's life on earth?")
    engine.runAndWait()
    engine.stop()

# hit ctrl+z to terminate the speech
