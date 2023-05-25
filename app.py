import cv2
import numpy as np
import streamlit as st
from PIL import Image

uploaded_file = st.file_uploader("Upload Image")
if uploaded_file is not None:
    image = Image.open(uploaded_file)

    
    img_array = np.array(image) / 4096
    st.image(img_array, caption='Input', use_column_width=True)
#     cv2.imwrite('out.jpg', cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))

