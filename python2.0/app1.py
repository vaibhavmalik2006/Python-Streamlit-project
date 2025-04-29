import streamlit as st
import os
from PIL import Image
from pathlib import Path

# --- Setup ---
GALLERY_DIR = "gallery_images"
os.makedirs(GALLERY_DIR, exist_ok=True)

st.set_page_config(page_title="📸 Image Gallery", layout="wide")
st.title("📸 Image Gallery App")

# --- Upload Section ---
st.sidebar.header("Upload Images")
uploaded_files = st.sidebar.file_uploader(
    "Choose images", type=["jpg", "jpeg", "png"], accept_multiple_files=True
)

save_images = st.sidebar.checkbox("Save uploaded images", value=True)

if uploaded_files:
    for file in uploaded_files:
        img = Image.open(file)
        if save_images:
            img.save(f"{GALLERY_DIR}/{file.name}")
        st.sidebar.success(f"{file.name} uploaded successfully!")

# --- Display Gallery ---
st.subheader("🖼️ Gallery")
img_files = list(Path(GALLERY_DIR).glob("*.png")) + \
            list(Path(GALLERY_DIR).glob("*.jpg")) + \
            list(Path(GALLERY_DIR).glob("*.jpeg"))

if not img_files:
    st.info("No images found. Upload some from the sidebar.")
else:
    cols = st.columns(4)
    for i, img_path in enumerate(img_files):
        img = Image.open(img_path)
        with cols[i % 4]:
            st.image(img, caption=img_path.name, use_column_width='always')
