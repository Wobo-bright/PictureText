# PictureText

*PictureText* is a Python-based project that uses Tesseract OCR to convert images into editable text. Whether you want to extract text from scanned documents, photos, or screenshots, this project provides a simple solution for converting visual content into usable text.

---

## Features

- *Text Extraction*: Convert images (JPEG, PNG, etc.) into text using the Tesseract OCR engine.
- *Preprocessing*: Built-in image processing to improve OCR accuracy (grayscale conversion, thresholding).
- *Easy Setup*: Simple Python code that integrates with the Tesseract OCR library.
- *Multi-Language Support*: Tesseract supports multiple languages for diverse use cases.

---

## Requirements

To run this project, you'll need the following:

- Python 3.x
- Tesseract OCR (installed locally on your system)
- Required Python packages:
  - pytesseract
  - opencv-python
  - Pillow

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Wobo-bright/PictureText.git
```

## Usage

1. *Run the Script*

    ```bash
    python main.py
    ```
    when you run the script, you'd be asked to upload the image file you want to read. do that by copying and pasting the complete path of that image file.
    if there are qoutation marks, remove them to prevent an error.
    

3. *Extract Text*

    After running the script, it will process the image and display the extracted text in your terminal.

---

## Contributing

Contributions to *PictureText* are welcome! If you have ideas for improvements, new features, or bug fixes, feel free to open an issue or submit a pull request.

---

## License

*PictureText* is licensed under the [MIT License](LICENSE).

---
