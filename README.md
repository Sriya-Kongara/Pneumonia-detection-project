# Pneumonia-detection-project

**Pneumonia Detection Using CNN-based Feature Extraction** 


**Abstract:**
Pneumonia is a life-threatening infectious disease affecting one or both lungs in humans commonly
caused by bacteria called Streptococcus pneumonia. One in three deaths in India is caused due to pneumonia
 as reported by World Health Organization (WHO).
 Chest X-Rays which are used to diagnose pneumonia need expert radiotherapists for evaluation. Thus,
 developing an automatic system for detecting pneumonia would be beneficial for treating the disease without
 any delay particularly in remote areas. Due to the success of deep learning algorithms in analysing medical
 images, Convolutional Neural Networks (CNNs) have gained much attention for disease classification.
 In addition, features learned by pre-trained CNN models on large-scale datasets are much useful in image
 classification tasks. In this work, we appraise the functionality of pre-trained CNN models utilized as feature
extractors followed by different classifiers for the classification of abnormal and normal chest X-Rays. We
 analytically determine the optimal CNN model for the purpose. Statistical results obtained demonstrates that
 pretrained CNN models employed along with supervised classifier algorithms can be very beneficial in
 analysing chest X-ray images, specifically to detect Pneumonia




 **INTRODUCTION**
 Pneumonia is a common and potentially serious respiratory infection characterized by inflammation of the
 air sacs in one or both lungs. It is typically caused by bacterial, viral, or fungal infections, with bacterial
 pneumonia being the most common type. Pneumonia can also develop as a complication of other
 respiratory conditions, such as influenza or bronchitis. It causes the air sacs, or alveoli, of the lungs to fill up
 with fluid or pus. Bacteria, viruses, or fungi may cause pneumonia. Symptoms can range from mild to
 serious and may include a cough with or without mucus (a slimy substance), fever, chills, and trouble
 breathing.
 How serious your pneumonia is depends on your age, your overall health, and what caused your infection.
 Bacterial pneumonia, which is the most common form, tends to be more serious than other types of
 pneumonia, with symptoms that require medical care. The symptoms of bacterial pneumonia can develop
 gradually or suddenly. Fever may rise as high as a dangerous 105 degrees F, with profuse sweating and
 rapidly increased breathing and pulse rate.




 **HOW CHEST X-RAY USED TO DETECT PNEUMONIA?**
 Chest X-rays are used to detect pneumonia by identifying specific features in the lungs. These features
 indicate inflammation, fluid buildup, or infection in the lung tissue, which are characteristic signs of
 pneumonia. Radiologists interpret these findings to diagnose pneumonia and determine its severity and
 extent. Chest X-rays are highly effective at detecting abnormalities in the lungs, including signs of
 pneumonia. They can provide valuable information to aid in the diagnosis and management of pneumonia.
 Some of the features for detecting pneumonia include edges, textures, and patterns within the lung opacities,
 such as consolidations, infiltrates, and ground-glass opacities, which are indicative of pneumonia, shapes,
 and sizes of the opacities present in the lung fields, which can help differentiate between different types and
 stages of pneumonia




 **PROPOSED SYSTEM**
 In recent years, advances in deep learning, particularly Convolutional Neural Networks (CNNs), have
 revolutionized medical image analysis, offering promising avenues for automated disease detection from
 radiological images. CNNs are uniquely suited for this task, as they can learn complex hierarchical features
 directly from raw image data, eliminating the need for handcrafted features and intricate preprocessing
 steps. In this context, this study aims to develop and evaluate a CNN-based model for pneumonia detection
 from chest X-ray images.
 Firstly, we preprocess the chest X-ray images, employing techniques such as resizing, normalization, and
 augmentation. This ensures consistency and improves the robustness of our dataset, allowing the CNN
 model to learn from a diverse range of images. Using a carefully designed CNN architecture, we then
 extract relevant features from the preprocessed images. During the training phase, we employ data
 augmentation techniques to further enhance the diversity of our dataset, Once trained, the CNN model is
 capable of classifying chest X-ray images into two categories: Pneumonia and Normal




**ALGORITHM USED**
 **CONVOLUTIONAL NEURAL NETWORK(CNN):**
 A convolutional neural network (CNN or ConvNet) is a network architecture for deep learningthat learns
 directly from data. CNNs are particularly useful for finding patterns in images to recognize objects, classes,
 and categories. A convolutional neural network can have tens or hundreds of layers that each learn to detect
 different features of an image. Filters are applied to each training image at different resolutions, and the
 output of each convolved image is used as the input to the next layer. The filters can start as very simple
 features, such as brightness and edges, and increase in complexity to features that uniquely define the object


  **ACTIVATION FUNCTIONS USED ARE:**
 • RELU- Arectified linear unit (ReLU) is an activation function that introduces the property of non
linearity to a deep learning model and solves the vanishing gradients issue. It interprets the positive
 part of its argument. It is one of the most popular activation functions in deep learning.
 • SIGMOID- Sigmoid is a mathematical function that maps input values to a value between 0 and 1,
 making it useful for binary classification


