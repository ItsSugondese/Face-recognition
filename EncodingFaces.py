import cv2
import face_recognition
import pickle
import os
import shelve


folderPath = 'unencoded-face'
pathList = os.listdir(folderPath)
imageDict = {}
studentIds = []
for path in pathList:
    imageDict.update({os.path.splitext(path)[0] : face_recognition.load_image_file(os.path.join(folderPath, path))})

def findEncoding(imageDict):
    encodingList = {}
    for student_id, images in imageDict.items():
            encoding = face_recognition.face_encodings(images)
            if encoding:
                 encodingList[student_id] = encoding
            
            
    return encodingList

print("Encoding started")

encodeDict = findEncoding(imageDict)

filePath = "EncodeFile.p"

existing_data = {}
try:
    with open(filePath, 'rb') as file:
        existing_data = pickle.load(file)
except FileNotFoundError:
    # If the file doesn't exist yet, initialize with an empty dictionary
    existing_data = {}
print(existing_data)
existing_data.update(encodeDict)

with open("EncodeFile.p", 'wb') as file:
    pickle.dump(existing_data, file)

print("Encoding completed")