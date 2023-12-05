import cv2
import pickle


cap = cv2.VideoCapture(0)

# importing encoded faces
file = open("EncodeFile.p", 'rb')
faces = pickle.load(file)
file.close()

print(faces.keys())



while True:
    success, img = cap.read()
    cv2.imshow("video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()