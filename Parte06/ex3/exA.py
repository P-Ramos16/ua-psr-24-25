#!/usr/bin/env python
import cv2

windowName = 'window - Ex3a'

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_bounding_box(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))

    return faces


def main():
    # initial setup
    capture = cv2.VideoCapture(0)
    cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

    while 1:
        _, image = capture.read() # get an image from the camera
        # add code to show acquired image
        # add code to wait for a key press


        faces = detect_bounding_box(image)

        for (x, y, w, h) in faces:
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 4)

        cv2.imshow(windowName, image)  # Display the image


        if cv2.waitKey(16) == ord('q'):
            return


if __name__ == '__main__':
    main()