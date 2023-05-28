## Medical Image Enhancement with Generative Adversarial Network

<!-- ## Introdcurion -->

<div align=center><img src="./figures/example1.PNG" width = "100%" height = "100%" /></div>


### Abstract

Medical imaging, including X-rays, CT scans, and MRI scans, plays a vital role in the identification and diagnosis of various medical conditions. 

However, these images often suffer from inherent limitations such as low quality, noise, artifacts, and distortions, posing challenges for accurate interpretation and diagnosis. In recent years, image enhancement techniques have emerged as powerful tools to improve the quality and clarity of medical images, thereby enhancing the accuracy of diagnosis and facilitating better understanding of the anatomy and physiology of the human body.

The improved quality and clarity of enhanced medical images enable medical professionals to gain deeper insights into anatomical structures and abnormalities, thus facilitating more accurate diagnoses. Consequently, the enhanced images assist in surgical planning, treatment decisions, and a comprehensive understanding of the patient's condition. By harnessing image enhancement techniques, medical practitioners can leverage the potential of medical imaging technology to its fullest, ultimately leading to improved patient care and outcomes.


<!-- **The framework of UEGAN:** -->
<div align=center><img src="./figures/GAN.png" width = "100%" height = "100%" /></div>


## Requirements and Installation
We recommended the following dependencies.
*  Python 3.6
*  PyTorch 1.4.0
*  tqdm 4.43.0
*  munch 2.5.0
*  torchvision 0.5.0


<!-- ## Installation -->
```
git clone [https://github.com/eezkni/UEGAN --recursive](https://github.com/HarshalDawkhare20/Medical-Image-Enhancement-Using-GAN)
cd UEGAN
```

### Getting the MIT-Adobe FiveK Dataset
 - Download the dataset from [https://data.csail.mit.edu/graphics/fivek/. (~50GB, SHA1)](https://www.kaggle.com/datasets/pranavraikokte/covid19-image-dataset)
 - Extract the data.
 - Open with Lightroom. Just click "upgrade" if Lightroom asks you to upgrade.

### Generating the Low-quality Images
 - Import the dataset into Adobe Lightroom.
 - In the `Collections` list (bottom left), select collection **`Inputs/InputAsShotZeroed`**.
 - Export all images in the following settings:
   - Select all images at the bottom or in the middle (select one and press `Ctrl-A`), right-click any of them and select `Export/Export...`. 
   - Export Location: `Export to`=`Specific folder`, `Folder`=`Your folder for low-quality images`.
   - File Settings: `Image Format`=`PNG`, `Color Space`=`sRGB`, `Bit Depth`=`8 bit/component`
   - Image Sizing: `Resize to Fit`=`Short Edge`, select `Don't Enlarge`, Fill in `512 pixels`, `Resolution` doesn't matter to ignort it.
   - Finally, click `Export`.

### Generating the High-quality Images
 - Import the FiveK dataset into Adobe Lightroom.
 - In the `Collections` list (bottom left), select collection **`Experts/C`**.
 - Export all images in the following settings:
   - Select all images at the bottom or in the middle (select one and press `Ctrl-A`), right-click any of them and select `Export/Export...`. 
   - Export Location: `Export to`=`Specific folder`, `Folder`=`Your folder for high-quality images`.
   - File Settings: `Image Format`=`PNG`, `Color Space`=`sRGB`, `Bit Depth`=`8 bit/component`
   - Image Sizing: `Resize to Fit`=`Short Edge`, select `Don't Enlarge`, Fill in `512 pixels`, `Resolution` doesn't matter to ignort it.
   - Finally, click `Export`.


## Testing
Having trained your models or the [pre-trained model on MIT-Adobe FiveK Dataset]([https://drive.google.com/file/d/1lBQOx-2YBEYemrPW-AtFZPv7MmdNEwRe/view?usp=sharing]) (put into ```./results/UEGAN-FiveK/models/```), to test the pre-trained UEGAN on FiveK, run the test script below.

## Command For Testing 
```
python main.py --mode test --version UEGAN-FiveK --pretrained_model 60 --is_test_nima True --is_test_psnr_ssim True
```

## Training
Prepare the training, testing, and validation data. The folder structure should be:
```
data
└─── fiveK
	├─── train
	|	├─── exp
	|	|	├──── a1.png                  
	|	|	└──── ......
	|	└─── raw
	|		├──── b1.png                  
	|		└──── ......
	├─── val
	|	├─── label
	|	|	├──── c1.png                  
	|	|	└──── ......
	|	└─── raw
	|		├──── c1.png                  
	|		└──── ......
	└─── test
		├─── label
		| 	├──── d1.png                  
		| 	└──── ......
		└─── raw
			├──── d1.png                  
			└──── ......
```
```raw/```contains low-quality images, ```exp/``` contains unpaired high-quality images, and ```label/``` contains corresponding ground truth.

To train UEGAN on FiveK, run the training script below.
```
python main.py --mode train --version UEGAN-FiveK --use_tensorboard True --is_test_nima True --is_test_psnr_ssim True
```

This script will create a folder named ```./results``` in which the resulting are saved. 
- The PSNR results will be saved to here: ```./results/psnr_val_results``` (including PSNR for each valiaded epoch and the summary)
- The SSIM results will be saved to here: ```./results/ssim_val_results``` (including SSIM for each valiaded epoch and the summary)
- The NIMA results will be saved to here: ```./results/nima_val_results``` (including NIMA for each valiaded epoch and the summary)
- The training logs will be saved to here: ```./results/UEGAN-FiveK/logs```
- The models will be saved to here: ```./results/UEGAN-FiveK/models```
- The intermediate results will be saved to here: ```./results/UEGAN-FiveK/samples```
- The validation results will be saved to here: ```./results/UEGAN-FiveK/validation```
- The test results will be saved to here: ```./results/UEGAN-FiveK/test```


To view training results and loss plots, run ```tensorboard --logdir=results/UEGAN-FiveK/logs```, and click the URL accordingly (For example, http://nzk-ub:6007/).

## User Interface 

User Interface is created with the help of Streamlit

All the code of UI is given in the file uichat3.py

Hence Integrating User Interface with GAN model as the backend 

In this we take an image as a input and given that image to the ML model working at the back.

Output of the model is displayed on the screen, hence one can easily see the Input Raw Image and Enhanced Image.


Thanks for your attention !
