import pytesseract
from PIL import Image
import os

class Extract:
    @staticmethod
    def extraction(image_path):

        try:
            # Validate path exists
            if not image_path:
                return "Error: No image path provided."
            
            if not os.path.exists(image_path):
                return f"Error: Image file not found at '{image_path}'."
            
            # Open image and extract text
            img = Image.open(image_path)
            
            # Configure Tesseract for better accuracy
            custom_config = r'--oem 3 --psm 6'
            text = pytesseract.image_to_string(img, config=custom_config)
            
            # Check if any text was detected
            if not text or not text.strip():
                return "No text detected in the image. Try:\n- Using a clearer image\n- Ensuring text is clearly visible\n- Checking image orientation"
            
            # Clean up the text
            cleaned_text = text.strip()
            
            return cleaned_text
            
        except pytesseract.TesseractNotFoundError:
            return """Error: Tesseract OCR is not installed or not found in PATH.

Installation instructions:
• Ubuntu/Debian: sudo apt-get install tesseract-ocr
• macOS: brew install tesseract  
• Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki

After installation, you may need to restart your terminal/IDE."""
            
        except PermissionError:
            return f"Error: Permission denied accessing '{image_path}'."
            
        except IsADirectoryError:
            return f"Error: '{image_path}' is a directory, not an image file."
            
        except Image.UnidentifiedImageError:
            return f"Error: '{image_path}' is not a valid image file or format is not supported."
            
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"
    
    @staticmethod
    def extraction_with_config(image_path, lang='eng', psm=6, oem=3):

        try:
            if not image_path or not os.path.exists(image_path):
                return "Error: Invalid image path."
            
            img = Image.open(image_path)
            custom_config = f'--oem {oem} --psm {psm}'
            text = pytesseract.image_to_string(img, lang=lang, config=custom_config)
            
            if not text.strip():
                return "No text detected in the image."
            
            return text.strip()
            
        except Exception as e:
            return f"An error occurred: {str(e)}"