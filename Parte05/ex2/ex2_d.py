import cv2
import numpy as np
import argparse



def main(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR) # Load an image
    
    sizeX, sizeY, numChannels = image.shape
    print(image.shape)
    print(type(image))

    lowerBounds = (0, 50, 0)
    upperBounds = (55, 255, 55)

    mask = cv2.inRange(image, lowerBounds, upperBounds)


    newImage = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow('window', newImage)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--image_path', dest='image_path', type=str, help='Set the image path')
    args = parser.parse_args()

    main(args.image_path)