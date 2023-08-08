import cv2
from deepface import DeepFace


def checkFace():
    face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    video = cv2.VideoCapture(0)

    while video.isOpened():
        _,frame = video.read()

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face=face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for x,y,w,h in face:
            img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)

            try:
                analyze = DeepFace.analyze(frame, actions=['emotion'])
                emotion=analyze[0]['dominant_emotion']
                print(emotion)
                cv2.putText(frame,emotion,(25,25),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,255,3))
                cv2.imshow('video',frame)
                key=cv2.waitKey(1)
                return emotion
            except:
                print("no face")
            
            
        # if key==ord('q'):
        #     break
    video.release()



# import cv2
# from deepface import DeepFace

# face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# cap=cv2.VideoCapture(0)

# while True:
#     ret,frame=cap.read()
#     result=DeepFace.analyze(img_path=frame,actions=['emotion'],enforce_detection=False)
#     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     faces=face_cascade.detectMultiScale(gray,1.1,4)

#     for (x,y,w,h) in faces:
#         cv2.reactangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
#     emotion=result[0]['dominant_emotion']
#     txt=str(emotion)
#     cv2.putText(frame,txt,(50,50),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,255,3))



#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()