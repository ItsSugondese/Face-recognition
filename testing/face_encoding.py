import PIL.Image
import PIL.ImageDraw
import face_recognition
import cv2

image = face_recognition.load_image_file("photo_7_2023-03-07_07-52-18.jpg")
image2 = face_recognition.load_image_file("image.png")
unknownImage = face_recognition.load_image_file("snapshot1.png")

face_encode = face_recognition.face_encodings(image)[0]
face_encode2 = face_recognition.face_encodings(image2)[0]
unknown_face = face_recognition.face_encodings(unknownImage)

knownFace  = [
    face_encode,
    face_encode2
]
for face in unknown_face:
    result = face_recognition.compare_faces(knownFace, face)
    name = "unknown"
    if(result[0]):
        name = "rohan"
    if(result[1]):
        name = "muji"

    print(name)



