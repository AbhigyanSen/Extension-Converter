import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
        except:
            print("could not recognize what you said")

speech_to_text()
