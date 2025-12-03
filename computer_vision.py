import cv2
import numpy as np
from PIL import Image
import tempfile
import os

class Processor:
    @staticmethod
    def process_image(image_input):
        
        temp_input_path = None
        
        try:
            # Handle file buffer (from Streamlit upload)
            if hasattr(image_input, 'read'):
                # Create temporary file for the uploaded image
                with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
                    tmp_file.write(image_input.read())
                    temp_input_path = tmp_file.name
                image_path = temp_input_path
            else:
                # It's already a file path
                image_path = image_input
            
            # Load image
            image = cv2.imread(image_path)
            
            if image is None:
                return "The image file could not be loaded. Please check the file.", None
            
            # Convert image to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Apply adaptive thresholding for better results
            _, thresh = cv2.threshold(gray, 135, 250, cv2.THRESH_BINARY)
            
            # Apply denoising
            denoised = cv2.fastNlMeansDenoising(thresh, None, 10, 7, 21)
            
            # Save the processed image
            processed_image_path = "processed_image.jpg"
            cv2.imwrite(processed_image_path, denoised)
            
            return "Image successfully processed.", processed_image_path
            
        except Exception as e:
            return f"An error occurred: {e}", None
            
        finally:
            # Clean up temporary file if created
            if temp_input_path and os.path.exists(temp_input_path):
                try:
                    os.unlink(temp_input_path)
                except:
                    pass