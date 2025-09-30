import cv2
import mediapipe as mp

# instalasi open hand
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# fungsi untuk mengenali gestur tangan
def recognize_gesture(hands_landmarks):
    # ambil posisi ujung jari
    ujung_jempol     = hands_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    ujung_telunjuk   = hands_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    ujung_jariTengah = hands_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ujung_manis      = hands_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    ujung_kelingking = hands_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    # thumbs up => jika hanya jempol yang diangkat
    if (ujung_jempol.y < ujung_telunjuk.y and
        ujung_jempol.y < ujung_jariTengah.y and
        ujung_jempol.y < ujung_manis.y and
        ujung_jempol.y < ujung_kelingking.y):
        return "Thumbs up"
    return "Gesture tidak diketahui"

# fungsi mendeteksi tangan dengan mediapipe
def detect_hands_gesture(image,hand):
    image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    results = hand.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # deteksi gesture
            gesture = recognize_gesture(hand_landmarks)
            # gambar tangan terdeteksi
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            # tampilkan teks gesture
            cv2.putText(image, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    return image

# Membuka Kamera 0 (biasanya webcam utama)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera tidak terbuka")
    exit()

while(cap.isOpened()):
    ret,frame = cap.read()
    if not ret:
        print("gagal menangkap frame")
        break
    
    frame = detect_hands_gesture(frame,hands)
    cv2.imshow("Hands gesture",frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()