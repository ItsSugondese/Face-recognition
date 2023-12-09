import cv2
import tkinter as tk
from PIL import Image, ImageTk
import pickle
import numpy as np
import face_recognition
import os

from csv_maker import MakeIt

detectCount = 0
detectKey = None

afterId = None

def update_image():
    global afterId
    ret, frame = cap.read()
    global detectCount 
    global detectKey
    
    if ret:
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        imgS = cv2.resize(rgb_image, (0,0), None, 0.5, 0.5)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        
        faceCurrFrame = face_recognition.face_locations(imgS)
        encodedCurrentFrame = face_recognition.face_encodings(imgS, faceCurrFrame)


    
        tk_image = ImageTk.PhotoImage(Image.fromarray(rgb_image))

        label.img = tk_image
        label.config(image=tk_image)

        for encoFace, faceLoc  in zip(encodedCurrentFrame, faceCurrFrame):
            matches = face_recognition.compare_faces(list(faces.values()), encoFace)
            faceDis = face_recognition.face_distance(list(faces.values()), encoFace)

            if True in matches:
                matchIndex = np.argmin(faceDis)
                fac = list(faces.keys())
                if detectKey is None or detectKey == fac[matchIndex]:
                    detectCount += 1
                    if detectCount == 3:
                        label.pack_forget()
                        label.destroy()
                        cap.release()
                        cv2.destroyAllWindows() 
                        detectCount = 0
                        
                        showStudent(detectedStudentId=fac[matchIndex])
            else:
                detectCount = 0
            
            
            print(detectCount)
    afterId = label.after(10, update_image)

def start_camera():
    start_button.pack_forget()
    closeButton.pack()
    global cap
    global label

    label = tk.Label(frame)
    label.pack()
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera

    # Set the width and height of the capture (adjust as needed)
    cap.set(3, 640)
    cap.set(4, 480)

    # Call the update_image function to start displaying the video
    update_image()
    
    label.pack()

def close_camera():
    cap.release()
    cv2.destroyAllWindows() 
    closeButton.pack_forget()
    label.destroy()
    studentPhotoLabel.destroy()
    
    start_button.pack()

def showStudent(detectedStudentId):
    global studentPhotoLabel
    image = retrunImageNameWithExtention(detectedStudentId)
    print(detectedStudentId)
    if image is not None:
        
        tk_image = ImageTk.PhotoImage(image)
        studentPhotoLabel = tk.Label(frame)
        studentPhotoLabel.pack()
        studentPhotoLabel.img = tk_image
        studentPhotoLabel.config(image=tk_image)

        csvClass = MakeIt()
        studentName = csvClass.getStudentNameFromCSV(detectedStudentId)
        studentNameLabel = tk.Label(frame)
        studentNameLabel.pack()
        studentNameLabel.config(text= studentName)
        print(studentName)
    else:
        raise Exception("Image not found")


def retrunImageNameWithExtention(name):
    possible_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']  # Add more if needed

    for ext in possible_extensions:
        try:
        # Attempt to open the image with the current extension
            return Image.open(os.path.join("encoded-face",(str(name) + ext)))
            break  # If successful, break out of the loop
        except FileNotFoundError:
            pass
        
    return None  

print("encoding started")
file = open("EncodeFile.p", 'rb')
global faces 
faces = pickle.load(file)
file.close()
print("encoding completed")
# Create a Tkinter window
root = tk.Tk()
root.title("Camera Capture")
root.geometry(f"{400}x{800}")
frame = tk.Frame(root, width=400, height=500)
frame.pack(anchor='nw', padx=20, pady= 20)

# Create a button to start the camera
start_button = tk.Button(frame, text="Check In", command=start_camera)
start_button.pack()

# Create a label to display the image
# label = tk.Label(frame)

closeButton = tk.Button(frame, text="Close", command=close_camera)

# Run the Tkinter main loop
root.mainloop()

# Release the video capture object when the program exits
if 'cap' in locals():
    cap.release()
