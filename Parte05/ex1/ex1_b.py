import cv2
import argparse



def main(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR) # Load an image
    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--image_path', dest='image_path', type=str, help='Set the image path')
    args = parser.parse_args()

    main(args.image_path)