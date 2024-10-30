import cv2
import argparse



def main(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR) # Load an image

    height, width = image.shape[:2]

    circled_image = cv2.circle(image, (int(width/2), int(height/2)), 15, (255, 0, 0), thickness=30)

    final_image = cv2.putText(circled_image, "PSR", (int(width/2) - 100, int(height/2) - 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), thickness=5)


    cv2.imshow('window', final_image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--image_path', dest='image_path', type=str, help='Set the image path')
    args = parser.parse_args()

    main(args.image_path)