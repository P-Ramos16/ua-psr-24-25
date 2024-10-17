import cv2
import numpy as np
import argparse



def main(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR) # Load an image
    
    sizeX, sizeY, numChannels = image.shape
    print(image.shape)
    print(type(image))


    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    image_thresholded = (image_gray > 128).astype(np.float32)
    
    
    cv2.imshow('window', image_thresholded)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--image_path', dest='image_path', type=str, help='Set the image path')
    args = parser.parse_args()

    main(args.image_path)