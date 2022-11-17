#!/usr/bin/python3
# -- coding: utf-8
#import qrcode, base64, io
from flask import Flask, request, render_template, flash
from flask_qrcode import QRcode
app = Flask(__name__)
qrcode = QRcode(app)
# echo -n "Ckrops-WebQRCodeGenerator-20221114"|sha512sum
app.config['SECRET_KEY'] = '7680ee6d5b19f6e01a09148cc5313392d5caaa248329d1f5330920ae29d8b15e34723c87fe255acd277ff83998671335911e89275b3bf0129fdb078e1a3bca3a'
@app.route('/', methods=['POST', 'GET'])
def qrcodegen():
 error = None
 answer = None
 if request.method == 'POST':
  answer = (request.form['text'])
#  rawBytes = io.BytesIO()
#  img.save(rawBytes, "JPEG")
#  img_base64 = base64.b64encode(rawBytes.read())
  if (request.form['text']):
   flash(answer)
  else:
   error = 'Invalid text'
   # the code below is executed if the request method
   # was GET or the credentials were invalid
 return render_template('qrcode.html', error=error, answer=answer)
app.run(host='0.0.0.0',port=2000)
