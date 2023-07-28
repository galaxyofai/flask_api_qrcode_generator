
from flask import Flask
from flask import render_template,request
# Import QRCode from pyqrcode
import pyqrcode
import png



app=Flask(__name__)

@app.route('/')
def home():
    # return "hello"
    return render_template('home.html')

@app.route('/about')
def about():
    # return "hello"
    return render_template('about.html')


#*******************************************QR CODE****************************************
@app.route('/qrcode',methods=['GET'])
def qr_code():
    return render_template('qrcode.html')


@app.route('/showqr',methods=['POST'])
def showqr():
    # String which represents the QR code
    # s = "www.geeksforgeeks.org"
    print("hiii")
    text=request.form['text']
    # Generate QR code
    url = pyqrcode.create(text)

    # Create and save the svg file naming "myqr.svg"
    url.svg("./static/img/myqr.png", scale = 8)

    # Create and save the png file naming "myqr.png"
    url.png('./static/img/myqr.png', scale = 6)
    return render_template('showqrcode.html')

if __name__=='__main__':
    app.run("0.0.0.0",8000,debug=True)
