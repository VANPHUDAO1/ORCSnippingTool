import sys

sys.path.insert(1, 'C:\\Users\\Hello\\python\\FinalProject_IVP501_6\\ORC_Snipping_Tool\\Business')

import Service

import cv2
input_img = cv2.imread('ImageFoders/Capture6.png')

def test_box_wrong_word_image_service():
    image = Service.box_wrong_word_image_service(input_img)
        # Display the image
    cv2.imshow('Image', image)

        # Wait for a key press to close the window
    cv2.waitKey(0)

        # Close all windows
    cv2.destroyAllWindows()
def test_box_all_word_image_service():

    image = Service.box_all_word_image_service(input_img)
        # Display the image
    cv2.imshow('Image', image)

        # Wait for a key press to close the window
    cv2.waitKey(0)

        # Close all windows
    cv2.destroyAllWindows()

def test_extract_text():

    print(Service.extract_text_service(input_img))

if __name__ == '__main__':

    #test_box_wrong_word_image_service()
    #test_box_all_word_image_service()
    test_extract_text()

