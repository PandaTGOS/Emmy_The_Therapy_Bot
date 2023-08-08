import pyttsx3 as p3
import speech_recognition as sr

def textToSpeech(whattosay):
    engine=p3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    engine.setProperty('rate',147)
    engine.say(whattosay)
    engine.runAndWait()


def speechToText():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")  
        return "None"
    
    return query


# def speechToText():
#     recognizer = sr.Recognizer()

#     while True:
#         try:
#             with sr.Microphone() as mic:
#                 recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                
#                 audio = recognizer.listen(mic)

#                 text = recognizer.recognize_google(audio)
#                 text = text.lower()

#                 print(f"Recognized {text}")

#         except:
#             recognizer = sr.Recognizer()
#             continue

# speechToText()
# textToSpeech("Hello omkaar. Nice to Meet you")