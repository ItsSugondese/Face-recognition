import cv2
import face_recognition
import pickle
import os
import shelve
from csv_maker import MakeIt

class NotAnIntegerError(Exception):
    pass

folderPath = 'unencoded-face'
pathList = os.listdir(folderPath)
imageDict = {}
studentIds = []
for path in pathList:
    imageDict.update({path : face_recognition.load_image_file(os.path.join(folderPath, path))})

def findEncoding(imageDict):
    encodingList = {}
    for student_id, images in imageDict.items():
            encoding = face_recognition.face_encodings(images)
            if encoding:
                stdId = str(os.path.splitext(student_id)[0])
                
                if not stdId.isdigit():
                    raise Exception("Value not in numeric format")
                encodingList[int(stdId)] = encoding[0]
                os.rename("unencoded-face/" + student_id, "encoded-face/" + student_id)
                csvMake = MakeIt()
                csvMake.updateCSV(int(stdId))
            else:
                 os.rename("unencoded-face/" + student_id, "fail-encode/" + student_id)
            
            
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