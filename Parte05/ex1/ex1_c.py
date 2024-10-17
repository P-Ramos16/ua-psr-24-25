import cv2
import argparse



def main(first_image, second_image):
    image1 = cv2.imread(first_image, cv2.IMREAD_COLOR) # Load an image
    cv2.imshow('window', image1)  # Display the image
    cv2.waitKey(3000) 

    image2 = cv2.imread(second_image, cv2.IMREAD_COLOR) # Load an image
    cv2.imshow('window', image2)  # Display the image
    cv2.waitKey(0) 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--first_image', dest='first_image', type=str, help='Set the first image path')
    parser.add_argument('--second_image', dest='second_image', type=str, help='Set the second image path')
    args = parser.parse_args()

    main(args.first_image, args.second_image)