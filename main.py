import cv2
from PIL import Image
import pytesseract

# Ask the user for the image path
image_path = input("Enter the full path to the image file: ")

try:
    # Load the image
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError("The image file was not found. Please check the path.")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Save the processed image temporarily
    processed_path = 'processed_image.jpg'
    cv2.imwrite(processed_path, thresh)

    # Extract text using pytesseract
    text = pytesseract.image_to_string(Image.open(processed_path))
    print("Extracted Text:")
    print(text)
except Exception as e:
    print(f"An error occurred: {e}")
