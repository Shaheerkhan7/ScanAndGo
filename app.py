from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

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

    img_stream = BytesIO()
    qr_img.save(img_stream, format='PNG')
    img_stream.seek(0) 

    return send_file(img_stream, as_attachment=True, download_name='qr.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
