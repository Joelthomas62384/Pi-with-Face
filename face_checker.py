import cv2
import face_recognition
import cvzone
import pickle
import numpy as np
import pyautogui

# Initialize the camera capture object
cap = cv2.VideoCapture(0)

counter = 0

def main():
    global counter
    print("Loading Encode File ...")
    file = open('encodeFile.p', 'rb')
    encodeListKnownWithIds = pickle.load(file)
    file.close()
    encodeListKnown, studentIds = encodeListKnownWithIds
    print("Encode File Loaded")

    try:
        while True:
            success, img = cap.read()
            img = cv2.flip(img, 1)
            img = cv2.resize(img, (680, 440))
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            faceCurFrame = face_recognition.face_locations(imgS)
            encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
            if faceCurFrame:
                for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                    matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                    faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                    print("matches", matches)
                    print("faceDis", faceDis)

                    matchIndex = np.argmin(faceDis)
                    print("Match Index", matchIndex)
                    if matches[matchIndex]:
                        
                        counter += 1
                        print(studentIds[matchIndex])
                        if counter >= 8:
                            pyautogui.press('q')
                            pyautogui.hotkey('alt','tab')
                            cap.release()

                            return studentIds[matchIndex]
                        
            cv2.imshow("Video",img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        pass
        # passqqqq
        # Release the camera capture object when done

if __name__ == "__main__":
    main()
