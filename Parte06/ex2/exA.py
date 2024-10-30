#!/usr/bin/env python
import cv2

windowName = 'window - Ex2a'

def main():
    # initial setup
    capture = cv2.VideoCapture(0)
    cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

    _, image = capture.read() # get an image from the camera
    # add code to show acquired image
    # add code to wait for a key press


    cv2.namedWindow(windowName)
    cv2.imshow(windowName, image)  # Display the image


    while cv2.waitKey(1000) != ord('q'):
        continue

    return

if __name__ == '__main__':
    main()