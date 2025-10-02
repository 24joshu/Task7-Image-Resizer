📷 Image Resizer Tool (Flask Project)

A simple Image Resizer Tool built using Python Flask, HTML, and CSS.
This tool allows users to upload an image, set custom width & height, resize the image, preview the result, and download it.

🚀 Features

Upload any image (JPG, PNG, JPEG, etc.)

Resize to custom width and height

Preview the resized image before downloading

Download the resized image in one click

Clean and modern UI with HTML & CSS

Built with Flask (Python backend)

📂 Project Structure
image_resizer_tool/
│── app.py                # Flask backend
│── static/
│   ├── style.css          # CSS styling
│── templates/
│   ├── index.html         # Upload page
│   ├── result.html        # Result/Download page
│── uploads/               # Stores uploaded images
│── resized/               # Stores resized images
│── requirements.txt       # Python dependencies

⚙️ Installation & Setup

Clone the Repository

git clone https://github.com/your-username/image-resizer-tool.git
cd image-resizer-tool


Install Dependencies

pip install -r requirements.txt


Run the Flask App

python app.py


Open in Browser

http://127.0.0.1:5000/

📦 Requirements

Python 3.8+

Flask 3.0.0

Pillow 10.0.0

Install via:

pip install Flask Pillow

📸 Screenshots

1. Upload Page
(Here you can upload image and set dimensions)

2. Result Page
(Preview resized image and download it)

🔮 Future Improvements

Option to maintain aspect ratio automatically

Allow resizing by percentage (%)

Add drag & drop image upload

Support bulk image resizing
