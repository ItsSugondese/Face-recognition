import cv2
import pickle
import face_recognition
import PIL.ImageDraw
import PIL.Image
import numpy as np
import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry(f"{400}x{500}")

frame = tk.Frame(root, width=400, height=500)
frame.pack(anchor='nw', padx=20, pady= 20)
cap = cv2.VideoCapture(0)

print("loading encoded file")
# importing encoded faces
file = open("EncodeFile.p", 'rb')
faces = pickle.load(file)
file.close()

print("encoding loading completed")



while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0,0), None, 0.5, 0.5)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    faceCurrFrame = face_recognition.face_locations(imgS)
    encodedCurrentFrame = face_recognition.face_encodings(imgS, faceCurrFrame)

    for encoFace, faceLoc  in zip(encodedCurrentFrame, faceCurrFrame):
        matches = face_recognition.compare_faces(list(faces.values()), encoFace)
        faceDis = face_recognition.face_distance(list(faces.values()), encoFace)

        if True in matches:
            matchIndex = np.argmin(faceDis)
            fac = list(faces.keys())
            print(fac[matchIndex])
        print(matches)
        top, right, bottom, left = faceLoc
    cv2.imshow("video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()       