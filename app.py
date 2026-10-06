from flask import Flask, render_template, request
import qrcode
import os
import base64
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_image = None
    if request.method == "POST":
        user_input = request.form.get("text")
        if user_input:
            # Membuat QR Code
            qr = qrcode.QRCode(box_size=10, border=4)
            qr.add_data(user_input)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Menyimpan gambar ke dalam memory buffer
            buffer = BytesIO()
            img.save(buffer, format="PNG")

            # Mengubah gambar menjadi base64 agar bisa ditampilkan di HTML
            qr_image = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return render_template("index.html", qr_image=qr_image)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True) 