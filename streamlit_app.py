import streamlit as st
from PyPDF2 import PdfReader

# ---------- App Config ----------
st.set_page_config(
    page_title="PDF Reader App",
    layout="wide"
)

# ---------- Sidebar ----------
st.sidebar.title("📂 Upload PDF")

uploaded_file = st.sidebar.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

# ---------- Main Area ----------
st.title("📄 PDF Content Viewer")

if uploaded_file is not None:
    try:
        reader = PdfReader(uploaded_file)

        full_text = ""

        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n\n"

        if full_text.strip():
            st.success("PDF loaded successfully")
            st.text_area(
                "Extracted Text",
                full_text,
                height=600
            )
        else:
            st.warning("No extractable text found in this PDF.")

    except Exception as e:
        st.error(f"Error reading PDF: {e}")

else:
    st.info("Upload a PDF from the sidebar to view its content.")
