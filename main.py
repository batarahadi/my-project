import cv2
import mediapipe as mp




# Membuka Kamera
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Kamera tidak terbuka")
    exit()

while(cap.isOpened()):
    ret,frame = cap.read()
    if not ret:
        print("gagal menangkap frame")
        break

    cv2.imshow("Hands gesture",frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()