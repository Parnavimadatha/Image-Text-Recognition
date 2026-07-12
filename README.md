# 🖼️ Image & Text Recognition using OCR

A Python-based Optical Character Recognition (OCR) application that extracts text from images using Tesseract OCR. The application provides a simple and interactive web interface built with Streamlit, allowing users to upload an image and instantly recognize the text present in it.

---

## 📌 Features

- Upload image files (.jpg, .jpeg, .png)
- Extract text using OCR
- Image preprocessing using OpenCV
- Interactive web interface with Streamlit
- Fast and easy-to-use application

---

## 🛠️ Technologies Used

- Python
- Streamlit
- OpenCV
- NumPy
- Pillow
- PyTesseract
- Tesseract OCR

---

## 📂 Project Structure

```
Image-Text-Recognition/
│
├── app.py
├── image_processor.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Parnavimadatha/Image-Text-Recognition.git
```

### Move into the project directory

```bash
cd Image-Text-Recognition
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install Tesseract OCR

Download and install Tesseract OCR for Windows.

Default installation path:

```
C:\Program Files\Tesseract-OCR\tesseract.exe
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

Open your browser and visit:

```
http://localhost:8501
```

---

## 📷 How it Works

1. Upload an image containing printed text.
2. Click **Recognize Text**.
3. The application preprocesses the image.
4. OCR extracts the text.
5. The recognized text is displayed on the screen.

---

## 📌 Future Enhancements

- Handwritten text recognition
- Multiple language support
- PDF text extraction
- Copy-to-clipboard feature
- Download extracted text as a file

---

## 👩‍💻 Author

**Parnavi Madatha**

GitHub:
https://github.com/Parnavimadatha
