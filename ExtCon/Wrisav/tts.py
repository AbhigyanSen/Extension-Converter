import pyttsx3

engine = pyttsx3.init()

# Adjusting rate of speech
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)  # You can adjust the rate as needed, 150 is just an example

# Selecting a voice
voices = engine.getProperty('voices')
print(voices)

x=input("enter voice number you want to use (0 - male, 1 - female): ")
# You can loop through the voices to see available options and select the one you prefer
engine.setProperty('voice', voices[int(x)].id)  # Selecting the second voice, you can change the index

message = input("Enter your message: ")

# Handling punctuation
# You can split the message into sentences and then say them individually
sentences = message.split('.')
for sentence in sentences:
    engine.say(sentence.strip())
    engine.say('.')  # Adding a pause for punctuation
    engine.runAndWait()
