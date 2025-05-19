import cv2
from spellchecker import SpellChecker
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import BeforeImageProcessing
import re

def spell_check_not_correction(word):
    spell = SpellChecker()
    corrected_word = spell.correction(word)
    if word != corrected_word:
        return corrected_word
    return word

def spell_check_return_correct(wrong_word):
    spell = SpellChecker()
    corrected_word = spell.correction(wrong_word)
    return corrected_word

def box_wrong_word_image(img):


    gray_img = BeforeImageProcessing.before_image_processing(image=img)       

    hImg, wImg = gray_img.shape

    boxes = pytesseract.image_to_data(gray_img)


    for x1, b in enumerate(boxes.splitlines()):
        if x1!=0:           
            b = b.split()
            if len(b) == 12:
                b[11] = re.sub(r"[^\w\s]", "", b[11])
                spell = SpellChecker()
                corrected_word = spell.correction(b[11])
            if len(b) == 12:
                b[11] = re.sub(r"[^\w\s]", "", b[11])                
                if b[11] != corrected_word: 
                    print(f'wrong word is {b[11]} and correct word is {corrected_word}')
                    x1,y1,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                    cv2.rectangle(gray_img, (x1,y1), (w + x1, h + y1),(0,0,255),1)
                    cv2.putText(gray_img, corrected_word, (x1,y1), cv2.FONT_HERSHEY_COMPLEX, 0.4 , (50,50,255), 1)
    return gray_img

def box_all_word_image(img):

    gray_img = BeforeImageProcessing.before_image_processing(image=img)       
    hImg, wImg = gray_img.shape

    boxes = pytesseract.image_to_data(gray_img)
    for x1, b in enumerate(boxes.splitlines()):
        if x1!=0:           
            b = b.split()
            if len(b) == 12:
                print(b[11])
            if len(b) == 12:                
                x1,y1,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(gray_img, (x1,y1), (w + x1, h + y1),(0,0,255),1)
                #cv2.putText(gray_img, b[11], (x1,y1), cv2.FONT_HERSHEY_COMPLEX, 0.4 , (50,50,255), 1)
    return gray_img

def extract_text(img):
    gray_img = BeforeImageProcessing.before_image_processing(image=img)
    #text = pytesseract.image_to_string(gray_img)
    new_text = pytesseract.image_to_string(gray_img)
    print(new_text)
    # Remove special characters using regular expression
    #cleaned_text = re.sub(r"[^\w\s]", "", new_text) 
    # Split the cleaned text into a list of words
    
    words = new_text.split()
    #print(words)
    '''
    for word in words:
        print(word)
        spell = SpellChecker()
        corrected_word = spell.correction(word)      
        if word != corrected_word :
            print(word + ' and ' + corrected_word)                          
            new_string = text.replace(word, corrected_word)
        else:
            new_string = text
    '''
    new_string =  ' '.join(words)
    return new_string




