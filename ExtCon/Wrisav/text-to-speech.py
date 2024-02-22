from gtts import gTTS
import gtts.lang
import os
import time

def text_to_speech(text, lang, slow=False):
    speech = gTTS(text=text, lang=lang, slow=slow)
    speech.save("D:\\AILABS\\New folder (2)\\output.mp3")

print("Enter text: ")
text = input()
print("")
print("Language codes: ", gtts.lang.tts_langs())
print("")
print("Enter language code for accent: ")
lang = input()

text_to_speech(text, lang)
print("Speech has been saved as output.mp3. Press any key to play the audio.")
input()
os.system("start D:\\AILABS\\New folder (2)\\output.mp3")
time.sleep(5) # Optional: Add a short delay before exiting the script