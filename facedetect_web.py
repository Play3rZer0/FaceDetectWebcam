# Import the library modules
import cv2
import sys

# Specify the path where Haar Cascade XML file is located
cascPath = <path to haar cascade file>
faceCascade = cv2.CascadeClassifier(cascPath)

# Prepare capture from webcam
video_capture = cv2.VideoCapture(0)

while True:
# Capture the video frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# You must enter the values for the parameters denoted with an x

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=<x>,
        minNeighbors=<x>,
        minSize=(xx, xx),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

# Drawing rectangle around the face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Show the frame
    cv2.imshow('Video', frame)

# Quit the program with the 'q' key is pressed

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture when program terminates
video_capture.release()
cv2.destroyAllWindows()
