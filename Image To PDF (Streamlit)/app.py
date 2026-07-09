import streamlit as st
import img2pdf

st.title("Image To PDF")

uploaded_files = st.file_uploader(
    "Upload Images", type="image/*", accept_multiple_files=True
)

if uploaded_files:
    try:
        pdf = img2pdf.convert(uploaded_files)
        st.write("Preview :material/preview: ")
        st.image(uploaded_files)

    except Exception as e:
        st.error(e)
    else:
        st.download_button(
            "Download PDF",
            file_name="output.pdf",
            data=pdf,
            icon=":material/download:",
            mime="application/pdf",
        )
