import cv2
import tkinter as tk
from PIL import Image, ImageTk

def update_image():
    ret, frame = cap.read()

    if ret:
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        tk_image = ImageTk.PhotoImage(Image.fromarray(rgb_image))

        label.img = tk_image
        label.config(image=tk_image)

    label.after(10, update_image)

def start_camera():
    global cap
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera

    # Set the width and height of the capture (adjust as needed)
    cap.set(3, 640)
    cap.set(4, 480)

    # Call the update_image function to start displaying the video
    update_image()

# Create a Tkinter window
root = tk.Tk()
root.title("Camera Capture")

# Create a label to display the image
label = tk.Label(root)
label.pack()

# Create a button to start the camera
start_button = tk.Button(root, text="Start Camera", command=start_camera)
start_button.pack()

# Run the Tkinter main loop
root.mainloop()

# Release the video capture object when the program exits
if 'cap' in locals():
    cap.release()
