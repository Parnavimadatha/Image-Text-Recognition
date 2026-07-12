import streamlit as st
from PIL import Image
from image_processor import extract_text

st.set_page_config(page_title="Image & Text Recognition")

st.title("🖼️ Image & Text Recognition using OCR")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Recognize Text"):
        text = extract_text(image)

        st.subheader("Recognized Text")

        if text.strip():
            st.text_area("Output", text, height=300)
        else:
            st.warning("No text detected.")