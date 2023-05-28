import streamlit as st
from PIL import Image
import main as dt
import os
import subprocess

def save_uploaded_image(uploaded_image, save_path):
    with open(save_path, 'wb') as f:
        f.write(uploaded_image.getbuffer())

def load_image(image_path):
    image = Image.open(image_path)
    return image

# def run_python_file(args):
#     # Run a python file with arguments
#     try:
#         subprocess.run(["python", "main.py"] + args.split(), check=True)
#         st.success("Python file executed successfully!")
#     except subprocess.CalledProcessError as e:
#         st.error(f"Error: {e}")

def run_python_file(args):
    # Run a python file with arguments
    try:
        virtualenv_path = r"C:\Users\harshal dawkhare\OneDrive\Documents\6 Sem\Mini Projects\MP 4\Final\mp4\Scripts\activate.bat"  # Replace with the path to your virtual environment's activation script
        activate_cmd = f"call {virtualenv_path} && python main.py --mode test --version UEGAN-FiveK --pretrained_model 60 --is_test_nima True --is_test_psnr_ssim True "
        subprocess.run(activate_cmd, shell=True, check=True)
        st.success("Python file executed successfully!")
    except subprocess.CalledProcessError as e:
        st.error(f"Error: {e}")


def main():
    st.title("Image Uploader and Viewer")

    # Sidebar
    st.sidebar.title("Options")
    uploaded_image = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        save_path = r"C:\Users\harshal dawkhare\OneDrive\Documents\6 Sem\Mini Projects\MP 4\Final\UEGAN\data\fivek\test\raw\1.jpg"
        save_uploaded_image(uploaded_image, save_path)
        st.sidebar.success("Image saved successfully!")

    run_python_file("--mode test --version UEGAN-FiveK --pretrained_model 92 --is_test_nima True --is_test_psnr_ssim True")

    # Main content
    st.header("View Image")
    image_path = r"C:\Users\harshal dawkhare\OneDrive\Documents\6 Sem\Mini Projects\MP 4\Final\UEGAN\results\UEGAN-FiveK\test\test_results\data\fivek\test\raw\1 (1)_60.00_testFakeExp.png"
    image = load_image(image_path)
    st.image(image, caption="Another Image")

if __name__ == "__main__":
    main()
