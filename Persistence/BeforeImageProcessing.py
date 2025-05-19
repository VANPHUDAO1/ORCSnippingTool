import cv2
import numpy as np

#3.Convert to grayscale
def convert_gray(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return gray_img

#4.normalization image
def normalization(image):

    norm_img = np.zeros((image.shape[0], image.shape[1]))
    image = cv2.normalize(image, norm_img, 0, 255, cv2.NORM_MINMAX)

    return image
#1.Skew Correction image
def deskew(image):

    co_ords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(co_ords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC,
    borderMode=cv2.BORDER_REPLICATE)

    return rotated

#5.Image Scaling image 
def set_image_dpi(image):

    h, w   = image.shape
    resize_image = cv2.resize(image, (w*2, h*2))

    return resize_image

#2.Noise Removal
def remove_noise(image):
    return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15)

#7.Thinning and Skeletonization
def morphilogical(image):

    kernel = np.ones((3,3),np.uint8)
    erosion = cv2.erode(image, kernel, iterations = 1)

    return erosion

#6.Thresholding or Binarization
def thresholding(image):

    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) [1]

#8.Edge image denoise
def edge(image):
    return cv2.Canny(image, 50, 150)

#Resize image
def resize_img(ing):
    img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

#Dilation and erosion image
def dilation_and_erosion_img(img):
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

#blur image
def blur_img(img):
    #cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    #cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)



def before_image_processing(image):

    #remove noise
    remove_noise_image = remove_noise(image)
    #convert to grayscale
    gray_image = convert_gray(remove_noise_image)
    #edge image denoise
    #edge_image = edge(gray_image)
    #normalization image
    norma_image = normalization(gray_image)
    #scaling image
    if norma_image.shape[0] < 300 or norma_image.shape[1] < 300:
        scale_image = set_image_dpi(norma_image)
    else:
        scale_image = norma_image  
    #Thresholding or Binarization
    thresh_image = thresholding(scale_image)

    #edge_image = edge(norma_image)

    return thresh_image



