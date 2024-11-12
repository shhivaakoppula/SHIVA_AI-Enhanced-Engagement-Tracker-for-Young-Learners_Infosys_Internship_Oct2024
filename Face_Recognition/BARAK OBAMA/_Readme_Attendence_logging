
#  Real-Time Face Recognition and Attendance Logging

This project performs real-time face recognition using a known face (Barack Obama) from a preloaded image, with results logged to an Excel file each time a recognition is made. The program processes a video input, detecting faces and matching them against a known face encoding using the `face_recognition` library. Once a face is recognized five times, the recognition information is saved to an Excel file.

## Requirements

Before running the code, ensure you have the following dependencies installed:

```bash
pip install opencv-python face-recognition pandas openpyxl
```

**Additional Requirements:**
 `opencv-python`: Used for video capture and displaying the video stream.
- `face-recognition`: Performs face detection and encoding comparisons.
- `pandas`: Handles the data storage and export to Excel.
- `openpyxl`: Enables saving the DataFrame to an Excel file.

## File Structure

 `main.py`: The main script for face recognition and attendance logging.
 `Barak Obama.jpg`: Image file of Barack Obama used as the reference for face recognition.
 `1000097197.mp4`: Video file used as the source for face recognition. You can substitute with any compatible video file.
 `attendance.xlsx`: Excel file generated as output, containing timestamps for recognized instances.

## How It Works

1. **Load the Known Face**: 
   The program loads a reference image of Barack Obama and generates face encodings from it to use as a match during recognition.

2. **Live Video Feed**:
    It opens a video file (`1000097197.mp4` in this case) and processes each frame.
    Every 2nd frame is analyzed for face recognition to reduce processing time.

3. **Face Detection and Recognition**:
   - For each detected face, it calculates the distance between the detected face encoding and the known face encoding.
   - If the distance is below a defined threshold (0.6), the face is recognized as Barack Obama.

4. **Logging Recognitions**:
   Each time a face is recognized, a bounding box and label are added to the video feed.
   The timestamped recognition is added to a DataFrame.
   Once the face is recognized 5 times, the data is saved to an Excel file (`recognized_faces.xlsx`).

5. **Display**: 
   The program displays the video stream with annotations for recognized faces.

6. **Exit Condition**:
    Press `q` to stop the video stream and save any remaining recognition data.

## Usage

1. Clone the repository and navigate to the directory:
   ```bash
   git clone https://github.com/your_username/Face-Recognition-Attendance.git
   cd Face-Recognition-Attendance
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. View the output in the `attendance.xlsx` file generated in the project folder.

## Configuration

**Threshold**: Adjust the `confidence_threshold` value in the code to make recognition stricter or more lenient.
 **Frame Skipping**: The `frame_skip` variable controls the number of frames skipped. Modify this to increase or decrease the processing speed.

## Troubleshooting

 **Camera Not Working**: Ensure the path to the video file is correct.
**Dependencies**: Ensure all required packages are installed using the `pip install` command.


