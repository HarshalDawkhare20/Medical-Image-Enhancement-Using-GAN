import streamlit as st
import os
import subprocess

def save_image(file):
    # Save the uploaded file to a specific folder with renaming as 1.jpg
    file_path = r"C:\Users\harshal dawkhare\OneDrive\Documents\6 Sem\Mini Projects\MP 4\Final\UEGAN\data\fivek\test\raw\1.jpg"
    with open(file_path, "wb") as f:
        f.write(file.read())
    st.success("Image saved successfully!")

def run_python_file():
    # Run a python file with arguments
    try:
        virtualenv_path = r"C:\Users\harshal dawkhare\OneDrive\Documents\6 Sem\Mini Projects\MP 4\Final\mp4\Scripts\activate.bat"  # Replace with the path to your virtual environment's activation script
        # activate_cmd = f"call {virtualenv_path} && python main.py --mode test --version UEGAN-FiveK --pretrained_model 60 --is_test_nima True --is_test_psnr_ssim True "
        activate_cmd = r"cd C:\Users\harshal dawkhare\OneDrive\Documents\6 Sem\Mini Projects\MP 4\Final && call .\mp4\Scripts\activate && cd UEGAN && python main.py --mode test --version UEGAN-FiveK --pretrained_model 60 --is_test_nima True --is_test_psnr_ssim True "
        subprocess.run(activate_cmd, shell=True, check=True)
        st.success("Python file executed successfully!")
    except subprocess.CalledProcessError as e:
        st.error(f"Error: {e}")

def show_output():
    # Display the contents of a specific output folder
    output_folder = r"C:\Users\harshal dawkhare\OneDrive\Documents\6 Sem\Mini Projects\MP 4\Final\UEGAN\results\UEGAN-FiveK\test\test_results\data\fivek\test\raw"
    if os.path.exists(output_folder):
        files = os.listdir(output_folder)
        if files:
            st.subheader("Output Files:")
            for file in files:
                file_path = os.path.join(output_folder, file)
                st.markdown(f"- [{file}]({file_path})")
        else:
            st.info("No output files found.")
    else:
        st.info("Output folder does not exist.")

def main():
    st.title("Streamlit File Handling Example")

    # Option 1: Take input from the user and save it as 1.jpg
    st.header("Option 1: Save an Image")
    uploaded_file = st.file_uploader("Upload an image")
    if uploaded_file is not None:
        save_image(uploaded_file)

    # Option 2: Run a python file with arguments
    # st.header("Option 2: Run a Python File")
    # args = st.text_input("Enter arguments (space-separated)")
    args = "--mode test --version UEGAN-FiveK --pretrained_model 60 --is_test_nima True --is_test_psnr_ssim True"
    if st.button("Run"):
        run_python_file()

    # Option 3: Show output from a specific folder
    st.header("Option 3: Show Output Files")
    show_output()

if __name__ == "__main__":
    main()
