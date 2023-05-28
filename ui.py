import streamlit as st
import cv2
import os
from PIL import Image
import main as dt
st.title('Medical Image Enhancement using GAN')
st.sidebar.subheader("Mini Project-4")

def load_image(image_file):
	img = Image.open(image_file)
	return img

source = ("from file", "camera")
source_index = st.sidebar.selectbox("select Images", range(len(source)), format_func=lambda x: source[x])

if source_index==0:
    st.sidebar.subheader("Image")
    image_file = st.sidebar.file_uploader("Upload Images", type=["png","jpg","jpeg"])


if source_index==1:
    image_file = st.camera_input("Take a picture")

if image_file is not None:
    st.subheader("Original Image")
    st.image(load_image(image_file),width=400)
    target=r"data\fivek\test\raw"
    ext=['.jpeg','.png','.jpg','.svg','.gif']
    for file in os.listdir(target): 
        if file.endswith(tuple(ext)):
            os.remove(target + file)
    with open(os.path.join("data\fivek\test\raw",image_file.name),"wb") as f:
        f.write(image_file.getbuffer())

    dt.main()
        
    a=Image.open(r"results\UEGAN-FiveK\test\test_results\data\fivek\test\raw\1 (1)_60.00_testFakeExp.png")
    # C:\Users\harshal dawkhare\OneDrive\Documents\6 Sem\Mini Projects\MP 4\Final\UEGAN\results\UEGAN-FiveK\test\test_results\data\fivek\test\raw\1 (1)_60.00_testFakeExp.png
    st.image(a,width=400)
        
       