import sys

sys.path.insert(1, 'C:\\Users\\Hello\\python\\FinalProject_IVP501_6\\ORC_Snipping_Tool\\Persistence')

import BeforeImageProcessing

import cv2

def test_before_image_processing():
    # Load the image
    image = cv2.imread('ImageFoders/Capture.png')
    # Check if the image was loaded successfully
    if image is None:
        print("Could not read the image.")
    else:

        image = BeforeImageProcessing.before_image_processing(image=image)
        # Display the image
        cv2.imshow('Image', image)

        # Wait for a key press to close the window
        cv2.waitKey(0)

        # Close all windows
        cv2.destroyAllWindows()

if __name__ == '__main__':

    test_before_image_processing()

