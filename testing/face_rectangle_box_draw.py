import PIL.Image
import PIL.ImageDraw
import face_recognition

image = face_recognition.load_image_file("photo_7_2023-03-07_07-52-18.jpg")

face_locations = face_recognition.face_locations(image)
pil_image = PIL.Image.fromarray(image)
print(pil_image)
no_of_faces = len(face_locations)
print(no_of_faces)

for face_location in face_locations:
    top, right, bottom, left = face_location
    draw = PIL.ImageDraw.Draw(pil_image)
    draw.rectangle([left, top, right, bottom], outline="red")
    
pil_image.show()