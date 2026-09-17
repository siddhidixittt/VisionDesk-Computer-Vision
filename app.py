import streamlit as st
from PIL import Image
import cv2
import numpy as np

from detector import PersonDetector
from analytics import analyze_detections, make_report_dataframe
from video_processor import process_video
from utils import draw_detections, save_uploaded_file

st.set_page_config(page_title="VisionDesk", page_icon="👁️", layout="wide")

st.title("👁️ VisionDesk")
st.subheader("Computer Vision Based Classroom Occupancy & Crowd Analytics")
st.write("Upload an image or video to detect people, calculate occupancy, and visualize crowd status.")

@st.cache_resource
def load_detector():
    return PersonDetector()

detector = load_detector()

with st.sidebar:
    st.header("Analysis Settings")
    confidence = st.slider("Detection confidence", 0.20, 0.90, 0.40, 0.05)
    warning_limit = st.number_input("Warning occupancy", min_value=1, value=10)
    critical_limit = st.number_input("Critical occupancy", min_value=2, value=20)
    input_mode = st.radio("Input type", ["Image", "Video"])

if input_mode == "Image":
    uploaded = st.file_uploader(
        "Upload a classroom/crowd image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded:
        try:
            image = Image.open(uploaded).convert("RGB")
            frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

            detections = detector.detect(frame, confidence)
            annotated = draw_detections(frame.copy(), detections)
            stats = analyze_detections(
                detections,
                warning_limit,
                critical_limit
            )

            col1, col2, col3 = st.columns(3)
            col1.metric("People Detected", stats["count"])
            col2.metric("Occupancy Status", stats["status"])
            col3.metric(
                "Average Confidence",
                f'{stats["avg_confidence"]:.2f}'
            )

            st.image(
                cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB),
                caption="Annotated Computer Vision Output",
                use_container_width=True
            )

            st.subheader("Detection Details")
            st.dataframe(
                make_report_dataframe(detections),
                use_container_width=True
            )

        except Exception as error:
            st.error(f"Unable to process the image: {error}")
    else:
        st.info("Upload an image to start analysis.")

else:
    uploaded = st.file_uploader(
        "Upload a classroom/crowd video",
        type=["mp4", "avi", "mov", "mkv"]
    )

    if uploaded:
        try:
            input_path = save_uploaded_file(uploaded)

            with st.spinner("Processing video..."):
                output_path, rows = process_video(
                    input_path,
                    detector,
                    confidence,
                    warning_limit,
                    critical_limit
                )

            st.success("Video analysis completed.")
            st.video(output_path)

            if rows:
                import pandas as pd

                dataframe = pd.DataFrame(rows)

                col1, col2 = st.columns(2)
                col1.metric("Frames Analysed", len(dataframe))
                col2.metric(
                    "Peak Occupancy",
                    int(dataframe["people_count"].max())
                )

                st.subheader("Occupancy Trend")
                st.line_chart(
                    dataframe.set_index("frame")["people_count"]
                )

                st.download_button(
                    "Download Analysis CSV",
                    dataframe.to_csv(index=False),
                    "visiondesk_report.csv",
                    "text/csv"
                )
        except Exception as error:
            st.error(f"Unable to process the video: {error}")
    else:
        st.info("Upload a video to start analysis.")
