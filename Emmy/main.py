import facerecog as fr
import emmychatbot as cb
import voices as v
import time as t


def decideExpression():
    while True:
        exp=fr.checkFace()
        if exp=="happy":
            return "You seem to be happy that is good."
        elif exp=="angry":
            return "You seem to be angry.would you be comfortable sharing the reason?"
        elif exp=="sad":
            return "You seem to be sad.what's making you upset ?"
        elif exp=="surprise":
            return "You seem to be surprised.In a good way or a bad way?"
        elif exp=="fear":
            return "You seem to be scared. Can i do anything to help you ?"
        else:
            continue



w="Hello! I am Emmy your very own personal therapy bot!"
print(w)
v.textToSpeech(w)


while True:
    query=v.speechToText()
    if "bye" in query:
        v.textToSpeech("Ok take care, bye for now!")
        break;
        
    speak=cb.tellit(query)
    if speak=='camera on':
        v.textToSpeech(speak)
        speak=decideExpression()

    v.textToSpeech(speak)
