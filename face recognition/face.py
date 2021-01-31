# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:04:51 2019

@author: Gunjan Mimo
"""

# >>>>>>>>face detection<<<<<<<
import cv2

# load the cascade for the face.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# load the cascade for the eyes.
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


def detect(gray, frame):  # create a function that takes as input the image in black and white (gray) and the original image (frame), and that will return the same image with the detector rectangles.
    # apply the detectMultiScale method from the face cascade to locate one or several faces in the image.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:  # For each detected face:
        # paint a rectangle around the face.
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # get the region of interest in the black and white image.
        roi_gray = gray[y:y+h, x:x+w]
        # get the region of interest in the colored image.
        roi_color = frame[y:y+h, x:x+w]
        # apply the detectMultiScale method to locate one or several eyes in the image.
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:  # For each detected eye:
            # paint a rectangle around the eyes, but inside the referential of the face.
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    return frame  # return the image with the detector rectangles.


video_capture = cv2.VideoCapture(0)  # turn the bcam on.

while True:  # repeat infinitely (until break):
    _, frame = video_capture.read()  # get the last frame.
    # do some colour transformations.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)  # get the output of our detect function.
    cv2.imshow('Video', canvas)  # display the outputs.
    if cv2.waitKey(1) & 0xFF == ord('q'):  # If  type on the keyboard:
        break  # stop the loop.

video_capture.release()  # turn the bcam off.
# destroy all the windows inside which the images re displayed.
cv2.destroyAllWindows()
