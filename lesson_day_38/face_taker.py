import cv2
import os

if __name__ == "__main__":

    def create_directory(directory):
        
        if not os.path.exists(directory):
            os.makedirs(directory)
            
    
    
    create_directory("images")
    
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
    cam = cv2.VideoCapture(0)  # Use index 0 for the default camera
    
    cam.set(3, 640)
    cam.set(4, 480)
    
    count = 0
    face_id = input("\nEnter user id (MUST be an integer) and press <return> --> ")
    print("\n[INFO] Initializing face capture. Look at the camera and wait...")
    
    while True:
        ret, img = cam.read()
        
        if not ret:
            print("Error: Failed to capture frame from the webcam.")
            break
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        if gray is None or gray.size == 0:
            print("Error: Failed to convert frame to grayscale.")
            break
        
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        
        if len(faces) == 0:
            print("No faces detected.")
        
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            count += 1
            
            cv2.imwrite(f"./images/Users-{face_id}-{count}.jpg", gray[y:y+h, x:x+w])
            
            cv2.imshow("image", img)
            
        k = cv2.waitKey(100) & 0xFF
        
        if k == 27:  # Press Esc to exit
            break
        
        elif count >= 30:  # Capture 30 images
            break
        
    print("\n[INFO] SUCCESS! Exiting Program.")
    
    cam.release()
    cv2.destroyAllWindows()
