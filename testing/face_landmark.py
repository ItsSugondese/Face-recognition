import PIL.Image
import PIL.ImageDraw
import face_recognition

image = face_recognition.load_image_file("image.png")

face_landmark_list = face_recognition.face_landmarks(image)

no_of_faces = len(face_landmark_list)
pil_image = PIL.Image.fromarray(image)
draw = PIL.ImageDraw.Draw(pil_image)
print(no_of_faces)

for face_landmark in face_landmark_list:
    for name, points in face_landmark.items():
        draw.line(points, fill="red", width= 2)
    
    
pil_image.show()