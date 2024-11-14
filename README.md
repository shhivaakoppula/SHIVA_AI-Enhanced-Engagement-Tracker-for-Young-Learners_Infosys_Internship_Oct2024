#    Image Processing : 
**Image processing involves techniques for analyzing, enhancing, and transforming images to extract useful information or improve visual quality. This field encompasses tasks like noise reduction, image sharpening, segmentation, and object recognition. It's widely used in areas like medical imaging, computer vision, and multimedia applications.** <br />
## Libraries or Frame Works Used - opencv <br />
## Version - 4.10.0.84  <br />
## Developed Logics -<br />
  ### A. Image_Noise removal & Closing Gaps<br />
  
  **Image Noise Removal:** The process of reducing random variations (noise) in an image to enhance clarity, often using filters.<br />

  ### Input & Output

  
  ![INPUT   Output  of noise removal closing gaps](https://github.com/user-attachments/assets/788d2b04-8fd6-49e0-b616-10a7817925c9)


  
  
  

  **Closing Gaps:** A morphological operation that fills small holes or gaps in an image to create more continuous and solid regions, typically applied after edge detection.<br />

  ### Input  & Output:

   ![INPUT   Output  of noise removal closing gaps](https://github.com/user-attachments/assets/788d2b04-8fd6-49e0-b616-10a7817925c9)



  ### B. Image_Template image<br />
  **Image Template:** A predefined pattern or sample image used in template matching to identify or locate specific features within a target image.<br />

  ### Input & Output:

  
  ![IMAGE TEMPLATE OUPUT](https://github.com/user-attachments/assets/1f6e3681-109d-4523-a685-6a396767d52c)

 

  ### C. Image_Colour image <br /> 
  **Color Image:** An image composed of multiple color channels (typically red, green, and blue), allowing it to display a wide spectrum of colors.<br />

  ### Input & Output::

  ![OUTPUT OF IMAGE](https://github.com/user-attachments/assets/2a1ab42d-e187-4ba8-970e-bb91e09558f0)


  ### D. Image_Concatenation image <br />
  
  **Image Concatenation:** The process of joining multiple images side-by-side or on top of each other to create a single combined image.<br />

  ### Input & Output:

  ![INPUT   OUTPUT OF HORIZONTAL CONCATENATION](https://github.com/user-attachments/assets/d0a5e400-91ef-4d4f-a057-875fdc0238da)

  
  
  ![Input   output for vertical concatenation](https://github.com/user-attachments/assets/d26b8d43-dc27-4fc7-88b5-c952c1c68d3c)



  
  ### E. Image_Contour image<br />
  
  **Image Contour:** The outline or boundary of objects within an image, detected to identify shapes and regions based on differences in color or intensity.<br />

  ### Input & Output:

  ![INPUT   OUPUT CONTOUR IMAGE](https://github.com/user-attachments/assets/667b15fa-3638-4fd5-90b2-34cfbd389426)
  

  ### F. Image_Crop image<br />
  
  **Image Crop:** The process of trimming or cutting out a specific portion of an image to focus on a particular area or remove unwanted sections.<br />

  ### Input & Output:

  
  ![INPUT   OUTPUT  IMAGE CROP](https://github.com/user-attachments/assets/47b7bea4-490e-435d-86e6-b151a3e753c8)
  

  
  ### G. Image_Detect and erosion image<br />
  
  **Image Detection and Erosion:** Image detection identifies specific features or objects, while erosion is a morphological operation that reduces boundaries in binary images, removing small noise and refining 
   edges.<br />

   ### Input & Output:

   
   ![OUTPUT  OF DIALTED   ERODED IMAGE](https://github.com/user-attachments/assets/56a68c89-2f5f-4605-8a8c-67ed6a554cc9)


   
  ### H. Image_edge detect image<br /> 
  **Image Edge Detection:** A technique used to identify and highlight the boundaries or edges within an image, helping to outline shapes and detect object contours.<br />

  ### Input & Output:

  
  ![INPUT   OUTPUT EDGE DETECT](https://github.com/user-attachments/assets/934135d9-adb6-489e-83a8-c2fe805ad8dc)
  


  ### I. Image_euqalized image<br />
  **Image Equalization:** The process of adjusting the intensity distribution in an image to enhance contrast, making details more visible across different lighting conditions.<br />

  ### Input & Output:

  ![INPUT   OUTPUT EQUALIZED IMAGE](https://github.com/user-attachments/assets/f6c67d8c-1a2a-4ddc-aabc-293a3c47bbd5)
  

  ### J. Image_hsv image<br />
  
  **Image HSV:** An image representation in the Hue, Saturation, and Value color space, which separates color information (hue) from intensity (value), offering a more intuitive way to manipulate colors.<br />

  ### Input & Output:

  
  ![INPUT   OUTPUT HSV](https://github.com/user-attachments/assets/cbacaf1b-0e3a-4599-82ca-9329dfb00a43)
  


  ### K. Image_morph image<br />
  
  **Image Morphing:** A technique that transforms one image into another by gradually changing its features, often used in animation or to blend shapes and textures.<br />

  ### Input & Output:

  
  ![INPUT   OUTPUT MORPH IMAGE](https://github.com/user-attachments/assets/4a5b0559-c08e-464a-99e6-321353aea78b)



  ### L. Image_resize image<br />
  
  **Image Resize:** The process of changing the dimensions of an image by scaling it up or down while maintaining or altering its aspect ratio.<br />

  ### Input & Output:

  ![INPUT   output image resize](https://github.com/user-attachments/assets/8b72a4b2-f9f5-45e6-b59c-23871b86793f)


  ### M. Image_rgb to grey image<br />
  **Image RGB to Grey:** The process of converting a colored image (RGB) to grayscale by averaging or weighted summing the red, green, and blue channels to produce a single intensity value.<br />

  ### Input & Output:

  ![INPUT   output RGB to Grey image](https://github.com/user-attachments/assets/372d1325-3f6a-4eb7-b140-a1d41f5f0592)
  

  ### N. Image_single image <br />
  **Single Image:** An individual visual representation captured or created in digital form, typically consisting of pixels arranged in a grid.<br />

  ### Input & Output:

  ![INPUT   output Single Image](https://github.com/user-attachments/assets/530bb4a8-c9eb-47e4-a51b-2740544dd9fc)
  

  ### O. Image_blur image<br />
  **Image Blur:** The process of smoothing an image by reducing sharp edges and details, often using filters like Gaussian blur to create a softer appearance.<br />

  ### Input & Output:

  ![INPUT   Output Blur Image](https://github.com/user-attachments/assets/9d4568a6-d57d-44d7-a7fa-d574a5ee1e71)

  ### P. Image_Rotated<br />

  **Image_Rotated:** typically refers to an image that has been turned at an angle from its original orientation, either clockwise or counterclockwise. This transformation is often used for adjusting or aligning 
  visuals to the desired viewpoint, especially when images are unintentionally tilted during capture. Rotation can be applied easily through image editing software, making it a common and straightforward 
  adjustment in digital imaging.<br />

   ### Input & Output:

   ![INPUT   output of rotated image](https://github.com/user-attachments/assets/e31d0b25-b5d4-46cd-82d7-6e00e0971bcd)




   #  Video Processing
   **Video processing involves manipulating and analyzing video data to improve quality, extract information, or enable specific functions like motion detection and object tracking. Techniques include frame-by- 
     frame enhancement, compression, and filtering for smooth playback or real-time processing. It’s crucial in fields like surveillance, streaming, and augmented reality.** <br />
## Libraries or Frame Works Used - opencv <br />
## Version - 4.10.0.84 <br /> 
## Developed Logics - <br />

### A. Video_multivid<br />

**Multi-Video:** The simultaneous display or processing of multiple video streams, often combined into a single output for comparison, editing, or analysis.<br />

### Input: 

### Output: 


### B. Video_fps<br />

**Video FPS (Frames Per Second):** The number of individual frames displayed per second in a video, determining its smoothness and motion quality.<br />

### Input: Webcam 

![Input Video Processing for fps](https://github.com/user-attachments/assets/28c36f69-3dc1-4ed5-91e5-cb058694617f)

### Output:

![Screenshot 2024-11-13 192000](https://github.com/user-attachments/assets/e439ebb0-fe2e-4ad5-aa9f-66a1f0b718e3)


### C. Video_save<br />

**Video Save:** The process of storing a video file in a specified format and location on a storage device for future access or playback.<br />

### Input:  Webcam  

 ![Input for video processing](https://github.com/user-attachments/assets/d50094c1-e987-49df-adc7-be8369fe424a)

### Output:

![Screenshot 2024-11-13 192000](https://github.com/user-attachments/assets/e439ebb0-fe2e-4ad5-aa9f-66a1f0b718e3)


### D. Video_stackingh<br />

**Video Stacking Horizontal:** The process of arranging multiple video clips side-by-side in a single frame, creating a horizontal sequence for comparison or simultaneous viewing.<br />

### Input:  Webcam  

![Input for video processing](https://github.com/user-attachments/assets/bf6ee5bc-bc2d-4f02-b5ff-177754372ff5)

### Output:

![Screenshot 2024-11-13 192000](https://github.com/user-attachments/assets/e439ebb0-fe2e-4ad5-aa9f-66a1f0b718e3)


### E. Video_stackingv<br />

**Video Stacking Vertical:** The process of arranging multiple video clips one above the other in a single frame, creating a vertical sequence for comparison or simultaneous viewing.<br />

### Input:  Webcam 

![Input for video processing](https://github.com/user-attachments/assets/3c08d93e-59c1-46ab-a50c-ff88cd5e25bd)

### Output:

![Screenshot 2024-11-13 192000](https://github.com/user-attachments/assets/e439ebb0-fe2e-4ad5-aa9f-66a1f0b718e3)


### F. Video_stream<br />
**Video Stream:** The continuous transmission of video data over the internet or a network, allowing real-time playback without needing to download the entire file.<br />

### Input:  Webcam   

![Input for video processing](https://github.com/user-attachments/assets/4a99296a-b41e-45d5-a4ee-aeb5c789af87)

### Output:

![Screenshot 2024-11-13 192000](https://github.com/user-attachments/assets/e439ebb0-fe2e-4ad5-aa9f-66a1f0b718e3)




 
  #  ANNOTATIONS
  **Annotations are additional labels or notes added to data, such as images or text, to provide context or highlight specific details. In machine learning, annotations are essential for supervised learning, 
    where labeled data helps train models for tasks like object detection or sentiment analysis. They’re widely used in tasks like image tagging, document markup, and speech recognition to improve model 
    accuracy.** <br />
## Libraries or Frame Works Used - opencv, labelimg <br />
## Version - 4.10.0.84 , version of labelImg - 1.8.6<br />
## Developed Logics -<br />

### A.data_segregate<br />

## Image and Label Segregation Script
This script organizes images based on their corresponding label files. It segregates matched image-label pairs into a `matched` directory and places unmatched images into an `unmatched` directory. The script supports custom file extensions and automatically creates directories if they don’t exist.<br />

  ### Input:
  ### Output: 

### B.label<br />

## Bounding Box Drawer for Images

This script reads images and their corresponding label files, draws bounding boxes around detected objects based on label coordinates, and saves the annotated images to an output directory. It handles label files in YOLO format, allowing for customization of file extensions and output location.

  ### Input: 
  ### Output: 

  ![gun](https://github.com/user-attachments/assets/51df31c0-7813-4599-b40b-53f3c82a5a39)


### C. label_manipulate<br />

## Class Number Updater for Label Files

This script updates class IDs in label files, replacing a specified old class ID with a new class ID. It reads each label file, modifies the class ID as needed, and saves the changes back to the file, handling any malformed entries gracefully. This tool is useful for batch updating class labels in YOLO-format datasets.

  ### Input: 
  ### Output: 

# Face_Recognition
**Face recognition is a biometric technology that identifies or verifies individuals by analyzing facial features in images or video. It involves detecting a face, extracting unique features, and comparing them 
  to a database for authentication or identification. Commonly used in security, smartphones, and social media, face recognition has applications in access control and personalized experiences.** <br />
 
  ## Libraries or Frame Works Used - opencv, labelimg <br />
  ## opencv-python == 4.10.0.84 <br />
  ## face_recognition == 1.3.0 <br /> 
  ## dlib == 19.24.6 <br />
  ## pandas ==  2.2.3 <br />
  ## numpy == 2.1.2 <br />
  ## datetime == 5.5 <br />
  ## imutils == 0.5.4 <br />
 #    Developed Logics -__ 
  
  ### A.attendence<br />
  **This project uses Python, OpenCV, and `face_recognition` to identify Barack Obama in a live video feed or video file. Recognized instances are marked in real time, and details (name, date, and time) are logged in an Excel file after every five successful recognitions. The application displays results in a video window and saves the log automatically.** <br /> 

  ### Input: Image of Barak Obama & Video
  
  ![Barak Obama](https://github.com/user-attachments/assets/a62c20bf-5d9d-4fc2-a16f-8db9f507e7c9)

  ### Output: 
  
  ![Screenshot 2024-11-13 221520](https://github.com/user-attachments/assets/9e7eebc6-0b86-4915-9e3c-ae54c43b5afd)

  
  ### B. Face_Recog<br />

  **This project uses Python, OpenCV, and `face_recognition` to detect and identify Barack Obama in a live video feed or video file. If the face matches the known image, it is labeled with "Barack Obama"; 
  otherwise, it displays "Not Barack Obama." The application runs in real time and displays the results in a video window.** <br />

  ### Input: Image of Barak Obama & Video

  ![Barak Obama](https://github.com/user-attachments/assets/a62c20bf-5d9d-4fc2-a16f-8db9f507e7c9)

  ### Output: 
  
  ### C. Test 1<br />

  **This script performs real-time face recognition using OpenCV and `face_recognition` on a video feed. It detects faces, compares them to a known image of Barack Obama, and logs the recognition date and time 
    in a DataFrame. If recognized, it annotates the video feed with labels, periodically saving the data to an Excel file.** <br />

  ### Input: Image of Barak Obama & Video

  ![Barak Obama](https://github.com/user-attachments/assets/a62c20bf-5d9d-4fc2-a16f-8db9f507e7c9)
  
  ### Output: 
  
  ### D. Tools<br /> 

  **This Python script uses OpenCV and `face_recognition` to perform face recognition on a video feed, identifying a known image of Barack Obama. It tracks and annotates recognized faces in real time, logging 
   the recognition time and date to an Excel file once a threshold of five recognitions is met. Users can end the video stream by pressing "q," and a final log save occurs upon exit.** <br /> 

  ### Input: Image of Barak Obama & Video
  
  ![Barak Obama](https://github.com/user-attachments/assets/a62c20bf-5d9d-4fc2-a16f-8db9f507e7c9)
  
  ### Output: 
  
  ### E. excel_sc<br />

  **This Python script performs real-time face recognition using OpenCV and `face_recognition`, comparing detected faces in a video feed to a known image of Barack Obama. It logs recognized faces with timestamps 
    and saves screenshots for each recognition at regular intervals, outputting all data to an Excel file with paths to the saved images. The program ends and saves the data upon pressing "q" or if the video 
    feed ends.** <br />

  ### Input: Image of Barak Obama & Video

  ![Barak Obama](https://github.com/user-attachments/assets/a62c20bf-5d9d-4fc2-a16f-8db9f507e7c9)
  
  ### Output: 

  ![Barack_Obama_2024-11-01_17-40-57](https://github.com/user-attachments/assets/e5a95ec2-b43a-4fd0-a80f-7f6a5f72a080)

  
  ![Screenshot 2024-11-13 223406](https://github.com/user-attachments/assets/80b26e02-f0dc-4a41-8860-112a1a8aa438)


  
  ### F. excel_sc_dt<br />

  **This Python script captures real-time face recognition using OpenCV and `face_recognition` to identify Barack Obama in a video feed, logging each recognition with timestamps and saving annotated screenshots. 
    Recognitions are recorded every two minutes, and a new log entry with a screenshot is created every five minutes. The data, including screenshot paths, is saved to an Excel file upon program exit or by 
    pressing "q."** <br />

  ### Input: Image of Barak Obama & Video

  ![Barak Obama](https://github.com/user-attachments/assets/a62c20bf-5d9d-4fc2-a16f-8db9f507e7c9)
  
  ### Output: 
  
  ![Barack_Obama_2024-11-01_18-16-03](https://github.com/user-attachments/assets/56410d62-d9d5-4d90-9f49-13b3ed03651e)

  
  ![Screenshot 2024-11-13 223253](https://github.com/user-attachments/assets/3f072c93-1bdf-4c28-82aa-bdd48fe8386a)


  
  ### G. attention_score<br />

  **This Python script performs real-time face recognition and attentiveness analysis on a video feed, identifying Barack Obama and calculating an attentiveness score based on head pose (yaw and pitch). 
    Screenshots are captured and saved when the individual is attentive, with recognition events and attention scores logged in an Excel file. The application uses OpenCV, `face_recognition`, and dlib for 
    facial detection and landmark analysis.** <br />

  ### Input: Image of Barak Obama & Video
  
  ![Barak Obama](https://github.com/user-attachments/assets/a62c20bf-5d9d-4fc2-a16f-8db9f507e7c9)
  
  ### Output: 
  
  ![Screenshot 2024-11-13 223041](https://github.com/user-attachments/assets/ddaea8f4-0b8c-44c8-b896-f0c58d4dac92)

  
  ![Barack Obama_2024-11-06_17-05-00](https://github.com/user-attachments/assets/c7ce1a24-43d1-4c9e-82d6-a67f42d39796)


  ### H. avg_attention_score<br />

  **This Python script performs real-time face recognition and attentiveness analysis on a video feed, identifying Barack Obama and calculating an attentiveness score based on head pose (yaw and pitch). 
    Screenshots are captured when the individual is attentive, and recognition events, along with attention scores, are logged in an Excel file. The script also calculates and appends the average attentiveness 
    score at the end of the session.** <br />


  ### Input: Image of Barak Obama & Video

  ![Barak Obama](https://github.com/user-attachments/assets/a62c20bf-5d9d-4fc2-a16f-8db9f507e7c9)
  
  ### Output: 
  
  ![Barack Obama_2024-11-06_17-13-08](https://github.com/user-attachments/assets/4d0d6230-96fc-4c9e-bde2-8cd7f2c37354)

  
  ![Screenshot 2024-11-13 222947](https://github.com/user-attachments/assets/2dfdbb18-c8e0-493d-b7f6-8f815a50b193)


  ### I. landmark<br />

  **This Python script performs real-time face recognition and attentiveness detection, identifying a known face (Barack Obama) and assessing attentiveness based on head pose (yaw and pitch). If the individual 
    is deemed attentive, a screenshot is captured, and the recognition event is logged in an Excel file. The script also highlights the face with a rectangle and displays an attentiveness status (Attentive/Not 
    Attentive) on the video stream.** <br />

  ### Input: Image of Barak Obama & Video

  ![Barak Obama](https://github.com/user-attachments/assets/a62c20bf-5d9d-4fc2-a16f-8db9f507e7c9)
  
  ### Output:
  
  ![Screenshot 2024-11-13 222617](https://github.com/user-attachments/assets/af59998c-d478-44f9-bb85-b9b69b6f7cd7)

  ![Barack Obama_2024-11-06_16-51-53](https://github.com/user-attachments/assets/26e25494-aefa-45b2-8972-0ab91a40ef37)


  ### J. Shiva_attendence_save<br />
  
  ### Input: Image of Shiva & live video through webcam
  ### Output: 

  ### K. Shiva_face_recognition<br /> 

  ### Input: Image of Shiva & live video through webcam
  ### Output: 

  ### L. Shiva_test<br />

  ### Input: Image of Shiva & live video through webcam
  ### Output: 
  
  ### M. Shiva_tools<br />
  
  ### Input: Image of Shiva & live video through webcam
  ### Output: 

  ### N. Shiva_excel_sc<br />

  ### Input: Image of Shiva & live video through webcam
  ### Output: 
  
  ### O. Shiva_excel_sc_dt<br />

  ### Input: Image of Shiva & live video through webcam
  ### Output: 
  
  ### P. Shiva_attention_score<br />

  ### Input: Image of Shiva & live video through webcam
  ### Output:
  
  ### Q. Shiva_avg_attention_score<br />

  ### Input: Image of Shiva & live video through webcam
  ### Output: 
  
  



  
