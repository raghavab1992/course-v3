import numpy as np
from flask import Flask, request, redirect, url_for
from flask import render_template
from PIL import Image
import base64
from io import BytesIO

app = Flask(__name__)

pics = []

@app.route('/')
def home():
    return("Hello World from rb1992!!:")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    return render_template('submit.html')

def img_base64(img):
    #print('map func call')
    img1 = img.stream.read()
    img2 = Image.open(BytesIO(img1))
    #print(type(img2))
    buffer = BytesIO()
    img2.save(buffer, format ='JPEG')
    return {'imgname':img.filename,'img':base64.b64encode(buffer.getvalue()).decode("utf-8")}

def img_base641(img):
    #print('map func call  :',img)
    img = open_image(img)
    buffer = BytesIO()
    img.save(buffer, format ='JPEG')
    return {'imgname':img.filename,'img':base64.b64encode(buffer.getvalue()).decode("utf-8")}

preds=[]
@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
     #   print('requesting files')
        pics = request.files.getlist('imgs')
        #flash('Upload completed')
    #print('converting base64', pics)
    for pic in pics:
        #print(preds)
        preds.append(img_base64(pic))
    #print('preds ::', preds)
    #return("TBD - Dynamic check")
    return render_template('predict.html', preds = preds)
    

