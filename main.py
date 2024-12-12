import cv2
from PIL import Image
import pytesseract


# Specify the path to Tesseract executable (required for Windows)
# Uncomment and modify this line for Windows users
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HP\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Function to extract text from an image
def extract_text_from_image(image_path):
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image not found at path: {image_path}")

        # Preprocess the image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        # Convert OpenCV image (numpy array) to PIL image
        processed_image = Image.fromarray(thresh)

        # Extract text
        text = pytesseract.image_to_string(processed_image)
        return text
    except Exception as e:
        return f"An error occurred: {e}"


# Path to the image
image_path = "my image.jpg"  # Replace with your image file path

# Extract and print text
extracted_text = extract_text_from_image(image_path)
print("Extracted Text:")
print(extracted_text)
