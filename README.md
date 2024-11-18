# AI Enhanced Engagement Tracker 📚

## Overview :🚀

AI Enhanced Engagement Tracker is an intelligent system designed to monitor and analyze user engagement levels in real-time. By leveraging AI and data analytics, it provides actionable insights to enhance productivity and interaction. This tool is ideal for educators, marketers, and workplace managers seeking to optimize engagement strategies.<br />


## Project Structure 

**It Contains Four Parts**

- **Image Processing**
- **Video Processing**
- **Annotations**
- **Face Recognition**




#    Image Processing : 
**Image processing involves techniques for analyzing, enhancing, and transforming images to extract useful information or improve visual quality. This field encompasses tasks like noise reduction, image sharpening, segmentation, and object recognition. It's widely used in areas like medical imaging, computer vision, and multimedia applications.** <br />

## Libraries or Frame Works Used -
## opencv <br />
- **Version - 4.10.0.84**  <br />

## Developed Logics -<br />
  
  ### A. Image_Noise removal & Closing Gaps<br />
  
  - **Image Noise Removal:** The process of reducing random variations (noise) in an image to enhance clarity, often using filters.<br />

  ### Input & Output

  
  ![INPUT   Output  of noise removal closing gaps](https://github.com/user-attachments/assets/788d2b04-8fd6-49e0-b616-10a7817925c9)


  
  
  

  - **Closing Gaps:** A morphological operation that fills small holes or gaps in an image to create more continuous and solid regions, typically applied after edge detection.<br />

  ### Input  & Output:

   ![INPUT   Output  of noise removal closing gaps](https://github.com/user-attachments/assets/788d2b04-8fd6-49e0-b616-10a7817925c9)



  ### B. Image_Template image<br />
  
  - **Image Template:** A predefined pattern or sample image used in template matching to identify or locate specific features within a target image.<br />

  ### Input & Output:

  
  ![IMAGE TEMPLATE OUPUT](https://github.com/user-attachments/assets/1f6e3681-109d-4523-a685-6a396767d52c)

 

  ### C. Image_Colour image <br /> 
  
  - **Color Image:** An image composed of multiple color channels (typically red, green, and blue), allowing it to display a wide spectrum of colors.<br />

  ### Input & Output::

  ![OUTPUT OF IMAGE](https://github.com/user-attachments/assets/2a1ab42d-e187-4ba8-970e-bb91e09558f0)


  ### D. Image_Concatenation image <br />
  
  - **Image Concatenation:** The process of joining multiple images side-by-side or on top of each other to create a single combined image.<br />

  ### Input & Output:

  ![INPUT   OUTPUT OF HORIZONTAL CONCATENATION](https://github.com/user-attachments/assets/d0a5e400-91ef-4d4f-a057-875fdc0238da)

  
  
  ![Input   output for vertical concatenation](https://github.com/user-attachments/assets/d26b8d43-dc27-4fc7-88b5-c952c1c68d3c)



  
  ### E. Image_Contour image<br />
  
  - **Image Contour:** The outline or boundary of objects within an image, detected to identify shapes and regions based on differences in color or intensity.<br />

  ### Input & Output:

  ![INPUT   OUPUT CONTOUR IMAGE](https://github.com/user-attachments/assets/667b15fa-3638-4fd5-90b2-34cfbd389426)
  

  ### F. Image_Crop image<br />
  
  - **Image Crop:** The process of trimming or cutting out a specific portion of an image to focus on a particular area or remove unwanted sections.<br />

  ### Input & Output:

  
  ![INPUT   OUTPUT  IMAGE CROP](https://github.com/user-attachments/assets/47b7bea4-490e-435d-86e6-b151a3e753c8)
  

  
  ### G. Image_Detect and erosion image<br />
  
  - **Image Detection and Erosion:** Image detection identifies specific features or objects, while erosion is a morphological operation that reduces boundaries in binary images, removing small noise and refining 
   edges.<br />

   ### Input & Output:

   
   ![OUTPUT  OF DIALTED   ERODED IMAGE](https://github.com/user-attachments/assets/56a68c89-2f5f-4605-8a8c-67ed6a554cc9)


   
  ### H. Image_edge detect image<br /> 
  
  - **Image Edge Detection:** A technique used to identify and highlight the boundaries or edges within an image, helping to outline shapes and detect object contours.<br />

  ### Input & Output:

  
  ![INPUT   OUTPUT EDGE DETECT](https://github.com/user-attachments/assets/934135d9-adb6-489e-83a8-c2fe805ad8dc)
  


  ### I. Image_euqalized image<br />
  
  - **Image Equalization:** The process of adjusting the intensity distribution in an image to enhance contrast, making details more visible across different lighting conditions.<br />

  ### Input & Output:

  ![INPUT   OUTPUT EQUALIZED IMAGE](https://github.com/user-attachments/assets/f6c67d8c-1a2a-4ddc-aabc-293a3c47bbd5)
  

  ### J. Image_hsv image<br />
  
  - **Image HSV:** An image representation in the Hue, Saturation, and Value color space, which separates color information (hue) from intensity (value), offering a more intuitive way to manipulate colors.<br />

  ### Input & Output:

  
  ![INPUT   OUTPUT HSV](https://github.com/user-attachments/assets/cbacaf1b-0e3a-4599-82ca-9329dfb00a43)
  


  ### K. Image_morph image<br />
  
  - **Image Morphing:** A technique that transforms one image into another by gradually changing its features, often used in animation or to blend shapes and textures.<br />

  ### Input & Output:

  
  ![INPUT   OUTPUT MORPH IMAGE](https://github.com/user-attachments/assets/4a5b0559-c08e-464a-99e6-321353aea78b)



  ### L. Image_resize image<br />
  
  - **Image Resize:** The process of changing the dimensions of an image by scaling it up or down while maintaining or altering its aspect ratio.<br />

  ### Input & Output:

  ![INPUT   output image resize](https://github.com/user-attachments/assets/8b72a4b2-f9f5-45e6-b59c-23871b86793f)


  ### M. Image_rgb to grey image<br />
  
  - **Image RGB to Grey:** The process of converting a colored image (RGB) to grayscale by averaging or weighted summing the red, green, and blue channels to produce a single intensity value.<br />

  ### Input & Output:

  ![INPUT   output RGB to Grey image](https://github.com/user-attachments/assets/372d1325-3f6a-4eb7-b140-a1d41f5f0592)
  

  ### N. Image_single image <br />
  
  - **Single Image:** An individual visual representation captured or created in digital form, typically consisting of pixels arranged in a grid.<br />

  ### Input & Output:

  ![INPUT   output Single Image](https://github.com/user-attachments/assets/530bb4a8-c9eb-47e4-a51b-2740544dd9fc)
  

  ### O. Image_blur image<br />
  
  - **Image Blur:** The process of smoothing an image by reducing sharp edges and details, often using filters like Gaussian blur to create a softer appearance.<br />

  ### Input & Output:

  ![INPUT   Output Blur Image](https://github.com/user-attachments/assets/9d4568a6-d57d-44d7-a7fa-d574a5ee1e71)

  ### P. Image_Rotated<br />

  
  - **Image_Rotated:** typically refers to an image that has been turned at an angle from its original orientation, either clockwise or counterclockwise. This transformation is often used for adjusting or 
  aligning visuals to the desired viewpoint, especially when images are unintentionally tilted during capture. Rotation can be applied easily through image editing software, making it a common and 
  straightforward adjustment in digital imaging.<br />

   ### Input & Output:

   ![INPUT   output of rotated image](https://github.com/user-attachments/assets/e31d0b25-b5d4-46cd-82d7-6e00e0971bcd)




   #  Video Processing
   
   **Video processing involves manipulating and analyzing video data to improve quality, extract information, or enable specific functions like motion detection and object tracking. Techniques include frame-by- 
     frame enhancement, compression, and filtering for smooth playback or real-time processing. It’s crucial in fields like surveillance, streaming, and augmented reality.** <br />

## Libraries or Frame Works Used - 
## Opencv <br />
-**Version - 4.10.0.84** <br /> 

## Developed Logics - <br />

### A. Video_multivid<br />

-**Multi-Video:** The simultaneous display or processing of multiple video streams, often combined into a single output for comparison, editing, or analysis.<br />

### Input: 

### Output: 


### B. Video_fps<br />

-**Video FPS (Frames Per Second):** The number of individual frames displayed per second in a video, determining its smoothness and motion quality.<br />

### Input & Output:




https://github.com/user-attachments/assets/3698f3f6-5e9d-4bb0-ac3f-ff888fef85ce





### C. Video_save<br />

-**Video Save:** The process of storing a video file in a specified format and location on a storage device for future access or playback.<br />

### Input & Output:

 
![INPUT (1)](https://github.com/user-attachments/assets/328168cb-68fe-4970-aa13-d786a8b2fac0)





### D. Video_stackingh<br />

-**Video Stacking Horizontal:** The process of arranging multiple video clips side-by-side in a single frame, creating a horizontal sequence for comparison or simultaneous viewing.<br />

### Input & Output:
 


![INPUT (3)](https://github.com/user-attachments/assets/4e49b32b-8572-4815-b190-ec4d81796d4c)





### E. Video_stackingv<br />

- **Video Stacking Vertical:** The process of arranging multiple video clips one above the other in a single frame, creating a vertical sequence for comparison or simultaneous viewing.<br />

### Input & Output:


![INPUT (2)](https://github.com/user-attachments/assets/84cd2a82-f1ac-457a-8509-c4952d80e66a)




### F. Video_stream<br />

- **Video Stream:** The continuous transmission of video data over the internet or a network, allowing real-time playback without needing to download the entire file.<br />

### Input & Output:



![INPUT](https://github.com/user-attachments/assets/f1eb8340-cff1-4a77-8769-202aa95e004a)






 
  #  ANNOTATIONS
  **Annotations are additional labels or notes added to data, such as images or text, to provide context or highlight specific details. In machine learning, annotations are essential for supervised learning, 
    where labeled data helps train models for tasks like object detection or sentiment analysis. They’re widely used in tasks like image tagging, document markup, and speech recognition to improve model 
    accuracy.** <br />
## Libraries or Frame Works Used - 

### 1.opencv <br />
- Version - 4.10.0.84 
### 2.labelimg <br />
- Version of labelImg - 1.8.6 <br />

## Developed Logics -<br />

### A.data_segregate<br />

**Image and Label Segregation Script**
This script organizes images based on their corresponding label files. It segregates matched image-label pairs into a `matched` directory and places unmatched images into an `unmatched` directory. The script supports custom file extensions and automatically creates directories if they don’t exist.<br /> 

### B.label<br />

**Bounding Box Drawer for Images**
This script reads images and their corresponding label files, draws bounding boxes around detected objects based on label coordinates, and saves the annotated images to an output directory. It handles label files in YOLO format, allowing for customization of file extensions and output location.



![gun](https://github.com/user-attachments/assets/51df31c0-7813-4599-b40b-53f3c82a5a39)


### C. label_manipulate<br />

**Class Number Updater for Label Files**
This script updates class IDs in label files, replacing a specified old class ID with a new class ID. It reads each label file, modifies the class ID as needed, and saves the changes back to the file, handling any malformed entries gracefully. This tool is useful for batch updating class labels in YOLO-format datasets.

### D. label_Image.txt<br />
 
![Screenshot 2024-11-15 142323](https://github.com/user-attachments/assets/847633f0-1c88-45cf-a189-321932207a3f)



# Face_Recognition 
- Face recognition is a biometric technology that identifies or verifies individuals by analyzing facial features in images or video. It involves detecting a face, extracting unique features, and comparing them 
  to a database for authentication or identification. Commonly used in security, smartphones, and social media, face recognition has applications in access control and personalized experiences. <br />
 
  ## Libraries or Frame Works Used - opencv, labelimg <br />
  
  ## 1.opencv-python :
  - Version== 4.10.0.84 <br />

  **OpenCV (Open Source Computer Vision) is a popular library in Python for real-time computer vision applications. It provides tools for image processing, object detection, and facial recognition, and is widely 
    used in AI, robotics, and automation.** <br />
  
  ## 2.face_recognition : 
  - Version == 1.3.0 <br /> 
  
  **Face recognition is a biometric technique that identifies or verifies individuals by analyzing facial features from images or video. It uses algorithms to map facial landmarks and match 
  them to stored images. Common applications include security systems, identity verification, and social media tagging.** <br />
 
  ## 3.dlib :
  - Version == 19.24.6 <br />

  **Dlib is a machine learning library that includes tools for facial recognition, image processing, and more. It’s known for its robust facial landmark detector and is widely used in applications requiring face 
    detection and alignment.** <br />
  
  ## 4.pandas : 
  - Version ==  2.2.3 <br />

  **Pandas is a data manipulation library in Python, commonly used for data analysis and manipulation of structured data. It provides DataFrame and Series objects, which make it easy to clean, explore, and 
    transform data for various analytics tasks.** <br />
  
  ## 5.numpy :
  - Version == 2.1.2 <br />

   **NumPy is a powerful Python library for numerical computing, providing support for large, multidimensional arrays and matrices. It enables efficient mathematical operations and forms the foundation for many 
     data science and machine learning libraries.** <br />
  
  ## 6.datetime :
  - Version == 5.5 <br />

  **The Date and Time modules in Python allow for handling date and time data, enabling tasks like timestamping, scheduling, and time zone conversions. These are essential in data logging, event tracking, and 
  time- based analysis.**  <br />
  
  ## 7.imutils :
  - Version == 0.5.4 <br />

  **Imutils is a Python library that simplifies image processing tasks using OpenCV, like resizing, rotating, and cropping images. It provides convenience functions that make it easier to implement standard 
    image transformations and manipulations.** <br />
 
 
 #    Developed Logics -__ 

#    Face Recognition - Barak Obama
  
  ### 1.attendence<br />
  
  **This project uses Python, OpenCV, and `face_recognition` to identify Barack Obama in a live video feed or video file. Recognized instances are marked in real time, and details (name, date, and time) are 
     logged in an Excel file after every five successful recognitions. The application displays results in a video window and saves the log automatically.** <br /> 

  ### Input & Output: 
  
  ![INPUT (1)](https://github.com/user-attachments/assets/bea03792-5a6e-49fd-9f60-579ed8d568d3)


  
  ### 2. Face_Recog<br />

  **This project uses Python, OpenCV, and `face_recognition` to detect and identify Barack Obama in a live video feed or video file. If the face matches the known image, it is labeled with "Barack Obama"; 
  otherwise, it displays "Not Barack Obama." The application runs in real time and displays the results in a video window.** <br />

  ### Input & Output: 

  ![FACE_RECOGNITION](https://github.com/user-attachments/assets/9dae315a-91b2-4d94-85a6-53367b871900)

  
  ### 3. Test 1<br />

  **This script performs real-time face recognition using OpenCV and `face_recognition` on a video feed. It detects faces, compares them to a known image of Barack Obama, and logs the recognition date and time 
    in a DataFrame. If recognized, it annotates the video feed with labels, periodically saving the data to an Excel file.** <br />

  ### Input & Output: 


  ![TEST](https://github.com/user-attachments/assets/fdca12bd-d2d6-44d5-884e-034f2413f927)
  

  ### 4. Tools<br /> 

  **This Python script uses OpenCV and `face_recognition` to perform face recognition on a video feed, identifying a known image of Barack Obama. It tracks and annotates recognized faces in real time, logging 
   the recognition time and date to an Excel file once a threshold of five recognitions is met. Users can end the video stream by pressing "q," and a final log save occurs upon exit.** <br /> 

  ### Input & Output: 

  
  ![TOOLS](https://github.com/user-attachments/assets/d7adaa6f-e5a7-4445-8b00-e44a84b8ab79)
  

  ### 5. excel_sc<br />

  **This Python script performs real-time face recognition using OpenCV and `face_recognition`, comparing detected faces in a video feed to a known image of Barack Obama. It logs recognized faces with timestamps 
    and saves screenshots for each recognition at regular intervals, outputting all data to an Excel file with paths to the saved images. The program ends and saves the data upon pressing "q" or if the video 
    feed ends.** <br />

  ### Input & Output: 

  
  ![EXCEL_SC](https://github.com/user-attachments/assets/02a1e0ed-3649-4574-a43e-11e55dab8950)


  

  
  ### 6. excel_sc_dt<br />

  **This Python script captures real-time face recognition using OpenCV and `face_recognition` to identify Barack Obama in a video feed, logging each recognition with timestamps and saving annotated screenshots. 
    Recognitions are recorded every two minutes, and a new log entry with a screenshot is created every five minutes. The data, including screenshot paths, is saved to an Excel file upon program exit or by 
    pressing "q."** <br />

  ### Input & Output: 
  

  ![INPUT (1)](https://github.com/user-attachments/assets/8be9d4ee-4e38-44ad-b05a-2ae4b3a343d1)


  

  ### 7. attention_score<br />

  **This Python script performs real-time face recognition and attentiveness analysis on a video feed, identifying Barack Obama and calculating an attentiveness score based on head pose (yaw and pitch). 
    Screenshots are captured and saved when the individual is attentive, with recognition events and attention scores logged in an Excel file. The application uses OpenCV, `face_recognition`, and dlib for 
    facial detection and landmark analysis.** <br />

  ### Input & Output: 

  ![ATTENTION_SCORE](https://github.com/user-attachments/assets/41bc042d-f3eb-499d-ab23-e0a550bbbf35)

  
 
  ### 8. avg_attention_score<br />

  **This Python script performs real-time face recognition and attentiveness analysis on a video feed, identifying Barack Obama and calculating an attentiveness score based on head pose (yaw and pitch). 
    Screenshots are captured when the individual is attentive, and recognition events, along with attention scores, are logged in an Excel file. The script also calculates and appends the average attentiveness 
    score at the end of the session.** <br />


  ###  Input & Output: 

  ![AVG_ATTENTION_SCORE](https://github.com/user-attachments/assets/2c861354-28a4-4a8b-834e-704a258454b8)


  ### 9. landmark<br />

  **This Python script performs real-time face recognition and attentiveness detection, identifying a known face (Barack Obama) and assessing attentiveness based on head pose (yaw and pitch). If the individual 
    is deemed attentive, a screenshot is captured, and the recognition event is logged in an Excel file. The script also highlights the face with a rectangle and displays an attentiveness status (Attentive/Not 
    Attentive) on the video stream.** <br />

  ### Input & Output: 

  ![INPUT 7 OUTPUT LANDMARK](https://github.com/user-attachments/assets/39666d68-6ecf-4bea-a790-1d613b807a50)


#    Face Recognition - SHIVA GOUD
  
  ### 1. Shiva_attendence_save<br />

**It is an automated attendance management system that simplifies tracking and monitoring attendance records. Built using Python and integrated with facial recognition technology, it ensures 
    accurate and efficient attendance logging. Ideal for educational institutions and workplaces, this project demonstrates advanced AI implementation in day-to-day applications.** <br />
  
  ### Input & Output : 

  ![SHIVA ATTENDENCE](https://github.com/user-attachments/assets/8c332ebc-b418-43f9-8bad-c8eff6645e03)


  ### 2. Shiva_face_recognition<br />
  **It is a Python-based project leveraging advanced machine learning and computer vision techniques for accurate face detection and recognition. It supports real-time recognition, making it 
     suitable for security systems and identity verification. This project showcases the implementation of deep learning models in practical applications.** <br />

  ### Input & Output: 

  
  ![SHIVA FACE RECOGNITION](https://github.com/user-attachments/assets/5c3f7698-bf5d-4ec2-b757-177e190aa7ff)
   

  ### 3. Shiva_test<br />
  
  **It is a Python-based project designed to automate testing processes, ensuring efficiency and reliability. It includes features for creating, managing, and executing test cases with detailed result 
     reporting. This project highlights the integration of automation in quality assurance workflows.** <br />

  ### Input & Output: 

  
  ![SHIVA TEST](https://github.com/user-attachments/assets/2a906a2a-8c6b-4d3e-bd67-7fbde89bb77d)
  

  ### 4. Shiva_tools<br />
  **It is a collection of versatile Python utilities designed to simplify everyday programming tasks. From data processing to file management, this toolkit offers solutions for various development 
    needs. It is a must-have for developers looking to boost productivity and efficiency.** <br />
  
  ### Input & Output: 

  ![SHIVA TOOLS](https://github.com/user-attachments/assets/582bce18-ef05-4c26-9377-e1d37f12d6f0)

  
  ### 5. Shiva_excel_sc<br />

  ### Input & Output:  

  ![SHIVA EXCEL SC](https://github.com/user-attachments/assets/992552b8-da7a-42d7-ba02-8333792277ca)

  
  ### 6. Shiva_excel_sc_dt<br />

  ### Input & Output: 

  ![SHIVA EXCEL SC DATE](https://github.com/user-attachments/assets/4022db7d-4f61-449a-801e-fa3164962000)

  
  ### 7. Shiva_attention_score<br />
  **Ite is a Python project designed to analyze and quantify attention levels in various contexts. It leverages data analytics and machine learning to provide insights into engagement and focus 
    metrics. This project is ideal for applications in education, productivity tracking, and user behavior analysis.** <br />

  ### Input & Output: 

  ![SHIVA ATTENTION SCORE](https://github.com/user-attachments/assets/b9332c0f-8f6c-4fa3-8be7-fb0fdf5ec0ca)

  
  ### 8. Shiva_avg_attention_score<br />
  **It is a Python project that calculates and evaluates the average attention score from collected data. It streamlines the process of aggregating individual attention metrics to 
    provide actionable insights. This tool is valuable for educators, analysts, and researchers focused on engagement trends.** <br />

  ### Input & Output: 
   
   ![Shiva AVG ATTENTION SCORE](https://github.com/user-attachments/assets/f8a27285-b8ef-4cdb-a8c9-fa5a7e78c186)
   

  ### 9. Shiva_landmark<br />
  **It is a Python-based project that identifies and tracks facial landmarks using computer vision techniques. It enables precise mapping of key facial features, useful for applications like emotion 
    detection, animation, and facial recognition. This project showcases the integration of AI in advanced visual analytics.** <br />

  ### Input & Output:

  
  ![SHIVA LANDMARK](https://github.com/user-attachments/assets/4814a298-e150-4eb2-b89c-5342dee53089)




  
