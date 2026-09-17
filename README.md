# VisionDesk 👁️

## Computer Vision Based Classroom Occupancy & Crowd Analytics

VisionDesk is a Computer Vision application that detects people in classroom or crowd images and videos, calculates occupancy, classifies crowd status, visualizes detections, and generates analytical reports.

The project demonstrates practical Computer Vision concepts including image processing, video processing, object detection, confidence scores, bounding boxes, visualization, and quantitative analysis.

---

## 1. Problem Statement

Manual counting of people in classrooms, laboratories, and small events is repetitive and difficult to perform continuously.

VisionDesk provides an automated Computer Vision solution that detects people from images or videos and converts those detections into useful occupancy information.

---

## 2. Objectives

- Detect people from images and videos.
- Calculate the number of detected people.
- Display bounding boxes around detected people.
- Display detection confidence.
- Classify occupancy as NORMAL, WARNING, or CRITICAL.
- Visualize occupancy trends for videos.
- Generate a downloadable CSV analysis report.
- Demonstrate modular Computer Vision implementation.

---

## 3. Features

### Image Analysis
- Upload JPG, JPEG, or PNG.
- Detect people.
- Display bounding boxes.
- Display confidence scores.
- Calculate occupancy.
- Display occupancy status.
- Display detection details.
- screenshots <img width="2880" height="1618" alt="Screenshot 2026-09-17 233808" src="https://github.com/user-attachments/assets/927b7df4-6c08-44fb-bcec-7c96c7e15ab5" />


### Video Analysis
- Upload MP4, AVI, MOV, or MKV.
- Process video frames.
- Detect people.
- Generate annotated video.
- Calculate occupancy per analysed frame.
- Display occupancy trend.
- Export results as CSV.

### Configurable Analysis
Users can change:

- Detection confidence threshold.
- Warning occupancy threshold.
- Critical occupancy threshold.

---

## 4. Major Functional Modules

### Module 1: Input and Pre-processing

Accepts image/video input and converts it into frames that can be processed using OpenCV.

### Module 2: Person Detection

Uses YOLOv8n through Ultralytics as the primary person detector.

OpenCV HOG is available as a fallback detector if YOLO cannot be loaded.

### Module 3: Occupancy Analytics

Processes detections and calculates:

- People count
- Average confidence
- Occupancy status

### Module 4: Visualization and Reporting

Produces:

- Annotated images
- Annotated videos
- Occupancy graphs
- CSV reports

---

## 5. Technologies Used

- Python
- OpenCV
- YOLOv8 / Ultralytics
- Streamlit
- NumPy
- Pandas
- Pillow
- PyTest

---

## 6. System Architecture

```text
                 USER
                   |
                   v
            STREAMLIT UI
                   |
                   v
          INPUT / PREPROCESSING
                   |
                   v
           PERSON DETECTOR
          /                \
      YOLOv8             OpenCV HOG
      Primary             Fallback
          \                /
           \              /
            v            v
          OCCUPANCY ANALYTICS
                   |
             +-----+------+
             |            |
             v            v
       VISUALIZATION    REPORT
             |            |
             v            v
      Annotated Output    CSV
```

---

## 7. Workflow

```text
Upload Image / Video
        |
        v
Read Input
        |
        v
Process Frame
        |
        v
Detect Persons
        |
        v
Filter Using Confidence
        |
        v
Count Persons
        |
        v
Compare With Thresholds
        |
        +------> NORMAL
        |
        +------> WARNING
        |
        +------> CRITICAL
        |
        v
Display Results
        |
        v
Generate Report
```

---

## 8. Occupancy Logic

The default thresholds are:

```text
People < 10
       -> NORMAL

10 <= People < 20
       -> WARNING

People >= 20
       -> CRITICAL
```

These thresholds are configurable from the Streamlit sidebar and are demonstration parameters, not universal safety limits.

---

## 9. Project Structure

```text
VisionDesk/
│
├── app.py
├── detector.py
├── analytics.py
├── video_processor.py
├── utils.py
├── config.py
├── requirements.txt
├── README.md
├── statement.md
│
├── tests/
│   └── test_analytics.py
│
├── assets/
│
└── outputs/
```

---

## 10. Installation

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd VisionDesk
```

### Step 2: Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

## 11. Run the Application

```bash
streamlit run app.py
```

The Streamlit application will open in a browser.

On the first YOLO run, the Ultralytics package may download the YOLOv8n model automatically.

---

## 12. Testing

Run:

```bash
pytest -q
```

The tests validate:

- Empty input
- NORMAL status
- WARNING status
- CRITICAL status
- Average confidence calculation

---

## 13. Testing Scenarios

The application should be manually tested with:

1. Empty/low-occupancy image.
2. Normal classroom image.
3. Crowded classroom image.
4. Different lighting conditions.
5. Partially occluded people.
6. Different camera angles.
7. Short classroom/crowd video.
8. Invalid or unsupported file type.

---

## 14. Design Decisions

### Why YOLOv8n?

YOLOv8n provides a lightweight object detection model suitable for a student Computer Vision application and can perform person detection without requiring the project to train a model from scratch.

### Why OpenCV?

OpenCV provides image and video processing functionality, frame handling, drawing utilities, and a classical HOG pedestrian detector.

### Why Streamlit?

Streamlit allows the Computer Vision pipeline to be demonstrated through an interactive web interface without requiring a large front-end implementation.

### Why a fallback detector?

The OpenCV HOG detector provides a secondary detection method if the YOLO model cannot be loaded.

---

## 15. Privacy Considerations

VisionDesk detects people but does not identify individuals.

The project does not implement:

- Face recognition
- Personal identity tracking
- Biometric databases
- Personal profiles

The objective is occupancy analysis rather than identity recognition.

---

## 16. Limitations

Detection performance can vary because of:

- Lighting
- Camera angle
- Image resolution
- Occlusion
- Crowding
- Object size
- Model confidence threshold

Therefore, detection results should be treated as computer-vision estimates rather than guaranteed counts.

---

## 17. Future Enhancements

- Zone-based occupancy analysis.
- Heat-map generation.
- Multi-camera support.
- People-flow estimation.
- Long-term occupancy statistics.
- Database storage.
- Precision, recall and IoU evaluation.
- Real-time CCTV input.
- Custom classroom boundary configuration.

---

## 18. Academic Relevance

This project applies Computer Vision concepts including:

- Image acquisition
- Video processing
- Object detection
- Bounding-box detection
- Confidence-based filtering
- Frame processing
- Visualization
- Computer Vision analytics

---

## 19. Author

**Student Project - VITyarthi Build Your Own Project**

Subject: Computer Vision
