import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESIZED_FOLDER = "resized"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["RESIZED_FOLDER"] = RESIZED_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESIZED_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return "No file uploaded!"

        file = request.files["image"]
        if file.filename == "":
            return "No file selected!"

        width = int(request.form.get("width", 0))
        height = int(request.form.get("height", 0))

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            # Resize image
            img = Image.open(filepath)
            resized_img = img.resize((width, height))
            resized_filename = f"resized_{filename}"
            resized_path = os.path.join(app.config["RESIZED_FOLDER"], resized_filename)
            resized_img.save(resized_path)

            return redirect(url_for("result", filename=resized_filename))
    return render_template("index.html")


@app.route("/result/<filename>")
def result(filename):
    return render_template("result.html", filename=filename)


@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(app.config["RESIZED_FOLDER"], filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
