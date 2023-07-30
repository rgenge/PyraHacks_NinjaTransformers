import cv2
import numpy as np

def detector(videopath):
#Load xml file with pedestrian images
    face_data = cv2.CascadeClassifier("pedestrian.xml")
    cap= cv2.VideoCapture(videopath)
    ret,frame = cap.read()
    while ret:
        #Convert to grayscale
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #Detect using face_data
        faces=face_data.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5, minSize=(30,30))
        #Draw box around pedestrian and diplay it
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y), (x + w, y + h), (255, 0, 0), 2)
        #reshape the video size in case its too big, it can get a bit "ugly"
        frame2 = cv2.resize(frame, (1000, 1400))
        cv2.imshow("frame", frame2)
        ret, frame = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release the video capture object.
    cap.release()
    # Close all windows.
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("To exit the program press 'q'")
    videopath = input("Enter de the video path:")
    detector(videopath)
