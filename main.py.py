import streamlit as st
import pandas as pd
import numpy as np
from rembg import remove
from PIL import Image
from io import BytesIO
import os
uploaded_file = st.file_uploader("Choose a file")
option=''
try:
    os.remove("input.png")
    os.remove("output.png")
except:
    pass
if uploaded_file is not None:
    
    bytes_data = uploaded_file.getvalue()
    image = Image.open(BytesIO(bytes_data))
    input = image.save("input.png")
    option = st.selectbox(
        'Select model',
        ('u2net ', 'u2netp', 'u2net_human_seg','u2net_cloth_seg','silueta'))

st.write('You selected:', option)

if st.button("Remove"):
   
    try:
        #output = remove(bytes_data)
        #st.image(output, caption='Sunrise by the mountains')
        # Importing required module

        os.system(f'rembg i -m {option} input.png output.png')
        image = Image.open('output.png')
        st.image(image, caption='Background removed')
        with open("output.png", "rb") as file:
            btn = st.download_button(
            label="Download image",
            data=file,
            file_name="flower.png",
            mime="image/png"
          )

    except:
        st.write("Please upload image")