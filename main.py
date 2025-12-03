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
        st.write("Use AI to clean up OCR errors and improve text quality")
        
        if st.button("Enhance text with AI"):
            try:
                from groq import Groq
                
                # Get API key from secrets
                api_key = st.secrets.get("GROQ_API_KEY")
                
                if not api_key:
                    st.error("GROQ_API_KEY not found in secrets. Please add it to `.streamlit/secrets.toml`")
                else:
                    with st.spinner("Enhancing text with AI..."):
                        client = Groq(api_key=api_key)
                        
                        chat_completion = client.chat.completions.create(
                            messages=[
                                {
                                    "role": "user",
                                    "content": f"""The following text was extracted from an image using OCR and may contain errors. 
Please correct any obvious OCR errors, fix formatting, and return the cleaned text. 
Maintain the original meaning and structure.

OCR Text:
{st.session_state['extracted_text']}"""
                                }
                            ],
                            model="llama-3.3-70b-versatile",
                            max_tokens=2000,
                            temperature=0.3,
                        )
                        
                        enhanced_text = chat_completion.choices[0].message.content
                        
                        st.subheader("Enhanced Text")
                        st.text_area("AI-Enhanced Result:", enhanced_text, height=200)
                        
            except ImportError:
                st.error("The `groq` package is not installed. Run: `pip install groq`")
            except Exception as e:
                st.error(f"Error enhancing text: {e}")
else:
    st.info("👆 Please upload an image to get started")