import cv2
import argparse



def main(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR) # Load an image
    
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    retval, image = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)
    
    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--image_path', dest='image_path', type=str, help='Set the image path')
    args = parser.parse_args()

    main(args.image_path)