<<<<<<< HEAD
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
=======
import streamlit as st
from computer_vision import Processor
from extraction import Extract
from PIL import Image

# Streamlit UI
st.title("PictureText")
st.write("An OpenCV OCR project that helps extract text from images in real time")
st.divider()

with st.sidebar:
    with st.expander("How to use"):
        st.write(
            """
            1. Upload an image
            2. Click the **Extract Text** button
            3. View the processed image and extracted text
            4. If text has errors, click **Enhance text with AI** to correct them
            """
        )
    
    with st.expander("Requirements"):
        st.info(
            """
            - Tesseract OCR must be installed
            - For AI enhancement, add ANTHROPIC_API_KEY to `.streamlit/secrets.toml`
            """
        )

# Image upload
st.subheader("1. Provide an Image")
source_img = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if source_img:
    # Display original image
    st.image(source_img, caption="Original Image", use_container_width=True)
    
    # Extract Text button
    if st.button("Extract Text", type="primary"):
        processor = Processor()
        extractor = Extract()
        
        with st.spinner("Processing image..."):
            # Process the image
            message, processed_path = processor.process_image(source_img)
            
            if processed_path:
                st.success(message)
                
                # Display processed image
                st.subheader("2. Processed Image")
                st.image(processed_path, caption="Processed Image", use_container_width=True)
                
                # Extract text
                with st.spinner("Extracting text..."):
                    extracted_text = extractor.extraction(processed_path)
                
                st.subheader("3. Extracted Text")
                st.text_area("Result:", extracted_text, height=200)
                
                # Store extracted text in session state for AI enhancement
                st.session_state['extracted_text'] = extracted_text
                
            else:
                st.error(message)
    
    st.divider()
    
    # AI Enhancement section
    if 'extracted_text' in st.session_state:
        st.subheader("4. Enhance Text with AI (Optional)")
        st.write("Use Claude to clean up OCR errors and improve text quality")
        
        if st.button("Enhance text with AI"):
            try:
                import anthropic
                
                # Get API key from secrets
                api_key = st.secrets.get("ANTHROPIC_API_KEY")
                
                if not api_key:
                    st.error("ANTHROPIC_API_KEY not found in secrets. Please add it to `.streamlit/secrets.toml`")
                else:
                    with st.spinner("Enhancing text with AI..."):
                        client = anthropic.Anthropic(api_key=api_key)
                        
                        message = client.messages.create(
                            model="claude-sonnet-4-20250514",
                            max_tokens=2000,
                            messages=[
                                {
                                    "role": "user",
                                    "content": f"""The following text was extracted from an image using OCR and may contain errors. 
Please correct any obvious OCR errors, fix formatting, and return the cleaned text. 
Maintain the original meaning and structure.

OCR Text:
{st.session_state['extracted_text']}"""
                                }
                            ]
                        )
                        
                        enhanced_text = message.content[0].text
                        
                        st.subheader("Enhanced Text")
                        st.text_area("AI-Enhanced Result:", enhanced_text, height=200)
                        
            except ImportError:
                st.error("The `anthropic` package is not installed. Run: `pip install anthropic`")
            except Exception as e:
                st.error(f"Error enhancing text: {e}")
else:
    st.info("👆 Please upload an image to get started")
>>>>>>> 329d64b (Added initial files)
