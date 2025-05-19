import sys

sys.path.insert(1, 'C:\\Users\\Hello\\python\\FinalProject_IVP501_6\\ORC_Snipping_Tool\\Persistence')

import ImageProcessing 

def box_wrong_word_image_service(image):
    return ImageProcessing.box_wrong_word_image(image)

def box_all_word_image_service(image):
    return ImageProcessing.box_all_word_image(image)

def extract_text_service(image):
    return ImageProcessing.extract_text(image)