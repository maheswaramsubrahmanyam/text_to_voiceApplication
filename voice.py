import pyttsx3
text_speech = pyttsx3.init()
answer = input("type what you want and i will convert in to voice : ")
text_speech.say(answer)
text_speech.runAndWait()
