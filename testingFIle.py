import cv2
import pickle


cap = cv2.VideoCapture(0)

# importing encoded faces
file = open("EncodeFile.p", 'rb')
faces = pickle.load(file)
file.close()

print(faces.keys())