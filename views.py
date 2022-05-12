from crypt import methods

from django.shortcuts import render
from app import  app
from flask import request, render_template, url_for
import os 
import cv2
import numpy as np 
from PIL import Image
import random
import  string
import pytesseract
import requests

# pytesseract.pytesseract.tesseract_cmd 

# Adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'D:\COURSE\Personal Projects\Mini Projects\Text Extract From Image\app\static\uploads'

#Rout to home page
@app.route('/', methods = ['GET', 'POST'])
def index():

    # Execute if request is get
    if request.method == 'GET':
        full_filename = 'images/white_bg.jpg'
        return render_template("index.html", full_filename = full_filename)

    # Execute if reqest is post
    if request.method == 'POST':
        image_upload = request.files['image_upload']
        imagename = image_upload.filename
        image = Image.open(image_upload)

        # Converting image to array
        image_arr = np.array(image.convert("RBG"))
        # Converting image to grayscale
        gray_img_arr = cv2.cvtColor(image_arr, cv2.COLOR_BAYER_BG2GRAY)
        # Converting image back to RGB
        image = Image.fromarray(gray_img_arr)

        # Printing lowercase
        letters = string.ascii_lowercase
        # Generating unique image name for dynamic image display
        name = ''.join(random.choice(letters) for i in range(10)) + '.png'
        full_filename = ' uploads/' + name

        # Extracting text from image        
        custom_config = r'-1 eng --oem 3 --psm 6'
        text = pytesseract.image_to_string(image, config = custom_config)
        
        # Removing symbol if any
        characters_to_remove = "!()@-*'>+-/,|$%#&~^"
        new_string = text
        for character in characters_to_remove:
            new_string = new_string.replace(character, '')

        # converting string to list ot display extracted text in sep line
        new_string = new_string.split('\n')

        # Saving image to display in HTML
        img = Image.fromarray(image_arr, 'RGB')
        img.save(os.path.joint(app.config['INITIAL_FILE_UPLOADS'], name))

        # Retuning template, filename, extrated text
        return render_template("index.html", full_filename = full_filename, text = new_string)

# Main Function
if __name__ == '__main__':
    app.run(debug=True)