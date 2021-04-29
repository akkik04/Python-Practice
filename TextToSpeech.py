# importing the necessary module for text-to-speech conversion.
from gtts import gTTS

# importing the module to play the audio.
import os

# recieving the text needed to convert to audio as input from the user.
user_text = input("Enter your text please: ")

# declaring the language to convert to.
language = 'en'

# passing the user inputted text and the language to the text-to-speech mechanism.
# using appropriate parameters (e.g., 'slow = True').
speech_object = gTTS(text = user_text, lang = language, slow = False)

# saving the converted audio in an mp3 file named 'speech'.
speech_object.save("speech.mp3")

# outputting the converted file as audio to the user.
os.system("start speech.mp3")