from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to generate QR code
@app.route('/generate', methods=['POST'])
def generate():
    url = request.form['url']
    qr_img = qrcode.make(url)

    # Save the QR code image
    qr_img_path = 'qr.png'
    qr_img.save(qr_img_path)

    return send_file(qr_img_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
