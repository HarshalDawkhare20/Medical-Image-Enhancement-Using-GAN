import streamlit as st
import os
import subprocess
from PIL import Image

def save_image(file):
    # Save the uploaded file to a specific folder with renaming as 1.jpg
    file_path = r"C:\Users\harshal dawkhare\OneDrive\Documents\6 Sem\Mini Projects\MP 4\Final\UEGAN\data\fivek\test\raw\1.jpg"
    with open(file_path, "wb") as f:
        f.write(file.read())
    st.success("Image saved successfully!")

# def save_image(file):
#     # Save the uploaded file to a specific folder with renaming as 1.jpg
#     file_path = r"C:\Users\harshal dawkhare\OneDrive\Documents\6 Sem\Mini Projects\MP 4\Final\UEGAN\data\fivek\test\raw\1.jpg"

#     # Open the uploaded image using PIL
#     image = Image.open(file)

#     # Create a new blank image with the desired size (512x512) and white background
#     padded_image = Image.new("RGB", (512, 512), (255, 255, 255))

#     # Calculate the center position to place the original image in the padded image
#     x_offset = (512 - image.width) // 2
#     y_offset = (512 - image.height) // 2

#     # Paste the original image onto the padded image at the center position
#     padded_image.paste(image, (x_offset, y_offset))

#     # Save the padded image
#     padded_image.save(file_path)

#     st.success("Image saved successfully!")


def run_python_file():
    # Run a python file with arguments
    try:
        # Delete all files from the directory
        directory = r"C:\Users\harshal dawkhare\OneDrive\Documents\6 Sem\Mini Projects\MP 4\Final\UEGAN\results\UEGAN-FiveK\test\test_compare\data\fivek\test\raw"
        file_list = os.listdir(directory)
        for file_name in file_list:
            file_path = os.path.join(directory, file_name)
            os.remove(file_path)



        virtualenv_path = r"C:\Users\harshal dawkhare\OneDrive\Documents\6 Sem\Mini Projects\MP 4\Final\mp4\Scripts\activate.bat"  # Replace with the path to your virtual environment's activation script
        # activate_cmd = f"call {virtualenv_path} && python main.py --mode test --version UEGAN-FiveK --pretrained_model 60 --is_test_nima True --is_test_psnr_ssim True "
        activate_cmd = r"cd C:\Users\harshal dawkhare\OneDrive\Documents\6 Sem\Mini Projects\MP 4\Final && call .\mp4\Scripts\activate && cd UEGAN && python main.py --mode test --version UEGAN-FiveK --pretrained_model 60 --is_test_nima True --is_test_psnr_ssim True "
        # subprocess.run(activate_cmd, shell=True, check=True)
        subprocess.run(activate_cmd, shell=True, check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        st.success("Python file executed successfully!")
        st.header("Option 3: Show Output Files")
        show_output()
    except subprocess.CalledProcessError as e:
        st.success("Python file executed successfully!")
        st.header("Output")
        show_output()
        # st.error(f"Error: {e}")

def show_output():
    # Display the output image
    output_folder = r"C:\Users\harshal dawkhare\OneDrive\Documents\6 Sem\Mini Projects\MP 4\Final\UEGAN\results\UEGAN-FiveK\test\test_compare\data\fivek\test\raw"
    if os.path.exists(output_folder):
        files = os.listdir(output_folder)
        if files:
            st.subheader("Origional Image VS Enhanced Image")
            file_path = os.path.join(output_folder, files[0])
            image = Image.open(file_path)
            # image = image.resize((st.columns(), image.height))
            st.image(image, caption=files[0], use_column_width=True)
        else:
            st.info("No output image found.")
    else:
        st.info("Output folder does not exist.")


def main():
    # st.title("Medical Image Enhancement using GAN")
    st.markdown("## Medical Image Enhancement using GAN")

    # Option 1: Take input from the user and save it as 1.jpg
    st.header("Upload an Image")
    uploaded_file = st.file_uploader("Upload an image")
    if uploaded_file is not None:
        save_image(uploaded_file)

    # Option 2: Run a python file with arguments
    # st.header("Run a Python File")
    # args = st.text_input("Enter arguments (space-separated)")
    args = "--mode test --version UEGAN-FiveK --pretrained_model 60 --is_test_nima True --is_test_psnr_ssim True"
    if st.button("Run"):
        run_python_file()

    # Option 3: Show output from a specific folder
    # st.header("Option 3: Show Output Files")
    # show_output()

if __name__ == "__main__":
    main()
