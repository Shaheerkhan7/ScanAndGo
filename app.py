from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)


# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")


# Route to generate QR code
@app.route("/generate", methods=["POST"])
def generate():
    url = request.form["url"]
    qr_img = qrcode.make(url)

    img_stream = BytesIO()
    qr_img.save(img_stream, format="PNG")
    img_stream.seek(0)

    return send_file(
        img_stream, as_attachment=True, download_name="qr.png", mimetype="image/png"
    )


# Route to generate QR code for vCard
@app.route("/generate_vcard", methods=["POST"])
def generate_vcard():
    name = request.form["name"]
    surname = request.form["surname"]
    telephone = request.form["tele"]
    location = request.form["location"]
    company = request.form["company"]
    title = request.form["title"]

    # Create a vCard string
    vcard_data = (
        "BEGIN:VCARD\n"
        "VERSION:3.0\n"
        f"N:{surname};{name}\n"
        f"FN:{name} {surname}\n"
        f"TEL;TYPE=CELL:{telephone}\n"  
        f"ADR;TYPE=HOME:;;{location}\n"  
        f"ORG:{company}\n"
        f"TITLE:{title}\n"
        "END:VCARD"
    )

    # Generate QR code from vCard data
    qr_img = qrcode.make(vcard_data)
    img_stream = BytesIO()
    qr_img.save(img_stream, format="PNG")
    img_stream.seek(0)

    return send_file(
        img_stream,
        as_attachment=True,
        download_name="vcard_qr.png",
        mimetype="image/png",
    )


if __name__ == "__main__":
    app.run(debug=True)
