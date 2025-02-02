import cv2
import numpy as np


def eyeTracker():
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    cap = cv2.VideoCapture(0)

    measuring = True
    measurements = []
    measurementCycles = 30

    while (measuring):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray,minNeighbors=15)
            if(measuring):
                try:
                    ex1, ey1, ew1, eh1 = eyes[0]
                    ex2, ey2, ew2, eh2 = eyes[1]

                    measurements.append(abs((ex1+ew1)/2-(ex2+ew2)/2))

                    if(len(measurements)>measurementCycles):
                        measuring = False
                        print(np.mean(measurements))
                        cap.release()
                        cv2.destroyAllWindows()
                        return np.mean(measurements)

                except:
                    print("Please stay still & take off GLASSES PRAYGE")
                    measurements = []
            
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    