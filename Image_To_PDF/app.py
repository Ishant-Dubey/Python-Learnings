import img2pdf
import streamlit as st

st.title("Image To PDF")

uploaded_files = st.file_uploader(
    "Upload Images", type="image/*", accept_multiple_files=True
)

a4_page_size = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
layout_function = img2pdf.get_layout_fun(a4_page_size)

if "images" not in st.session_state:
    st.session_state.images = []


def reorder_up(idx):
    lst = st.session_state.images
    if idx > 0:
        lst[idx], lst[idx - 1] = lst[idx - 1], lst[idx]


def reorder_down(idx):
    lst = st.session_state.images
    if idx < len(lst) - 1:
        lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]


if uploaded_files:
    new_sig = [(f.name, f.size) for f in uploaded_files]
    old_sig = [(f.name, f.size) for f in st.session_state.images]

    if new_sig != old_sig and len(new_sig) != len(old_sig):
        st.session_state.images = list(uploaded_files)
else:
    st.session_state.images = []

if st.session_state.images:
    st.write("Preview :material/preview: ")
    for i, img_file in enumerate(st.session_state.images):
        key_base = f"{img_file.name}_{i}"

        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.image(img_file, caption=img_file.name)
        with col2:
            st.button(
                "up",
                key=f"up_{key_base}",
                on_click=reorder_up,
                args=(i,),
                width="stretch",
                icon=":material/arrow_circle_up:",
            )
        with col3:
            st.button(
                "down",
                key=f"down_{key_base}",
                on_click=reorder_down,
                args=(i,),
                width="stretch",
                icon=":material/arrow_circle_down:",
            )

    try:
        image_bytes = [f.getvalue() for f in st.session_state.images]
        pdf = img2pdf.convert(
            image_bytes, rotation=img2pdf.Rotation.ifvalid, layout_fun=layout_function
        )

    except Exception as e:
        st.error(f"Failed to create pdf as {e}", icon="🚨")
    else:
        st.download_button(
            "Download PDF",
            file_name="output.pdf",
            data=pdf,
            icon=":material/download:",
            mime="application/pdf",
        )
