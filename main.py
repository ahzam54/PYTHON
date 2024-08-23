import speech_recognition as sr
import nltk
from nltk.tokenize import word_tokenize
from gtts import gTTS
import os

# Initialize speech recognition
r = sr.Recognizer()

# Define a function to process voice commands
def process_voice_command(audio):
    # Transcribe spoken words
    text = r.recognize_google(audio, language="en-US")
    # Tokenize the text
    tokens = word_tokenize(text)
    # Perform actions based on the tokens
    if "hello" in tokens:
        respond("Hello, how can I assist you?")
    elif "what" in tokens:
        respond("I'm JARVIS, your AI assistant.")
    else:
        respond("I didn't understand that. Please try again.")

# Define a function to respond with spoken words
def respond(text):
    # Generate spoken response
    tts = gTTS(text=text, lang="en")
    # Save the audio file
    tts.save("response.mp3")
    # Play the audio file
    os.system("mpg321 response.mp3")

# Start listening for voice commands
while True:
    with sr.Microphone() as source:
        audio = r.listen(source)
        process_voice_command(audio)