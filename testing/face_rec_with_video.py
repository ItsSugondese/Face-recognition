import PIL.Image
import PIL.ImageDraw
import face_recognition
import cv2
import numpy as np

image = face_recognition.load_image_file("photo_7_2023-03-07_07-52-18.jpg")
face_encode = face_recognition.face_encodings(image)[0]
knownFace = [face_encode]

# Open the default camera (usually camera index 0)
cap = cv2.VideoCapture(0)

while True:
    # Capture and resize the frame for better performance
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    unknown_encode = face_recognition.face_encodings(frame)
    pil_image = PIL.Image.fromarray(frame)
    try:
        face_locations = face_recognition.face_locations(frame)
        print(len(face_locations))
        for face_location in face_locations:
            top, right, bottom, left = face_location
            draw = PIL.ImageDraw.Draw(pil_image)
            draw.rectangle([left, top, right, bottom], outline="red", width=2)
            print(face_location)
    except Exception as e:
        print(e)


    cv2.imshow('Faces', np.array(pil_image))


    for face in unknown_encode:
        result = face_recognition.compare_faces(knownFace, face)
        print(result)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
