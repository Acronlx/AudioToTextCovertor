import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("SPEAK NOW: ")
    audio = r.listen(source)


try:
    print("YOU SAID: " + r.recognize_google(audio, language='en-US'))
except sr.UnknownValueError:
    print("SORRY , I DID NOT UNDERSTAND THAT.")
except sr.RequestError as e:
    print("COULD NOT REQUEST RESULTS ROM API : {0}".format(e))
