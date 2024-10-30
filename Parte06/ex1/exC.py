import argparse
import cv2
import numpy as np
from functools import partial

# Global variables
windowName = 'window - Ex3a'
global currentColour
image = 255 * np.ones(shape=(400, 600, 3), dtype=np.uint8)

def mouse_handler(event, x, y, flags, params):
    global currentColour
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Painting {currentColour} at ({x}, {y})")

        circled_image = cv2.rectangle(image, (x-2, y-2), (x+2, y+2), currentColour, thickness=-1)

        cv2.imshow(windowName, circled_image)


def main():
    global currentColour
    currentColour = [0, 0, 255]

    height, width = image.shape[:2]

    cv2.namedWindow(windowName)
    cv2.imshow(windowName, image)  # Display the image
    
    cv2.setMouseCallback(windowName, mouse_handler)

    while 1:
        char = cv2.waitKey(1000)

        if char == ord('r'):
            print("pressed r")
            currentColour = [0, 0, 255]

        elif char == ord('g'):
            print("pressed g")
            currentColour = [0, 255, 0]

        elif char == ord('b'):
            print("pressed b")
            currentColour = [255, 0, 0]

        elif char == ord('q'):
            print("pressed q -> quitting")
            return
    

if __name__ == '__main__':
    main()