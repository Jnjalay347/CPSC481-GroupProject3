# Frontend UI

import streamlit as st

st.title("Resume Screening System")

# Upload PDF resumes
uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type="pdf",
    accept_multiple_files=True
)

# Search section
query = st.text_input("Enter job keyword search")
