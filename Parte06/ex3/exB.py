#!/usr/bin/env python
import cv2
import numpy as np

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


        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


        faces = detect_bounding_box(image)


        # Create a mask for the faces
        mask = np.zeros_like(gray)

        facedImage = image

        for (x, y, w, h) in faces:
            mask[y:y+h, x:x+w] = 255
            facedImage = cv2.rectangle(facedImage, (x, y), (x + w, y + h), (0, 255, 0), 4)

        edges = cv2.Canny(image, 100, 100)
        edges[mask == 255] = 0
        
        edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        
        edges_colored[np.where((edges_colored == [255, 255, 255]).all(axis=2))] = [0, 0, 255]

        #final_image = cv2.addWeighted(facedImage, 0.5, edges_colored, 0.5, 0)
        final_image = cv2.add(facedImage, edges_colored, 0)

        cv2.imshow(windowName, final_image)  # Display the image


        if cv2.waitKey(16) == ord('q'):
            return


if __name__ == '__main__':
    main()