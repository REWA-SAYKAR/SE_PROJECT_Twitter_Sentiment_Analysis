import streamlit as st
from PIL import Image

hide_menu = """
<style>
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}
</style>
"""

showWarningOnDirectExecution = False
image = Image.open('C:/Users/Admin/Downloads/CBDA-main/CBDA-main/icons/logo.png')


st.set_page_config(page_title = "CBDA", page_icon = image)

st.markdown(hide_menu, unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.image(image , use_column_width=True, output_format='auto')


st.sidebar.markdown("---")


st.sidebar.markdown("<br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'> © 2024 | Janhavi Thikekar & Rewa Saykar </h1>", unsafe_allow_html=True)

st.image(image , use_column_width=True)
