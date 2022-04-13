import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("ask your remedy")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"you asked for : {text}")
    except:
        print("sorry cant hear anything")
