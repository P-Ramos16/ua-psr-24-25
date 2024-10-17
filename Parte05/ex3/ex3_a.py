import argparse
import cv2
import numpy as np

# Global variables
window_name = 'window - Ex3a'
image_gray = None
alpha_slider_max = 255

def onTrackbar(threshold):
    global image_gray # use global var
    image_thresholded = (image_gray > threshold).astype(np.float32)

    cv2.imshow(window_name, image_thresholded)  # Display the image


def main(image_path):

    image = cv2.imread(image_path, cv2.IMREAD_COLOR) # Load an image
    global image_gray # use global var

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)
    
    cv2.imshow(window_name, image_gray)  # Display the image
    


    trackbar_name = 'Alpha x %d' % alpha_slider_max
    cv2.createTrackbar(trackbar_name, window_name , 0, alpha_slider_max, onTrackbar)
    # Show some stuff
    onTrackbar(0)



    cv2.waitKey(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image_path', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    main(args['image_path'])