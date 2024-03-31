import cv2
import numpy as np
import os

if __name__ == "__main__":
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer.yml")
    print(recognizer)
    face_cascade_Path = "haarcascade_frontalface_default.xml"
    
    faceCascade = cv2.CascadeClassifier(face_cascade_Path)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    id = 0
    
    names = ["None", "Enkh-Aldar"]
    
    cam = cv2.VideoCapture(1)
    cam.set(3, 640) 
    cam.set(4, 400)
    
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h),(0, 225, 0), 2)
            
            id, confidence = recognizer.predict(gray[y : y + h, x : x + w])
            
            if confidence > 51:
                try:
                    name = names[id]
                    confidence = "{0}%".format(round(confidence))
                except IndexError as e:
                    print(e)
                    name = "Who are you?"
                    confidence = "N/A"
            else: 
                name = "Who are you?"
                confidence = "N/A"
                
            cv2.putText(img, name, (x, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, confidence, (x + 5, y + h -5), font, 1, (255, 255, 0), 1)
            
        cv2.imshow("camera", img)
        
        
        k = cv2.waitKey(10) & 0xFF
        if k == 27:
            break
        
    print("\n [INFO] Exiting Program.")
    cam.release()
    cv2.destroyAllWindows()
    