**IMPLEMENTATION STEPS:**
 **1. PREPROCESSING:**
 • First load images from a directory structure where each subdirectory represents a different class, and
 the images are stored within these subdirectories.
 • Foreach image file, it reads the image as grayscale and resizes it to the specified target_size.
 • Then normalization of the pixel values of the image data is done. Normalizing the pixel values is a
 common preprocessing step in deep learning tasks involving image data. By dividing the pixel values by
 255.0, you're scaling them to the range [0, 1].
 • Thereshaping is done to ensure that the data has the correct shape expected by the CNN model.
 
**2. DATA AUGUMENTATION:**
 • Data augmentation is a technique used to artificially increase the size of the training dataset by
 applying various transformations.
 • rotation_range: Rotation range in data augmentation refers to the degree or range of rotation applied to
 images during the augmentation process.
 • zoom_range: zoom range typically refers to the range of zoom levels that can be applied to an image
 i.e a range within which zoom into images is applied.
 • width_shift_range: It refers to the range by which an image can be horizontal. When applying a width
 shift to an image, it is shifted horizontally by a random distance within the specified range.
 • height_shift_range:A range within which shift images vertically are applied.
 • Atlast horizontal_flip: whether to flip images horizontally technique is applied.
 
**3. CLASSIFICATION:**
 • Thegoal of classification is to build a model that can accurately predict the class labels of new, unseen
 data based on the patterns learned from the training dataset.
 • ACNNarchitecture is designed which is suitable for image classification tasks. Our CNN architecture
 includes variations of convolutional layers followed by pooling layers and fully connected layers for
 classification.
 • Dataset is split into train, test, and validation sets. The training set is used to train the model, while the
 validation set is used to monitor performance during training.
 • Our CNN model is trained using a data generator, i.e. through the fit() method the model is trained
 using batches of augmented data generated by a data generator.
 • This holistic approach ensures that the CNN model learns robust features from the chest X-ray images
 and effectively discriminates between pneumonia-positive and pneumonia-negative cases.
• The model is employed to predict probabilities for each input image, indicating the likelihood of
 pneumonia presence.
 • These probabilities are then converted into binary classes through a thresholding mechanism, where
 probabilities above 0.5 are classified as positive, while those equal to or below 0.5 are classified as
 negative.
 
 **4. MODELEVALUATION:**
 • Thetrained CNN model's performance is evaluated on a separate test dataset and the loss and accuracy
 metrics are determined





  **SOFTWARE REQUIREMENTS:**
 • Operating System: Windows 10, 7, 8.
 • Language: Python.
 • Google Collaboratory
 • IDE : Anaconda– Spyder.
 • Pandas
 • Numpy
 • Matplotlib
 • Seaborn.
 • Scikit-learn.
 • OpenCV(cv2).
 • Keras.



 
**HARDWARE REQUIREMENTS:**
 • CPU:Intel Core i3 or more.
 • Hard Disk : 1000 GB.
 • RAM:4GBor8GB.
 • Storage : 512GB or more.
 • GPU-Intel.




**STEPS FOR PROJECT EXECUTION:** 

**EXECUTING PYTHON SCRIPTS IN ANACONDA:**  
In Spyder, you typically execute Python scripts directly within the integrated development 
environment (IDE).  
1. Open Spyder: Launch Spyder from Anaconda Navigator or your applications menu.  
2. Create or Open a Script: Create a new Python script by clicking on "File" > "New 
File" > "Python Script" in Spyder. Alternatively, open an existing Python script by 
clicking on "File" > "Open..." and selecting the script file.  
3. Write Your Code: Write your Python code in the script editor. Execute Code: To 
execute a single line of code, place the cursor on the line and press Ctrl + Enter. To 
execute the entire script, click on the green play button ("Run file") in the toolbar, or 
press F5. Alternatively, you can execute selected code by highlighting it and pressing 
Ctrl + Enter.


**EXECUTING STREAMLIT CODE IN ANACONDA:** 
To execute a Python script that contains Streamlit code using Anaconda Prompt, you can do 
so by following these steps: 
1. Open Anaconda Prompt: Open Anaconda Prompt from your applications menu or by 
searching for it on your system.  
2. Navigate to the Directory: Use the cd command to navigate to the directory where 
your Python script is located. 
3. Activate Environment: If you're using a specific conda environment, activate it using 
the conda activate command. 
4. Execute the Streamlit Script: Once you're in the correct directory, you can execute the 
Streamlit script using the streamlit run command. 
streamlit run file.py. 
73 
5. Access the Streamlit App: After executing the command, Streamlit will start a local 
server, and you'll see a message indicating the URL where you can access your 
Streamlit app (typically http://localhost:8501). Open a web browser and navigate to this 
URL to view and interact with your Streamlit app.


**EXECUTING CODE IN GOOGLE COLLAB:** 
Steps for executing code in Google Collaboratory: 
1. Upload Your File to Google Colab:  
 Open the Google Colab notebook where you want to execute the code.  
 Click on the "Files" tab on the left sidebar.  
 Click on the "Upload" button and select the file (e.g., file.py) from your local 
system.  
2. Mount Google Drive:  
 If your file is located in your Google Drive, you'll need to mount your 
Google Drive to access it.  
 Run the following code cell and follow the authentication steps: 
from google.colab import drive 
drive.mount('/content/drive') 
3. Execute Code:  
 To execute a code cell, click on the play button (triangle icon) on the left side 
of the cell, or press Shift + Enter.  
 The code will be executed, and the output (if any) will be displayed below 
the cell.  
 You can execute code cells sequentially or in any order you prefer.
